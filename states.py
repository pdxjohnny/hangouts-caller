'''
states.py

Contains the various states the caller can be in. These help it determine what
it should do next or be doing.
'''

NOT_READY = "not_ready"
HAS_LOGIN_INFO = "has_login_info"
LOGIN = "login"
READY = "ready"
MAKE_CALL = "make_call"
IN_CALL = "in_call"
END_CALL = "end_call"
ERROR = "error"
