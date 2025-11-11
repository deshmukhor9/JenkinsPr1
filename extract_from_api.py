import requests
import pandas as pd
import os
token = os.getenv('APP_TOKEN')
response = requests.get('https://jsonplaceholder.typicode.com/users')
data = response.json()
df = pd.DataFrame(data)
print(df[['id','name']])