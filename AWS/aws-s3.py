
##task5  create a data frame of your choice , generate 100 rows and then load into s3
import pandas as pd
import boto3
import io
import numpy as np

# create a DataFrame with 100 rows and 5 columns of random data
data = {
    'col1': np.random.randint(0, 100, 100),
    'col2': np.random.randint(0, 100, 100),
    'col3': np.random.randint(0, 100, 100),
    'col4': np.random.randint(0, 100, 100),
    'col5': np.random.randint(0, 100, 100),
}

df = pd.DataFrame(data)

# save the DataFrame to a CSV file
csv_buffer = io.StringIO()
df.to_csv(csv_buffer, index=False)

# upload the CSV file to an S3 bucket
s3 = boto3.resource('s3')
bucket_name = 'my-bucket-name'
file_name = 'my-file-name.csv'
s3.Object(bucket_name, file_name).put(Body=csv_buffer.getvalue())



