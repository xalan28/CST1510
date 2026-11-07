"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

#==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.DataFrame({
    "labels":["R-001" , "R-002" , "R-003" , "R-004", "R-005"],
    "values":[ 50 , 110 , 95 , 20 , 75],
    "limit" :[100 , 100 , 100 , 100 , 100]
    })
df.to_csv("my_records.csv") 
df = pd.read_csv("my_records.csv")



# your column(s) go here
df["percent"] = (df['values'] / df['limit']) *100
df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >=100 else "WARNING" if p >=90 else "OK")




print(df[df["status"] != "OK"])
counts = df.groupby("status").size()
print(counts) 
df.to_csv("my_records.csv", index=False)

counts.plot(kind="bar")
# plt.title("status count")
# plt.xlabel("Status")
# plt.ylabel("Number of Records")

plt.savefig("records.png")
plt.show()


