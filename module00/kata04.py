kata = (0, 4, 132.42222, 10000, 12345.67)

one = "{:.2e}".format(kata[3])
two = "{:.2e}".format(kata[4])

print(f"module_{kata[0]:02}, ex_{kata[1]:02} : {round(kata[2], 2)}, {one}, {two}")