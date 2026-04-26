import pandas as pd 

def sp_tracker(data):
    sp = 0
    ret = []
    for ins in data: 
        if ins["opcode"].startswith("addi") and (ins["args"][0] == "sp" or ins["args"] == "x2"):
            sp = sp + int(ins["args"][2])

        ret.append(sp)

    return ret

def extract_rd_rs(data):
    ret = []

    def get_reg_from_mem(arg):
        # estrae il registro da "offset(reg)" oppure ritorna arg
        if "(" in arg:
            return arg.split("(")[1].replace(")", "")
        return arg

    for ins in data:
        args = ins["args"]

        # sicurezza base (evita index error)
        if len(args) == 0:
            continue

        if ins["category"] == "ALU":
            # rd sempre primo argomento
            rd = args[0]

            rs = []
            if len(args) > 1:
                rs.append(args[1])

            # se NON è immediata (tipo addi) e NON è mv
            if len(args) > 2 and not (ins["opcode"].endswith("i") or ins["opcode"] == "mv"):
                rs.append(args[2])

            ret.append({
                "rd": rd,
                "rs": rs
            })

        elif ins["category"] == "memory_read":
            # lw rd, offset(rs)
            if len(args) > 1:
                rs = get_reg_from_mem(args[1])

                ret.append({
                    "rd": args[0],
                    "rs": [rs]
                })

        elif ins["category"] == "memory_write":
            # sw rs, offset(rd)
            if len(args) > 1:
                rd = get_reg_from_mem(args[1])

                ret.append({
                    "rd": rd,
                    "rs": [args[0]]
                })

    # ---- pandas part ----

    if not ret:
        return pd.DataFrame()

    registers = pd.DataFrame(ret)

    rd_counts = registers["rd"].value_counts()
    rs_counts = registers.explode("rs")["rs"].value_counts()

    union = sorted(set(rd_counts.index) | set(rs_counts.index))

    result = pd.DataFrame({
        "rd": rd_counts,
        "rs": rs_counts
    }).fillna(0).loc[union]

    return result
def build_df(data):
    timeline_sp = sp_tracker(data)
    return (pd.DataFrame(data),timeline_sp)

    
