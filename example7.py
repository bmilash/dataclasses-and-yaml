# example6.py: program configuration data class, read it in from YAML, and
# override some settings on the command line.

from dataclasses import dataclass
import yaml
import argparse

# Define our program's configuration data class.
@dataclass
class Config:
	statistic: str='t-test'
	alpha: float=0.05
	paired: bool=False
	alternative: str='two-sided'

# Read in our saved configuration object. If the file isn't found create
# a default configuration.
try:
	config = yaml.load( open("saved_config.yaml","r"), Loader=yaml.Loader )
except FileNotFoundError:
	config = Config()

# Create a command line argument parser.
parser=argparse.ArgumentParser( prog='example6.py',
	description='Example showing dataclasses and argument parsing' )
parser.add_argument("--alpha", 
	type=float, 
	default=config.alpha,
	help="significant (alpha) level")

# Parse the command line arguments.
args = parser.parse_args()

# Override the config values we read in from the file.
config.alpha=args.alpha

print(config)

# Finally - save our configuration for re-use in a later run.
yaml.dump( config, open("saved_config.yaml","w") )
