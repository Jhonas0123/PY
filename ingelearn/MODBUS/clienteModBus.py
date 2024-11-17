# aqui se llama a la libreria del cliente pero primero hay que instalar pymodbus 
# desde terminal
from pymodbus.client import ModbusTcpClient
# libreria para determinar tiempos
import time
# aqui se debe colocar la IP del clienten al que nos conectaremos
cliente = ModbusTcpClient("192.168.5.20")
#conectar
cliente.connect()
# Comandos posibles:
# Lectura ---
# cliente.read_coils(direccion,cantidad)
# cliente.read_discrete_inputs(direccion,cantidad)
# cliente.read_input_registers(direccion,cantidad)
# cliente.read_holding_registers(direccion,cantidad)
# Escritura ---
# cliente.write_coil(direccion,valor)
# cliente.write_register(direccion,cantidad)

cliente.connect()
try:
    while True:
        cliente.write_coil(1,True)
        time.sleep(0.5)
        cliente.write_coil(1,False)
        time.sleep(0.5)

except KeyboardInterrupt:
    cliente.close()