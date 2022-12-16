def decimal_to_binary(decimal: int) -> str:
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary


def binary_to_decimal(binary: str) -> int:
    decimal = 0
    # for i in binary:
    #     decimal *= 2
    #     decimal += int(i)
    binary = binary[::-1]
    for i, el in enumerate(binary):
        decimal += int(el) * (2 ** i)
    return decimal


def text_to_morse(text: str) -> str:
    morses_code = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': ' '
    }
    text = text.upper()
    morse = ''
    for i in text:
        morse += morses_code.get(i, '')
        morse += ' '
    return morse


def morse_to_text(morse: str) -> str:
    morse = morse.replace('   ', ' | ')
    morses_code = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': '|'
    }
    text = ''
    for el in morse.split():
        for key, val in morses_code.items():
            if el == val:
                text += key
                continue
    return text


def offset_list(lst: list, offset: int) -> list:
    if abs(offset) < len(lst):
        return lst[-offset:] + lst[:-offset]
    if abs(offset) == len(lst):
        return lst
    if abs(offset) > len(lst):
        offset -= (offset // len(lst)) * len(lst)
        return lst[-offset:] + lst[:-offset]


lst = [1, 2, 3, 4, 'dsfgsd', 'dsfgdsfg', 'sdfg', 3, 4, 5, 'sdfgsdfg', 'dfgsdfg']


# lst = list(filter(lambda x: isinstance(x, str), lst))
# print(lst)


def filter_list(lst: list) -> list:
    # i = 0
    # while i < len(lst):
    #     if not isinstance(lst[i], str):
    #         del lst[i]
    #     else:
    #         i += 1
    for i in range(len(lst) - 1, -1, -1):
        if not isinstance(lst[i], str):
            del lst[i]
    return lst


def reverse_list(lst: list) -> list:
    for i in range(len(lst) // 2):
        lst[i], lst[~i] = lst[~i], lst[i]
    return lst


numbers = [5, 6, 3, 6, 3, 65, 3, 6, 3, 6, 7, 21, 5, 3, 6, 4, 5, 658, 4, 68]
numbers.sort(key=lambda x: True if x % 2 else False)


def sum_of_neighbors(numbers: list[int]) -> list[int]:
    result = []
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            result.append(numbers[i-1] + numbers[0])
        else:
            result.append(numbers[i-1] + numbers[i+1])
    return result


def find_country(city: str) -> str | None:
    countries = {
        'Belarus': ['Minsk', 'Gomel', 'Mogilev', 'Brest'],
        'Russia': ['Moscow', 'SPB', 'Kaliningrad'],
        'Poland': ['Vroclav', 'Varshawa']
    }
    for country, cities in countries.items():
        if city in cities:
            return country


def filter_users(users: dict[int, dict[str, str]]) -> list[str]:
    result = []
    for user in users.values():
        if not user.get('email'):
            result.append(user['name'])
    return result


users = {
    1: {
        'name': 'name1',
        'email': 'email@email.com'
    },
    2: {
        'name': 'name2',
        'email': ''
    },
    3: {
        'name': 'name3',
        'email': None
    },
    4: {
        'name': 'name4'
    },
}
users = list(filter(lambda x: not x.get('email'), users.values()))


# SMS — может нести в себе информацию длиною 140 байт, цифры,
# символы и буквы латинского алфавита занимают 1 байт,
# русские же буквы занимают 2 байт
# На вход подается текст, необходимо сказать, на сколько SMS-ок
# данное сообщение будет разбито для отправки


def sms_spliter(sms: str) -> int:
    from string import printable
    bytes_count = len(sms.encode())
    # bytes_count = 0
    # for el in sms:
    #     bytes_count += 1 if el in printable else 2
    count = bytes_count / 140
    if count.is_integer():
        return int(count)
    else:
        return int(count) + 1


# ВВОДИТСЯ СУММА, ВВОДИТСЯ ПРОЦЕНТНАЯ СТАВКА, СКАЗАТЬ ЧЕРЕЗ СКОЛЬКО ЛЕТ
# ВКЛАД УВЕЛИЧИТСЯ МИНИМУМ ВДВОЕ (КАПИТАЛИЗАЦИЯ)


def deposit_calculator(deposit: float, percent: float) -> int:
    year = 0
    percent += 1
    double_deposit = deposit * 2
    while deposit < double_deposit:
        deposit *= percent
        year += 1
    return year


# На вход поступает количество секунд, сказать сколько это часов:минут:секунд
# пример: 7336 → 02:02:16


def time_from_seconds(seconds: int) -> str:
    hour = seconds // 3600
    seconds %= 3600
    minute = seconds // 60
    seconds %= 60
    hour = str(hour).zfill(2)
    minute = str(minute).zfill(2)
    minute = str(minute).zfill(2)
    seconds = str(seconds).zfill(2)
    time = f'{hour}:{minute}:{seconds}'
    return time
