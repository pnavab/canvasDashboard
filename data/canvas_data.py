import sys
sys.path.append('/home/pablo/projects/duoBypass')
import requests
import json
import util.constants as constants

def getJsonData():
    try:
        response = requests.get(
            constants.URL,
            params=constants.PARAMS,
            headers=constants.HEADER
        )
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# print(getJsonData())