# example3b.py - python list of objects, and data class defined in
# a separate file.
import yaml

# Read the list back in from the YAML file.
copy_of_cities = yaml.load( open("cities.yaml","r"), Loader=yaml.Loader )

print("Copy of list of RMACC cities:")
for city in copy_of_cities:
	print(city)
