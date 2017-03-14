#port scanner by rajpal arora :P

import socket
import sys
count = 0

host=raw_input("type the name of the website to be scanned:")
print 'socket created'

try:
    remote_ip=socket.gethostbyname(host)
except socket.gaierror :
    print "host name could not be resolved"
    sys.exit()

print "ip address of " + host + " is " + remote_ip

for port in range(0,1024):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.20)
        result=s.connect_ex((remote_ip,port))
        if result==0:
            count=count+1
            print 'Port opened : %d' %(port)
        
    except KeyboardInterrupt:
        print '\n you have pressed ctrl+c'
        sys.exit()

    except socket.error:
        print 'Cannot connect to server' 
        sys.exit()

print ' total ports open : %d ' %(count)

