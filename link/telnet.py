import socket, select, string, sys
from django.shortcuts import get_object_or_404, render
from .models import Psychic

def telnet(request):
    link = get_object_or_404(Psychic, pk=1)
    #main function
    host = link.host
    port = link.port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print '<p>Unable to connect</p>'
        sys.exit()

    print '<p>Connected to remote host</p>'

    while 1:
        socket_list = [sys.stdin, s]

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print '<p>Connection closed</p>'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)

            #user entered a message
            else :
                msg = sys.stdin.readline()
                s.send(msg)
