import getpass

user = getpass.getuser()
passwd = getpass.getpass()

def svc_login(user, passwd):
    if passwd == "123":
        return True

if svc_login(user, passwd):    # You must write svc_login()
   print('Right!')
else:
   print('Wrong!')