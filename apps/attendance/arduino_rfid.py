import serial, requests

url = 'http://127.0.0.1:8000/attendance/register/'

try:
    serial_connection = serial.Serial("COM4", 9600)
except:
    exit()
else:
    rfid_bytes = serial_connection.readline()
    if rfid_bytes:
        rfid_string = rfid_bytes[1:-2].decode('utf-8')
        data = requests.post(url, data={'rfid': rfid_string})
    serial_connection.close()
