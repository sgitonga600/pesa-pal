import re

# instruction set
instructions = {
    'halt': 0x00,
    'nop': 0x01,
    'li': 0x02,
    'lw': 0x03,
    'sw': 0x04,
    'add': 0x05,
    'sub': 0x06,
    'mult': 0x07,
    'div': 0x08,
    'j': 0x09,
    'jr': 0x0A,
    'beq': 0x0B,
    'bne': 0x0C,
    'inc': 0x0D,
    'dec': 0x0E
}

def assembler(input_file, output_file):
    # symbol table
    labels = {}

    # read assembly code
    with open(input_file, 'r') as f:
        code = f.read()

    # remove comments and whitespaces
    code = re.sub(r';.*\n', '\n', code)
    code = re.sub(r'\n+', '\n', code)
    code = code.strip()

    # split code into lines
    code_lines = code.split('\n')

    # first pass: find labels and store their memory addresses
    address = 0x0000CFFF
    for line in code_lines:
        if line.endswith(':'):
            label = line[:-1]
            labels[label] = address
        else:
            address += 2

    # second pass: encode instructions
    encoded = []
    for line in code_lines:
        if line.endswith(':'):
            continue
        # split line into instruction and operands
        match = re.match(r'(\w+)\s*(.*)', line)
        instruction = match.group(1)
        operands = match.group(2)
        # encode instruction
        if instruction in instructions:
            opcode = instructions[instruction]
            if instruction == 'li':
                # li R1 0x00000000
                match = re.match(r'R(\d)\s+0x([0-9a-fA-F]+)', operands)
                if match:
                    register = int(match.group(1))
                    immediate = int(match.group(2), 16)
                    instruction = (opcode << 12) | (register << 8) | immediate
                    encoded.append(instruction)
            elif instruction in ['lw', 'sw', 'add', 'sub', 'mult', 'div', 'jr']:
                # lw R1 R2
                match = re.match(r'R(\d)\s+R(\d)', operands)
                if match:
                    register1 = int(match.group(1))
                    register2 = int(match.group(2))
                    instruction = (opcode << 12) | (register1 << 8) | (register2 << 4)
                    encoded.append(instruction)
            elif instruction in ['j', 'beq', 'bne']:
                # j 0x00000000
                match = re.match(r'0x([0-9a-fA-F]+)', operands)         
            elif instruction in ['j', 'beq', 'bne']:
                # j 0x00000000
                match = re.match(r'0x([0-9a-fA-F]+)', operands)
                if match:
                    address = int(match.group(1), 16)
                    instruction = (opcode << 12) | address
                    encoded.append(instruction)
            elif instruction in ['inc', 'dec']:
                # inc R1
                match = re.match(r'R(\d)', operands)
                if match:
                    register = int(match.group(1))
                    instruction = (opcode << 12) | (register << 8)
                    encoded.append(instruction)
            else:
                print(f'Error: Invalid instruction {instruction}')
                return
        else:
            print(f'Error: Unknown instruction {instruction}')
            return

    # output encoded instructions
    with open(output_file, 'wb') as f:
        for instruction in encoded:
            f.write(instruction.to_bytes(2, byteorder='little'))

