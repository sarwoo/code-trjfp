from enum import Enum, auto

class SourceCategory(Enum):
    HOSPITALITY = auto()
    PRIVATE = auto()
    RDC = auto()
    RETAIL = auto()

class ProductCategory(Enum):
    BAKERY = auto()
    DAIRY = auto()
    DRINKS = auto()
    FRESH_PRODUCE = auto()
    MEAT_FISH_POULTRY_EGGS = auto()
    OTHER = auto()
    PRE_PREPARED_MEALS = auto()

class ProductTemperature(Enum):
    AMBIENT = auto()
    CHILLED = auto()
    FROZEN = auto()

# This isn't right
class Food:

    def __init__(self, source) -> None:
        self.source_category = source

food = Food(SourceCategory.HOSPITALITY)


print(food.source_category)