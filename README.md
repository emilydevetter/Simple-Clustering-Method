# Simple Clustering Method

Github repository: *github.com/yourAccount/Name-of-App* *(provide the link to the repository where the code of the App
can be found)*

## Description

A simple clustering method for location-based data. Outputs two CSV files that groups GPS point together based on
avergage nearest neighbor distance.

## Documentation

This app will find the nearest neighbor distance for each GPS Point, take the average nearest neighbor distance for the
dataset, use that average as the radius of a buffer, buffer each GPS point, and group GPS points together if their
buffers overlap.

### Application scope

#### Generality of App usability

This app was designed for the analysis of black bear movement data associated with the UW- Stevens Point Black Bear
Project. Compatability with other projects unknown.

#### Required data properties

This app should work for terrestrial, non-migratory, animal movement data.

### Input type

`MovingPandas.TrajectoryCollection`

### Output type

`MovingPandas.TrajectoryCollection`

### Artefacts

`details.csv`: csv-file that lists rows within the dataframe that are within the average nearest neighbor distance of
another row of data.

`summary.csv`: csv-file that tacks-on an additional column of data that groups rows of data that are within the average
nearest neighbor distance together with a number.

### Settings

`Timestamp Range` (Timestamprange): The period of time you are interested in clustering points together.

### Changes in output data

This app produces an entirely new summary csv-file that includes `Row`, `NeighborCount`, and `NeighborRows` columns and
does not include the inputed dataframe.

This app produces a details csv-file that tacks on a `CenterRow` column that groups GPS points together by assigning a
number to GPS points that fall within the average nearest neighbor distance of other GPS points.

### Most common errors

Code written with specific column titles in mind. "Latitude[deg], Longitude[deg]" are transformed into "lat and lon".
This could make the app incompatible with some datasets.

### Null or err[app-configuration.json](app-configuration.json)or handling

**Setting `Timestamp Range`:** If no dates are specified, the app will run the entire dataset, which may produce an
inaccurate average nearest neighbor distance and therefore illogical clusters if the animal of interest was relocated by
humans due to a nusiance concern or hibernating.  
