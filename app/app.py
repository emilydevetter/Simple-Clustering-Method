from sdk.moveapps_spec import hook_impl
from sdk.moveapps_io import MoveAppsIo
from movingpandas import TrajectoryCollection
import logging
import matplotlib.pyplot as plt

# showcase for importing functions from another .py file (in this case from "./app/getGeoDataFrame.py")
from app.getGeoDataFrame import get_GDF


class App(object):

    def __init__(self, moveapps_io):
        self.moveapps_io = moveapps_io

    @hook_impl
    def execute(self, data: TrajectoryCollection, config: dict) -> TrajectoryCollection:

        logging.info(f'Welcome to the {config}')

        import pandas as pd
import numpy as np
import os
from datetime import datetime
from sklearn.neighbors import BallTree

# Read the CSV file. Replace 'your_file.csv' with your file path.


# Make sure your CSV has columns named 'lat' and 'lon'


file_name = input(
    'Enter the black bear sow record (include .csv): ')

df = pd.read_csv(file_name)

# Extract the latitude and longitude columns


lat = df['Latitude[deg]'].values

lon = df['Longitude[deg]'].values

# Combine lat and lon into a single array


latlon = np.column_stack((lat, lon))

latlon_rad = np.radians(latlon)

# Build the BallTree using the haversine metric


tree = BallTree(latlon_rad, metric='haversine')

# Query the tree: k=2 to include the point itself and its nearest neighbor


distances, indices = tree.query(latlon_rad, k=2)

# The first column is distance 0 (self), so take the second column


earth_radius_km = 6371

nn_distances_km = distances[:, 1] * earth_radius_km

# Calculate the average nearest neighbor distance


avg_nn_distance = nn_distances_km.mean()

print("Average nearest neighbor distance (km):", avg_nn_distance)

# ——— Phase 2: Find all neighbors within that radius ———


# Convert avg_nn_distance back into radians

radius_rad = avg_nn_distance / earth_radius_km

# for all points (rows), get all indices (row numbers) of the points that would be within radius_rad (including itself)

indices_within_radius = tree.query_radius(latlon_rad, r=radius_rad)

#

# i = 0

# indices_within_radius = tree.query_radius(latlon_rad, r=radius_rad)

# neighbors = raw_neighbors[raw_neighbors != i]     # drop itself

# df_neighbors = df.iloc[neighbors]

# print(f"\nNeighbors of row {i+1}:")

# print(df_neighbors)


# ——— Build summary & details, print with 1‑based row numbers ———


summary = []

details = []

for idx, raw_neighbors in enumerate(indices_within_radius):

    point_row = idx + 1  # make 1‑based

    neigh_idxs = raw_neighbors[raw_neighbors != idx]

    # Print to screen

    print(

        f"Row {point_row} has {len(neigh_idxs)} neighbors within "

        f"{avg_nn_distance:.2f} km → {[int(n) + 1 for n in neigh_idxs]}"

    )

    # Collect summary info

    summary.append({

        'Row': point_row,

        'NeighborCount': len(neigh_idxs),

        'NeighborRows': ",".join(str(n + 1) for n in neigh_idxs)

    })

    # Collect detailed neighbor rows

    for n in neigh_idxs:
        row = df.iloc[n].copy()

        row['CenterRow'] = point_row

        details.append(row)

# ——— Save to CSV ———


summary_df = pd.DataFrame(summary)

details_df = pd.DataFrame(details)

# 1) Strip off “.csv” from the original name to get a clean base

base, _ = os.path.splitext(file_name)

# 2) Create a timestamp string

ts = datetime.now().strftime("%Y%m%d_%H%M%S")

# 3) Build your output filenames

summary_fname = f"{base}_summary_{ts}.csv"

details_fname = f"{base}_details_{ts}.csv"

# 4) Save to file

summary_df.to_csv(summary_fname, index=False)

details_df.to_csv(details_fname, index=False)

print(f"Saved summary to {summary_fname}")

print(f"Saved details to {details_fname}")

        # showcase injecting App settings (parameter `year`)
        data_gdf = get_GDF(data)  # translate the TrajectoryCollection to a GeoDataFrame
        logging.info(f'Subsetting data for {config["year"]}')
        # subset the data to only contain the specified year
        if config["year"] in data_gdf.index.year:
            result = data_gdf[data_gdf.index.year == config["year"]]
        else:
            result = None

        # showcase creating an artifact
        if result is not None:
            result.plot(column=data.get_traj_id_col(), alpha=0.5)
            plot_file = self.moveapps_io.create_artifacts_file("plot.png")
            plt.savefig(plot_file)
            logging.info(f'saved plot to {plot_file}')
        else:
            logging.warning("Nothing to plot")

        # showcase accessing auxiliary files
        auxiliary_file_a = MoveAppsIo.get_auxiliary_file_path("auxiliary-file-a")
        with open(auxiliary_file_a, 'r') as f:
            logging.info(f.read())

        # Translate the result back to a TrajectoryCollection
        if result is not None:
            result = TrajectoryCollection(
                result,
                traj_id_col=data.get_traj_id_col(),
                t=data.to_point_gdf().index.name,
                crs=data.get_crs()
            )

        # return the resulting data for next Apps in the Workflow
        return result

