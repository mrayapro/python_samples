print(True and True is {True and True})


print(True and False is {True and False})
print(False and False is {False and False})
print()
print(True or True is {True or True})
print(True or False is {True or False})
print(False or False is {False or False})
print()
print(not True is {not True})
print(not False is {not False})
print()

print(True and not True is {True and not True})  # Always False
print(True or not True is {True or not True})    # Always True

rain = True
snow = False
print((rain and snow) or (not rain and not snow))  # Use brackets to group

print(True is {True and True})
