import serial as conn
#nunca de los nunca se debe de abrir el serial monitor cuando este conectado con el arduino ya que dara un error
arduino = conn.Serial(port="COM8", baudrate=9600, timeout=1)
print("conexion con arduino exitosa")

while True:
    a = arduino.readline()
    a = a.decode()
    a = a.strip()
    print(a)