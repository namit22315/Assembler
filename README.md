# Assembler
        An assembler is a software tool or program that translates assembly language code into machine code, which can be directly executed by a computer's processor. It plays a vital role in the development of low-level software and system programming, as it bridges the gap between human-readable assembly instructions and the binary representations understood by the hardware.

        Assembly language is a low-level programming language that closely corresponds to the machine language instructions of a specific computer architecture. It uses mnemonic codes to represent individual instructions, memory addresses, and data operands. Assembly language provides a more human-readable and manageable alternative to working directly with binary machine code.

        The assembler reads the assembly code, processes each instruction, and generates the corresponding machine code

# Table of Contents:
        1. Contributions
        2. Introduction
        3. Prerequisites
        4. Usage
        5. Supported Instructions


# 1. Contributions:
        (i) Namit Jain (2022315)
        (ii) Prayag Parashar (2022377)
        (iii) Naman Jindal (2022311)
        (iv) Niteen Kumar (20223xx)

# 2. Introduction
        The Assembler program is designed to convert assembly language instructions into 
        machine code that can be executed by a computer. It follows a simple and straightforward
        approach, translating each assembly instruction into its binary representation.

        The program is written in Python, which provides a high-level and easy-to-understand
        syntax, making it suitable for educational purposes or small-scale projects.

# 3. Prerequisites
        To run this Assembler program, you need to have the following software installed on your system:

        Python (version 3.6 or higher)

# 4. Usage
        (i) Clone the repository or download the source code files.
        (ii) Open a terminal or command prompt and navigate to the program's directory.
        (iii) Run the program using the following command:
```python
                python assembler.py input.txt
```
        Replace input_file.asm with the path to your assembly code file and output_file.mc
         with the desired filename for the generated machine code.
        (iv)The program will read the assembly code from the input file, assemble
         it, and save the machine code to the output file.

# 5. Supported Instructions
        The Assembler program supports a subset of assembly instructions. 
        
        Here is a list of the supported instructions:
        LOAD - Load a value into a register
        STORE - Store a value from a register into memory
        ADD - Add two values and store the result in a register
        SUB - Subtract one value from another and store the result in a register
        MULT - Multiply two values and store the result in a register
        DIV - Divide one value by another and store the result in a register
        MOV Imm - Performs reg1 = $Imm where Imm is a 7 bit value.
        MOV REG - Move content of reg2 into reg1.
        CMP - Compares reg1 and reg2 and sets up the FLAGS register.
        JUMP - Unconditionally jump to a specific memory address
        JUMPEQ - Jump to a specific memory address if two values are equal
        JUMPLT - Jump to a specific memory address if one value is less than another
        JUMPGT - Jump to a specific memory address if one value is greater than another
        LEFT SHIFT - Left shifts reg1 by $Imm, where $Imm is a 7 bit value.
        RIGHT SHIFT - Right shifts reg1 by $Imm, where $Imm is a 7 bit value.
        XOR - Performs bitwise XOR of reg2 and reg3. Stores the result in reg1.
        OR - Performs bitwise OR of reg2 and reg3. Stores the result in reg1.
        AND - Performs bitwise AND of reg2 and reg3. Stores the result in reg1.
        Invert - Performs bitwise NOT of reg2. Stores the result in reg1.
        HALT - Stops the machine from executing until reset.
