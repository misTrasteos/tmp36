from quick2wire.gpio import pins, In, Out
from time import sleep
import datetime

spiCLK = 1
spiMISO = 4
spiMOSI = 5
spiCS = 6
inAnalogico = 0

def leerAnalogico():
    pinCLK = pins.pin(spiCLK , direction=Out)
    pinMISO = pins.pin(spiMISO , direction=In)
    pinMOSI = pins.pin(spiMOSI , direction=Out)
    pinCS = pins.pin(spiCS , direction=Out)
      
    pines = [pinCLK, pinMISO, pinMOSI, pinCS]

    try:
        for p in pines:
            p.open()

        pinCS.value = 1
        pinCLK.value = 0
        pinCS.value = 0

        envio = inAnalogico
        envio |= 0x18
        envio <<= 3

        for i in range(5):
            if envio & 0x80:
                pinMOSI.value = 1
            else:
                pinMOSI.value = 0

            envio <<= 1
            pinCLK.value = 1
            pinCLK.value = 0

        valor = 0
        
        for i in range(12):
            pinCLK.value = 1
            pinCLK.value = 0
            valor <<= 1

            if pinMISO.value:
                valor |= 0x1
            
        pinCS.value = 1

        valor /= 2
        
        return valor
    finally:
        for p in pines:
            p.close()


if __name__ == '__main__':
    try:  
        while True:
            ahora = datetime.datetime.now().strftime('%Y%m%d%H%m%S')
            lectura0 = leerAnalogico()
            milivoltios = lectura0 * (3300.0 / 1024.0)
            tempC = ((milivoltios - 100.0) / 10.0) - 40
            
            with open('lecturas_tmp36.txt', 'at') as f:
                f.write(ahora + ';' + str(tempC) + '\n')

            sleep(10)            
    except KeyboardInterrupt:
        pass
