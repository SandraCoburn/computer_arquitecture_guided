import sys
if len(sys.argv) < 2:
    print("Please pass in a second filename: python3 in_and_out.py second_filename.py")
    sys.exit()
file_name = sys.argv[1]
try:
    with open(file_name) as file:
        for line in file:
            split_line = line.split("#")
            command = split_line[0].strip()
            print(command)

            if command == "":
                continue
            num = int(command, 2)
            #print(type(command))
            print(f"{num:8b} is {num}")

except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.argv[1]} file was not found")
    sys.exit()