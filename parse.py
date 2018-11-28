import pickle

from bs4 import BeautifulSoup

soup = BeautifulSoup(open('data/html/四角号码检字表（勘误版）.htm', encoding='gb18030'))

section = soup.body.div

print(section['class'])

# get printable text, instead of using element for more quickly
raw_data = section.text

data_list = raw_data.split()

print(len(data_list))

clean_data_list = [i for i in data_list if i.startswith('*')]

print(len(clean_data_list))

print('-' * 20)

dict_data = {}

duplicate_coding_char = []

for item in clean_data_list:
    try:
        raw_code, chars = item.split('：')

        assert raw_code.startswith('*')
        assert len(chars)
        assert ' ' not in chars

        code = raw_code[1:]

        char_list = [i for i in chars]
        assert len(char_list)

        for char in char_list:
            if char in dict_data:
                duplicate_coding_char.append(char)

            dict_data[char] = code

        print((code, char_list))
    except:
        print('*' * 20)
        print(item)
        raise

with open('data.pkl', 'wb') as fd:
    pickle.dump(dict_data, fd)

print('{} has at least two different coding'.format(duplicate_coding_char))
