import serial


class Printer(printer):
    serial_interface = serial.Serial(printer['device'], 115200, timeout=2)
    def getStatus():
        #M31
        serial_interface.write('M31')
        print('Status: %s' % serial_interface.readline())

    def getTimeSinceStart():
        print('getting the time since start')

    def pausePrint():
        #M25
        serial_interface.write('M31')
        print('Pause SD print')

    def getSDStatus():
        #M27
        #Get SD status
        print('getting the SD Status')

    def writeToSD():
        #M28
        #Begin write to SD card.
        #Example: M28 filename.gco File specified by filename.gco is created (or overwritten if it exists) on the SD card and all subsequent commands sent to the machine are written to that file. Writing to file is terminated with M29.
        #M29
        #Stop SD write.
        print('writing to SD Card')

    def getTemp():
        #M105
        #Returns current temperatures.
        print('getting the temperatures')

    def emergStop():
        #M112
        #Emergency stop
        print('Emergency Stop')