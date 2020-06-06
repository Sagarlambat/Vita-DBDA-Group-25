#To import pandas and read csv file
'''
import pandas as pd
df=pd.read_csv("E:\\Automobile_data.csv")
'''
#Question 1: From given data set print first and last five rows.

'''
print(df.head(5))
print(df.tail(5))
'''
#Question 2: Clean data and update the CSV file.
#df.fillna(0,inplace=True)
#Question 3: Find the most expensive car company name.
'''
car_name=df[['company','price']][df['price']==df['price'].max()]
>>> print(car)
'''
#Question 4: Print All Toyota Cars details.
'''
car_detail=df[df.company=='toyota']
print(car_detail)
'''
#Question 5: Count total cars per company.
'''
count=df['company'].value_counts()
print("Total count as per company:\n",count)
'''
#Question 6: Find each company’s Higesht price car.
'''
car_company=df.groupby('company')
high_price=car_company['company','price'].max()
print(high_price)'
'''
#Question 7: Find the average mileage of each car making company.
'''
car_making=df.groupby('company')
>>> avg_mileage=car_making['company','average-mileage'].mean()
>>> print(avg_mileage)
'''
#Question 8: Sort all cars by Price column.
'''
car_price=df.sort_values(by=['price','company'],ascending=False)
>>> print(car_price)
'''
#Question 9: Concatenate two data frames using the following conditions
#Create two data frames using the following two Dicts, Concatenate those two data frames and create a key for each data frame.
'''
import pandas as pd
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
df1=pd.DataFrame.from_dict(GermanCars)
df2=pd.DataFrame.from_dict(japaneseCars)
df3=pd.concat([df1,df2],keys=['Germany','Japan'])
print(df3)
'''
#Question 10: Merge two data frames using the following condition
#Create two data frames using the following two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.
'''
import pandas as pd
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
Car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
df1=pd.DataFrame.from_dict(Car_Price)
df2=pd.DataFrame.from_dict(Car_Horsepower)
df3=pd.merge(df1,df2,on='company')
print(df3)
'''







