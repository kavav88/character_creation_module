from random import randint


def attack(char_name, char_class):
    desc_action = 'нанёс урон противнику равный'
    if char_class == 'warrior':
        return f'{char_name} {desc_action} {5 + randint(3, 5)}'
    if char_class == 'mage':
        return f'{char_name} {desc_action} {5 + randint(5, 10)}'
    if char_class == 'healer':
        return f'{char_name} {desc_action} {5 + randint(-3, -1)}'
    return f'{char_name} не аттаковал'


def defence(char_name, char_class):
    if char_class == 'warrior':
        return f'{char_name} блокировал {10 + randint(5, 10)} урона'
    if char_class == 'mage':
        return f'{char_name} блокировал {10 + randint(-2, 2)} урона'
    if char_class == 'healer':
        return f'{char_name} блокировал {10 + randint(2, 5)} урона'
    return f'{char_name} не заблокировал урон'


def special(char_name, char_class):
    desc_action = 'применил специальное умение'
    if char_class == 'warrior':
        return f'{char_name} {desc_action} «Выносливость {80 + 25}»'
    if char_class == 'mage':
        return f'{char_name} {desc_action} «Атака {5 + 40}»'
    if char_class == 'healer':
        return f'{char_name} {desc_action} «Защита {10 + 30}»'
    return (f'{char_name} не {desc_action}')


def start_training(char_name, char_class):
    desc_request = 'Введи одну из команд:'
    desc_attack = 'attack — чтобы атаковать противника'
    desc_defence = 'defence — чтобы блокировать атаку противника'
    desc_special = 'special — чтобы использовать свою суперсилу'
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(f'{desc_request} {desc_attack}, {desc_defence} или {desc_special}.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
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


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
