import json
import urllib2
import websocket

import states
import hangouts

APIPathLogin = "/api/login"
APIPathCaller = "/api/caller"

class Caller(object):
    """
    Caller implements methods to comunicate with the call center.
    """
    def __init__(self):
        super(Caller, self).__init__()
        self.ws = False
        self.browser_process = False
        self.state = False

        self.set_state(states.NOT_READY)

    def login_call_center(self, host, token, loginData):
        data = json.dumps(loginData)
        req = urllib2.Request(host + APIPathLogin)
        req.add_header('Content-Type', 'application/json')
        res = urllib2.urlopen(req, data)
        resData = json.load(res)
        return resData["token"]

    def on_state_has_login_info(self, message):
        print 'Called on_state_has_login_info'
        try:
            self.browser_process = hangouts.start_browser(self)
        except Exception as e:
            self.ws.send(json.dumps({
                'error': 'browser failed to start: {0}'.format(str(e))
            }))

    def on_state_login(self, message):
        print 'Called on_state_login'
        hangouts.sign_in(self.gmail_user, self.gmail_pass)
    
    def on_message(self, ws, message):
        print "Got message:", message
        data = {}
        try:
            data = json.loads(message)
        except Exception as e:
            print 'Error while decoding message into json', e
        if 'state' in data:
            method = hasattr(self, 'on_state_'+data['state'])
            if method != False:
                method = getattr(self, 'on_state_'+data['state'])
                try:
                    method(data)
                except Exception as e:
                    print 'While trying to call method', e 
        elif 'set' in data and 'value' in data:
            setattr(self, data['set'], data['value'])
            print getattr(self, data['set'])

    def on_error(self, ws, error):
        print error

    def on_close(self, ws):
        if self.browser_process != False:
            try:
                self.browser_process.terminate()
                print 'Closed browser process'
            except Exception as e:
                print 'Failed to close browser process'
                raise e
        print "### closed ###"

    def on_open(self, ws):
        print "Connection opened"
        self.set_state(self.state)

    def set_state(self, state):
        self.state = state
        if self.ws != False:
            try:
                self.ws.send(json.dumps({
                    'state': state
                }))
            except Exception as e:
                print 'Could not update server of state'
                print e
        else:
            print 'No websocket, state set localy'

    def create(self, host, username, password):
        token = self.login_call_center(host, "", {
            "username": username,
            "password": password
        })

        wshost = host.replace("http", "ws")

        ws = websocket.WebSocketApp(wshost+APIPathCaller,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            header     = {"Authorization: Bearer "+token}
        )

        self.ws = ws

    def run_forever(self):
        if self.ws != False:
            self.ws.run_forever()
            return True
        return False
