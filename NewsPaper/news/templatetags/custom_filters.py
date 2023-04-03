from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    if isinstance(value, str) and isinstance(arg, int): # проверяем, что value — это точно строка, а arg — точно число, чтобы не возникло курьёзов
        return str(value) * arg
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}') # в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку



@register.filter(name='censor')
def censor(value):
    arStr = str(value).split()
    badWords = ['mat']

    ln = len(badWords)

    filtered_message = ''
    string = ''
    string2 = ''
    subtitle = '*'

    flag = 0
    for i in arStr:
        string += i
        string2 = string.lower()

        for j in badWords:
            if j == string2:
               filtered_message += subtitle * len(string)
               flag -= 1
               string = ''
            if not string2 in j:
                flag += 1

        if flag == ln:
            filtered_message += string
            string = ''

    if string2 != '' and string2 not in arStr:
        filtered_message += string
    elif string2 != '':
        filtered_message += subtitle * len(string)

    return filtered_message