import boto3
import csv
from io import StringIO

# S3 bucket details
bucket_name = 'my-demospotify-bucket'
file_key = 'spotify_top_1000_tracks.csv'  # double-check if it ends in .csv

# Create an S3 client
s3_client = boto3.client('s3')

# Get the CSV object
response = s3_client.get_object(Bucket=bucket_name, Key=file_key)

# Read the file content into a string
csv_data = response['Body'].read().decode('utf-8')

# Use StringIO to create a file-like object
csv_file = StringIO(csv_data)

# Read the CSV data using csv.reader
csv_reader = csv.reader(csv_file)

# Get the header
header = next(csv_reader)
print("Header:", header)

# Print the first 5 rows
print("\nFirst 5 rows of the CSV:")
for i, row in enumerate(csv_reader):
    if i < 5:  # Print only first 5 rows
        print(row)
    else:
        break
