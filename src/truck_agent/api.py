"""
Data types that are passed to the agents and expected in return
"""
from typing import List, Dict, Literal, Union
from pydantic import BaseModel


# Request and response

class CargoOffer(BaseModel):
    uid: int  # unique cargo id
    origin: str
    dest: str
    name: str
    price: float  # how much do you get for the cargo
    eta_to_cargo: float
    km_to_cargo: float
    km_to_deliver: float
    eta_to_deliver: float


class TruckState(BaseModel):
    balance: float
    uid: int
    loc: str
    hours_since_full_rest: float
    time: float


class DecideRequest(BaseModel):
    truck: TruckState
    offers: List[CargoOffer]


class DecideResponse(BaseModel):
    command: Literal["ROUTE", "DELIVER", "SLEEP"]
    argument: Union[str, int, None] = None


# The world map data can be found in src/resources/map.json
# Also see src/truck_agent/map.py for parsing the file
class Road(BaseModel):
    dest: str
    km: float
    kmh: float
    major: bool


class Location(BaseModel):
    city: str
    country: str
    lat: float
    lng: float
    population: int
    roads: List[Road]
