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

def build_df():
    data = get_instructions()
    timeline_sp = sp_tracker(data)
    return (pd.DataFrame(data),timeline_sp)

    
