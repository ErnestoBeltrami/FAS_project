import pandas as pd 
from parser import get_instructions

def sp_tracker(data):
    sp = 0
    ret = []
    for ins in data: 
        if ins["opcode"].startswith("addi") and (ins["args"][0] == "sp" or ins["args"] == "x2"):
            sp = sp + int(ins["args"][2])

        ret.append(sp)

    return ret

def extract_rd_rs():
    ret = []

    data = get_instructions()
    
    for i in data: 
        if i["category"] == "ALU":
            rs = [i["args"][1]]
            
            if not (i["opcode"].endswith("i") or i["opcode"] == "mv"):
                rs.append(i["args"][2])

            ret.append({
                "rd" : i["args"][0],
                "rs" : rs
                })
        elif i["category"] == "memory_read": 
            offset,rs = i["args"][1].split("(")
            rs = rs.replace(")", "")
            ret.append({
                "rd" : i["args"][0],
                "rs" : [rs]
                })
        elif i["category"] == "memory_write":
            offset,rd = i["args"][1].split("(")
            rd = rd.replace(")", "")
            ret.append({
                "rd" : rd,
                "rs" : [i["args"][0]]
                })

    registers = pd.DataFrame(ret)
    rd = registers["rd"].value_counts()
    rs = registers.explode("rs")["rs"].value_counts()
    
    union = sorted(set(rd.index) | set(rs.index))
    data = pd.DataFrame({
        "rd" : rd,
        "rs" : rs
        }).fillna(0).loc[union]

    return data
            
def build_df():
    data = get_instructions()
    timeline_sp = sp_tracker(data)
    return (pd.DataFrame(data),timeline_sp)

    
