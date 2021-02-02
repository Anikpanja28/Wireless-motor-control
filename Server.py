import serial
import socket
import time
import keyboard  # using module keyboard
  
    
arduino = serial.Serial('COM4', 9600)
time.sleep(1)
new_socket = socket.socket()
host_name = "192.168.1.7"
s_ip = socket.gethostbyname(host_name)
 
port = 8080
 
new_socket.bind((host_name, port))
print( "Binding successful!")
print("This is your IP: ", s_ip)

 
new_socket.listen(1) 
 
 
conn, add = new_socket.accept()
print("Connected")



while True:
    transmit = keyboard.read_key()
    #print(transmit)
    transmit = transmit.encode()
    time.sleep(0.1)

    conn.send(transmit)
