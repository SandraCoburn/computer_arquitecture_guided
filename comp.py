# The index into the momeory arra, aka location, address, pointer
# 1 - PRINT_BEEJ
# 2 - HALT
# 3 - SAVE_REG store a value in a register
# 4 - PRINT_REG print the register value ind ecimal
# 5 - PUSH
# 6 - POP
# 7 - CALL
# 8 - RET
import sys
import dis
memory = [0] * 256 # think of as a big array of bytes, 8-bits per byte
address = 0
registers = [0] * 8
registers[7] = 0xf4 #stack pointer
#Load the program file
# with open("print_comp.txt") as f:
#     for line in f:
#         print(line, end="")
#         if line == "\n":
#             continue
#         temp = line.split()
#         memory[address] = int(temp[0])
#         #print(line.strip())
#         address += 1
# print(memory[:10])

# with open("print_comp.txt") as f:
#     for line in f:
#         try:
        
#             temp = line.split()
#             memory[address] = int(temp[0])
#             #print(line.strip())
#              address += 1
#         except ValueError:
#             pass
#         except IndexError:
#             pass
# print(memory[:10])

# Load the program file
address = 0

if len(sys.argv) != 2:
	print("usage: comp.py progname")
	sys.exit(1)

try:
	with open(sys.argv[1]) as f:
		for line in f:
			line = line.strip()
			temp = line.split()

			if len(temp) == 0:
				continue

			if temp[0][0] == '#':
				continue

			try:
				memory[address] = int(temp[0])

			except ValueError:
				print(f"Invalid number: {temp[0]}")
				sys.exit(1)

			address += 1

except FileNotFoundError:
	print(f"Couldn't open {sys.argv[1]}")
	sys.exit(2)

if address == 0:
	print("Program was empty!")
	sys.exit(3)

#print(memory[:10])
#sys.exit(0)

'''
registers[3] = 37
'''
registers = [0] * 8
SP = 7
running = True
pc = 0 #program counter, the index into memory of the currently-executing instructions (extruction pointer)
while running:
    ir = memory[pc] #instruction register
    if ir == 1:
        print("Beej!")
        pc += 1
    elif ir == 2:
        running = False
        pc += 1

    elif ir == 3:
        reg_num = memory[pc + 1]
        value = memory[pc+2]
        registers[reg_num] = value
        print(f"{registers[reg_num]}")
        pc += 3
    elif ir == 4:
        reg_num = memory[pc + 1]
        print(registers[reg_num])
        pc += 2
    elif ir == 5: #push
        #Decrement SP
        registers[7] -= 1
        # Get value from register
        reg_num = memory[pc+1]
        value = registers[reg_num] # we want to push this value
        #store it on the stack
        top_of_stack_addr = registers[7]
        memory[top_of_stack_addr] = value
        print(f"stack: {memory[0xE4:0xF4]}")
        pc += 2
        
    elif ir == 6: #POP
        #Get value from the top of the stack
        top_of_stack_addr = registers[7]
        value = memory[top_of_stack_addr]
        #Get the register number and store the value there
        reg_num = memory[pc+1]
        registers[reg_num] = value
        pc += 2
    elif ir == 7: # CALL
        # push return address
        ret_addr = pc + 2
        registers[SP] -= 1
        memory[registers[SP]] = ret_addr
        #call the subroutine
        reg_num = memory[pc+1]
        pc = registers[reg_num]
        #dont_set_pc = True
    elif ir == 8: #RET
        #pop the return add off the stack
        ret_addr = memory[registers[SP]]
        registers[SP] += 1
        #set the pc ot it
        pc = ret_addr
    else:
        print(f"Invalid instruction {ir} code at address {pc}")
        sys.exit()
    if ir & 0b00010000 == 0:
        pc =+ (ir >> 6) + 1
dis.dis("__main__")  #to check for the amount of memory
'''
#This doesn't work for this guided but will for the ls8.py :
number_of_arguments = ir >> 6 #right shift number by 6
size_of_this_instruction = number_of_arguments + 1
pc += size_of_this_instruction
'''
'''
    #print("ir",ir)
                ## Get register number
                reg = self.ram[pc+1]
                ### Get the addresa to jump to, from the register.
                address = self.reg[reg]
                print("address", address)
                ### push command after CALL onto the stack
                return_address = pc + 2
                ### decrement stack pointer
                self.reg[7] -= 1
                sp = self.reg[7]
                print("stack", sp)
                ### put the return address ont he stack
                self.ram[sp] = return_address
                ### then look at register, jump to that address
                pc = address
                self.trace()

 # pop the return address off the stack
                sp = self.reg[7]
                return_address = self.ram[sp]
                self.reg[7] += 1
                # go to the return address. set the pc to return address
                pc = return_address
'''