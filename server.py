import socket
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
s = socket.socket()
host = '127.0.0.1'
port = 4096
s.bind((host, port))

s.listen(5)

while (1):
  msg = ser.readline()
  c, addr = s.accept()
  print 'Got connection from', addr
  c.send(msg)
  c.close()
