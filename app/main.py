class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_person = []
    for dic in people:
        person = Person(name=dic["name"], age=dic["age"])
        list_person.append(person)
    for index, value in enumerate(people):
        for i in range(len(people)):
            if list_person[i].name == value.get("wife"):
                list_person[index].wife = list_person[i]
            elif list_person[i].name == value.get("husband") :
                list_person[index].husband = list_person[i]

    return list_person
