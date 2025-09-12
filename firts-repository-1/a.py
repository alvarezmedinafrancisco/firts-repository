nose = int(input("teclea un numero"))
total = 1

for n in range(1, nose + 1):
    total *= n

print("el factorial de", nose, "es", total)
