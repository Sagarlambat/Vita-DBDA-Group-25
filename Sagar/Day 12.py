import pandas as pd
df=pd.read_csv('d:\Automobile_data.csv')

#1.From given data set print first and last five rows.
'''
print(df.head(5))
print(df.tail(5))
'''
#2.Clean data and update the CSV file.
#df.fillna(0,inplace=True)
#3.Find the most expensive car company name.
'''
car_max= df[['company','price']][df['price']==df['price'].max()]
print(car_max)
'''
#4.Print All Toyota Cars details.
'''
c=df[df.company=='toyota']
print(c)
'''
#5.Count total cars per company.
'''
a=df['company'].value_counts()
print(a)
print(df.groupby(['company']).count())
'''
#6.Find each company’s Higesht price car.
'''
a=df.groupby(['company'])[['price']].max()
print(a)
'''
#7.Find the average mileage of each car making company.
'''
a=df.groupby(['company'])[['average-mileage']].mean()
print(a)
'''
#8.Sort all cars by Price column.
'''
a=df.sort_values(['price'])
print(a)
'''
#Question 9: Concatenate two data frames using the following conditions
#Create two data frames using the following two Dicts,
#Concatenate those two data frames and create a key for each data frame.
'''
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
a=pd.DataFrame(GermanCars)
b=pd.DataFrame(japaneseCars)
c=pd.concat([a,b],keys=['Germany','Japan'])
print(c)
'''
#Question 10: Merge two data frames using the following condition
#Create two data frames using the following two Dicts, Merge two data frames,
#and append the second data frame as a new column to the first data frame.
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
Car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
a=pd.DataFrame(Car_Price)
b=pd.DataFrame(Car_Horsepower)
c=pd.merge(a,b,on='Company')
print(c)
