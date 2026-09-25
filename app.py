# I want to create a simple app that helps forest reserves keep track of the trees they plant. e.g for community charity events

# What I want the program to do

# Allow a forest reserve to register their name and county/location
# Add a tree planting record with a date, number of trees planted
# View records - see what they planted and when
# Update record
# Delete a record

# FOREST RESERVE: ID, NAME, COUNTY, LOCATION
# PLANTING RECORD: ID, FOREST RESERVE, DATE, NUMBER OF TREES PLANTED

import os
import streamlit as st
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Get MongoDB connection string
mongo_uri = os.environ.get("MONGO_URI")

# Check if it exists
if not mongo_uri:
    st.error("MONGO_URI is not set.")
    st.stop()

# Connect to MongoDB
client = MongoClient(
    mongo_uri,
    serverSelectionTimeoutMS=5000
)

try:
    client.admin.command("ping")
    st.success("MongoDB connected!")
except Exception as e:
    st.error(f"MongoDB connection failed: {e}")
    st.stop()

# Select a database
db = client["kenya_forest_tracker"]

# Select collections
forest_reserves = db["forest_reserves"]
planting_records = db["planting_records"]

# App title
st.title("Kenya Forest Tracker")

st.write("Keep track of trees planted by forest reserves.")

# Register a forest reserve
st.header("Register a Forest Reserve")

name = st.text_input("Forest reserve name")
county = st.text_input("County")
location = st.text_input("Location")

if st.button("Register Forest Reserve"):

    if not name or not county or not location:
        st.error("Please fill in all fields.")

    else:
        forest_reserve = {
            "name": name,
            "county": county,
            "location": location
        }

        forest_reserves.insert_one(forest_reserve)

        st.success(f"{name} registered successfully!")

# View registered forest reserves

st.header("Forest Reserves")

reserves = list(forest_reserves.find())

if not reserves:
    st.info("No forest reserves registered yet.")
else:
    for reserve in reserves:
        st.write(f"**{reserve['name']}**")
        st.write(f"County: {reserve['county']}")
        st.write(f"Location: {reserve['location']}")
        st.divider()

# Add tree planting record

st.header("Add Tree Planting Record")

reserves = list(forest_reserves.find())

if not reserves:
    st.info("Register a forest reserve first.")
else:
    reserve_names = [reserve["name"] for reserve in reserves]

    selected_reserve = st.selectbox(
        "Forest reserve",
        reserve_names,
        key="add_reserve"
    )

    planting_date = st.date_input("Planting date")

    trees_planted = st.number_input(
        "Number of trees planted",
        min_value=1,
        step=1
    )

    if st.button("Add Planting Record"):

        reserve = next(
            r for r in reserves
            if r["name"] == selected_reserve
        )

        planting_record = {
            "forest_reserve_id": reserve["_id"],
            "date": datetime.combine(
                planting_date,
                datetime.min.time()
            ),
            "trees_planted": trees_planted
        }

        planting_records.insert_one(planting_record)

        st.success("Planting record added successfully!")

# View planting records

st.header("Planting Records")

records = list(planting_records.find())

if not records:
    st.info("No planting records yet.")
else:
    for record in records:

        reserve = forest_reserves.find_one(
            {"_id": record["forest_reserve_id"]}
        )

        st.write(f"**Forest reserve:** {reserve['name']}")
        st.write(f"Date: {record['date'].strftime('%Y-%m-%d')}")
        st.write(f"Trees planted: {record['trees_planted']}")
        st.divider()

# Update planting record

st.header("Update Planting Record")

records = list(planting_records.find())

if not records:
    st.info("No planting records to update.")
else:
    record_options = [
        f"{record['_id']} - {record['trees_planted']} trees"
        for record in records
    ]

    selected_record = st.selectbox(
        "Select a record to update",
        record_options,
        key="update_record"
    )

    record_index = record_options.index(selected_record)
    record = records[record_index]

    new_trees = st.number_input(
        "New number of trees",
        min_value=1,
        value=record["trees_planted"],
        step=1
    )

    if st.button("Update Record"):

        planting_records.update_one(
            {"_id": record["_id"]},
            {"$set": {"trees_planted": new_trees}}
        )

        st.success("Planting record updated successfully!")

# Delete planting record

st.header("Delete Planting Record")

records = list(planting_records.find())

if not records:
    st.info("No planting records to delete.")
else:
    record_options = [
        f"{record['_id']} - {record['trees_planted']} trees"
        for record in records
    ]

    selected_record = st.selectbox(
        "Select a record to delete",
        record_options,
        key="delete_record"
    )

    record_index = record_options.index(selected_record)
    record = records[record_index]

    if st.button("Delete Record"):

        planting_records.delete_one(
            {"_id": record["_id"]}
        )

        st.success("Planting record deleted successfully!")