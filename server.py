import socket
import serial
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600)
s = socket.socket()
host = '127.0.0.1'
port = 4096
s.bind((host, port))

s.listen(5)

while (1):
  ser.flushInput()
  ser.flushOutput()
  send = input()
  ser.write(send)
  sleep(0.1)
  bytes = ser.inWaiting()
  if (bytes > 0):
    msg = ser.readline()
    print msg
  #c, addr = s.accept()
  #print 'Got connection from', addr
  #msg = ser.readline()
  #send = input()
  #ser.write(send)
  #msg = c.receive()
  #c.send(msg)
  #c.close()
