from auto_test import auto_test


@auto_test(req="better to mention monkey and bear", overwrite=True)
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
