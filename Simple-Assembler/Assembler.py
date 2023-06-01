op = {"add": '00000',
      "sub": '00000',
      "mov": '0001100000',
      "ld": '00000',
      "st": '00000',
      "mul": '00000',
      "div": '00000',
      "rs": '00000',
      "ls": '00000',
      "xor": '00000',
      "or": '00000',
      "and": '00000',
      "not": '00000',
      "cmp": '00000',
      "jmp": '00000',
      "jlt": '00000',
      "jgt": '00000',
      "je": '00000',
      "hlt": '00000',
      }

reg = {'R0': ['000', 0],
       'R1': ['001', 0],
       'R2': ['010', 0],
       'R3': ['011', 0],
       'R4': ['100', 0],
       'R5': ['101', 0],
       'R6': ['110', 0],
       'FLAGS': ['111', 0]}
z=0
statements={}

while (1):
    try:
        line = input()
        line=line.strip()
        if (line != ""):
            
                
            statements[z] = [line.split(), z]
            z += 1
    except EOFError:
        break


error12=[]

def spaceerror():
    for i in statements.keys():
        for j in statements[i][0]:
            x=len(j)
            j=j.strip()
            y=len(j)
            if(x!=y):
                error12.append("More than one spaces for separating different elements of an instruction at line "+str(statements[i][1]))
                

def checkr():   #function to check if any variable is defined after a non var instruction is given
    i=0
    while(statements[i][0][0]=="var"):
        i=i+1
    for j in range(i,len(statements)):
        if(statements[j][0][0]=="var"):
            
           error12.append("variable decleration after an instruction at line "+str(statements[j][1]))

def check_digit (l) :
     for i in range(len(l)):
          for j in l[i][0]:
               if j[0]=="$":
                    if str(j[1::]).isdigit()==False:
                         error12.append(f"Error in line {l[i][1]} : {j} is not an integer")
     

def invalid_op(l):
    x = len(l) - 1
    for i in range (x+1):
        if l[i][0][0] not in op.keys() and l[i][0][0] != "var":
            error12.append(f"Error in line {l[i][1]} : invalid operand")

def check_flg (l):
     for i in range(len(l)):
          if l[i][0][0] != 'mov':
               if "FLAGS" in l[i][0]:
                    error12.append(f"Error in line {l[i][1]} : illegal use of flags")
def error1(l):
    if l[0][0] in ["add", "sub", "mul", "xor", "or", "and"]:
        if (len(l[0])) !=4:
            error12.append(f"Error in line {l[1]} : {l[0][0]} must contain 3 parameters")
        
        else:
            p=l[0][1:]
            for i in range(len(p)):
                if p[i] not in reg.keys():
                    error12.append(f"Error in line {l[1]} : operand {i} is not a correct register name")
                   
    if l[0][0] == "mov":
        if len(l[0]) != 3:
            error12.append(f"Error in line {l[1]} : {l[0][0]} must contain 2 parameters")
            
        else:
            p=l[0][1:]
            if p[1][0]=="$":
                if p[0] not in reg.keys():
                    
                   error12.append(f"Error in line {l[1][0]} is not a correct register name")
                if p[1][1:].isdigit() == False:
                    
                    error12.append("no integer value is provided")
                    
            else:
                for i in range(len(p)):
                    if p[i] not in reg.keys():
                        
                        error12.append(f"Error in line {l[1]} : {l[0][2]} is not a correct register name")
    if l[0][0] in ["ld","st"]:
        if len(l[0]) !=3:
           
            error12.append(f"Error in line {l[1]} : {l[0][0]} must contain 2 parameters")
        else:
            p=l[0][1:]
            if p[0] not in reg.keys():
               
                error12.append(f"Error in line {l[1]} : operand 0 is not a correct register name")
            if p[1] not in v.keys():
                
                error12.append(f"error in line {l[1]} : No variable named {p[1]}")
    if l[0][0] in ["div","not","cmp"]:
        if len(l[0]) != 3:
            
            error12.append(f"Error in line {l[1]} : {l[0][0]} must contain 2 parameters")
        else:
            p=l[0][1:]
            for i in range(len(p)):
                if p[i] not in reg.keys():
                   
                    error12.append(f"Error in line {l[1]} : operand is not a correct register name")
    if l[0][0] in ["rs","ls"]:
        if len(l[0]) !=3:
            
            error12.append(f"Error in line {l[1]} : {l[0][0]} must contain 2 parameters")
        else:
            p=l[0][1:]
            if p[0] not in reg.keys():
                
                error12.append(f"Error in line {l[1]} : operand is not a correct register name")
            if p[1][0] != "$":
                
                error12.append(f"Error in line {l[1]} : operand 1 is not a correct immediate value")
            elif p[1][0] == "$" and p[1][1:].isdigit()==False:
               
                error12.append("Error in line {l[1]} : o integer value is provided")

    



def solve (l):
    
    sol=False
    for i  in range (len(l)) :
        if l[i][0][0] in ["jmp" , "jgt" , "jlt"  , "je"] :
            if l[i][0][1]  in labels.keys():
                sol=True
                break
            else:
                 sol=False
        if  not sol and l[i][0][0] in ["jmp" , "jgt" , "jlt"  , "je"] :
            error12.append(f"Error at line {l[i][1]} : Missing label")
        


def hlt_error (l) :
    x = len(l) - 1
    count = 0
    for i in range (x+1):
         if l[i][0][0] == "hlt" :
              count += 1

    if count > 1 :
         error12.append("more than one halt statement")
    elif count == 0:
         error12.append("halt statement not present")
    elif count == 1:
         if l[x][0][0] != "hlt" :
              error12.append("halt is not the last statement")
                
def convert1(a):
    # convert integer to 16 bit binary
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]
    while len(x) < 16:
        x += '0'
    bnr = x[::-1]
    return bnr


def convert(a):
    # convert integer to 7 bit binary
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]
    while len(x) < 7:
        x += '0'
    bnr = x[::-1]
    return bnr


def mov1(l):
    s = "000100"
    s = s + reg[l[1]][0]
    s = s + convert(int(l[2][1:]))
    return s

 
def mov2(l):
    s = "0001100000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    return s


def add(l):
    s = "0000000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    
    return s


def sub(l):
    s = "0000100"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    
    return s


def mul(l):
    s = "0011000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    return s


def div(l):
    s = "0011100000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    return s


def left_shift(l):
    s = "010010"
    s = s + reg[l[1]][0]
    s = s + convert(int(l[2][1:]))
    return s




def right_shift(l):
    s = "010000"
    s = s + reg[l[1]][0]
    s = s + convert(int(l[2][1:]))
    return s


def xor_fnc(l):
    s = "0101000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    return s


def or_fnc(l):
    s = "0101100"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    return s


def and_fnc(l):
    s = "0110000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    return s


def not_fnc(l):
    s = "0110100000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    return s


def load(l):
    s = "001000"
    s = s + reg[l[1]][0]
    s = s + v[l[2]][0]
    return s


def store(l):
    s = "001010"
    s = s + reg[l[1]][0]
    s = s + v[l[2]][0]
    return s


def compare(l):
    s = "0111000000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    return s


def jump_uncond(l):
    s = "011110000"
    s = s + labels[l[1]]
    return s


def jump_if_less(l):
    s = "111000000"
    s = s + labels[l[1]]
    return s


def jump_if_greater(l):
    s = "111010000"
    s = s + labels[l[1]]
    return s


def jump_if_equal(l):
    s = "111110000"
    s = s + labels[l[1]]
    return s
def halt(l):
    return "1101000000000000"


def jump(l):
    curr=l[0][1]
   
    for i in statements.keys():
        
        if statements[i][0][0]==curr:
            global prog_count
            prog_count=i
            break
    else:
        error12.append("No such label found")

labels={} #to store all labels in code
#ret list is for storing the final binary output
ret = []


# # All labels in code
# for i in range(len(statements)):
#     if statements[i][0][0]=='jmp' or statements[i][0][0]=='jlt':
#         labels.append(statements[i][0][1])
#     elif statements[i][0][0]=='jlt' or statements[i][0][0]=='jgt':
#         labels.append(statements[i][0][1]) 
         
# the raise error line was used so that we can raise error during binary creation but then we handled the error generation using aa different fucntion
def main(line):
    if (line[0][0] in op.keys()):
        
        if (line[0][0] == 'mov'):
            if (line[0][2] in reg.keys()):
                ret.append(mov2(line[0]))
            else:
                ret.append(mov1(line[0]))
        elif (line[0][0] == "add"):
                ret.append(add(line[0]))
        elif (line[0][0] == "sub"):
                ret.append(sub(line[0]))
        elif (line[0][0] == "mul"):
                ret.append(mul(line[0]))
        elif (line[0][0] == "div"):
                ret.append(div(line[0]))
        elif (line[0][0] == "ld"):
                ret.append(load(line[0]))
        elif (line[0][0] == "st"):
                ret.append(store(line[0]))
        elif (line[0][0] == "rs"):
                ret.append(right_shift(line[0]))
        elif (line[0][0] == "ls"):
                ret.append(left_shift(line[0]))
        elif (line[0][0] == "or"):
                ret.append(or_fnc(line[0]))
        elif (line[0][0] == "xor"):
                ret.append(xor_fnc(line[0]))
        elif (line[0][0] == "and"):
                ret.append(and_fnc(line[0]))
        elif (line[0][0] == "not"):
                ret.append(not_fnc(line[0]))
        elif (line[0][0] == "cmp"):
                ret.append(compare(line[0]))
        elif (line[0][0] == "jmp"):
                ret.append(jump_uncond(line[0]))
        elif (line[0][0] == "jlt"):
                ret.append(jump_if_less(line[0]))
        elif (line[0][0] == "jgt"):
                ret.append(jump_if_greater(line[0]))
        elif (line[0][0] == "je"):
                ret.append(jump_if_equal(line[0]))
        elif (line[0][0] == "hlt"):
            ret.append(halt(line[0]))
        
    else:
        # raise error
        pass
reserved=["add","sub","mul","div","jmp","jgt","jlt","je","cpm","ld","st","not","xor","or","and","ls","rs","mov","hlt","R0","R1","R2","R3","R4","R5","R6","FLAGS","var"]

# to check if anything other than alphanumeric and _ is used in variable and label names
vname="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_"

#v dictionary to store keys as variable names and values as memory addresses
v = {}
# for i in statements.keys():
#     if (statements[i][0][0] == 'var'):
#         if(statements[i][0][1] in reserved):
#             print("Reserved words cannot be used as variable names line no =>"+str(statements[i][1]))
#             error_in_prog=True
#             break
        
for i in statements.keys():
    if (statements[i][0][0] == 'var'):
        if (len(statements[i][0]) == 1):
            error12.append(f"error in line {statements[i][1]} : No variable name {statements[i][0]}")
            # wer+="Invalid Instruction at line "+str(statements[i][1])+"\n"
            # print("Invalid Instruction at line "+str(statements[i][1]))
#            exit(0)
        if(statements[i][0][1] in reserved):
            error12.append("Reserved words cannot be used as variable names")
            # wer+="Reserved words cannot be used as variable names line no =>"+str(statements[i][1])+"\n"
            # print("Reserved words cannot be used as variable names line no =>"+str(statements[i][1]))
#            exit(0)
        for k in statements[i][0][1]:
            if(k not in vname):
                error12.append("invalid literal in variable names at line ")
                # wer+="invalid literal in variable names at line "+str(statements[i][1])+"\n"
                # print("invalid literal in variable names at line "+str(statements[i][1]))
#               exit(0)
        v[statements[i][0][1]] = 0
    elif (statements[i][0][0][-1:] == ':'):
        if (statements[i][0][0][:-1] in labels):
            error12.append("Two labels with same name -> Invalid Instruction at line ")
            # wer+="Two labels with same name -> Invalid Instruction at line "+str(statements[i][1])+"\n"
            # print("Two labels with same name -> Invalid Instruction at line "+str(statements[i][1]))
#            exit(0)
        if(statements[i][0][0][:-1] in reserved):
            error12.append("Reserved words cannot be used as label names line number")
            # wer+="Reserved words cannot be used as label names line number =>"+str(statements[i][1])+"\n"
            # print("Reserved words cannot be used as label names line number =>"+str(statements[i][1]))
#            exit(0)
        for k in statements[i][0][0][:-1]:
            if(k not in vname):
                error12.append("invalid literal in label names at line ")
        # binary conversion
        labels[statements[i][0][0][:-1]] = convert(int(i) - len(v))
        del statements[i][0][0]

    


#assinging addresses to variables
k = 0
for i in v.keys():
    # binary
    v[i] = [convert(len(statements) - len(v) + k), ""]
    k += 1

# Define a function that extracts the line number from each error string
def get_line_number(error_string):
    return int(error_string.split()[3])



# ************************error checking *********************************


spaceerror() # functio to check if multiple spaces are entered
checkr()    # to check if variables are decleared after an instruction of some opcode is given
check_digit(statements)
solve (statements)
invalid_op(statements)
check_flg(statements)
for i in statements.keys():
    error1(statements[i])

hlt_error(statements)


if len(error12) != 0:


# Print the sorted list

    for error in  range(len(error12)):
        print(error12[error])
        if error != len(error12) - 1:
            print("\n")




# if no error found binary file creation starts and then printing it

else:
    
    for prog_count in statements.keys():
        present=False
        for i in labels.keys():

            if str(i)==str(statements[prog_count][0][0][0:-1]):
                present=True
            else:
                present=False
        if not present:
            main([statements[prog_count][0]])
    
        elif present:
        
            main([statements[prog_count][0][1::]])
    
    
    for j in range(len(ret)):
        print(ret[j])
        if j != len(ret)-1:
             print("\n")
       
