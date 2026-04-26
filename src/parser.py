import json

def valid(line): 
    line = line.strip()
    if line.startswith(("#",".",":","call")) or line.endswith(":") or not line:
        return False
    else:
        return True

def parse(line,i): 
    inst = line.split()
    
    if len(inst) >= 2:
        args = inst[1].split(",")

        opcode = inst[0]
        
        category = ""

        if opcode in ["add","sub","or","and","xor","mv","addi","ori","andi","xori","sll","srl","sra","slli","srli","srai"]:
            category = "ALU"

        elif opcode in ["lw","ld"]:
            category = "memory_read"

        elif opcode in ["sw","sd"]:
            category = "memory_write"

        elif opcode.startswith(("j","call","ret","jr")):
            category = "function"

        elif opcode.startswith("b"):
            category = "branch"

        else:
            category = "unknown" 
    
    else:
        opcode = inst[0]
        category = "unknown"
        args = []

    result = {
            "line" : i,
            "opcode": opcode,
            "category": category,
            "args": args
            } 
    
    return result



def get_instructions(filename):

    instructions = []
    i = 0
    with open(filename) as f:
        for line in f:
            if valid(line) :
                instruction = parse(line,i)
                if not instruction["category"] == "unknown":
                    instructions.append(instruction)
                    i = i+1

    return instructions


