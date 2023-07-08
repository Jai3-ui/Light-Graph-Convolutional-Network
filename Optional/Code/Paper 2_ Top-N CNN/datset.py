import pandas as pd
df=pd.read_csv("rating.csv")
l=df.values.tolist()
string=""
for i in l:
    x=str(i[0])+" "+str(i[1])+" "+str(i[2])+"\n"
    string+=x
with open("BXBOOK.txt","w") as file:
    file.write(string)