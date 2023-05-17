# Definition of City object.
from dataclasses import dataclass

@dataclass 
class City:
    name: str
    latitude: float
    longitude: float
