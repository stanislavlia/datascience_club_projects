
import os
import click
import requests
import logging
import tqdm
from pprint import pprint

SOURCE_API_URL="https://randomuser.me/api/"
FETCH_N_DOCS=10


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

pprint(fetch_batch(url=SOURCE_API_URL, number_of_users=100))
    
