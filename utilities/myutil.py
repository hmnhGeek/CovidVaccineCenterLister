import pandas as pd

def get_state_id(state_ids, state):
    return state_ids[state_ids["state_name"] == state]["state_id"].tolist()[0]

def get_district_id(district_ids, district):
    return district_ids[district_ids["district_name"] == district]["district_id"].tolist()[0]