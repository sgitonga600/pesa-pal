# pesa-pal
# assembly
The assembler and simulator are both Python scripts that can be run using the Python interpreter. Here's an example of how you can run them in a command line environment:

1. Assembler: assuming you have a file called program.asm that contains the assembly code, and you want to output the encoded instructions to a file called 'program.bin'

             python assembler.py program.asm program.bin

2. Simulator: assuming you have encoded instructions in a file called 'program.bin'

            python simulator.py program.bin

3. You need to make sure that the python is installed in your computer and the assembler.py, simulator.py and the files you want to run are in the same directory or give the proper path to the file.

Additionally, you can run these scripts within an IDE like PyCharm, which provides a user-friendly interface to run and debug your code.

It's also worth noting that you can run these programs using python's built in function 'exec()' or 'eval()' but it is not recommended as it can be a security vulnerability.

