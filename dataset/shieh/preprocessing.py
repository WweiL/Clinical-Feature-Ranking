import pandas as pd

path = "/home/yui/Desktop/r-project/dataset/shieh/raw/pone.0233188.s002.xlsx"

df = pd.read_excel(path)

name = "Tainan2020dataset"

df1 = pd.DataFrame(columns=["sex_1male_0female", "age", "dose", "PFS", "surgery", "volume", "death_status", "overall_survival_years", "chemotherapy_yes1_no0", "chemotherapy_group", "diagnostic_year", "TMZ"])

print("shieh - Tainan2020dataset")
print("old data sample:")
print(df.sample(1))

df1["sex_1male_0female"] = df["gender"]
df1["age"] = df["age"]
df1["chemotherapy_yes1_no0"] = df["Chemo"]
df1["dose"] = df["dose"]
df1["PFS"] = df["PFS"]
df1["surgery"] = df["surgery"]
df1["volume"] = df["volume"]
df1["death_status"] = df["statusOS"]
df1["overall_survival_years"] = df["OS"]
df1["chemotherapy_group"] = df["Chemogroup"]
df1["diagnostic_year"] = df["diagnostic year"]
df1["TMZ"] = df["TMZ"]

print("new data sample:")
print(df1.sample(1))

df1.to_csv("/home/yui/Desktop/r-project/dataset/shieh/processed/" + name + ".csv", index=False)
df1.to_csv("/home/yui/Desktop/r-project/glioblastomaEHRsData/data-raw/" + name + ".csv", index=False)