word=input('enter a word: ')

word2=' '

for i in word:
    if not 'a' in i:
        if 'A' not in i:
            word2 += i

print(word2)