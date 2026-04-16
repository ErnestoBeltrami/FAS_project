from analyzer import build_df

def prova(): 
    df = build_df()
    df["category"].value_counts().plot(kind="bar")
    


