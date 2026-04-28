import matplotlib.pyplot as plt

def instruction_count(df):
    counts = df["opcode"].value_counts()

    plt.figure(figsize=(8,5))

    bars = plt.bar(counts.index, counts.values)

    for b in bars:
        y = b.get_height()
        plt.text(
            b.get_x() + b.get_width()/2,
            y + 0.5,
            str(int(y)),
            ha='center'
        )

    plt.xlabel("Opcode")
    plt.ylabel("Count")
    plt.title("Instruction frequency")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def sp_timeline(t1,t2):
    plt.plot(t1,color="red",label="non optimized")
    plt.plot(t2,color="blue", label="optimized")
    plt.legend() 
    plt.title("Static Evolution of StackPointer")
    plt.xlabel("Line")
    plt.ylabel("sp_value")
 
    plt.show()

def category_pie(df):
    df["category"].value_counts().plot(kind = "pie")
    plt.show()

def registers_usage(registers):
    registers.plot(kind="bar")
    plt.show()
