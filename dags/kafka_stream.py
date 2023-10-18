import random
import uuid
from datetime import datetime
import requests
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2023, 10, 13, 19, 15)
}

def get_data(city_name):


    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": city_name}

    headers = {
        "X-RapidAPI-Key": "your api key here",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    res = requests.get(url, headers=headers, params=querystring)
    response = res.json()
    return response


def format_data(response):
    data = {}

    location = response['location']
    current = response['current']
    condition = response['current']['condition']

    data['id'] = str(uuid.uuid4())
    data['city'] = location["name"]
    data['region'] = location['region']
    data['latitude'] = location['lat']
    data['longitude'] = location['lon']
    data['temp_c'] = current['temp_c']
    data['last_updated'] = current['last_updated']
    data['condition'] = condition['text']
    data['humidity'] = current['humidity']
    data['feelslike_c'] = current['feelslike_c']


    return data

def stream_data():
    import json
    import time
    from kafka import KafkaProducer

    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time = time.time()
    while True:
        if time.time() > curr_time + 2: #1 minute
            break
        try:
            german_popular_cities= ["Berlin",
                "Hamburg",
                "Munich",
                "Cologne",
                "Frankfurt am Main",
                "Stuttgart",
                "Düsseldorf",
                "Dortmund",
                "Essen",
                "Leipzig",
                "Bremen",
                "Dresden",
                "Hanover",
                "Nuremberg",
                "Duisburg",
                "Bochum",
                "Wuppertal",
                "Bielefeld",
                "Bonn",
                "Münster",
                "Wiesbaden",
                "Schwerin",
                "Mainz",
                "Saarbrücken",
                "Potsdam",
                "Magdeburg",
                "Erfurt",
                "Kiel",
                "Würzburg",
            ]

            city_name = random.choice(german_popular_cities)
            res = get_data(city_name)
            res = format_data(res)
            # print(json.dumps(res, indent=3))
            producer.send('weather_data', json.dumps(res).encode('utf-8'))

        except KeyError as e:
            print(f"KeyError: {e}")
            print("Response structure:")
            print(json.dumps(res, indent=3))



with DAG('weather_automation',
         default_args=default_args,
         schedule='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )
# stream_data()

