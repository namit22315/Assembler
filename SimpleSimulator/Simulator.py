statements = {}
var = 0
pc = "0000000" 
reg = {'000': "0000000000000000",
       '001': "0000000000000000",
       '010': "0000000000000000",
       '011': "0000000000000000",
       '100': "0000000000000000",
       '101': "0000000000000000",
       '110': "0000000000000000",
       '111': "0000000000000000"}

def remove_newline(line):
    if line.endswith('\n'):
        line = line[:-1]
    if line.endswith('\r'):
        line = line[:-1]
    return line

def Convert_to_16bit(a):

    bnr = bin(a).replace('0b', '')
    ans = bnr[::-1]  
    while len(ans) < 16:
        ans += '0'
    bnr = ans[::-1]
    return bnr


def convert_to_7bit(a):

    bnr = bin(a).replace('0b', '')
    ans = bnr[::-1]  
    while len(ans) < 7:
        ans += '0'
    bnr = ans[::-1]
    return bnr

while (True):
    try:
        line = input().strip()
        if(line!=""):

            line = remove_newline(line)
            k = convert_to_7bit(var)
            statements[k] = line

            var += 1
    except EOFError:
        break

MEM = statements.copy()
mlen = len(MEM)
while (mlen <= 127):
    MEM[convert_to_7bit(mlen)] = "0000000000000000"
    mlen+=1

def mov1(l,pc):
    reg["111"]="0000000000000000"
    reg[l[6:9]]=Convert_to_16bit(int(l[8:]))
    return convert_to_7bit(int(pc,2)+1)


def mov2 (l,pc):
    reg[l[10:13]]=Convert_to_16bit(int(reg[l[13:16]]))
    reg["111"]="0000000000000000"
    return convert_to_7bit(int(pc,2)+1)

def Mul_ (l,pc):
    reg["111"] = "0000000000000000"
    n1 = int(reg[l[10:13]], 2)
    n2 = int(reg[l[13:16]], 2)
    x = (n1 * n2)
    y = bin(x)
    if len(y) > 18:
        reg[l[7:10]]=y[-16:]
        reg['111'] = Convert_to_16bit(int(reg['111'], 2) + 8)

    else:
        reg[l[7:10]] = Convert_to_16bit(x)
    return convert_to_7bit(int(pc,2)+1)

def Div_ ( l,pc):
    reg["111"]="0000000000000000"
    n1 = int(reg[l[10:13]], 2)
    n2 = int(reg[l[13:16]], 2)
    x = (n1 // n2)
    y = n1 % n2
    x = Convert_to_16bit(x)
    y = Convert_to_16bit(y)
    reg["000"]=x
    reg["001"]=y
    return convert_to_7bit(int(pc,2)+1)
def Add_ (l,pc):
    reg["111"] = "0000000000000000"
    n1 = int(reg[l[10:13]], 2)
    n2 = int(reg[l[13:16]], 2)
    x = (n1 + n2)
    y = bin(x)
    if len(y) > 18:
        reg[l[7:10]] = y[-16:]
        reg['111'] = Convert_to_16bit(int(reg['111'], 2) + 8)
    else:
        reg[l[7:10]] = Convert_to_16bit(x)
    return convert_to_7bit(int(pc, 2) + 1)

def Sub_ (l,pc):
    reg["111"] = "0000000000000000"
    n1 = int(reg[l[10:13]], 2)
    n2 = int(reg[l[13:16]], 2)
    x = (n1 - n2)
    if x < 0:
        reg[l[7:10]] ="0000000000000000"
        reg['111'] = Convert_to_16bit(int(reg['111'], 2) + 8)
    else:
        reg[l[7:10]] = Convert_to_16bit(x)
    return convert_to_7bit(int(pc,2)+1)

    return convert_to_7bit(int(pc,2)+1)

def LeftShift (l,pc):
    reg["111"] = "0000000000000000"
    x = int(reg[l[6:9]], 2) << int(l[9:], 2)
    x = Convert_to_16bit(x)
    if (len(x) > 16):
        reg['111'] = (bin(int(reg['111'], 2) + 8))[2:]
    else:
        reg[l[6:9]] = x
    return convert_to_7bit(int(pc,2)+1)

def RightShift (l,pc):
    reg["111"] = "0000000000000000"
    x = int(reg[l[6:9]], 2) >> int(l[9:], 2)
    x = Convert_to_16bit(x)
    reg[l[6:9]] = x
    return convert_to_7bit(int(pc,2)+1)


def xOR_(l,pc):
    reg["111"] = "0000000000000000"
    reg[l[7:10]] = Convert_to_16bit(int(reg[l[10:13]], 2) ^ int(reg[l[13:]], 2))
    return convert_to_7bit(int(pc,2)+1)

def OR_(l,pc):
    reg["111"] = "0000000000000000"
    reg[l[7:10]] = Convert_to_16bit(int(reg[l[10:13]], 2) | int(reg[l[13:]], 2))
    return convert_to_7bit(int(pc,2)+1)

# def div(l,pc):
#     reg["111"]="0000000000000000"
#     n1 = int(reg[l[10:13]], 2)
#     n2 = int(reg[l[13:16]], 2)
#     if n2==0:
#         reg["000"]="0000000000000000"
#         reg["001"]='0000000000000000'
#         reg['111'] = Convert_to_16bit(int(reg['111'], 2) + 8)
#     else:
#         x = (n1 // n2)
#         y = n1 % n2
#         print( x )
#         x = Convert_to_16bit(x)
#         y = Convert_to_16bit(y)
#         reg["000"]=x
#         reg["001"]=y
#     return Convert_to_16bit(int(pc,2)+1)

def And_(l,pc):
    reg["111"] = "0000000000000000"
    reg[l[7:10]] = Convert_to_16bit(int(reg[l[10:13]], 2) & int(reg[l[13:]], 2))

    return convert_to_7bit(int(pc,2)+1)
def Not_(l,pc):
    
    reg["111"] = "0000000000000000"
    lam=Convert_to_16bit(int(reg[l[13:]], 2))
    lam=lam.replace("0","2")
    lam=lam.replace("1","0")
    lam=lam.replace("2","1")
    reg[l[10:13]] = lam
    return convert_to_7bit(int(pc,2)+1)

def Jump(l,pc):
    return l[9:]

def JumpIfLess(l,pc):
    if (reg['111'][-3] == '1'):
        return l[9:]
    else:
        return convert_to_7bit(int(pc, 2) + 1)


def JumpIfGreater(l,pc):
    if (reg['111'][-2] == '1'):
        return l[9:]
    return convert_to_7bit(int(pc,2)+1)


def JumpIfEqual(l,pc):
    if (reg['111'][-1] == '1'):
        return l[9:]
    return convert_to_7bit(int(pc, 2) + 1)

def Load_(l,pc):
    reg["111"] = "0000000000000000"
    reg[l[6:9]] = MEM[l[9:16]]

    return convert_to_7bit(int(pc,2)+1)

def Store_(l,pc):
    reg["111"] = "0000000000000000"
    MEM[l[9:]] = reg[l[6:9]]

    return convert_to_7bit(int(pc,2)+1)

def _Compare(l,pc):

    reg['111'] = '0000000000000000'
    if int(reg[l[10:13]], 2) == int(reg[l[13:16]], 2):
        reg['111'] = Convert_to_16bit(int(reg['111'], 2) + 1)
    elif int(reg[l[10:13]], 2) > int(reg[l[13:16]], 2):
        reg['111'] = Convert_to_16bit(int(reg['111'], 2) + 2)
    elif int(reg[l[10:13]], 2) < int(reg[l[13:16]], 2):
        reg['111'] = Convert_to_16bit(int(reg['111'], 2) + 4)
    return convert_to_7bit(int(pc,2)+1)



def Halt(pc):
    RfDump()
    print()
    return pc

def PcDump(pc):
    print(str(pc),end="        ")


def MemDump():
    for i in MEM.keys():
        print(MEM[i])


def RfDump():
    for i in reg.keys():
        print(reg[i],end=" ")
    print()

def solve(pc):
    c=0
    while(1):
    
        if pc.endswith('\n') or pc.endswith('\r'):
            pc = pc[:-1]
        if len(pc) > 7:
            pc = pc [1:]

        
        c += 1
        PcDump(pc)
        if(pc == convert_to_7bit(len(statements)-1)):
            RfDump()
            break
        if (statements[pc[0:7]][0:5] == "00000"):
            pc=Add_(statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "00001"):
            pc = Sub_ (statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "00010"):
            pc=mov1(statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "00011"):
            pc=mov2(statements[pc[0:7]],pc)
        elif (statements[pc[0:7]][0:5] == "00100"):
            pc = Load_ (statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "00101"):
            pc=Store_(statements[pc[0:7]],pc)
        elif (statements[pc[0:7]][0:5] == "00110"):
            pc = Mul_(statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "00111"):
            pc=Div_(statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "01000"):
            pc=RightShift(statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "01001"):
            pc=LeftShift(statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "01010"):
            pc=xOR_(statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "01011"):
            pc=OR_(statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "01100"):
            pc=And_(statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "01101"):
            pc=Not_(statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "01110"):
            pc=_Compare(statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "01111"):
            pc=Jump(statements[pc],pc)
        elif (statements[pc[0:7]][0:5] == "11100"):          
            pc=JumpIfLess(statements[pc],pc)
            reg["111"] = "0000000000000000"
        elif (statements[pc[0:7]][0:5] == "11101"):      
            pc=JumpIfGreater(statements[pc],pc)
            reg["111"] = "0000000000000000"
        elif (statements[pc[0:7]][0:5] == "11111"):        
            pc=JumpIfEqual(statements[pc],pc)
            reg["111"] = "0000000000000000"
        elif (statements[pc[0:7]][0:5] == "11010"):        
            pc=Halt(pc)
            RfDump()
            break
        RfDump()
        if len (statements) == c:
            break
    MemDump()
solve(pc)
