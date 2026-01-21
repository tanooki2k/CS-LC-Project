import time
import serial
import mb_detect


def find_microbit_port():
    port = mb_detect.find()
    if port:
        return serial.Serial(port, 115200)
    else:
        raise ValueError("Serial port not found!")

def read_serial(ser: serial.Serial, period: float, epsilon: float):
    start_time = time.time()
    raw_data = []

    while True:
        line = ser.readline().decode().strip()
        delta = (time.time() - start_time) % period
        if delta < epsilon or delta > period - epsilon :
            raw_data.append(line)
        else:
            if raw_data:
                print(raw_data)
                raw_data = []

if __name__ == "__main__":
    serial = find_microbit_port()
    read_serial(serial, 5, 1.5)
