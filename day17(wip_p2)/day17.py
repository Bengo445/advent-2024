
_input = open("input.txt", "r").read().split("\n\n")

regs = []
for line in _input[0].split("\n"):
    regs.append(int(line.split(": ")[1]))
instructions = list(map(int, _input[1].strip("Program: ").split(",") ))

inst_pointer = 0
output = ""

def get_combo(combo:int):
    if combo <= 3: return combo
    elif combo <= 6: return regs[combo-4]
    else: print("invalid combo operand"); return False

def adv(combo:int):
    val = regs[0]/(pow(2,get_combo(combo)))
    regs[0] = int(val)
def bxl(literal:int):
    regs[1] = regs[1] ^ literal
def bst(combo:int):
    regs[1] = get_combo(combo) % 8
def jnz(literal:int):
    global inst_pointer
    if regs[0] != 0:
        inst_pointer = literal
    else:
        inst_pointer += 2
def bxc(ignore:int):
    regs[1] = regs[1] ^ regs[2]
def out(combo:int):
    global output
    val = get_combo(combo) % 8
    output += str(val) + ","
def bdv(combo:int):
    val = regs[0]/(pow(2,get_combo(combo)))
    regs[1] = int(val)
def cdv(combo:int):
    val = regs[0]/(pow(2,get_combo(combo)))
    regs[2] = int(val)

OP = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


while inst_pointer < len(instructions):
    instruction = instructions[inst_pointer]
    operand = instructions[inst_pointer+1]


    print(f"p:{inst_pointer} inst:{instruction}({OP[instruction].__name__}) oper:{operand} regs:{regs}")

    OP[instruction](operand)

    if instruction != 3:
        inst_pointer += 2



print(inst_pointer, regs)
print(output.strip(","))