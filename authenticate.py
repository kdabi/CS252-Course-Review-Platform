from pexpect import pxssh
s = pxssh.pxssh()
username = raw_input("Enter Your username: ")
psswd = raw_input("Enter the password for " + username )
try:
    if s.login ('vyom.cc.iitk.ac.in', username, psswd):
        print "SSH session login successful"
        s.logout()
except:
        print "Password is incorrect"
