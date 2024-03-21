import numpy as numpy
import pandas as pd

#Part A
#A.)
table = numpy.random.random(15)
table = table * 19 + 1
#reshape 3x5
shapedTable = table.reshape(3, 5)
#print array shape
print(shapedTable.shape)
print(shapedTable)
#replace each max value in each row with 0
shapedTable[numpy.arange(len(shapedTable)), shapedTable.argmax(1)] = 0
print(shapedTable)
#create a 2 dimentional array of size 4x3 with 4 byte integer elements
arr = numpy.zeros((4, 3), dtype = numpy.int32)
print(arr.shape)
print(type(arr))
print(arr.dtype)

#B.)
A = numpy.array([[3, -2],[1, 0]])
eigenvalues, eigenvectors = numpy.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

#C.)
#compute the sum of the diagonal element of a given array
q3Array = numpy.array([[0, 1, 2], [3, 4, 5]])
print(q3Array)
trace = numpy.trace(q3Array)
print("sum:", end='')
print(trace)

#D.)
newShapeArr = numpy.array([[1, 2], [3, 4], [5, 6]])
newShapeArr.reshape(2, 3)
print(newShapeArr)











#Part B
#Read CSV
df = pd.read_csv('/Users/joshuamoore/Downloads/data.csv')

#Show basic statistical description
description = df.describe()
print("Basic Statistical Description:")
print(description)

#Check and replace null values with the mean
if df.isnull().values.any():
    df.fillna(df.mean(), inplace=True)

#Aggregating data using min, max, count, mean for selected columns
aggregated_data = df[['Duration', 'Calories']].agg(['min', 'max', 'count', 'mean'])
print("\nAggregated Data:")
print(aggregated_data)

#Filter dataframe for calories between 500 and 1000
filtered_df_1 = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]

#Filter dataframe for calories > 500 and pulse < 100
filtered_df_2 = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]

#Create new dataframe w/ "Maxpulse" column
df_modified = df.drop(columns=['Maxpulse'])

#Delete "Maxpulse" column from main dataframe df
df.drop(columns=['Maxpulse'], inplace=True)

#Convert datatype of Calories column to int
df['Calories'] = df['Calories'].astype(int)

#Display Stuff
print("\nFiltered DataFrame (calories between 500 and 1000):")
print(filtered_df_1)
print("\nFiltered DataFrame (calories > 500 and pulse < 100):")
print(filtered_df_2)
print("\nModified DataFrame (without 'Maxpulse' column):")
print(df_modified)
print("\nMain DataFrame (with 'Maxpulse' column deleted and Calories as int):")
print(df)