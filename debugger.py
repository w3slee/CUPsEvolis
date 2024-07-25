import serial

# Function to establish serial connection
def establish_serial_connection():
    print("Enter serial connection parameters:")
    port = input("Port (e.g., COM1): ")
    baudrate = int(input("Baudrate (e.g., 9600): "))
    timeout = int(input("Timeout (e.g., 1): "))

    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        print("Serial connection established.")
        return ser
    except serial.SerialException as e:
        print("Error establishing serial connection:", e)
        return None

# Function to display menu and execute commands
def display_menu(ser):
    while True:
        print("\nEvolis Card Printer Command Menu:")
        print("1. Adjustment Commands")
        print("2. Downloading Commands")
        print("3. Motor Commands")
        print("4. Parameter Commands")
        print("5. Read Commands")
        print("6. Sequence Commands")
        print("7. Write Commands")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            adjustment_commands(ser)
        elif choice == "2":
            downloading_commands(ser)
        elif choice == "3":
            motor_commands(ser)
        elif choice == "4":
            parameter_commands(ser)
        elif choice == "5":
            read_commands(ser)
        elif choice == "6":
            sequence_commands(ser)
        elif choice == "7":
            write_commands(ser)
        elif choice == "8":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle adjustment commands
def adjustment_commands(ser):
    while True:
        print("\nAdjustment Commands:")
        print("1. Adjust sensor")
        print("2. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            p1 = input("Enter p1 (e.g., c for color sensor): ")
            p2 = input("Enter p2 (e.g., 150): ")
            command = f"(ESC)Ase;{p1};{p2}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle downloading commands
def downloading_commands(ser):
    while True:
        print("\nDownloading Commands:")
        print("1. Download bitmap")
        print("2. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            p1 = input("Enter p1 (e.g., y for yellow): ")
            p2 = input("Enter p2 (e.g., 128): ")
            data = input("Enter data: ")
            command = f"(ESC)Dbc;{p1};{p2};{data}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle motor commands
def motor_commands(ser):
    while True:
        print("\nMotor Commands:")
        print("1. Run step motor")
        print("2. Run feeder motor")
        print("3. Run up & down motor")
        print("4. Run ribbon motor")
        print("5. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            p1 = input("Enter p1: ")
            command = f"(ESC)Mc;{p1}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "2":
            p1 = input("Enter p1: ")
            command = f"(ESC)Mf;{p1}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "3":
            p1 = input("Enter p1: ")
            command = f"(ESC)Mh;{p1}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "4":
            p1 = input("Enter p1: ")
            command = f"(ESC)Mr;{p1}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle parameter commands
def parameter_commands(ser):
    while True:
        print("\nParameter Commands:")
        print("1. Set monochrome bitmap printing mode")
        print("2. Set color contrast value")
        print("3. Set errors management")
        print("4. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            p1 = input("Enter p1: ")
            command = f"(ESC)Pbm;{p1}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "2":
            p1 = input("Enter p1: ")
            p2 = input("Enter p2: ")
            p3 = input("Enter p3: ")
            command = f"(ESC)Pc;{p1};{p2};{p3}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "3":
            p1 = input("Enter p1: ")
            o1 = input("Enter o1: ")
            command = f"(ESC)Pem;{p1};{o1}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle read commands
def read_commands(ser):
    while True:
        print("\nRead Commands:")
        print("1. Read selected monochrome printing mode type")
        print("2. Read contrast value")
        print("3. Read firmware checksum value")
        print("4. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            command = "(ESC)Rbm(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "2":
            p1 = input("Enter p1: ")
            command = f"(ESC)Rc;{p1}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "3":
            command = "(ESC)Rck(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle sequence commands
def sequence_commands(ser):
    while True:
        print("\nSequence Commands:")
        print("1. Self adjust printer")
        print("2. Copy")
        print("3. Sequence transmission through serial port")
        print("4. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            o1 = input("Enter o1: ")
            command = f"(ESC)Sa;{o1}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "2":
            command = "(ESC)Sc(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "3":
            p1 = input("Enter p1: ")
            p2 = input("Enter p2: ")
            p3 = input("Enter p3: ")
            command = f"(ESC)Scom;{p1};{p2};{p3}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle write commands
def write_commands(ser):
    while True:
        print("\nWrite Commands:")
        print("1. Write barcode")
        print("2. Fill bitmap with data")
        print("3. Write monochrome line")
        print("4. Write monochrome text")
        print("5. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            p1 = input("Enter p1: ")
            p2 = input("Enter p2: ")
            p3 = input("Enter p3: ")
            p4 = input("Enter p4: ")
            p5 = input("Enter p5: ")
            p6 = input("Enter p6: ")
            p7 = input("Enter p7: ")
            data = input("Enter data: ")
            command = f"(ESC)Wb;{p1};{p2};{p3};{p4};{p5};{p6};{p7};{data}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "2":
            p1 = input("Enter p1: ")
            o1 = input("Enter o1: ")
            command = f"(ESC)Wcb;{p1};{o1}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "3":
            p1 = input("Enter p1: ")
            p2 = input("Enter p2: ")
            p3 = input("Enter p3: ")
            p4 = input("Enter p4: ")
            p5 = input("Enter p5: ")
            command = f"(ESC)Wl;{p1};{p2};{p3};{p4};{p5}(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "4":
            command = "(ESC)Wt(CR)"
            ser.write(command.encode())
            print("Command sent.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# Main function
def main():
    ser = establish_serial_connection()
    if ser:
        display_menu(ser)
        ser.close()

if __name__ == "__main__":
    main()
