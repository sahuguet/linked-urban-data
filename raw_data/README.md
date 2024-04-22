# For Schools
 
 The raw data comes from the OpenData Portal at https://data.cityofnewyork.us/Education/2019-2020-School-Locations/wg9x-4ke6/about_data .

 However, the dataset contains some duplicates. We remove them using `awk '!seen[$0]++' nyc_school_locations.csv > nyc_school_locations_unique.csv`.

 We manually create a TTL file using `nyc_school.py`: the Python script runs a SQL query against the CSV file to extract the `location_code`, `location_name`, `primary_address_line_1` and then outputs some triples in the TTL format.

 We then normalize the content using `java -jar rdf-toolkit.jar -ibn --source nyc_school.ttl > nyc_school_pretty.ttl`.

 The final triples are in `nyc_school_pretty.ttl`.

 ## Issues
* the orginal data contains duplicates
* the data does not have zip code informaton which is bad for the address
* the data is from 2022

## TODOs
* add more information for each school, e.g. grades, contact information.