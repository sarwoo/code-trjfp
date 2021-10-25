# Class that  defines 
from enum import Enum

class Source:

    class Category(Enum):
        HOSPITALITY = 1
        PRIVATE = 2
        RDC = 3
        RETAIL = 4
        
    all = []

    def __init__(self, name: str, catagory: Category) -> None:

        assert type(name) == str
        assert type(catagory) == Source.Category

        self.__name = name
        self.__category = catagory

        Source.all.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', Source.{self.category})"

source = Source('Aldi', Source.Category.RETAIL)
print(source)
