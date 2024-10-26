import requests
from pprint import pprint
import json


r = requests.get('https://randomuser.me/api/')

print("Status code: ", r.status_code)
print(type(r.json()))

user_json = r.json() #dict




def parse_json(user_json: dict) -> dict:
    # Extract ID
    id = user_json["results"][0]["id"]["name"] + " " + user_json["results"][0]["id"]["value"]
    
    # Extract name details
    first_name = user_json["results"][0]["name"]["first"]
    last_name = user_json["results"][0]["name"]["last"]
    
    # Extract location details
    location_city = user_json["results"][0]["location"]["city"]
    location_country = user_json["results"][0]["location"]["country"]
    location_latitude = user_json["results"][0]["location"]["coordinates"]["latitude"]
    location_longitude = user_json["results"][0]["location"]["coordinates"]["longitude"]
    location_postcode = user_json["results"][0]["location"]["postcode"]
    location_state = user_json["results"][0]["location"]["state"]
    location_street_info = f"{user_json['results'][0]['location']['street']['name']}, {user_json['results'][0]['location']['street']['number']}"
    
    # Extract other fields
    email = user_json["results"][0].get("email")
    gender = user_json["results"][0].get("gender")
    
    # Extract login details
    login_uuid = user_json["results"][0]["login"].get("uuid")
    login_username = user_json["results"][0]["login"].get("username")
    login_password = user_json["results"][0]["login"].get("password")
    
    # Extract contact details
    phone = user_json["results"][0].get("phone")
    cell = user_json["results"][0].get("cell")
    
    # Extract date of birth and registration details
    date_of_birth = user_json["results"][0]["dob"].get("date")
    age = user_json["results"][0]["dob"].get("age")
    date_of_registration = user_json["results"][0]["registered"].get("date")
    
    # Extract picture link
    photo_link = user_json["results"][0]["picture"].get("large")
    
    return {
        "id": id,
        "firstname": first_name,
        "lastname": last_name,
        "location_city": location_city,
        "location_country": location_country,
        "location_state": location_state,
        "location_latitude": location_latitude,
        "location_longitude": location_longitude,
        "location_postcode": location_postcode,
        "location_street_info": location_street_info,
        "email": email,
        "gender": gender,
        "login_uuid": login_uuid,
        "login_username": login_username,
        "login_password": login_password,
        "phone": phone,
        "cell": cell,
        "date_of_birth": date_of_birth,
        "age": age,
        "date_of_registration": date_of_registration,
        "photo_link": photo_link
    }


pprint(parse_json(user_json))


# pprint(user_json)

# with open("example.json", "w") as f:
#     json.dump(user_json, f, indent=4)

# print("============================")
# print("Email: ", user_json["results"][0]["email"])
# print("Gender: ", user_json["results"][0]["gender"])
# print("Phonenumber: ", user_json["results"][0]["cell"])
