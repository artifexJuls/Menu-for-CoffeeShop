import os.path
import random
import time
from easygui import *
import json


coffemenu = ('images\\c5d3533af5a86bd4966d9206c4ddaaee.gif', 'images\\da318526245381.563536837107b.gif',
             'images\\b8a2d007e93b475b92aea523f75feb92.gif')
cmakolikmenu = ('images\\1115353179b2a4213ea888579cf50635.gif', 'images\\original.gif', 'images\\croisant.gif')


class WorkDataJson:
    def __init__(self):
        self.basket = os.path.join('data', 'basket.json')
        self.clients_base = os.path.join('data', 'clients_base.json')
        self.menu = os.path.join('data', 'menu.json')
        self.staff = os.path.join('data', 'staff.json')

    def read_basket_file(self):
        with open(self.basket, "r", encoding='utf-8') as basket:
            return json.load(basket)

    def read_clients_baza_file(self):
        with open(self.clients_base, "r", encoding='utf-8') as client_data:
            return json.load(client_data)

    def read_menu_file(self):
        with open(self.menu, "r", encoding='utf-8') as menu:
            return json.load(menu)

    def read_staff_file(self):
        with open(self.staff, "r", encoding='utf-8') as staff:
            return json.load(staff)

    def write_basket_file(self, input_data):
        with open(self.basket, "w", encoding='utf-8') as basket:
            json.dump(input_data, basket, ensure_ascii=False)

    def write_clients_baza_file(self, input_data):
        with open(self.clients_base, "w", encoding='utf-8') as client_data:
            json.dump(input_data, client_data, ensure_ascii=False)

    def write_menu_file(self, input_data):
        with open(self.menu, "w", encoding='utf-8') as menu:
            json.dump(input_data, menu, ensure_ascii=False)

    def write_staff_file(self, input_data):
        with open(self.staff, "w", encoding='utf-8') as staff:
            json.dump(input_data, staff, ensure_ascii=False)


def discount():
    key = 0
    choice2 = buttonbox('Чи є у вас карта на знижку?', 'CoffeShop',
                        ['Бажаєте зареєструвати', 'Я маю знижку', 'Продовжити без знижки'],
                        image='images\\signing-icon-anim.gif')
    if choice2 == 'Бажаєте зареєструвати':
        file2 = WorkDataJson().read_clients_baza_file()
        key = random.randrange(1000000, 9999999)
        name = enterbox("Введіть ваше ім`я", cancel_choice='Відміна')
        msgbox(f'{name} Ваш код для знижки - {key}')
        file2[key] = {'Ім`я': name, 'Знижка': 0, 'Сума': 0}
        WorkDataJson().write_clients_baza_file(file2)
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
    elif choice2 == 'Продовжити без знижки':
        clients_code = 0

    return clients_code


# def coffe(choice):
#     but = []
#     [but.append(i) for i in base_menu[choice].keys()]
#     but.append("Відміна")
#     lst = ""
#     for txt in base_menu.get(choice):
#         lst += f'{txt} - {base_menu.get(choice).get(txt).get("Ціна")} {base_menu.get(choice).get(txt).get("Валюта")}\n'
#     choise = buttonbox(lst, "CoffeeShop", but, coffemenu)
#     if choise != "Відміна":
#         counting(choice, choise)
#     elif choise == "Відміна":
#         choice = "Відміна"
#     lst_menu_in_milk = ["Капучино", "Латте", "Флет Уайт", "Раф кава"]
#     if choise in lst_menu_in_milk:
#         choice_of_milk(choise)
#     else:
#         milk_yes_no = buttonbox("Бажаєте молоко до кави?",'Milk',['Так','Ні'],image='images\\35.gif')
#         if milk_yes_no == "Так":
#             choice_of_milk(choise)
#         else:
#             pass
#
# def choice_of_milk(choise):
#     milk = buttonbox(f"З якого молока вам приготувати {choise}", 'Milk',
#                      ['Кокосове', 'Бананове', 'Вівсяне', 'Мигдальне','Простому'], image='images\\37.gif')
#     if milk == 'Кокосове':
#         msgbox(f'Ви вибрали {choise} на Кокосовому молоці', image='images\34.gif')
#     elif milk == 'Бананове':
#         msgbox(f'Ви вибрали {choise} на Банановому молоці', image='images\\33.gif')
#     elif milk == 'Вівсяне':
#         msgbox(f'Ви вибрали {choise} на Вівсяному молоці', image='images\\36.gif')
#     elif milk == 'Мигдальне':
#         msgbox(f'Ви вибрали {choise} на Мигдальному молоці', image='images\\35.gif')
#     elif milk == 'Простому':
#         msgbox(f'Ви вибрали {choise} на Простому молоці', image='images\\35.gif')
#
#     return 'Done'
#
# def smacolik(choice):
#     but = []
#     [but.append(i) for i in base_menu[choice].keys()]
#     but.append("Відміна")
#     lst = ""
#     for txt in base_menu.get(choice):
#         lst += f'{txt} - {base_menu.get(choice).get(txt).get("Ціна")} {base_menu.get(choice).get(txt).get("Валюта")}\n'
#     choise = buttonbox(lst, "CoffeeShop", but, cmakolikmenu)
#     if choise != "Відміна":
#         counting(choice, choise)
#
#
# def counting(choice, choise):                               # choice - вид товару (каваб смаколики), choise - к-ть товару
#     while True:
#         amounts = enterbox(f'Скільки {choise} вам потрібно?')
#         price = base_menu.get(choice).get(choise).get("Ціна")
#         if base_menu.get(choice).get(choise).get("Кількість") >= int(amounts):
#             koshel1 = buttonbox(f"Ви додали до кошика {amounts} {choise}", "CoffeeShop", ["Далі"],
#                                 image='images\\Cjey.gif')
#             with open(koshel, "r", encoding='utf-8') as menu:
#                 data1 = json.load(menu)
#             if choise in data1:
#                 data1[choise]["Кількість"] = data1[choise]["Кількість"] + int(amounts)
#                 data1[choise]["Ціна"] = data1[choise]["Кількість"] * price
#             else:
#                 data1[choise] = {"Кількість": int(amounts), "Ціна": price * int(amounts),
#                                  "Валюта": base_menu.get(choice).get(choise).get("Валюта")}
#             with open(koshel, "w", encoding='utf-8') as menu:
#                 json.dump(data1, menu, ensure_ascii=False)
#             return koshel1
#
#         else:
#             koshel2 = buttonbox(f"На жаль {choise}у такій кількості немає, введіть меншу", "CoffeeShop",
#                                 ["Меню", "Оплата"], image='images\\giphy.gif')
#
# def cleaning_basket():
#     with open(koshel, "r", encoding='utf-8') as menu:
#         data = json.load(menu)
#     data.clear()
#     with open(koshel, "w", encoding='utf-8') as menu:
#         json.dump(data, menu, ensure_ascii=False)
#
#     return 'Done'
#
#
# def smacolik(choice):
#     but = []
#     [but.append(i) for i in base_menu[choice].keys()]
#     but.append("Відміна")
#     lst = ""
#     for txt in base_menu.get(choice):
#         lst += f'{txt} - {base_menu.get(choice).get(txt).get("Ціна")} {base_menu.get(choice).get(txt).get("Валюта")}\n'
#     choise = buttonbox(lst, "CoffeeShop", but, cmakolikmenu)
#     if choise != "Відміна":
#         counting(choice, choise)
#     return "Yes"
#
# def discount():
#     key = 0
#     choice2 = buttonbox('Чи є у вас карта на знижку?', 'CoffeShop',
#                         ['Бажаєте зареєструвати', 'Я маю знижку', 'Продовжити без знижки'],
#                         image='images\\signing-icon-anim.gif')
#     if choice2 == 'Бажаєте зареєструвати':
#         with open(clientsPath, 'r', encoding='utf-8') as file1:
#             file2 = json.load(file1)
#         key = random.randrange(1000000, 9999999)
#         name = enterbox("Введіть ваше ім`я", cancel_choice='Відміна')
#         msgbox(f'{name} Ваш код для знижки - {key}')
#         file2[key] = {'Ім`я': name, 'Знижка': 0, 'Сума': 0}
#         with open(clientsPath, 'w', encoding='utf-8') as file3:
#             json.dump(file2, file3, ensure_ascii=False)
#         clients_code = key
#         discount = 0
#     elif choice2 == 'Я маю знижку':
#         clients_code = enterbox('Введіть свій код на знижку')
#         with open(clientsPath, 'r', encoding='utf-8') as file1:
#             file2 = json.load(file1)
#
#             if str(clients_code) in file2:
#                 discount = file2.get(clients_code).get("Сума") / 500
#                 if discount > 20:
#                     discount = 20
#
#                 name = file2.get(clients_code).get("Імя")
#                 msgbox(f'{name}, знижка {discount}%')
#     elif choice2 == 'Продовжити без знижки':
#         clients_code = 0
#
#     return clients_code
#
#
# def receipt(clients_code):
#     with open(koshel, 'r', encoding='utf8') as file1:
#         pay_k = json.load(file1)
#         summ_tovar = 0.0
#         info_chek = ''
#         for txt in pay_k:
#             info_chek += f'{txt} - {pay_k.get(txt).get("Ціна")} {pay_k.get(txt).get("Валюта")}\n'
#             summ_tovar += pay_k.get(txt).get("Ціна")
#         with open(clientsPath, 'r', encoding='utf8') as file1:
#             pay_r = json.load(file1)
#         if clients_code not in pay_r:
#             info = f'{info_chek} \n Загальна сума покупки = {summ_tovar} \n Ваша знижка: 0%'
#             msgbox(info, 'CoffeeShop', 'Оплата', image='images\\money.gif')
#             discount = 0
#         else:
#             discount = pay_r.get(clients_code).get("Сума") / 500
#             if discount > 20:
#                 discount = 20
#             summ_zn = summ_tovar - (summ_tovar * (discount / 100))
#             info = f'{info_chek} \n Загальна сума покупки = {summ_tovar} \n Ваша знижка:{discount}% \n Сума до оплати з урахування знижки - {summ_zn}'
#             var = buttonbox(info, 'CoffeeShop', ['Оплата', 'Повернутись до покупок', 'Видалити позиції'],
#                             image='images\\money.gif')
#         if var == 'Оплата':
#             payment(clients_code, pay_r, summ_tovar)
#         elif var == 'Повернутись до покупок':
#             pass
#         elif var == 'Видалити позиції':
#             dell_position(pay_k)
#     return discount
#
#
# def dell_position(pay_k):
#     var_choice = multchoicebox('Виберіть позиції для видалення', 'Delete position', pay_k.keys())
#     for i in var_choice:
#         pay_k.pop(i)
#     with open(koshel, 'w', encoding='utf8') as file1:
#         json.dump(pay_k, file1, ensure_ascii=False)
#     return "Yes"
#
#
# def payment(clients_code, pay_r, summ_tovar):
#     msgbox("Відскануйте QR код для оплати", image='images\\56.gif')
#     pay = buttonbox("Пройшла оплата чи ні?", 'Pay', ['Ok', 'No'])
#     if pay == "Ok":
#         if clients_code in pay_r:
#             pay_r[clients_code]['Сума'] = pay_r[clients_code]['Сума'] + summ_tovar
#             with open(clientsPath, 'w', encoding='utf8') as file1:
#                 json.dump(pay_r, file1, ensure_ascii=False)
#         msgbox("Оплата пройшла успішно, Приємного", image='images\\Cjey.gif')
#         del_cosh = {}
#         with open(koshel, 'w', encoding='utf8') as file1:
#             json.dump(del_cosh, file1, ensure_ascii=False)
#         choice = "Відміна"
#         return choice
#
#
#     else:
#         time.sleep(5)
#         del_cosh = {}
#         with open(koshel, 'w', encoding='utf8') as file1:
#             json.dump(del_cosh, file1, ensure_ascii=False)
#
#         msgbox("Термін очікування вичерпано, вас поставлено на лічильник, наші люди йдуть до вас ,АТБ")
#         choice = "Відміна"
#         return choice
#
#
# def loginPersonal():
#     choice_login = multenterbox("Введіть логін та пароль", "CoffeeShop", ["Логін", "Пароль"])
#     with open(Personal, "r", encoding='utf-8') as menu:
#         data = json.load(menu)
#     if choice_login[0] == data.get(choice_login[0])["Login"]:
#         if int(choice_login[1]) == data.get(choice_login[0])["Password"]:
#             return personal_do()
#         else:
#             msgbox("Не вірний пароль", image='images\giphy.gif')
#     else:
#         msgbox("Такого користувача не знайдено", image='images\giphy.gif')
#
#
# def personal_do():
#     choice = buttonbox(f"Вхід дозволено \nНаступні дії?", "CoffeeShop",
#                        ['Склад', "Головна"],
#                        image='images\\smartparcel-empty-box.gif')
#     if choice == 'Склад':
#         storage()
#     elif choice == 'Головна':
#         return 'Ok'
#     else:
#         personal_do()
#
#
# def product():
#     name = buttonbox("Де саме ви хочете додати продукт?", 'New', ['Кава', 'Смаколики', 'Назад'],
#                      images='images\\99ff0608104912d023a5642ee8baf1b0.gif')
#     if name == 'Назад':
#         return storage()
#     list_product = multenterbox("Введіть параметри продукту", "Product", ["Назва", "Ціна", "Валюта", "Кількість"])
#     type_prod = list_product[0]
#     price = float(list_product[1])
#     currency = list_product[2]
#     count_prod = int(list_product[3])
#     with open(inventoryPath, "r", encoding='utf-8') as menu:
#         data = json.load(menu)
#     if name in data:
#         data[name].update({type_prod: {"Назва": type_prod, "Ціна": price, "Валюта": currency, "Кількість": count_prod}})
#     else:
#         data[name] = {type_prod: {"Назва": type_prod, "Ціна": price, "Валюта": currency, "Кількість": count_prod}}
#     with open(inventoryPath, "w", encoding='utf-8') as menu:
#         json.dump(data, menu, ensure_ascii=False)
#
#
# def change(do):
#     while True:
#         with open(inventoryPath, "r", encoding="utf-8") as koshik:
#             data = json.load(koshik)
#         choose_del = multenterbox(f"Введіть назву продукту для того щоб {do}", 'change',
#                                   ['Тип продукту(Кава\Смаколики)', 'Продукт', 'Кількість'])
#         if do == 'Додати':
#             data.get(choose_del[0]).get(choose_del[1])['Кількість'] += int(choose_del[2])
#         elif do == 'Відняти':
#             data.get(choose_del[0]).get(choose_del[1])['Кількість'] -= int(choose_del[2])
#         with open(inventoryPath, "w", encoding="utf-8") as koshik:
#             json.dump(data, koshik, ensure_ascii=False)
#         return 'ok'
#
#
# def storage():
#     with open(inventoryPath, "r", encoding="utf-8") as koshik:
#         data = json.load(koshik)
#     smakol_count = [dat for dat in data['Смаколики']]
#     kava_count = [dat for dat in data['Кава']]
#     smakol = [data['Смаколики'][i]['Кількість'] for i in smakol_count]
#     kava = [data['Кава'][i]['Кількість'] for i in kava_count]
#
#     kava_pars = []
#     smakol_pars = []
#
#     for i in range(len(smakol_count)):
#         kava_pars.append('\n'+kava_count[i] + ' = ' + str(kava[i]) + 'шт')
#         smakol_pars.append(smakol_count[i] + ' = ' + str(smakol[i]) + 'шт')
#
#     for i in range(len(kava_pars)):
#         pars = len(kava_pars[i])
#
#         if pars < 18:
#             result = 18 - len(kava_pars[i])
#             kava_pars[i] += ' ' * result
#
#     all_pars = []
#
#     for i in range(len(kava_pars)):
#         all_pars.append(kava_pars[i] + ' '*10 + smakol_pars[i])
#
#     global magic
#     magic = ' '.join([i for i in all_pars])
#     choose = buttonbox(f"{magic}", 'Склад', ['Назад', 'Додати товар', 'Відняти товар', 'Головна'])
#
#     if choose == 'Назад':
#         return personal_do()
#     elif choose == 'Додати товар':
#         change('Додати')
#     elif choose == 'Відняти товар':
#         change('Відняти')
#     elif choose == 'Головна':
#         return 'Ok'
#
#
# def all_info():
#     with open(koshel, 'r', encoding='utf8') as file1:
#         pay_r = json.load(file1)
#         summ_tovar = 0.0
#         info_chek = ''
#         for txt in pay_r:
#             info_chek += f'{txt} - {pay_r.get(txt).get("Ціна")} {pay_r.get(txt).get("Валюта")}\n'
#             summ_tovar += pay_r.get(txt).get("Ціна")
#         info_chek += f'\nЗагальна сума покупки: {summ_tovar}'
#     msgbox(info_chek, "info")
