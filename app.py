import streamlit as st
import requests
import pandas as pd
import json, datetime

from utilities.myutil import get_state_id, get_district_id

# make api calls
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
states_id_api_r = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states", headers=headers)

state_ids = pd.json_normalize(json.loads(states_id_api_r.content.decode('utf-8'))['states'])

st.markdown("# COVID Vaccine Scheduler")
st.markdown("""View vaccination centers and appointments. Start by selecting state on left panel. 
This page is using official government open source APIs https://apisetu.gov.in/public/marketplace/api/cowin

This application is created by **Himanshu Sharma**. Visit https://github.com/hmnhGeek for more information.
""")

sidebar = st.sidebar
select_state = sidebar.selectbox(
    "Select state",
    state_ids["state_name"].tolist()
)

if select_state:
    id_of_state = get_state_id(state_ids, select_state)
    district_id_api_r = requests.get(f'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{id_of_state}', headers=headers)
    st.title(district_id_api_r.status_code)
    # district_ids = pd.json_normalize(json.loads(district_id_api_r.content.decode('utf-8'))["districts"])

    # select_district = sidebar.selectbox(
    #     "Select district",
    #     district_ids["district_name"].tolist()
    # )

    # if select_district:
    #     id_of_district = get_district_id(district_ids, select_district)
    #     apt_date = sidebar.date_input(
    #         "Choose a date for appointment",
    #         datetime.datetime.now()
    #     )

    #     apt_date = apt_date.strftime("%d-%m-%Y")
    #     appointments_by_district_id_api_r = requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={id_of_district}&date={apt_date}', headers=headers)
    #     appointments_df = pd.json_normalize(json.loads(appointments_by_district_id_api_r.content.decode('utf-8'))["sessions"]) #.drop("session_id", axis=1, inplace=True)

    #     appointments_df.rename({'long': 'lon'}, axis=1, inplace=True)

    #     st.header("All Available appointments")
    #     st.subheader(f'State: {select_state}, District: {select_district}')
    #     st.subheader(f'Appointment Date: {apt_date}')
    #     st.dataframe(appointments_df)

    #     try:
    #         st.header("Vaccine distribution")

    #         st.bar_chart(appointments_df.groupby("vaccine").sum()["available_capacity"])

    #         st.header("Vaccination locations")
    #         st.write("The locations shown are subjected to the co-ordinates provided in the data.")
    #         st.map(appointments_df[["lat", "lon"]])

    #         try:
    #             st.header("Filter data")

    #             b = st.selectbox(
    #                 "Filter by block",
    #                 ["All"] + appointments_df["block_name"].unique().tolist()
    #             )

    #             v = st.selectbox(
    #                 "Select a vaccine",
    #                 ["All"]+appointments_df["vaccine"].unique().tolist()
    #             )

    #             a = st.selectbox(
    #                 "Select min. age limit",
    #                 ["All"]+appointments_df["min_age_limit"].unique().tolist()
    #             )
                
    #             if b != "All" and v != "All"  and a != "All":
    #                 st.dataframe(appointments_df[(appointments_df["vaccine"] == v) & (appointments_df["min_age_limit"] == a) & (appointments_df["block_name"] == b)])
    #             elif b != "All" and v != "All" and a == "All":
    #                 st.dataframe(appointments_df[(appointments_df["block_name"] == b) & (appointments_df["vaccine"] == v)])
    #             elif b != "All" and v == "All" and a != "All":
    #                 st.dataframe(appointments_df[(appointments_df["block_name"] == b) & (appointments_df["min_age_limit"] == a)])
    #             elif b != "All" and v == "All" and a == "All":
    #                 st.dataframe(appointments_df[(appointments_df["block_name"] == b)])
    #             elif b == "All" and v != "All" and a != "All":
    #                 st.dataframe(appointments_df[(appointments_df["vaccine"] == v) & (appointments_df["min_age_limit"] == a)])
    #             elif b == "All" and v != "All" and a == "All":
    #                 st.dataframe(appointments_df[(appointments_df["vaccine"] == v)])
    #             elif b == "All" and v == "All" and a != "All":
    #                 st.dataframe(appointments_df[(appointments_df["min_age_limit"] == a)])
    #             elif b == "All" and v == "All" and a == "All":
    #                 st.dataframe(appointments_df)


    #             st.dataframe(appointments_df[(appointments_df["vaccine"] == chosen_vaccine) & (appointments_df["min_age_limit"] == agelimit) & (appointments_df["block_name"] == block)])
    #         except:
    #             pass
            
    #     except:
    #         pass