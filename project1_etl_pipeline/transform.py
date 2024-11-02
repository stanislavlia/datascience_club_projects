import country_converter as coco

country = ["USA", "Russia", "Japan", "Germany"]
iso_standard = "ISO2"

for c in country:
    print(c, coco.convert(c, to=iso_standard))


#Datetime
import pandas as pd
import json
from datetime import datetime

with open("batch50users.json", "r") as f:
    batch = json.load(f)


date_registration = batch["users"][2]["date_of_registration"]
date_registration = datetime.fromisoformat(date_registration.replace("Z", "+00:00"))

print(date_registration.year)
print(date_registration.month)
print(date_registration.day)
print(date_registration.hour)
print(date_registration.minute)

    
    
df = pd.DataFrame(batch["users"])

print(df.head(3))
    
