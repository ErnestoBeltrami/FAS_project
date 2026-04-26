import matplotlib.pyplot as plt

def instruction_count(df): 
    df["opcode"].value_counts().plot(kind="bar")
    plt.show() 

def sp_timeline(timeline):
    plt.plot(timeline)
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
