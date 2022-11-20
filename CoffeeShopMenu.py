from defs import *
while True:
    choice = buttonbox("Ласкаво просимо в кав'ярню", 'CoffeeShop', ['Перейти до покупки', "Персонал", 'Вихід'],
                       image='images\\212409.gif')
    if choice == 'Перейти до покупки':
        clients_code = discount()
        with open(inventoryPath, "r", encoding='utf-8') as menu:
            base_menu = json.load(menu)
            while choice != 'Відміна':
                choice = buttonbox("Що бажаєте купити?: ", "CoffeeShop", ['Кава', "Смаколики",'Оплата', 'Переглянути кошик', "Відміна"],
                                   image='images\\763a73bb9b8e0bdf01e02f523946a313.gif')
                if choice == "Кава":
                    coffe(choice)

                elif choice == "Смаколики":
                    smacolik(choice)

                elif choice == 'Відміна':
                    cleaning_basket()

                elif choice == 'Переглянути кошик':
                    receipt(clients_code)

                elif choice == 'Оплата':
                    receipt(clients_code)


    elif choice == "Персонал":
        loginPesonal()

    elif choice == 'Вихід':
        break

    else:
        continue