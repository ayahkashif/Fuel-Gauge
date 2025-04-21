#x/y

while True:
    fraction = input("Fraction: ")
    if "/" in fraction:
        x, y = fraction.split("/")
        if x.isdigit() and y.isdigit() and int(x) <= int(y):
            try:
                int(x) / int(y)
            except ZeroDivisionError:
                pass
            else:
                break

x = int(x)
y = int(y)
if (x/y * 100) <= 1:
    print("E")
elif (x/y * 100) >= 99:
    print("F")
else:
    print(round(int(x)/int(y) * 100), "%", sep="")
