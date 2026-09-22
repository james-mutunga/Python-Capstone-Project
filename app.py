import pandas as pd

counties = [
    "Nairobi", "Kisumu", "Kilifi", "Machakos",
    "Nakuru", "Meru", "Kajiado"
]

# Fixed dummy data
data = [
    [1, "Nairobi", 3.2, "forest"],
    [2, "Kisumu", 5.0, "bushland"],
    [3, "Kilifi", 2.1, "grassland"],
    [4, "Machakos", 7.4, "forest"],
    [5, "Nakuru", 1.8, "bushland"],
    [6, "Meru", 4.6, "grassland"],
    [7, "Kajiado", 6.3, "forest"]
]

df = pd.DataFrame(data, columns=["site_id", "county", "area_cleared_ha", "land_type"])

# index=False stops the .csv from creating it's own indexes (?)
df.to_csv("cleared_sites.csv", index=False)

land_types = ["forest", "bushland", "grassland"]

# Show available counties first. the .join function here removes the "[]", quotes and commas
print("Available counties:", ", ".join(counties))

# Ask the user which county they want
county_input = input("Enter a county to check cleared sites: ").strip().title()

# Filter the data from just that county
county_data = df[df["county"] == county_input]

if county_data.empty:
    print(f"No cleared sites found for {county_input}.")
else:
    # Trees per hectare, by land type (our conservative minimum values)
    trees_per_ha = {
        "forest": 400,
        "bushland": 100,
        "grassland": 20
    }

    county_data["trees_owed"] = county_data["area_cleared_ha"] * county_data["land_type"].map(trees_per_ha)

    print(f"\nCleared sites in {county_input}:")
    print(county_data[["site_id", "land_type", "area_cleared_ha", "trees_owed"]])

    total_trees = county_data["trees_owed"].sum()
    print(f"\nTotal trees owed for {county_input}: {int(total_trees)}")

