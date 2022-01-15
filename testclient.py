import socket
import threading
import sys
def send_to_server(socket):
    name_message = input()
    byte_name_message = name_message.encode("utf-8")
    socket.send(byte_name_message)
    while True:
        message = input()
        byte_message = message.encode("utf-8")
        socket.send(byte_message)
        brdcst_msg = socket.recv(1024)
        if message=="quit()":
            socket.close()
            break
        #elif 
        elif brdcst_msg=="admin" + ": " + name_message:
            sock.close()
            break

        
def recv_messages(socket):
 
    while True:
        
        brdcst_msg = socket.recv(1024)
        
        if brdcst_msg!="quit()":
            bm_str = brdcst_msg.decode("utf-8")
            print(bm_str)
        else:
            socket.close()
            print("exited")
            sys.exit()
    #change this loop to make sure the client only closes if it knows it recieves quit from an admin


hostname = socket.gethostname()
port = 5000
sock = socket.socket()
print("socket has been created")
sock.connect((hostname,port))
print("connected")
print("If a message is found to be harmful, you will be removed by an admin")
info = sock.recv(1024)
print(info)
client_message = input().encode("utf-8")   #client responds with their name
sock.send(client_message)


# while True:
        
#     if client_message!="quit":
#             sock.send(client_message.encode("utf-8")) #client side sends the name as bytes to the server
#                     #server_message = sock.recv(1024)
#             print(client_message)
            
            

#     elif client_message == "quit":
#             sock.close()
#     break



thread_ob=threading.Thread(target=send_to_server, args=([sock]))
thread_ob.start()
thread_ob=threading.Thread(target=recv_messages, args=([sock]))
thread_ob.start()
    
                

