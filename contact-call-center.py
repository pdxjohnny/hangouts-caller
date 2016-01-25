import os
import sys
import time
import json
import thread
import urllib2
import websocket

HOST_VAR = "HANGOUTS_CALL_CENTER_HOST"
USERNAME_VAR = "HANGOUTS_CALL_CENTER_USERNAME"
PASSWORD_VAR = "HANGOUTS_CALL_CENTER_PASSWORD"
APIPathLogin = "/api/login"
APIPathCaller = "/api/caller"

def login(host, token, loginData):
    req = urllib2.Request(host + APIPathLogin)
    req.add_header('Content-Type', 'application/json')
    res = urllib2.urlopen(req, json.dumps(loginData))
    resData = json.load(res)
    return resData["token"]

def on_message(ws, message):
    print "Got message:"
    print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    for line in sys.stdin:
        print "Sending"
        ws.send(line)
    ws.close()

def main():
    if not HOST_VAR in os.environ:
        print "Need \"{0}\" environment variable set".format(HOST_VAR)
        print "\tExample: {0}=ws://example.com/ {1}".format(HOST_VAR, \
            sys.argv[0])
        # Exit with EINVAL, invalid argument
        sys.exit(22)
    if not USERNAME_VAR in os.environ:
        print "Need \"{0}\" environment variable set".format(USERNAME_VAR)
        print "\tExample: {0}=ws://example.com/ {1}".format(USERNAME_VAR, \
            sys.argv[0])
        # Exit with EINVAL, invalid argument
        sys.exit(22)
    if not PASSWORD_VAR in os.environ:
        print "Need \"{0}\" environment variable set".format(PASSWORD_VAR)
        print "\tExample: {0}=ws://example.com/ {1}".format(PASSWORD_VAR, \
            sys.argv[0])
        # Exit with EINVAL, invalid argument
        sys.exit(22)

    host = os.environ[HOST_VAR]

    token = login(host, "", {
        "username": os.environ[USERNAME_VAR],
        "password": os.environ[PASSWORD_VAR]
    })
    websocket.enableTrace(True)
    wshost = host.replace("http", "ws")
    ws = websocket.WebSocketApp(wshost+APIPathCaller,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        header     = {"Authorization: Bearer "+token}
        )

    ws.run_forever()

if __name__ == "__main__":
    main()
