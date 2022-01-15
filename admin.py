
import hashlib
import socket
import threading
import sys

def send_to_server(socket):
    while True:
        message = input()
        byte_message = message.encode("utf-8")
        socket.send(byte_message)
        if message=="quit":
            socket.close()
            break
def recv_messages(socket):
    while True:
        try:
            brdcst_msg = socket.recv(1024)
        except:
            sock.close()
            break

#admin can:
    #kick out a certain client
    #temporarily pause the activity on the server
    # ^^ pause people's messages from sending but the messages should send after admin unpauses
    
            


hostname = socket.gethostname()
port = 5000
sock = socket.socket()
print("socket has been created")
sock.connect((hostname,port))
print("connected")
print("you are an admin")
info = sock.recv(1024)
client_message = hashlib.sha224(b'this is an admin').hexdigest()
client_message_bytes = client_message.encode("utf-8")
  #client responds with their name
sock.send(client_message_bytes)


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