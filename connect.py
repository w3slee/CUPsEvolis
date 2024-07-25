import serial

# Open the serial port
ser = serial.Serial("COM1", 9600, timeout=1)

# Construct the command
command = b'\x1bRcr\r'

# Send the command
ser.write(command)

# Close the serial port
ser.close()
