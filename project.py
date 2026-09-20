# I started by importing 2 major tools that i'll be using for my project (pandas and matplotlib)
# pandas to store my data in tables
# matplotlib to create my ratings chart

"""This code will loads up a chart that will show us whether movies are getting worse over time."""

import pandas as pd
import matplotlib.pyplot as plt

# Here I defined my datafield "tmdb_5000_movies.csv" which i will use to extract my findings
df = pd.read_csv("tmdb_5000_movies.csv")

# This code will allow me to get the year of release for each movie in my data set
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
df = df.dropna(subset=["release_date"])
df["year"] = df["release_date"].dt.year

# This code here allows me to remove unreliable ratings
df = df[df["vote_count"] >= 50]
print("Movies used:", len(df))

# This code allows me to group the data into decades
df["decade"] = (df["year"] // 10) * 10
by_decade = df.groupby("decade")["vote_average"].agg(["mean", "count"])
print(by_decade)

# This code here allows me to draw the chart 'ratings_by_decade' using matplotlib
plt.plot(by_decade.index, by_decade["mean"], marker="o")
plt.xlabel("Decade")
plt.ylabel("Average rating (out of 10)")
plt.title("Are movies getting better or worse over time?")
plt.savefig("ratings_by_decade.png")
plt.show()
