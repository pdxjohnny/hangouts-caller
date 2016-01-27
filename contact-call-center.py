#!/usr/bin/env python

import os
import sys

import caller

HOST_VAR = "HANGOUTS_CALL_CENTER_HOST"
USERNAME_VAR = "HANGOUTS_CALL_CENTER_USERNAME"
PASSWORD_VAR = "HANGOUTS_CALL_CENTER_PASSWORD"
HOST_VAR_DEFAULT = "http://localhost:8080"
USERNAME_VAR_DEFAULT = "user"
PASSWORD_VAR_DEFAULT = "pass"

def check_env_vars():
    if not HOST_VAR in os.environ:
        print "\"{0}\" environment variable not set".format(HOST_VAR)
        print "\tDefault: {0}".format(HOST_VAR_DEFAULT)
        print "\tExample: {0}={1} {2}".format(HOST_VAR, \
            HOST_VAR_DEFAULT, sys.argv[0])
        os.environ[HOST_VAR] = HOST_VAR_DEFAULT
    if not USERNAME_VAR in os.environ:
        print "\"{0}\" environment variable not set".format(USERNAME_VAR)
        print "\tDefault: {0}".format(USERNAME_VAR_DEFAULT)
        print "\tExample: {0}={1} {2}".format(USERNAME_VAR, \
            USERNAME_VAR_DEFAULT, sys.argv[0])
        os.environ[USERNAME_VAR] = USERNAME_VAR_DEFAULT
    if not PASSWORD_VAR in os.environ:
        print "\"{0}\" environment variable not set".format(PASSWORD_VAR)
        print "\tDefault: {0}".format(PASSWORD_VAR_DEFAULT)
        print "\tExample: {0}={1} {2}".format(PASSWORD_VAR, \
            PASSWORD_VAR_DEFAULT, sys.argv[0])
        os.environ[PASSWORD_VAR] = PASSWORD_VAR_DEFAULT

def main():
    check_env_vars()

    host = os.environ[HOST_VAR]
    username = os.environ[USERNAME_VAR]
    password = os.environ[PASSWORD_VAR]

    connection = caller.Caller()
    connection.create(host, username, password)

    connection.run_forever()

if __name__ == "__main__":
    main()
