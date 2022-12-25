from random import randint

# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Define attack function."""
    desc_action: str = 'нанёс урон противнику равный'
    if char_class == 'warrior':
        return f'{char_name} {desc_action} {5 + randint(3, 5)}'
    if char_class == 'mage':
        return f'{char_name} {desc_action} {5 + randint(5, 10)}'
    if char_class == 'healer':
        return f'{char_name} {desc_action} {5 + randint(-3, -1)}'
    return f'{char_name} не аттаковал'


def defence(char_name: str, char_class: str) -> str:
    """Define defence function."""
    if char_class == 'warrior':
        return f'{char_name} блокировал {10 + randint(5, 10)} урона'
    if char_class == 'mage':
        return f'{char_name} блокировал {10 + randint(-2, 2)} урона'
    if char_class == 'healer':
        return f'{char_name} блокировал {10 + randint(2, 5)} урона'
    return f'{char_name} не заблокировал урон'


def special(char_name: str, char_class: str) -> str:
    """Define special function."""
    desc_action: str = 'применил специальное умение'
    if char_class == 'warrior':
        return f'{char_name} {desc_action} «Выносливость {80 + 25}»'
    if char_class == 'mage':
        return f'{char_name} {desc_action} «Атака {5 + 40}»'
    if char_class == 'healer':
        return f'{char_name} {desc_action} «Защита {10 + 30}»'
    return (f'{char_name} не {desc_action}')


def start_training(char_name: str, char_class: str) -> str:
    """Define training start function."""
    desc_request: str = 'Введи одну из команд:'
    desc_attack: str = 'attack — чтобы атаковать противника'
    desc_defence: str = 'defence — чтобы блокировать атаку противника'
    desc_special: str = 'special — чтобы использовать свою суперсилу'
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(f'{desc_request} {desc_attack}, {desc_defence} или {desc_special}.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Define class selection function."""
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя.'
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.'
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель.'
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или любую'
                               'другую кнопку, чтобы выбрать другого'
                               'персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
