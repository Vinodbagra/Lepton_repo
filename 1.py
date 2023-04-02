import requests
from bs4 import BeautifulSoup
import csv

url = "https://stores.vishalmegamart.com/shopping-mart-arjun-nagar-jaipur-30519/home"

access_key = '43c102b047f9912bf7def401e6142450'

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

store_name = soup.find(class_="br-info-card-str-name mb-0").get_text()

store_address = soup.find(class_="mb-2 pb-2 w-100 d-flex br-info-card-str-loc").get_text()

store_timings = soup.find(class_="mb-2 pb-2 w-100 d-flex br-info-card-str-time").get_text()

store_phone_no = soup.find(class_="mb-2 pb-2 w-100 d-flex br-info-card-str-cont").get_text() 

Api_endpoint = f'http://api.positionstack.com/v1/forward?access_key={access_key}&query={store_address}'
res = requests.get(Api_endpoint).json()


if res['data']:
    latitude = res['data'][0]['latitude']
    longitude = res['data'][0]['longitude']
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print(f"Error: Unable to get coordinates from address: {store_address}")



filename = "store_details.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Store Name', 'Address', 'Phone Number', 'Timings','latitude','longitude'])
    writer.writerow([store_name, store_address, store_phone_no, store_timings,latitude,longitude])