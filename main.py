import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data.csv")
print(df)

print(df.head())

print(df.shape)
print(df.info())
print(df.describe())

total_sales = df["Sales"].sum()
print("total_sales:",total_sales)

average_profit = df["Profit"].mean()
print("average profit:",average_profit)

highest_sales = df["Sales"].max()
print("Highest_sales:", highest_sales)

print(df[df["Sales"]==highest_sales])

dept_sales = df.groupby("Department")["Sales"].mean()

print(df.groupby("City")["Profit"].sum())

#visualizations Bar chart
df = pd.read_csv("sales_data.csv")
dept_sales.plot(kind="bar")
plt.title("Average Sales by Department")
plt.xlabel("Department")
plt.ylabel("Average Sales")
plt.savefig("Depart_avg.png")
plt.show()

#Sales Distribution Histogram

sns.histplot(df["Sales"])

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig("Distribution.png")

plt.show()

#Heatmap

corr = df[["Sales", "Profit"]].corr()

print(corr)

sns.heatmap(corr,
            annot=True,
            cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")

plt.show()

