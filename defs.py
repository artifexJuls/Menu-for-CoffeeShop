import os.path
import random
import time
from easygui import *
import json


coffemenu = ('images\\c5d3533af5a86bd4966d9206c4ddaaee.gif', 'images\\da318526245381.563536837107b.gif',
             'images\\b8a2d007e93b475b92aea523f75feb92.gif')
cmakolikmenu = ('images\\1115353179b2a4213ea888579cf50635.gif', 'images\\original.gif', 'images\\croisant.gif')

inventoryPath = os.path.join('data', 'Menu.json')
koshel = os.path.join('data', 'KoselAll.json')
clientsPath = os.path.join('data', 'clients_baza.json')
Personal = os.path.join('data', 'Personal.json')
with open(inventoryPath, "r", encoding='utf-8') as menu:
    base_menu = json.load(menu)

def coffe(choice):
    but = []
    [but.append(i) for i in base_menu[choice].keys()]
    but.append("Відміна")
    lst = ""
    for txt in base_menu.get(choice):
        lst += f'{txt} - {base_menu.get(choice).get(txt).get("Ціна")} {base_menu.get(choice).get(txt).get("Валюта")}\n'
    choise = buttonbox(lst, "CoffeeShop", but, coffemenu)
    if choise != "Відміна":
        counting(choice, choise)
    elif choise == "Відміна":
        choice = "Відміна"
    print("choise", choise)
    lst_menu_in_milk = ["Капучино", "Латте", "Флет Уайт", "Раф кава"]
    if choise in lst_menu_in_milk:
        choice_of_milk(choise)
    else:
        milk_yes_no = buttonbox("Бажаєте молоко до кави?",'Milk',['Так','Ні'],image='images\\35.gif')
        if milk_yes_no == "Так":
            choice_of_milk(choise)
        else:
            pass

def choice_of_milk(choise):
    milk = buttonbox(f"З якого молока вам приготувати {choise}", 'Milk',
                     ['Кокосове', 'Бананове', 'Вівсяне', 'Мигдальне','Простому'], image='images\\37.gif')
    if milk == 'Кокосове':
        msgbox(f'Ви вибрали {choise} на Кокосовому молоці')
    elif milk == 'Бананове':
        msgbox(f'Ви вибрали {choise} на Банановому молоці', image='images\\34.gif')
    elif milk == 'Вівсяне':
        msgbox(f'Ви вибрали {choise} на Вівсяному молоці', image='images\\36.gif')
    elif milk == 'Мигдальне':
        msgbox(f'Ви вибрали {choise} на Мигдальному молоці', image='images\\35.gif')
    elif milk == 'Простому':
        msgbox(f'Ви вибрали {choise} на Простому молоці', image='images\\35.gif')

    return 'Done'

def smacolik(choice):
    but = []
    [but.append(i) for i in base_menu[choice].keys()]
    but.append("Відміна")
    lst = ""
    for txt in base_menu.get(choice):
        lst += f'{txt} - {base_menu.get(choice).get(txt).get("Ціна")} {base_menu.get(choice).get(txt).get("Валюта")}\n'
    choise = buttonbox(lst, "CoffeeShop", but, cmakolikmenu)
    if choise != "Відміна":
        counting(choice, choise)


def counting(choice, choise):
    while True:
        amounts = enterbox(f'Скільки {choise} вам потрібно?')
        price = base_menu.get(choice).get(choise).get("Ціна")
        print(price)
        if base_menu.get(choice).get(choise).get("Кількість") >= int(amounts):
            koshel1 = buttonbox(f"Ви додали до кошика {amounts} {choise}", "CoffeeShop", ["Далі"],
                                image='images\\Cjey.gif')
            with open(koshel, "r", encoding='utf-8') as menu:
                data1 = json.load(menu)
            if choise in data1:
                data1[choise]["Кількість"] = data1[choise]["Кількість"] + int(amounts)
                data1[choise]["Ціна"] = data1[choise]["Кількість"] * price
            else:
                data1[choise] = {"Кількість": int(amounts), "Ціна": price * int(amounts),
                                 "Валюта": base_menu.get(choice).get(choise).get("Валюта")}
            with open(koshel, "w", encoding='utf-8') as menu:
                json.dump(data1, menu, ensure_ascii=False)
            return koshel1

        else:
            koshel2 = buttonbox(f"На жаль {choise}у такій кількості немає, введіть меншу", "CoffeeShop",
                                ["Меню", "Оплата"], image='images\\giphy.gif')

def cleaning_basket():
    with open(koshel, "r", encoding='utf-8') as menu:
        data = json.load(menu)
    data.clear()
    with open(koshel, "w", encoding='utf-8') as menu:
        json.dump(data, menu, ensure_ascii=False)

    return 'Done'


def smacolik(choice):
    but = []
    [but.append(i) for i in base_menu[choice].keys()]
    but.append("Відміна")
    lst = ""
    for txt in base_menu.get(choice):
        lst += f'{txt} - {base_menu.get(choice).get(txt).get("Ціна")} {base_menu.get(choice).get(txt).get("Валюта")}\n'
    choise = buttonbox(lst, "CoffeeShop", but, cmakolikmenu)
    if choise != "Відміна":
        counting(choice, choise)

def discount():
    key = 0
    print("1")
    choice2 = buttonbox('Чи є у вас карта на знижку?', 'CoffeShop',
                        ['Бажаєте зареєструвати', 'Я маю знижку'],
                        image='images\\signing-icon-anim.gif')
    if choice2 == 'Бажаєте зареєструвати':
        with open(clientsPath, 'r', encoding='utf-8') as file1:
            file2 = json.load(file1)
        key = random.randrange(1000000, 9999999)
        name = enterbox("Введіть ваше ім`я")
        msgbox(f'{name} Ваш код для знижки - {key}')
        file2[key] = {'Ім`я': name, 'Знижка': 0, 'Сума': 0}
        with open(clientsPath, 'w', encoding='utf-8') as file3:
            json.dump(file2, file3, ensure_ascii=False)
        clients_code = key
        discount = 0
    elif choice2 == 'Я маю знижку':
        clients_code = enterbox('Введіть свій код на знижку')
        with open(clientsPath, 'r', encoding='utf-8') as file1:
            file2 = json.load(file1)

            if str(clients_code) in file2:
                discount = file2.get(clients_code).get("Сума") / 500
                if discount > 20:
                    discount = 20

                name = file2.get(clients_code).get("Імя")
                msgbox(f'{name}, знижка {discount}%')

    return clients_code


def receipt(discount):
    with open(koshel, 'r', encoding='utf8') as file1:
        pay_r = json.load(file1)
        summ_tovar = 0.0
        info_chek = ''
        for txt in pay_r:
            info_chek += f'{txt} - {pay_r.get(txt).get("Ціна")} {pay_r.get(txt).get("Валюта")}\n'
            summ_tovar += pay_r.get(txt).get("Ціна")
        with open(clientsPath, 'r', encoding='utf8') as file1:
            pay_r = json.load(file1)
        if clients_code not in pay_r:
            msgbox(
                f'{info_chek} \n Загальна сума покупки = {summ_tovar} \n Ваша знижка: 0%',
                'CoffeeShop', 'Оплата', image='images\\money.gif')
        else:
            summ_zn = summ_tovar - (summ_tovar * (discount / 100))
            msgbox(
                f'{info_chek} \n Загальна сума покупки = {summ_tovar} \n Ваша знижка:{discount}% \n Сума до оплати з урахування знижки - {summ_zn}',
                'CoffeeShop', 'Оплата', image='images\\money.gif')
        payment(clients_code, pay_r, summ_tovar)
    return


def payment(clients_code, pay_r, summ_tovar):
    print(pay_r)
    msgbox("Відскануйте QR код для оплати", image='images\\56.gif')
    pay = buttonbox("Пройшла оплата чи ні?",'Pay',['Ok','No'])
    if pay == "Ok":
        if clients_code in pay_r:
            pay_r[clients_code]['Сума'] = pay_r[clients_code]['Сума'] + summ_tovar
            with open(clientsPath, 'w', encoding='utf8') as file1:
                json.dump(pay_r, file1, ensure_ascii=False)
        msgbox("Оплата пройшла успішно, Приємного", image='images\\Cjey.gif')
        del_cosh = {}
        with open(koshel, 'w', encoding='utf8') as file1:
            json.dump(del_cosh, file1, ensure_ascii=False)
        choice = "Відміна"
        return choice


    else:
        time.sleep(5)
        del_cosh = {}
        with open(koshel, 'w', encoding='utf8') as file1:
            json.dump(del_cosh, file1, ensure_ascii=False)

        msgbox("Термін очікування вичерпано, вас поставлено на лічильник, наші люди йдуть до вас ,АТБ")
        choice = "Відміна"
        return choice

def loginPesonal():
    choice_login = multenterbox("Введіть лигін та пароль", "CoffeeShop", ["Логін", "Пароль"])
    with open(Personal, "r", encoding='utf-8') as menu:
        data = json.load(menu)
    if choice_login[0] == data.get(choice_login[0])["Login"]:
        if int(choice_login[1]) == data.get(choice_login[0])["Password"]:
            choice = buttonbox(f"Вхід дозволено \nНаступні дії?", "CoffeeShop", ['Додати товар','Склад','Видалити товар',"Відмінa"],
                               image='images\\smartparcel-empty-box.gif')
            if choice == 'Додати товар':
                coffee1 = product()
            elif choice == 'Склад':
                storage()
            elif choice == 'Видалити товар':
                delete()
            else:
                choice = "Персонал"
        else:
            msgbox("Не вірний пароль", image='images\\giphy.gif')
    else:
        msgbox("Такого користувача не знайдено", image='images\\giphy.gif')


def product(self):
    list_product = multenterbox("Введіть параметри продукту", "Product", ["Тип", "Назва", "Ціна", "Валюта", "Кількість"])
    self.type_prod = list_product[0]
    self.name = list_product[1]
    self.price = float(list_product[2])
    self.currency = list_product[3]
    self.count_prod = int(list_product[4])
    with open(inventoryPath, "r", encoding='utf-8') as menu:
        data = json.load(menu)
    if self.type_prod in data:
        data[self.type_prod].update({self.name: {"Назва": self.name, "Ціна": self.price, "Валюта": self.currency, "Кількість": self.count_prod}})
    else:
        data[self.type_prod] = {self.name: {"Назва": self.name, "Ціна": self.price, "Валюта": self.currency, "Кількість": self.count_prod}}
    with open(inventoryPath, "w", encoding='utf-8') as menu:
        json.dump(data, menu, ensure_ascii=False)
def delete():
    while True:
        with open(koshel, "r", encoding='utf-8') as koshik:
            data = json.load(koshik)
        choose_del = enterbox(f"{[i for i in data]}\nЯкий продукт видаляємо?")
        choose_del2 = enterbox(f"{[i for i in data]}\nКількість продукту, який видаляємо?")
        if data.get(choose_del).get('Кількість') < choose_del2:
            del data[choose_del]
        elif data.get(choose_del).get('Кількість') > choose_del2:
            data.update({choose_del: {'Кількість': choose_del2}})
        else:
            continue
        with open(koshel, 'w', encoding='utf-8') as koshik:
            data1 = json.dump(data, koshik)
        choice = buttonbox(f"Ваш кошик {data1}\nВидалити ще щось?', 'main', ['Так', 'Ні']")
        if choice == 'Так':
            return True
        else:
            return False
def storage():
    with open(koshel, "r", encoding='utf-8') as koshik:
        data = json.load(koshik)
    msgbox(f"{[data.get(k) [data.get(v)] for k,v in data]}")
