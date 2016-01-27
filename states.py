'''
states.py

Contains the various states the caller can be in. These help it determine what
it should do next or be doing.
'''

NOT_READY = "not_ready"
READY = "ready"
WORKING = "in_call"
ERROR = "error"
LOGIN = "login"
HAS_LOGIN_INFO = "has_login_info"
