from adress import Adress
from mail import Mailing

to_adress = Adress('350024', 'Krasnodar', 'Krasnaya', '120', '16')
from_adress = Adress('350000', 'Krasnoyarsk', 'Golubaya', '100', '160')

result = Mailing(to_adress, from_adress, 1000, 'Заказное письмо')

print(f"{result.track} из {result.from_adress.index}, {result.from_adress.city}, "
      f"{result.from_adress.street}, {result.from_adress.house} - "
      f"{result.from_adress.apartment} в {result.to_adress.index}, "
      f"{result.to_adress.city}, {result.to_adress.house} - "
      f"{result.to_adress.apartment}. Стоимость {result.cost} рублей.")
