import pandas as pd

path = "/home/yui/Desktop/r-project/dataset/berendsen/raw/pone.0222717.s001.xlsx"

df = pd.read_excel(path)

name = "Utrecht2019dataset"

print("berendsen - Utrecht2019dataset")
print("old data sample:")
print(df.sample(1))

df1 = pd.DataFrame(columns=["age", "adjuvant_treatment", "biopsy_debulking", "KPS", "SVZ_status", "survival_days_from_surgery", "death_status"])

df1["age"] = df["age"]
df1["adjuvant_treatment"] = df["adjuvant_treatment"]
df1["SVZ_status"] = df["SVZ status"]
df1["biopsy_debulking"] = df["biopsy_debulking"]
df1["KPS"] = df["KPS"]
df1["death_status"] = df["censoring"]
df1["survival_days_from_surgery"] = df["survival "]

print("new data sample:")
print(df1.sample(1))

df1.to_csv("/home/yui/Desktop/r-project/dataset/berendsen/processed/" + name + ".csv", index=False)
df1.to_csv("/home/yui/Desktop/r-project/glioblastomaEHRsData/data-raw/" + name + ".csv", index=False)