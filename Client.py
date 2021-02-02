import time, socket, sys, serial, keyboard
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")


arduino = serial.Serial('COM4', 9600)
arduino.readline(1)
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080
 
print('This is your IP address: ',ip)
print('IP ADDRESS')
server_host = "192.168.0.3"


 
 
socket_server.connect((server_host, sport))
print("connected") 

message = socket_server.recv(1024)
while True:


    
    key = message.decode()
    print(key)
    message = socket_server.recv(1024)
    if(key == 'w'):
        arduino.write(b'1')
        
        time.sleep(0.1)

    if(key == 's'):
        arduino.write(b'0')
       
        time.sleep(0.1)

