import random
words = ['book', 'tree', 'elephent', 'airplane', 'tiger', 'apple']
temp = words[random.randint(0, len(words)-1)]
chances = 2*len(temp)
answer = []
for i in range(len(temp)): answer.append('-')
word = []
for i in range(len(temp)): word.append(temp[i])
while chances>0:
    for j in range(len(answer)): print(answer[j], end=' ')
    print('(',chances,'♡ )')
    char = input("Char: ").lower()
    if char in word:
        while char in word:
            answer[word.index(char)] = char
            word[word.index(char)] = ''
        if '-' not in answer: break
    else: chances -= 1
if chances==0: print("**************GAME OVER**************")
else: 
    for j in range(len(answer)): print(answer[j], end=' ')
    print('\n', "**************WON**************")