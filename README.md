# Kenya Forest Tracker

## 1. What is the problem?

Forest reserves and community groups may organize tree-planting activities, but keeping track of these activities manually can become difficult.

Important information such as **where trees were planted, when they were planted, and how many trees were planted** can end up scattered across notebooks, spreadsheets, or other records.

The Kenya Forest Tracker is a simple application designed to help forest reserves keep organized records of their tree-planting activities, including community and charity events.

---

## 2. What tools did I use?

I used the following tools to build the application:

* **Python** — used to build the application logic.
* **Streamlit** — used to create the web interface.
* **MongoDB** — used to store forest reserve and tree-planting records.
* **PyMongo** — used to connect Python to MongoDB and perform database operations.
* **python-dotenv** — used to manage the MongoDB connection string through environment variables.

The application uses two main collections:

### Forest Reserves

* ID
* Name
* County
* Location

### Planting Records

* ID
* Forest Reserve
* Date
* Number of Trees Planted

The application connects the planting records to the forest reserve they belong to using the forest reserve's MongoDB ID.

---

## 3. What insights or solutions do I want to discover?

The main goal is to make tree-planting records easier to create, access, and maintain.

The application allows users to:

* Register a forest reserve.
* Record a tree-planting activity.
* Record the date of the activity.
* Record the number of trees planted.
* View previous planting activities.
* Update incorrect or changing records.
* Delete records that are no longer needed.

An important future opportunity would be to use the collected records to answer questions such as:

* How many trees has a forest reserve planted over time?
* How frequently are planting activities taking place?
* Which locations are participating in planting activities?
* How many trees are being planted through community events?

This would turn the application from simply storing records into a tool that can help organizations understand their tree-planting activities.

---

## 4. How would a community benefit from this work?

The application provides a simple way for forest reserves and community groups to maintain organized tree-planting records.

Instead of relying entirely on scattered or paper-based records, planting activities can be stored in one database and accessed through the application.

This can help communities:

* **Improve record keeping** by keeping planting information in one place.
* **Reduce manual paperwork** when recording planting activities.
* **Track progress** by keeping a history of planting events.
* **Improve accountability** by maintaining records of when and where planting activities happened.
* **Support future decision-making** by providing historical data that can later be
