# computer_arquitecture_guided

## Number Bases

- Base 2 - binary 0-1
- Base 8 - octal 0-7
- Base 10 - decima 0-9
- Base 16 - 0 1 2 3 4 5 6 7 8 9 A B C D E F 10
- Base 64

          16's place

  - +------ 8's place (0b1000's place)
  - |+----- 4's place (0b100's place)
  - ||+---- 2's place (0b10's place)
  - |||+--- 1's place (0b1's place)
  - |||
  - 1010

11011 = 1*16 + 1*8 + 0*4 + 1*2 + 1\*1 = 27

### Convert from binary to Hexadecimal

0b 0110 0111 # two nibbles
6 7
0x67

0b 1111 1101
F D
0xFD

### hex colors

color: #ffff00
color: rgb(255,255,0) (green, red, blue)

## Bitwise operations:

- AND, OR, NOT, XOR, NOR, NAND

### "AND masking", stencil

- subnet mask 255.255.255.0

#### Bitwise AND can mask out parts of a number, or clean individual bits of a numer to 0

#### Bitwise OR can set individual bits (or groups of bits) to 1

## Bit Shifting

- 01100111 >> 6 #it will shift 6 numbers = 01

## Analogy in Base 10 of extracting numbers. shiftin bites it's like deviding by the base

vv
1234567
0123456 shift 3 right (AKA // 1000)
0012345
0001234

00000034 mask out the 34

## Now in Binary

0101001010110 shift right by 6
& 0001111 mask the resutl

if n is a power of 2:
x % n
is the same as
x & (n-1)

## Where to store variables if we have too many for the registers?

- Stack: push, pop, storage
- RAM == memory
- Registers, caches, RAM, hard drive
- memory: a way to store info and get it back
- For the project:
  - Stack pointer starts at the top at F3 because the ones before that are reserved for something else
  - Stack bottom is reserved for the instructions at the bottom of thestack

godbolt.org -- to check how the stack works

## CPU Stack

- Store pushed items in RAM
- Pointer to the top of the stack

## Subroutines

- We need a Stack to save the address where a function is to be executed

### Stack subroutien

- When you call, push the return addr on the stack, jump to the funnction
- When you return , pop the return addr off the stack, set the PC to it
