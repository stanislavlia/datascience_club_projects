import pandas as pd
import country_converter
from datetime import datetime
import json
import click


def load_batch_to_df(path : str):
    
    with open(path, "r") as file:
        batch_json = json.load(file)

    df = pd.DataFrame(batch_json["users"])
    
    return df


def convert_country_code(country_name : str):
    
    iso_code = country_converter.convert(country_name, to="ISO2")
    return iso_code



def transform_data_batch(df : pd.DataFrame):
    
    #Conversion to float
    df["location_longitude"] = df["location_longitude"].astype(float)
    df["location_latitude"] = df["location_latitude"].astype(float)
    df["country_iso2"] = df["location_country"].apply(convert_country_code)
    
    
    # Parse registration date
    df["date_of_registration"] = pd.to_datetime(df["date_of_registration"])
    df["date_of_birth"] = pd.to_datetime(df["date_of_birth"])
    df["extract_time"] = pd.to_datetime(df["extract_time"])

    df["year_of_registration"] = df["date_of_registration"].dt.year
    df["month_of_registration"] = df["date_of_registration"].dt.month
    df["day_of_registration"] = df["date_of_registration"].dt.day


    df["gender"] = df["gender"].replace({"male" : "M",
                                        "female" : "F"})

    df["password_length"] = df["login_password"].apply(len)
    df["loging_length"] = df["login_username"].apply(len)

    df["transform_timestamp"] = datetime.now()
    
    return df



@click.command()
@click.option('--batch_path', type=str, help='Path to saved json batch')
@click.option('--result_path', type=str, help='Path to save transformed data (CSV)')
def transform_step(batch_path, result_path):
    
    df  = load_batch_to_df(batch_path)
    
    transformed_df = transform_data_batch(df)
    
    
    transformed_df.to_csv(result_path)
    
    
    
transform_step()
        
        