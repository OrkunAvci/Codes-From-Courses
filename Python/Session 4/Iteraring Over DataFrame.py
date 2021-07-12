import pandas as pd

data = {'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka'],
		'Age': [21, 19, 20, 18],
		'Stream': ['Math', 'Commerce', 'Arts', 'Biology'],
		'Percentage': [88, 92, 95, 70]
}

df = pd.DataFrame(data, columns = ['Name', 'Age', 'Stream', 'Percentage'])
print("Given Dataframe :\n", df)

print("\nIterating over rows using index attribute :")
for i in df.index:
	print(df['Name'][i], df['Stream'][i])

print("\nIterating over rows using loc function :")
for i in range(len(df)):
	print(df.loc[i, "Name"], df.loc[i, "Age"])

print("\nIterating over rows using iloc function :")
for i in range(len(df)) :
	print(df.iloc[i, 0], df.iloc[i, 2])

print("\nIterating over rows using iterrows() method :")
for index, row in df.iterrows():
	print(row["Name"], row["Age"])

print("\nIterating over rows using itertuples() method :")
for row in df.itertuples(index=True, name='Pandas'):
	print(getattr(row, "Name"), getattr(row, "Percentage"))

print("\nIterating over rows using apply function :")
print(df.apply(lambda row: row["Name"] + " " + str(row["Percentage"]), axis=1))
