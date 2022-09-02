my_login = 'testrock75@gmail.com'
my_code = '0CC2-4F28-831B'
my_cabinet = 'Личный кабинет'
captain_daughter = 'Капитанская дочка'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


def generate_string(n):
    return 'x' * n


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

list_discount_phone_mail_negative = [
    '', 'testrock75gmail.com', '@gmail.com', 'testrock75@gmail com', 'максим@gmail.com', -1, 0, '+79995', '+79995621',
    '+7999562154', '7544A0C-AE8E', generate_string(1001), russian_chars(), russian_chars().upper(), special_chars()
]


list_my_discount_code_negative = [
    '', -1, 0, '7544A0C-AE8E', generate_string(1001), russian_chars().upper(), special_chars()
]

list_discount_phone_mail_positive = [
    '+79291295001', my_login, my_code
]

list_social_elements = [
    'ВКонтакте', 'ОК', '@mail', 'Яндекс', 'Google'
]

list_header_personal = [
    'Сообщения', 'Мой лабиринт', 'Отложено', 'Корзина'
]

list_header_personal_button_my_maze_dropdown_menu = [
    'Заказы', 'вы смотрели', 'отложенные', 'баланс', 'настройки', 'выход'
]



# idis_list_discount_phone_mail_negative = [
#     'empty_value', 'email_no_name', 'email_no_dot', 'email_cyrillic', 'negative_number', 'zero', 'phone_5_characters',
#     'phone_8_characters', 'phone_10_characters', 'invalid_discount_code', '1001_characters', 'russian',
#     'RASSIAN', 'specials'
# ]
