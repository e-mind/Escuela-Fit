import serial
from urllib.request import urlopen, pathname2url

serial_conection = serial.Serial("COM4", 9600)
url_origin = 'http://127.0.0.1:8000/pase_lista/asistencia/{}/'

# while True:
try:
    rfid_bytes = serial_conection.readline()
    if rfid_bytes:
        rfid_string = rfid_bytes[1:-2].decode('utf-8')
        url_arguments = url_origin.format(pathname2url(rfid_string))
        data = urlopen(url_arguments).read().decode('utf-8')
        print(data)
except:
    serial_conection.close()
    exit()
