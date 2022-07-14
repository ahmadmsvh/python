import serial.tools.list_ports as port_list
import serial
import time

ports = list(port_list.comports())
for p in ports:
    print (p)

    s = serial.Serial('COM6')
    res = s.read()
    print(res)

serialString = ""
while 1:

    if serialPort.in_waiting > 0:
        serialString = serialPort.readline()

        try:
            print(serialString.decode("Ascii"))
        except:
            pass