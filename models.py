våra_anställda = ["Kalle", "Amanda", "Sergei", "Adam"]
anstallda_id = 10
anstallda = {
    "person1": {
        "namn": "Anna Svensson",
        "alder": 34,
        "roll": "Data Scientist",
        "erfarenhet_år": 10
    },
    "person2": {
        "namn": "Björn Larsson",
        "alder": 42,
        "roll": "AI Forskare",
        "erfarenhet_år": 15
    },
    "person3": {
        "namn": "Cecilia Öberg",
        "alder": 38,
        "roll": "Systemutvecklare",
        "erfarenhet_år": 12
    },
    "person4": {
        "namn": "David Karlsson",
        "alder": 45,
        "roll": "Projektledare",
        "erfarenhet_år": 18
    },
    # Lägg till fler anställda efter behov
}
class Person:
    def __init__(self, name:str, age:int, length:int) -> None:
        self.name = name
        self.age = age
        self.length = length

class ListOfPersons:
    _list = []

    @classmethod
    def get_list(cls)->list:
        return cls._list.copy()