class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_data = [Person(name=d["name"], age=d["age"]) for d in people]
    for i, v in enumerate(people):
        if v.get("wife"):
            person_data[i].wife = Person.people[v["wife"]]
        elif v.get("husband"):
            person_data[i].husband = Person.people[v["husband"]]


    print(person_data)

    return person_data
