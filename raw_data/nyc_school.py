import duckdb
import sys

QUERY = "SELECT location_code, location_name, primary_address_line_1 FROM 'https://raw.githubusercontent.com/sahuguet/linked-urban-data/main/raw_data/nyc_school_locations.csv' WHERE Status_descriptions != 'Closed'"
QUERY = "SELECT location_code, location_name, primary_address_line_1 FROnyc_school_locations_unique.csv' WHERE Status_descriptions != 'Closed'"
rows = duckdb.sql(QUERY).fetchall()

PREAMBLE = """
@prefix s: <http://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

"""

statements = []
for row in rows:
    (url, name, address) = row
    statement = f"""
<https://www.schools.nyc.gov/schools/{url}> a s:School;
skos:prefLabel "{name}" ;
s:address [ 				
    a s:PostalAddress ;
    s:streetAddress "{address}" 
] ;
.
"""
    statements.append(statement)

sys.stdout.write(PREAMBLE + "\n".join(statements))