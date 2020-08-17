# The index into the momeory arra, aka location, address, pointer
# 1 - PRINT_BEEJ
# 2 - HALT
# 3 - SAVE_REG store a value in a register
# 4 - PRINT_REG print the register value ind ecimal

memory = [ # think of as a big array of bytes, 8-bits per byte
1, # PRINT_BEEJ
3, # SAVE_REG R4 37, instructions itself also called apcode
4, # 4 and 37 are arguments to SAVE_REG, also called operands
37,
4, # PRINT_REG R4
4,
2 #HALT
]

'''
registers[3] = 37
'''
registers = [0] * 8

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