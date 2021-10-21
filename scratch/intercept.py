# Weight 
# "Date Intercepted","Location","Company","Town/City","Source Category","Temperature","Product","Weight (in grams)","Type"
from dataclasses import dataclass
from enum import Enum, auto

class ProductCategory(Enum):
    BAKERY = 1
    DAIRY = 2
    DRINKS = 3
    FRESH_PRODUCE = 4
    MEAT_FISH_POULTRY_EGGS = 5
    OTHER = 6
    PRE_PREPARED_MEALS = 7

class ProductTemperature(Enum):
    AMBIENT = 1
    CHILLED = 2
    FROZEN = 3

@dataclass
class Donation:
    weight: float
    product: str
    temperature: str
    donation_type: str
    company: str
    source_category: str

    def __

item = Donation(14.5, "bakery", "ambient")

print(item)
