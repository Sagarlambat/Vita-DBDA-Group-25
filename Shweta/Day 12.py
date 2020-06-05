#Q1) From given data set print first and last five rows
import pandas as pd
df=pd.read_csv("e:\\Automobile_data.csv")
print(df.head(5))
print(df.tail(5))

#Q2) Clean data and update the CSV file.

#Q3) Find the most expensive car company name.
car=df[['company','price']][df['price']==df['price'].max()]
print(car)

#Q4) Print All Toyota Cars details.
car_details=df[df.company=='toyota']
print("All car details",car_details)

#Q5) Count total cars per company.
c=df["company"].value_counts()
print("Total count per company is:\n",c)

#Q6) Find each company’s Higesht price car.
car=df.groupby(["company"])[["average-mileage"]].mean()
print("Avg mileage of each company is: ",car)

#Q7) Find the average mileage of each car making company.
car=df.groupby(["company"])[["average-mileage"]].mean()
print("Avg mileage of each company is: ",car)

#Q8) Sort all cars by Price column.
car=df.sort_values(['price'])
print("Sorted list is: \n",car)

#Q9) Concatenate two data frames using the following conditions
#Create two data frames using the following two Dicts, Concatenate those two data frames and create a key for each data frame.
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
a=pd.DataFrame(GermanCars)
b=pd.DataFrame(japaneseCars)
c=pd.concat([a,b],keys=["Germany","Japan"])
print(c)

#Q10) Merge two data frames using the following condition
#Create two data frames using the following two Dicts, Merge two data frames, and append the
#second data frame as a new column to the first data frame.
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
x=pd.DataFrame(Car_Price)
y=pd.DataFrame(Car_Horsepower)
z=pd.merge(x,y,on='Company')
print(z)
