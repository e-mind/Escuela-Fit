import serial, requests

serial_conection = serial.Serial("COM4", 9600)
url = 'http://127.0.0.1:8000/pase_lista/asistencia/'

# while True:
try:
    rfid_bytes = serial_conection.readline()
    if rfid_bytes:
        rfid_string = rfid_bytes[1:-2].decode('utf-8')
        data = requests.post(url, data={'rfid': rfid_string})
except:
    serial_conection.close()
    exit()
else:
    serial_conection.close()
