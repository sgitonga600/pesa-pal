def simulator(input_file):
    # initialize memory and registers
    memory = bytearray(65536)
    registers = [0] * 5
    pc = 0x0000CFFF

    # load program into memory
    with open(input_file, 'rb') as f:
        f.readinto(memory, pc)

    # fetch-decode-execute loop
    while True:
        # fetch instruction
        instruction = int.from_bytes(memory[pc:pc+2], byteorder='little')
        pc += 2

        # decode instruction
        opcode = instruction >> 12
        register1 = (instruction >> 8) & 0xF
        register2 = (instruction >> 4) & 0xF
        register3 = instruction & 0xF
        immediate = instruction & 0xFF

        # execute instruction
        if opcode == 0x00:
            # halt
            print("Program halted")
            break
        elif opcode == 0x01:
            # nop
            pass
        elif opcode == 0x02:
            # li R1 0x00000000
            registers[register1] = immediate
        elif opcode == 0x03:
            # lw R1 R2
            address = registers[register2]
            registers[register1] = int.from_bytes(memory[address:address+4], byteorder='little')
        elif opcode == 0x04:
            # sw R1 R2
            address = registers[register1]
            memory[address:address+4] = registers[register2].to_bytes(4, byteorder='little')
        elif opcode == 0x05:
            # add R3 R1 R2
            registers[register3] = registers[register1] + registers[register2]
        elif opcode == 0x06:
            # sub R3 R1 R2
            registers[register3] = registers[register1] - registers[register2]
        elif opcode == 0x06:
            # sub R3 R1 R2
            registers[register3] = registers[register1] - registers[register2]
        elif opcode == 0x07:
            # mult R3 R1 R2
            registers[register3] = registers[register1] * registers[register2]
        elif opcode == 0x08:
            # div R3 R1 R2
            registers[register3] = registers[register1] // registers[register2]
        elif opcode == 0x09:
            # j 0x00000000
            pc = instruction & 0x0FFF
        elif opcode == 0x0A:
            # jr R1
            pc = registers[register1]
        elif opcode == 0x0B:
            # beq R1 R2 R3
            if registers[register1] == registers[register2]:
                pc = registers[register3]
        elif opcode == 0x0C:
            # bne R1 R2 R3
            if registers[register1] != registers[register2]:
                pc = registers[register3]
        elif opcode == 0x0D:
            # inc R1
            registers[register1] += 1
        elif opcode == 0x0E:
            # dec R1
            registers[register1] -= 1

        # log register values
        print(registers)

