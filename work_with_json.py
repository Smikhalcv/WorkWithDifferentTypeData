# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
#
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort или sorted.

import json
from collections import defaultdict

with open('newsafr.json', encoding='utf-8') as newsafr:
    news = json.load(newsafr)
    list_news = news['rss']['channel']['items'] #Список тем
    def sort_dict_word():
        list_word_6c = []
        for description_list in list_news:
            for word in description_list['description'].split():
                word = word.lower()
                if len(word) > 6:
                    list_word_6c.append(word) # Список всех слов из новостей
        dict_no_sort = defaultdict(int) # Словарь слов, где ключ слово, значение количество его в новостях
        for word in list_word_6c:
            dict_no_sort[word] += 1
        dict_no_sort = dict(dict_no_sort)
        sort_list_word = list(dict_no_sort.values())
        sort_list_word.sort()
        sort_list_word.reverse()
        sort_list_word = sort_list_word[:10] # Сортированный по убыванию список количество слов
        sort_dict_10 = {} # Словарь слова и количество его в новотях
        for count in sort_list_word:
            for item in dict_no_sort:
                if count == dict_no_sort[item]:
                    sort_dict_10[item] = count
                if len(sort_dict_10.keys()) == 10:
                    break
                else:
                    continue
        return sort_dict_10

    def results(sort_dict_word = sort_dict_word()):
        print('Перечень часто встречающихся слов в новостях и их количество, в порядке убывания: ')
        for key in sort_dict_word:
            print(f'{key} : {sort_dict_word[key]}')

    results()