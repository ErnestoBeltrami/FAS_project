import json

def valid(line): 
    line = line.strip()
    if line.startswith(("#",".",":","call")) or line.endswith(":") or not line:
        return False
    else:
        return True

def parse(line): 
    inst = line.split()
    args = inst[1].split(",")

    opcode = inst[0]
    
    category = ""

    if opcode in ["add","sub","or","and","xor","mv","addi","addw"]:
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
    
    result = {
            "opcode": opcode,
            "category": category,
            "args": args
            } 
    
    return result



def main():

    instructions = []

    with open("input.txt") as f:
        for line in f:
            if valid(line) :
                instruction = parse(line)
                if not instruction["category"] == "unknown":
                    instructions.append(instruction)

    with open("instructions.json", "w") as f:
        json.dump(instructions,f,indent=2)

if __name__ == "__main__":
    main()


