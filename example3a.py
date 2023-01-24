# example3a.py - python list of objects, and data class defined in
# a separate file.
import yaml

import city

# Create a list of cities.
selected_rmacc_cities = [
	city.City( "Tempe", 33.40, -111.93 ),
	city.City( "Las Cruces", 32.30, -106.77 ),
	city.City( "Boulder", 40.01, -105.25 ),
	city.City( "Salt Lake City", 40.75, -111.88 ),
]

# Save the list to a YAML file.
yaml.dump( selected_rmacc_cities, open("cities.yaml","w") )
