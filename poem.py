import time as tm
import random
dictionary = []
def poems():
    global dictionary
    stressed_letters = ['А', 'Я', 'О', 'Ё', 'У', 'Ю', 'Э', 'Е', 'И', 'Ы']
    vowel_letters = ['а', 'я', 'о', 'ё', 'у', 'ю', 'э', 'е', 'и', 'ы']

    #message = 'грЕчка скОро бУдет по сОрок'
    with open('message.txt', 'r', encoding='utf-8') as mes_file:
        message = mes_file.readline()
    print(message)

    final_dict = {'word': '', 'letters': ''}

    # Получение unix-времени и времени в формате гггг-мм-дд чч:мм:сс
    unix_time = int(tm.time())
    # print(unix_time)
    str_date = tm.strftime('%Y-%m-%d %H:%M:%S', tm.localtime(unix_time))
    # print(type(unix_time))
    # print(str_date)
    # Получение времени в формате гггг-мм-дд чч:мм:сс из unix
    t = tm.strptime(str_date, '%Y-%m-%d %H:%M:%S')
    # print(int(tm.mktime(t)))
    key_list = []
    key = "".join(str(unix_time))

    # print('key=', key)

    def dictionary():
        data = []

        with open('dataset.txt', 'r', encoding='utf-8') as dict:
            for row in dict:
                data.append(row)

        # print(data)
        dictionary = []
        for i in data:
            current_word = ''
            for j in i:
                if j != '\n':
                    current_word += j
                else:
                    break
            dictionary.append(current_word)

        for i in dictionary:
            dictionary.remove('')

        return dictionary

    dictionary = dictionary()

    # print(dictionary)

    def get_stressed_syllable(word):
        # получаем номер уданого слога
        # print(word)
        count = 0
        stressed_letter_num = 0
        # print(count)
        for i in word:
            if i in vowel_letters:
                count += 1
                # print(count, i)
            if i in stressed_letters:
                count += 1
                stressed_letter_num = count
                # print("stressed_letter")
        final_dict.update({'word': word, 'stressed': [count, stressed_letter_num]})
        return count, stressed_letter_num

    def message_moving(message, key):
        message = message.split()
        print(message)
        empty_word = '*****'
        poem_first_stage = [i for i in range(34)]
        # print(len(poem_first_stage))
        current_number = 0
        summ_num = current_number
        for i in range(len(message)):
            current_number = int(key[i])
            # print(current_number)
            summ_num += current_number
            # print(summ_num)
            poem_first_stage[summ_num] = message[i]
        poem_first_stage.pop(0)
        for i in poem_first_stage:
            if i not in message:
                poem_first_stage[poem_first_stage.index(i)] = empty_word
        return poem_first_stage

    def delete_words_from_dictionary():
        #global dictionary
        for i in dictionary:
            if get_stressed_syllable(i)[0] > 2:
                dictionary.remove(i)

    def poem_generate(poem):

        ending = ['на', 'го', 'ия']
        variant = 0  # Для случайного выбора одного из вариантов окончания слов в коцне строки для рифмы
        #global dictionary
        not_this_words = []  # чтобы слова не повторялись, будем добавлять их сюда
        for j in dictionary:
            if len(j) > 1:
                if (j[-2] + j[-1] == ending[variant]):
                    word = j + '8'
                    not_this_words.append(j)
        # print(not_this_words)
        local_stessed = 0

        if get_stressed_syllable(poem[0])[1] == 1:
            ending_str = [3, 7, 11, 15, 19, 23, 27]
            global_stressed = [3, 5, 7, 9, 11]  # номера ударных слогов
            current_stressed = 0  # Текущая сумма слогов в ударении
            for i in range(len(poem)):

                if poem[i] == '*****':
                    stress = get_stressed_syllable(poem[i])[0]
                    current_stressed += stress
                    flag = False

                    while flag == False:

                        # print(i, end = '')
                        if i in ending_str:
                            word = not_this_words[random.randint(0, len(not_this_words) - 1)]
                        else:

                            word = dictionary[random.randint(0, len(dictionary) - 1)]
                        if get_stressed_syllable(word)[1] == 2 and word not in poem:
                            flag = True
                            # print(flag)
                    poem[i] = word

        print(not_this_words)

        # return poem2

    # 1 7 9 12 17

    '''
    Описание алгоритма:
    1. Сумма слогов первой строки = 9
    2. Сумма слогов второй строки = 8
    3. Ударные слоги - чётные

    4. Берём слово, определяем его номер.
    5. Определяем номер этого слова в строке
    6. Если номер слова в строке - пятый, то запоминаем последние две буквы 
    7. Заполняем все слова ДО рассматриваемого:
        9. Нужно, чтобы на каждой строчке было 5 слов


    5. повторяем так со всеми словами
    6. 
    7. 
    '''

    form = """_*_*_*_*_
              _*_*_*_*"""

    def print_poem(poem):
        data = ''
        try:
            num = 0
            for i in range(7):
                for j in range(4):
                    print(poem[num], end=' ')
                    data += poem[num]
                    data += ' '
                    num += 1
                print()
                data += '\n'

        except IndexError:
            pass
        return data
    def save_poem(poem):
        # Получение unix-времени и времени в формате гггг-мм-дд чч:мм:сс
        unix_time = int(tm.time())
        # print(unix_time)
        str_date = tm.strftime('%Y-%m-%d %H:%M:%S', tm.localtime(unix_time))
        # print(type(unix_time))
        with open('result.txt', 'w', encoding='utf-8') as poem_file:
            poem_file.writelines(poem)
            #poem_file.writelines(str_date)

    # print(poem1)
    delete_words_from_dictionary()
    poem1 = message_moving(message, key)

    poem_generate(poem1)


    save_poem(print_poem(poem1))



if __name__ ==  '__main__':
    poems()