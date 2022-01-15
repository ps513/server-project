from os import pipe

import hashlib
import socket
import threading
import sys
  
def admin(connection, address, names_dictionary):
  connection.send(b"you may kick users out of the chat and pause messaging. To kick out, type the name with parentheses directly after, ex:Piper()")
  while True:
      
    info = connection.recv(1024)
    info_str = info.decode("utf-8")
    print(info_str)
    if info_str!="quit()" and info_str[:-2] not in names_dictionary:
      
          print("admin: " + info_str)
          connection.sendall(info)
          brdcst_info = "admin" + ": " + info_str
          broadcast(names_dictionary, brdcst_info)
    elif info_str[:-2] in names_dictionary and info_str[-2]=="()":
      names_dictionary[info_str[:-2]].close()
      #names_dictionary[info_str[:-2]].send(b'quit:)
      del names_dictionary[info_str[:-2]]
      print(len(names_dictionary.keys()), " users in chat")
      leave_chat = info_str + " left the chat " + str(len(names_dictionary))+ " remaining in chat"
      broadcast(names_dictionary, leave_chat)
    
      
    else:
          connection.close() 
          #connection.shutdown(socket.SHUT_RDWR)
          break
        
        
      


def messaging(connection, address, names_dictionary):
  connection.send(b"What is your name?")
  connection.send(b'to quit, send: quit()')
  clientname_bytes = connection.recv(1024)
  clientname_str = clientname_bytes.decode("utf-8")
  while clientname_str in names_dictionary:
    connection.send(b"name already taken, please choose another name")
    clientname_bytes = connection.recv(1024)
    clientname_str = clientname_bytes.decode("utf-8")

  names_dictionary[clientname_str]=connection
  admin_hash= hashlib.sha224(b'this is an admin').hexdigest()
  if clientname_str!=admin_hash:
    print(clientname_str + " has joined the chat")
  else:
    clientname_str = "admin"
    thread_ob=threading.Thread(target=admin, args=(connection,address, names_dictionary))
    thread_ob.start()
      
  while True:
    try:
      info = connection.recv(1024)
      info_str = info.decode("utf-8")
      if info_str!="quit()":
        print(clientname_str + ": " + info_str)
        connection.sendall(info)
        brdcst_info = clientname_str + ": " + info_str
        broadcast(names_dictionary, brdcst_info)
          
    except:
      print(len(names_dictionary.keys()), " users in chat")
      connection.close() 
      #connection.shutdown(socket.SHUT_RDWR)
      global number_of_users
      number_of_users-=1
      del names_dictionary[clientname_str]
      leave_chat = clientname_str + " left the chat " + str(number_of_users)+ " remaining in chat"
      broadcast(names_dictionary, leave_chat)
      
      print(clientname_str + " has exited")
      break
      #sys.exit()}
    


      

def broadcast(names_dictionary, message):
  for connection in names_dictionary.values():
    connection.send(message.encode("utf-8") )

sock = socket.socket()
socket.AF_INET6
print(sock)
hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)
print(hostname)
print(ipaddress)
port = 5000
address = (ipaddress,port)
sock.bind(address)
print("socket is bound")
names_dictionary={}
number_of_users = 0
client = " people in chat"
number_of_users = 0


sock.listen(20)
while True:
  connection, address = sock.accept()
  number_of_users+=1
  print(number_of_users, client)
  #connections.append(connection)
  print("client is accepted")
  thread_ob=threading.Thread(target=messaging, args=(connection,address, names_dictionary))
  thread_ob.start()





    



    

      


