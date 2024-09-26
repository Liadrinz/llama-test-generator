from auto_test import auto_test


@auto_test(req="test boarder values")
def feed(animal: str, age: int):
    if age < 2:
        return "milk"
    if animal in ["cat", "dog"]:
        return "beef"
    if animal in ["rabbit", "deer"]:
        return "carrot"
    if animal in ["cow", "bull", "sheep", "goat"]:
        return "grass"
    return "water"
