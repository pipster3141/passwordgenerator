#Password Generator - Trevor Dalton - 10/2/2016

import random
from random import randint


def dicParser(dictionary,letterLength):
    fine = open(dictionary,'r')
    firstList = []
    sortedList = []
    for line in fine:
        strippedLine = line.strip()
        loweredStrippedLine = strippedLine.lower()
        if not '\'' in loweredStrippedLine:
            firstList.append(loweredStrippedLine)
    for word in firstList:
        if len(word) == letterLength:
            sortedList.append(word)
    fine.close()
    return(sortedList)


def letterSwitcher(word,positions,capitalChoice):
    consonants = ['b','c','d','f','g','k','l','m','p','r','s','t','y']
    #Here I take some letters that don't work as well unless they're replaced
    #With each other
    firstLetters = ['w','h','j','v','z','n']
    vowels = ['a','e','i','o','u']
    print(word,'was changed to')
    wordAsList = list(word)
    for position in positions:
        if wordAsList[position] in ('q','x'):
            wordAsList[position] = 'a'
        if wordAsList[position] in consonants:
            randy = randint(0,len(consonants)-1)
            while consonants[randy] == wordAsList[position]:
                randy = randint(0,len(consonants)-1)
            wordAsList[position] = consonants[randy]
            if capitalChoice == '2':
                wordAsList[position] = consonants[randy].upper() 
        elif wordAsList[position] in firstLetters:
            randy = randint(0,len(firstLetters)-1)
            while firstLetters[randy] == wordAsList[position]:
                randy = randint(0,len(firstLetters)-1)
            wordAsList[position] = firstLetters[randy]
            if capitalChoice == '2':
                wordAsList[position] = firstLetters[randy].upper()
        elif wordAsList[position] in vowels:
            randy = randint(0,len(vowels)-1)
            while vowels[randy] == wordAsList[position]:
                randy = randint(0,len(vowels)-1)
            wordAsList[position] = vowels[randy]
            if capitalChoice == '2':
                wordAsList[position] = vowels[randy].upper()
    newWord = ''.join(wordAsList)
    return newWord
    

def locations(word,count):
    whileCheck = True
    while whileCheck:
        positions = []
        for i in range(count):
            randomNum = randint(0,len(word)-1)
            while randomNum in positions:
                randomNum = randint(0,len(word)-1)
            positions.append(randomNum)
        whileCheck = ( len(positions) != len(set(positions)) )
        if whileCheck > 0:
            whileCheck = False
    return positions


def intro():
    print('This program is based around one theory')
    print('That the most efficient password will be one')
    print('based on a real word but isn\'t a real word')
    print('That way one can have a memorable yet safe password')
    print()


def numGetter():
    numLength = int(input('How many numbers are you wanting in your password? (I recommend more than 3 or more)'))
    numbers = ''
    for i in range(numLength):
        randomNum = str(randint(0,9))
        numbers += randomNum
    return numbers

def capitalSwitcher(newWord,positions):
    wordAsList = list(newWord)
    for position in positions:
        wordAsList[position] = wordAsList[position].upper()
    newWord = ''.join(wordAsList)
    return newWord
    

def capitalIntro():
    #Now I try and get capital letters
    print()
    print('You\'re going to have 4 choices with capital letters')
    print('#1, Don\'t do anything')
    print('#2, Make every letter we switch in a capital')
    print('#3, Make a the first letter a capital')
    print('#4, Or make a set amount of letters chosen randomly capital letters')
    print('Keep in mind capital letters make your password super safe')
    print('and that #2 and #4 are the best options')
    capitalChoice = 0
    while not capitalChoice in ('1','2','3','4'):
        capitalChoice = input('which option are you going to choose? (1-4)')
    return capitalChoice


def main():
    intro()
    numbers = numGetter()
    print()
    #Now I get the word
    print('Keep in mind your word must be between 1 and 20 letters')
    letterLength = int(input('How many letters are you going to want?'))
    print()
    if letterLength < 1:
        letterLength = 1
    elif letterLength > 20:
        letterLength = 20
    listOfWords = dicParser('dictionary.txt',letterLength)
    word = random.choice(listOfWords)
    #Now I get positions
    print('Keep in mind you can\'t change more letters than there are letters in the word')
    count = int(input('How many letters are you going to want changed? (rec: 1-3)'))
    if count > letterLength:
        count = letterLength
    capitalChoice = capitalIntro()
    if capitalChoice == '4':
        capitalCount = 10000
        while capitalCount > len(word) or capitalCount < 1:
            capitalCount = int(input('How many letters are you wanting to be made capital?'))
    print()
    positions = locations(word,count)
    newWord = letterSwitcher(word,positions,capitalChoice)
    while newWord in listOfWords:
        newWord = letterSwitcher(word,positions,capitalChoice)
    if capitalChoice == '3':
        newList = list(newWord)
        newList[0] = newList[0].upper()
        newWord = ''.join(newList)
    if capitalChoice == '4':
        positions = locations(newWord,capitalCount)
        newCapWord = capitalSwitcher(newWord,positions)
        print(newCapWord + numbers)
    else:
        print(newWord + numbers)
    return


main()
