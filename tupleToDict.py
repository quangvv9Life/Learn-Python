# (74, 'Sinh tố Detox thơm ngon thanh lọc cơ thể', 'Sữa chua ', 'yogurt', 'Yogurt', None, None, None, None, None, '1 cup', '1', 'nu.totalFat', '0 g', 10)

# (74, 'Sinh tố Detox thơm ngon thanh lọc cơ thể', 'Sữa chua ', 'yogurt', 'Yogurt', None, None, None, None, None, '1 cup', '1', 'nu.totalProt', '0 g', 10)

# (74, 'Sinh tố Detox thơm ngon thanh lọc cơ thể', 'Sữa chua ', 'yogurt', 'Yogurt', None, None, None, None, None, '1 cup', '1', 'nu.totalCarb', '0 g', 10)


# def conversion(tup, dict):
#     for x, y, z in tup:
#         dict.setdefault(x, []).append(y,z)
#     return dict


# tups = [("Boba", 21,22,23), ("Din", 19,22,23), ("Grogu", 46,22,23), ("Ahsoka", 11,22,23)]

# dictionary = {}
# print(conversion(tups, dictionary))

tup = ((11, "eleven"), (21, "mike"), (19, "dustin"), (46, "caleb"))
print(tup)

dct = dict(map(reversed, tup))
print(dct)