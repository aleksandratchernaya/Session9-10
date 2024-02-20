import random
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.extend(["eldberry", "fig", "grape"])
fruits += ["honeydew", "kiwi", "lemon"]

print(fruits)

random_fruit = random.choice(fruits)
