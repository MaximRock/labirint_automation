my_login = 'testrock75@gmail.com'
my_code = '7546-4A0C-AE8E'
my_cabinet = 'Личный кабинет'
captain_daughter = 'Капитанская дочка'
book_author = 'Пушкин Александр Сергеевич'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


def generate_string(n):
    return 'x' * n


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


"""Для теста авторизации"""
list_discount_phone_mail_negative = [
    '', 'testrock75gmail.com', '@gmail.com', 'testrock75@gmail com', 'максим@gmail.com', -1, 0, '+79995', '+79995621',
    '+7999562154', '7544A0C-AE8E', generate_string(1001), russian_chars(), russian_chars().upper(), special_chars()
]

"""Для теста авторизации"""
list_my_discount_code_negative = [
    '', -1, 0, '7544A0C-AE8E', generate_string(1001), russian_chars().upper(), special_chars()
]

"""Для теста авторизации"""
list_discount_phone_mail_positive = [
    '+79291295001', my_login, my_code
]

"""Для теста авторизации"""
list_social_elements = [
    'ВКонтакте', 'ОК', '@mail', 'Яндекс', 'Google'
]

"""Для теста личного кабинета в header"""
list_header_personal = [
    'Сообщения', 'Мой лабиринт', 'Отложено', 'Корзина'
]

"""Для теста личного кабинета в header ссылка Мой лабиринт"""
list_header_personal_button_my_maze_dropdown_menu = [
    'Заказы', 'вы смотрели', 'отложенные', 'баланс', 'настройки', 'выход'
]

"""Для теста поля Поиск, вводимое значение Капитанская дочка"""
list_of_values_in_the_search_field = [
    'Капитанская Дочка', 'капитанская дочка', 'КАПИТАНСКАЯ ДОЧКА', 'КаПиТаНсКаЯ дОчКа', 'дочка капитанская',
    'rfgbnfycrfz ljxrf', 'каитанская дка', '  капитанская дочка', 'капитанская дочка  ',
    'капитанская    дочка', '|\\/!@#$%^&*()-_=+`~?"№;:[]{}капитанская дочка',
    'капитанская|\\/!@#$%^&*()-_=+`~?"№;:[]{} дочка', 'капитанская дочка|\\/!@#$%^&*()-_=+`~?"№;:[]{}'
]

# idis_list_discount_phone_mail_negative = [
#     'empty_value', 'email_no_name', 'email_no_dot', 'email_cyrillic', 'negative_number', 'zero', 'phone_5_characters',
#     'phone_8_characters', 'phone_10_characters', 'invalid_discount_code', '1001_characters', 'russian',
#     'RASSIAN', 'specials'
# ]
