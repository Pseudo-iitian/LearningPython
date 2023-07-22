# Example 1: Accepts items with the small letter “o” in the new list

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
nameswith_o = [item for item in names if "o" in item]
print(nameswith_o)

# Example 2: Accepts items which have more than 4 letters
namesgreaterthan4 = [item for item in names if len(item)>4]
print(namesgreaterthan4)
