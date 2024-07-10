import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10]

game=True

myMoney=0

while game==True:
    j=1
    k=1
    print("Hello youngling. Welcome to blackjack.")
    bet=int(input("How much would you like to bet?"))
    #my list
    myCardList=[]
    #dealer list
    dealerCardList=[]
    #dealer cards
    DealerCard1=random.choice(cards)
    DealerCard2=random.choice(cards)
    dealerCardList.append(DealerCard1)
    dealerCardList.append(DealerCard2)

    #my cards
    myFirstCard=random.choice(cards)
    mySecondCard=random.choice(cards)
    myCardList.append(myFirstCard)
    myCardList.append(mySecondCard)

    print("The dealer's cards are",DealerCard1,"and the other is face down.")
    print("\n")
    print("You currently have",myMoney,"money","Now we deal. Here are your cards:",myCardList)


    while k<2:
    
        playerChoice=input("Hit, double your bet, or stand? Please enter h,d,or s.").lower()
        
        if playerChoice=="h":
            myCardList.append(random.choice(cards))
            print("Here are your cards:",myCardList)


        elif playerChoice=="d":
            bet*=2
            print("Your bet is now",bet)

        elif playerChoice=="s":
            print("Your dealer's other card was",DealerCard2)
            k=3

    
        if sum(myCardList)==21:
            print("BLACKJACK! You won and earned",bet,".")
            myMoney+=bet
            k=3

        elif sum(myCardList)>21:
            print ("You busted!")
            myMoney-=bet
            k=3
            


    if sum(myCardList)<21:
        while True:        
    
            if sum(dealerCardList)<17:
                dealerCardList.append(random.choice(cards))
                print("Dealer cards:",dealerCardList)
            elif sum(dealerCardList)>=17 and sum(dealerCardList)<=21:
                break
            elif sum(dealerCardList)>21:
                print("The dealer busted and lost!")
                myMoney+=bet
                break


    if sum(dealerCardList)<=21 and sum(myCardList)<=21 and sum(myCardList)>sum(dealerCardList):
        print("You won!")
        myMoney+=bet

    elif sum(dealerCardList)<=21 and sum(myCardList)<=21 and sum(myCardList)<sum(dealerCardList):
        print("The dealer won!")
        myMoney-=bet
    if sum(dealerCardList)<=21 and sum(myCardList)<=21 and sum(myCardList)==sum(dealerCardList):
        print("Push!")

cards=[11,2,3,4,5,6,7,8,9,10,10,10]

game=True

while game==True:
    j=1
    k=1
    bet=int(input("How much would you like to bet?"))
    print("You have",bet,"money.")
    #my list
    myCardList=[]
    #dealer list
    dealerCardList=[]
    #dealer cards
    DealerCard1=random.choice(cards)
    DealerCard2=random.choice(cards)
    dealerCardList.append(DealerCard1)
    dealerCardList.append(DealerCard2)

    #my cards
    myFirstCard=random.choice(cards)
    mySecondCard=random.choice(cards)
    myCardList.append(myFirstCard)
    myCardList.append(mySecondCard)

    print("The dealer's cards are",DealerCard1,"and the other is face down.")
    print("\n")
    print("Now we deal. Here are your cards:",myCardList)


    while k<2:
    
        playerChoice=input("Hit, double your bet, or stand? Please enter h,d,or s.").lower()
        
        if playerChoice=="h":
            myCardList.append(random.choice(cards))
            print("Here are your cards:",myCardList)