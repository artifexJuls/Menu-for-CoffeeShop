import json
import os.path
import random
import time
from easygui import *

from defs import *

inventoryPath = os.path.join('data', 'Menu.json')
koshel = os.path.join('data', 'KoselAll.json')
clientsPath = os.path.join('data', 'clients_baza.json')
Personal = os.path.join('data', 'Personal.json')
with open(inventoryPath, "r", encoding='utf-8') as menu:
    base_menu = json.load(menu)

coffemenu = ('images\\c5d3533af5a86bd4966d9206c4ddaaee.gif', 'images\\da318526245381.563536837107b.gif',
             'images\\b8a2d007e93b475b92aea523f75feb92.gif')
cmakolikmenu = ('images\\1115353179b2a4213ea888579cf50635.gif', 'images\\original.gif', 'images\\croisant.gif')

while True:
    choice = buttonbox("Ласкаво просимо в кав'ярню", 'CoffeeShop', ['Перейти до покупки', "Персонал", 'Вихід'],
                       image='images\\212409.gif')
    if choice == 'Перейти до покупки':
        with open(inventoryPath, "r", encoding='utf-8') as menu:
            base_menu = json.load(menu)
            while True:
                choice = buttonbox("Що бажаєте купити?: ", "CoffeeShop", ['Кава', "Смаколики", "Відміна"],
                                   image='images\\763a73bb9b8e0bdf01e02f523946a313.gif')
                if choice == "Кава":
                    but = []
                    [but.append(i) for i in base_menu[choice].keys()]
                    but.append("Відміна")
                    lst = ""
                    for txt in base_menu.get(choice):
                        lst += f'{txt} - {base_menu.get(choice).get(txt).get("Ціна")} {base_menu.get(choice).get(txt).get("Валюта")}\n'
                    choise = buttonbox(lst, "CoffeeShop", but, coffemenu)
                    if choise != "Відміна":
                        counting(choice)
                    else:
                        continue

                    choice_of_milk(choice)

                elif choice == "Смаколики":
                    but = []
                    [but.append(i) for i in base_menu[choice].keys()]
                    but.append("Відміна")
                    lst = ""
                    for txt in base_menu.get(choice):
                        lst += f'{txt} - {base_menu.get(choice).get(txt).get("Ціна")} {base_menu.get(choice).get(txt).get("Валюта")}\n'
                    choise = buttonbox(lst, "CoffeeShop", but, cmakolikmenu)
                    if choise != "Відміна":
                        counting(choice)
                    else:
                        continue

                    discount()
                    receipt()
                    msgbox("Відскануйте QR код для оплати", image='images\\56.gif')
                    # pay = input("Зчитування")
                    payment()

                elif choice == 'Відміна':
                    cleaning_basket()
                    break

    elif choice == "Персонал":
        loginPesonal()


    elif choice == 'Вихід':
        break

    else:
        continue