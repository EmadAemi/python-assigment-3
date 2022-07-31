import random
words = ['book', 'tree', 'elephent', 'airplane', 'tiger', 'apple']
word = words[random.randint(0, len(words)-1)]
chances = 2*len(word)
answer = []
while chances>0:
    for j in range(len(answer)): print(answer[j], end=' ')
    for j in range(len(word)-len(answer)): print('_', end=' ')
    print('(',chances,'♡ )')
    char = input("Char: ")
    if(char != word[len(answer)]): chances -= 1
    else: answer.append(char)
    if len(answer)==len(word): break
if chances==0: print("**************GAME OVER**************")
else: print("**************WON**************")

