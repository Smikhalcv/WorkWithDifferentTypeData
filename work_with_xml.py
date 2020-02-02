import xml.etree.ElementTree as ET
from collections import defaultdict

tree = ET.parse('newsafr.xml')
root = tree.getroot()

def list_news(): # Функция получения списка слов новостей
    str_news = ''
    list_word_news = []
    i = 0
    for i in range(len(root[0])-6):
        str_news += root[0][i+6][2].text + ' '
        i += 1
    list_news = str_news.split()
    for word in list_news:
        word = word.lower()
        if len(word) > 6:
            list_word_news.append(word)
        else:
            continue
    return list_word_news

def sort_dict_word(list_word_6c = list_news()):
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

def results(sort_dict_word = sort_dict_word(list_word_6c = list_news())):
    print('Перечень часто встречающихся слов в новостях и их количество, в порядке убывания: ')
    for key in sort_dict_word:
        print(f'{key} : {sort_dict_word[key]}')

results()
