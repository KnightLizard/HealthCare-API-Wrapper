import requests

url = "https://data.healthcare.gov/api/1/metastore/schemas"
res = requests.get(url)

print(res.json())