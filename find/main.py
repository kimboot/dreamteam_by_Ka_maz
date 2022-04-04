def find(array, key):
    for index, a in enumerate(array):
        if a == key:
            return index


array = ["kak", "stop", "sell", "student", "fall", "merc"]
key = "sell"
print(find(array, key))