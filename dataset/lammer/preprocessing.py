import pandas as pd

path = "/home/yui/Desktop/r-project/dataset/lammer/raw/pone.0248612.s001.xlsx"

df = pd.read_excel(path)

name = "Munich2019dataset"

print("lammer - Munich2019dataset")
print("old data sample:")
print(df.sample(1))

df1 = pd.DataFrame(columns=["cHsp70_level_high1_low0", "age", "MGMT_methylation_methylated1_unmethylated0", "PFS", "progress_yes1_no0", "sex", "overall_survival_months", "death_status"])

df1["cHsp70_level_high1_low0"] = df["cHsp70"].map({"high": 1, "low": 0})
df1["age"] = df["age [years]"]
df1["MGMT_methylation_methylated1_unmethylated0"] = df["MGMT methylation (1=methylated, 0=unmethylated)"]
df1["PFS"] = df["PFS [months]"]
df1["progress_yes1_no0"] = df["progression (1=yes, 0=no)"]
df1["sex"] = df["sex"]
df1["overall_survival_months"] = df["OS [months]"]
df1["death_status"] = df["OS status (1=deceased, 0=living)"]

print("new data sample:")
print(df1.sample(1))

df1.to_csv("/home/yui/Desktop/r-project/dataset/lammer/processed/" + name + ".csv", index=False)
df1.to_csv("/home/yui/Desktop/r-project/glioblastomaEHRsData/data-raw/" + name + ".csv", index=False)