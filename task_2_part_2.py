# Import necesaty libraries for the task

import pandas as pd

# Load the data
data = pd.read_excel('data.xlsx')

### data checking #############################################################

# Check for null values and print a summary, sinde the data doesn't have null values there is not manipulation needed
 
# null_summary = data.isnull().sum()
# print("Null values summary:")
# print(null_summary)

# I used this part of the code to check if I needed to change the datatype of the time column 

# print("Data types:")
# print(data.dtypes)

####################################################################

# Change the datatype of the time column 
data['time'] = pd.to_datetime(data['time'])

# Create a new column for the 15-minute time buckets
data['time_bucket'] = data['time'].dt.floor('15T')

# Group by the 15-minute time buckets and calculate total sales and transaction counts
result = data.groupby('time_bucket').agg({'sales': 'sum','time': 'count'}).reset_index() # Count the number of transactions in each time bucket

# Rename columns as the example format
result.columns = ['Time', 'Sales', 'Transcations']

# Ensure the 'Time' column is in the format provided 
result['Time'] = result['Time'].dt.strftime('%Y-%m-%dT%H:%M:%S.0000000Z')

# Write the results to a CSV file
result.to_csv('sales_transactions_every_15_minutes.csv', index=False)