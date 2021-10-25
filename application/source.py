# Class that  defines 
from enum import Enum

class Source:

    class Category(Enum):
        HOSPITALITY = 'Hospitality'
        PRIVATE = 'Private'
        RDC = 'RDC'
        RETAIL = 'Retail'

    def __init__(self, name: str, catagory: Category) -> None:
        assert type(name) == str
        assert type(catagory) == Source.Category
        self.__name = name
        self.__category = catagory.value

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    def save(self):
        with open('data.csv', 'a') as file:
            file.write(f'"{self.name}","{self.category}"\n')

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', Source.{self.category})"
