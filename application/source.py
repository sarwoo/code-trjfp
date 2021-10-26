# Class that  defines the source
from enum import Enum


class Source:
    class Category(Enum):
        HOSPITALITY = 'Hospitality'
        PRIVATE = 'Private'
        RDC = 'RDC'
        RETAIL = 'Retail'

    def __init__(self, name: str, category: Category) -> None:
        assert type(name) == str
        assert type(category) == Source.Category
        self.__name = name
        self.__category = category.value

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', Source.{self.category})"

    def save(self):
        with open('data.csv', 'a') as file:
            file.write(f'"{self.name}","{self.category}"\n')


