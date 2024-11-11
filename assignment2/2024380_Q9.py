words = list(map(str, input('enter space seperated words: ').split()))
for i in words:
    if i.isalpha() == False:
        print('Invalid input')
        exit()

def insert_word(megalist, word):
    current_list = megalist
    for char in word:
        found = False
        for item in current_list:
            if item[0] == char:
                current_list = item[1]
                found = True
                break
        if not found:
            new_list = [char, []]
            current_list.append(new_list)
            current_list = new_list[1]
    current_list.append(word)

def main(words):
    megalist = []
    for word in words:
        insert_word(megalist, word)
    return megalist

def delete_word(word, curent_list):
    if word in curent_list:
        curent_list.remove(word)
        return main(curent_list)
    else:
        return 'Word not found'

def add_word(word, curent_list):
    curent_list.append(word)
    return main(curent_list)

def search_word(word, curent_list):
    out = []
    for i in curent_list:
        if word in i:
            out.append(i)
    return out

megalist = main(words)
print(megalist)
while True:
    print('1. Add word')
    print('2. Delete word')
    print('3. Search word')
    print('4. Exit')
    try:
        choice = int(input('Enter your choice: '))
    except ValueError:
        print('Invalid choice')
        continue
    if choice == 1:
        word = str(input('Enter the word to add: '))
        print(add_word(word, words))
    elif choice == 2:
        word = str(input('Enter the word to delete: '))
        print(delete_word(word, words))
    elif choice == 3:
        word = str(input('Enter the word to search: '))
        print(search_word(word,words))
    elif choice == 4:
        break
    else:
        print('Invalid choice')

def test():
    assert main(['hello']) == [['h', [['e', [['l', [['l', [['o', ['hello']]]]]]]]]]]
    assert delete_word('nik',['hello']) == 'Word not found'
    assert add_word('nik',['hello']) == [['h', [['e', [['l', [['l', [['o', ['hello']]]]]]]]]], ['n', [['i', [['k', ['nik']]]]]]]

test()