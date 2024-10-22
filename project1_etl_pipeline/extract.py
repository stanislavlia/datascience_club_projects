
import os
import click
import requests
import logging
import tqdm
import datetime
import json
from pprint import pprint

# TODO
# 1) Use click
# 2) Make api calls Asynchronous



SOURCE_API_URL="https://randomuser.me/api/"
FETCH_N_DOCS=10
RETRIEVED_DATA_DIR="./data/"

def fetch_user_from_api(url : str, timeout : int = 1):
    
    user = requests.get(url=url,
                        timeout=timeout,
                        headers={"Authorization" : "Bearer <some_token>"})
    
    user_json = user.json()
    logging.info(f"Status code of request: {user.status_code}")
    
    return user_json


def fetch_batch(url : str, number_of_users : int):
    
    collected_users = []

    for _ in tqdm.tqdm(range(number_of_users), desc=f"Fetching {number_of_users} from API..."):
        
        user = fetch_user_from_api(url=url,
                                   timeout=5)
        
        collected_users.append(user)
    
    
    return collected_users


def load_batch_to_json(users, filepath):
    
    batch = {
        "users_list": users,
        "number_users": len(users),
        "batch_proccessed_ts": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Human-readable timestamp
    }

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(batch, f, ensure_ascii=False, indent=4)

    print(f"Successfully saved {len(users)} users to {filepath}")



if __name__ == "__main__":
    
    users = fetch_batch(url=SOURCE_API_URL, number_of_users=100)
    
    load_batch_to_json(users=users, filepath="./data/users_batch1.json")