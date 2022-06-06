num_db = int(input("Input number of product"))
all_prodacts = []
data_base = ()
i1 = 0
for i in range(0, num_db):
    name = input("Input name") #введите наименование продукта
    price = input("Input price") #введите цену родукта
    quantity = input("Input quantity") #введите количество
    pieces = input("Input pieces") # введите единицы измерения
    data_base = (i, {"name": name, "price":price,"quantity":quantity, "pieces":pieces})
    all_prodacts.append(data_base)
product_dict = {'name':[], 'price':[], 'quantity':[], 'pieces':[]}
for my in all_prodacts:
    product_dict['name'].append(my[1]['name'])
    product_dict['price'].append(my[1]['price'])
    product_dict['quantity'].append(my[1]['quantity'])
    product_dict['pieces'].append(my[1]['pieces'])
print(product_dict)
