import random
#list representing all the cards
cardList = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']
valueList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]
count = 0
userScore = 0
terminate = False
while count < 2:
    #a random card is chosen
    card1 = random.choice(cardList)
    #the random card's index is found
    cardIndex = cardList.index(card1)
    #the random card's index is used to find the value
    value1 = valueList[cardIndex]
    userScore+=value1
    del cardList[cardIndex]
    del valueList[cardIndex]
    count+=1
    print (card1)
    if (count == 2):
        print ("Player 1 score is" , userScore)   
keepGoing = True
while keepGoing:
    ask = input("Do you want to (h)it or (s)tand?:")
    if ask == "h":
        #a random card is chosen
        card1 = random.choice(cardList)
        #the random card's index is found
        cardIndex = cardList.index(card1)
        #the random card's index is used to find the value
        value1 = valueList[cardIndex]
        userScore+=value1
        del cardList[cardIndex]
        del valueList[cardIndex]
        print ("You got", card1)
        print ("Player 1 score is" , userScore)
        if userScore > 21:
            print ("You lose!")
            terminate = True
            break
    else:
        keepGoing == False
        break
if terminate == False:
    newCount = 0
    newuserScore = 0
    while newCount < 2:
        #a random card is chosen
        card1 = random.choice(cardList)
        #the random card's index is found
        cardIndex = cardList.index(card1)
        #the random card's index is used to find the value
        value1 = valueList[cardIndex]
        newuserScore+=value1
        del cardList[cardIndex]
        del valueList[cardIndex]
        newCount+=1
        print (card1)
        if (newCount == 2):
            print ("Dealer's score is" , newuserScore)
            while (newuserScore <= 17):
                print ("Dealer will hit!")
                card1 = random.choice(cardList)
                cardIndex = cardList.index(card1)
                value1 = valueList[cardIndex]
                newuserScore+=value1
                del cardList[cardIndex]
                del valueList[cardIndex]
                print (card1)
                print ("Dealer's score is", newuserScore)
    if (userScore > newuserScore and userScore <= 21):
        print ("Player 1 wins!")
    elif (newuserScore > userScore and newuserScore <= 21):
        print ("Dealer wins!")
    elif (newuserScore > userScore and newuserScore > 21):
        print ("Player 1 wins!")    
    else:
        print("It's a tie!")


##    if (userScore > newuserScore and userScore <= 21):
##        print ("Player 1 wins!")
##    elif (newuserScore > userScore):
##        if (newuserScore <= 21):
##            print("Dealer wins!")
##        else:
##            print("Player 1 wins!")
##    else:
##        print("It's a tie")

             
        
