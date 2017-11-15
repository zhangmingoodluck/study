# Author Mike
import getpass

_username = "cat"
_password = "a"
username = input("username:")
password = input("password:")
if username == _username and password == _password:
    print("oye".format(name=username))
else:
    print("fuck off baby!")
print(username, password)
