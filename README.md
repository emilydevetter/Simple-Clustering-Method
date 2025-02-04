# Name of App *(Give your app a short and informative title. Please adhere to our convention of Title Case without hyphens (e.g. My New App))*

Simple Clustering Method

Github repository: *github.com/yourAccount/Name-of-App* *(provide the link to the repository where the code of the App can be found)*

## Description
A simple clustering method for location-based data.

## Documentation
This app will find the nearest neighbor distance for each GPS Point, take the average nearest neighbor distance for the dataset, use that average as the radius of a buffer, buffer each GPS point, and group GPS points together if their buffers overlap. The clusters will then be color-coded and visualized on a simple map. I imagine using it to make observations about or find patterns regarding how an animal is interacting with the landscape.  

### Application scope
#### Generality of App usability
I am designing this app as part of an internship through my university. Truthfully, I have never coded before and am learning as I go. The underlying purpose of this app is to assist in answering location-based questions proposed by the Wisconsin Black Bear Project. So, if this app is producing no or odd results... bear with me (get it?). 

This app was designed to analyze black bear movement data, maybe it will also work with other critters.  

#### Required data properties
This app should work for terrestrial, non-migratory, animal movement data. 

### Input type
*Indicate which type of input data the App requires.*

*Example*: `MovingPandas.TrajectoryCollection`

### Output type
*Indicate which type of output data the App produces to be passed on to subsequent Apps.*

*Example:* `MovingPandas.TrajectoryCollection`

### Artefacts
*If the App creates artefacts (e.g. csv, pdf, jpeg, shapefiles, etc), please list them here and describe each.*

*Example:* `rest_overview.csv`: csv-file with Table of all rest site properties

### Settings 
*Please list and define all settings/parameters that the App requires to be set by the App user, if necessary including their unit. Please first state the Setting name the user encounters in the Settings menu defined in the appspecs.json, and between brackets the argument used in the Python code to be able to identify it quickly in the code if needed.*

*Example:* `Radius of resting site` (radius): Defined radius the animal has to stay in for a given duration of time for it to be considered resting site. Unit: `metres`.

### Changes in output data
*Specify here how and if the App modifies the input data. Describe clearly what e.g. each additional column means.*

*Examples:*

The App adds to the input data the columns `Max_dist` and `Avg_dist`. They contain the maximum distance to the provided focal location and the average distance to it over all locations. 

The App filterers the input data as selected by the user. 

The output data is the outcome of the model applied to the input data. 

The input data remains unchanged.

### Most common errors
*Please describe shortly what most common errors of the App can be, how they occur and best ways of solving them.*

### Null or error handling
*Please indicate for each setting as well as the input data which behaviour the App is supposed to show in case of errors or NULL values/input. Please also add notes of possible errors that can happen if settings/parameters are improperly set and any other important information that you find the user should be aware of.*

*Example:* **Setting `radius`:** If no radius AND no duration are given, the input data set is returned with a warning. If no radius is given (NULL), but a duration is defined then a default radius of 1000m = 1km is set. 
