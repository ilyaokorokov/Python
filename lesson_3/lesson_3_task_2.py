from smartphone import Smartphone

catalog = []

catalog.append(Smartphone('Apple', 'iPhone 15', '89892697101'))
catalog.append(Smartphone('Apple', 'iPhone 14', '88005553535'))
catalog.append(Smartphone('Apple', 'iPhone 13', '+79892697101'))
catalog.append(Smartphone('Apple', 'iPhone 12', '89885556669'))
catalog.append(Smartphone('Apple', 'iPhone 11', '89892690000'))

for item in catalog:
    if item.number[:2] == '+7':
        print(item.brand, '-', item.model, '. ', item.number)
    else:
        print("Номер телефона экземпляра не соответствует формату +7")
        new_number = input("Укажите телефон с +7: ")
        item.number = new_number

print("Обновленный каталог: ")
for item in catalog:
    print(item.brand, '-', item.model, '. ', item.number)
