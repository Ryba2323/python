
shop_list = []

shop_list.append(input("Co na zakupy?: "))
for lista in shop_list:
    print(lista)
    break



file = open("zakupy.txt", "w")

file.write(lista)

file.close()


