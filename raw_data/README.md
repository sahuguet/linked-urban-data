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

# For Police Precincts

We extract the data from the website. See Colab at https://colab.research.google.com/drive/1QhzfAtsvPhPkf_qgzpXOlkWf6iyWvUEn#scrollTo=mNUSXDlkSLOP .

## Issues
* the RDF is sorting precincts as strings instead of numbers. We don't get the logical sequence, [1, 2, 3, etc.] but [1, 10, 11, etc.]
* the namespace prefix does not work. We have to use the full and long URI. I filed a bug at https://github.com/edmcouncil/rdf-toolkit/issues/74

## TODOS
* format address properly. Currently, this is just TEXT.

# Public Libraries

We extract the data from the respective websites.
1. the opendata datasets are too old.
2. the opendata datasets do not contain the link the branch website

The code is in a [Google Colab](https://colab.research.google.com/drive/1iBsNNLExIAb78PcR-jAhCgQ80qZxNO8l?usp=sharing).

We unify all branches across boroughs using the following URI scheme
```
nyc.gov/libraries/Bk-
nyc.gov/libraries/Bx-
nyc.gov/libraries/M-
nyc.gov/libraries/Q-
nyc.gov/libraries/SI-
```

For each branch we provide

* id
* name
* address
* url
* opening hours (TODO)

## Parks
We get the data from Opendata at https://nycopendata.socrata.com/Recreation/Parks-Properties/enfh-gkve/about_data .

We process the data and generate the TTL triples.
See `parks.ipynb`.

### TODOs
* there are few issues with quotes in the name
* some entries are missing an address
* some entries are not a park or a playground; today default is park
* add polygons
* add amenities