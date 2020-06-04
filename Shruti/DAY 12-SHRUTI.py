import pandas as pd
df=pd.read_csv("c:\Automobile_data.csv")

#1.
print(df[0:5])
print(df.head(5))
print(df.iloc[0:5])

#3.
car_max= df[['company','price']][df['price']==df['price'].max()]
print("most expensive car company name",car_max)

#4.
x=df[df.company=="toyota"]
print("Toyota company details:",x)

#5.
x=df["company"].value_counts()
print("Total cars per company\n:",x)

#6.
avg_mileage= df['company','average-mileage']
print("most expensive car company name",avg_mileage)

#7.
x=df.groupby(['company'])[['average-mileage']].mean()
print("average mileage of each car making company\n",x)

#8.
x=df.sort_values(by='price')
print("all cars by Price column",x)

#9.
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
x=pd.DataFrame(GermanCars)
y=pd.DataFrame(japaneseCars)
z=pd.concat([x,y],keys=['Germany','Japan'])
print(z)

#10.
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
Car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
x=pd.DataFrame(Car_Price)
y=pd.DataFrame(Car_Horsepower)
z=pd.merge(x,y,on='Company')
print(z)
