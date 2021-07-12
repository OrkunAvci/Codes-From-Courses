import pandas as pd

dummy = {
	'cars': ["BMW", "Volvo", "Ford"],
	'passings': [3, 7, 2]
}
dataframe = pd.DataFrame(dummy)
print(dataframe)

dummy = [1, 7, 2]
series = pd.Series(dummy, index = ["x", "y", "z"])
print(series)

print(dataframe.loc[0])

print(dataframe.loc[range(2)])

dataframe = pd.read_csv("./CSV/data.csv")
print(dataframe)

print(dataframe.info())
