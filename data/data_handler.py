import sys
sys.path.append('/home/pablo/projects/duoBypass')
import requests
import json
import util.constants as constants
import datetime
from canvas_data import *

def parse_raw_canvas_data(raw_canvas_json):
    output = {}
    if (len(raw_canvas_json) > 0):
        for assignment in raw_canvas_json:
            assignment_name = assignment['assignment']['name']
            assignment_due_date = assignment['assignment']['all_dates'][0]['due_at']
            assignment_description = assignment['assignment']['description']
            output[assignment_name] = {"due_at": assignment_due_date, "description": assignment_description}
            print(output[assignment_name]['due_at'])
        return output
    else:
        print("no homework")
        
(parse_raw_canvas_data(getJsonData()))