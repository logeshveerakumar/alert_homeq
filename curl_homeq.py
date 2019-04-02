import smtplib
import requests
import json
import sched
import time
import os

API_ENDPOINT = "https://www.homeq.se/api/v1/search/"
headers = {"content-type": "application/json; charset=UTF-8"}
data = {"query": "göteborg", "status": "all", "rooms": {"min": "min", "max": "max"}, "area": {"min": "min", "max": "max"}, "rent": {
    "min": "min", "max": "max"}, "sorting": {"key": "date_publish", "direction": "desc"}, "boolean_flags": [], "exclude_reserved": False}

house_id = []

s = sched.scheduler(time.time, time.sleep)


def do_something(sc):
    r = requests.post(url=API_ENDPOINT, headers=headers, data=json.dumps(data))
    # extracting response text
    results = r.text


    results = json.loads(results)
    results = results["results"]

    for result in results:
        if result not in house_id:
            house_id.append(result)
            try:
                print(result["id"])
            except KeyError as e:
                print(result["estate"])
    
    

    
    s.enter(5, 1, do_something, (sc,))


s.enter(5, 1, do_something, (s,))
s.run()

