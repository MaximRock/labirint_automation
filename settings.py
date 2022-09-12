my_login = 'testrock75@gmail.com'
my_code = '7546-4A0C-AE8E'
my_cabinet = 'Личный кабинет'
book_russian = 'Капитанская дочка'
book_russian1 = 'Капитанская дочка1'
book_author_russian1 = 'Пушкин Александр Сергеевич1'
book_author_english1 = 'Щерба Анастасия Владимировна1'
book_author_russian = 'Пушкин Александр Сергеевич'
book_titles_english = 'Программирование на Python'
book_author_english = 'Щерба Анастасия Владимировна'
book_titles_edgar_raven = 'Ворон'
book_author_edgar_allan_poe = 'По Эдгар Аллан'


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
    '+79291298001', my_login, my_code
]

"""Для теста авторизации, имя файла скринщота"""
list_social_elements = [
    'ВКонтакте', 'ОК', '@mail', 'Яндекс', 'Google'
]

"""Для теста личного кабинета в header, имя файла скринщота"""
list_header_personal = [
    'Сообщения', 'Мой лабиринт', 'Отложено', 'Корзина'
]

"""Для теста личного кабинета в header ссылка Мой лабиринт"""
list_header_personal_button_my_maze_dropdown_menu = [
    'Заказы', 'вы смотрели', 'отложенные', 'баланс', 'настройки', 'выход'
]

"""Для теста поля Поиск, вводимое значение Капитанская дочка"""
list_of_values_in_the_search_field_rassian = [
    'Капитанская Дочка', 'капитанская дочка', 'КАПИТАНСКАЯ ДОЧКА', 'КаПиТаНсКаЯ дОчКа', 'дочка капитанская',
    'rfgbnfycrfz ljxrf', 'каитанская дка', '  капитанская дочка', 'капитанская дочка  ',
    'капитанская    дочка', '|\\/!@#$%^&*()-_=+`~?"№;:[]{}капитанская дочка',
    'капитанская|\\/!@#$%^&*()-_=+`~?"№;:[]{} дочка', 'капитанская дочка|\\/!@#$%^&*()-_=+`~?"№;:[]{}' 'дочка',
    'капитан', 'капитанская', 'Пушкин Александр Сергеевич', 'Пушкин'
]

"""Для теста поля Поиск, вводимое значение Программирование на Python"""
list_of_values_in_the_search_field_english = [
    'Программирование на Python', 'Python программирование', 'Python', 'Программирование',
    'Щерба Анастасия Владимировна', 'Щерба'
]

"""Для теста поля Поиск, вводимое значение 'по эдгар алан ворон', тест 'эдгар ворон' passed, остальные failed"""
list_of_values_in_the_search_field_edgar_allan_poe_raven = [
    'эдгар ворон', 'по ворон', 'по алан ворон', 'алан ворон'
]

"""Для теста поля Поиск, вводимые значения - пустое поле, один пробел, два пробела"""
list_of_values_in_the_search_field_empty_spaces = [
    '', ' ', '  '
]
