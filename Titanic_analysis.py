import pandas as pd
df= pd.read_csv("train.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.columns)
df["Age"]=df["Age"].fillna(df["Age"].median())
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
print(df["Cabin"].isnull().sum())
df["Cabinknown"]=df["Cabin"].notna().astype(int)
print(df["Cabinknown"].value_counts())
print(df["Survived"].value_counts())
survival_rate=df["Survived"].mean()*100
print(f"overall survival rate: {survival_rate:.2f}%")
print(df.groupby("Sex")["Survived"].mean().mul(100).round(2))
print(df.groupby("Pclass")["Survived"].mean().mul(100).round(2))
import matplotlib.pyplot as plt
survival_by_class = df.groupby("Pclass")["Survived"].mean() * 100
survival_by_class.plot(kind="bar")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")
plt.show()
survival_by_gender = df.groupby("Sex")["Survived"].mean() * 100
survival_by_gender.plot(kind="bar")
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.show()
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate (%)")
plt.show()
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 12, 18, 35, 60, 100],
    labels=["Child", "Teen", "Young Adult", "Adult", "Senior"])
print(df["AgeGroup"].value_counts())
survival_by_age = df.groupby("AgeGroup", observed=True)["Survived"].mean() * 100
print(survival_by_age.round(2))
survival_by_age = df.groupby("AgeGroup", observed=True)["Survived"].mean() * 100
survival_by_age.plot(kind="bar")
plt.title("Survival Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Survival Rate (%)")
plt.show()
survival_gender_class = df.groupby(["Pclass", "Sex"])["Survived"].mean() * 100
print(survival_gender_class.round(2))
survival_gender_class = df.groupby(  ["Pclass", "Sex"])["Survived"].mean() * 100
survival_gender_class.unstack().plot(kind="bar")
plt.title("Survival Rate by Gender and Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")
plt.legend(title="Gender")
plt.show()
