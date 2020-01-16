#Create an empty set named showroom.
showroom = set()

#Add four of your favorite car model names to the set.

showroom.add("mustang")
showroom.add("sprinter")
showroom.add("pinto")
showroom.add("corolla")

#Print the length of your set.
print(len(showroom))

#Pick one of the items in your show room and add it to the set again.
showroom.add("mustang")

#Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)

#Using update(), add two more car models to your showroom with another set.
addedModels = ("Delorian", "Tesla Model X")
showroom.update(addedModels)
print(showroom)

#You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("pinto")
print(showroom)