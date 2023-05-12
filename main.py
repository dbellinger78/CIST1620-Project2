from tkinter import *
from video_poker import *
from PIL import Image, ImageTk

def main():    
    window = Tk()
    window.title('Video Poker')
    window.geometry('1400x900')
    window.configure(background="green")
    window.resizable(False, False)

    deckNoShuffle = newDeck()

    resultFrame = Label(window, bg='green', text='Draw Poker - Jacks or Better to Win', font='30pt', fg="white")
    resultFrame.pack(pady=10)
    handFrame = Frame(window, bg="green")
    handFrame.pack(pady=20)
    card1_label = Label(handFrame, text="Card 1", bd="0")
    card1_label.grid(row=1, column=0, padx=20, pady=5, ipadx=40)
    card2_label = Label(handFrame, text="Card 2", bd="0")
    card2_label.grid(row=1, column=1, padx=20, pady=5, ipadx=40)
    card3_label = Label(handFrame, text="Card 3", bd="0")
    card3_label.grid(row=1, column=2, padx=20, pady=5, ipadx=40)
    card4_label = Label(handFrame, text="Card 4", bd="0")
    card4_label.grid(row=1, column=3, padx=20, pady=5, ipadx=40)
    card5_label = Label(handFrame, text="Card 5", bd="0")
    card5_label.grid(row=1, column=4, padx=20, pady=5, ipadx=40)
    blankCard = 'cards/blank-card.png'
    c1 = ImageTk.PhotoImage(Image.open(blankCard))
    c2 = ImageTk.PhotoImage(Image.open(blankCard))
    c3 = ImageTk.PhotoImage(Image.open(blankCard))
    c4 = ImageTk.PhotoImage(Image.open(blankCard))
    c5 = ImageTk.PhotoImage(Image.open(blankCard))
    card1_image = Label(handFrame, image=c1)
    card1_image.grid(row=0, column=0)
    card2_image = Label(handFrame, image=c2)
    card2_image.grid(row=0, column=1)
    card3_image = Label(handFrame, image=c3)
    card3_image.grid(row=0, column=2)
    card4_image = Label(handFrame, image=c4)
    card4_image.grid(row=0, column=3)
    card5_image = Label(handFrame, image=c5)
    card5_image.grid(row=0, column=4)
    card1_image.image = c1
    card2_image.image = c2
    card3_image.image = c3            
    card4_image.image = c4            
    card5_image.image = c5
    card1button = Button(handFrame, text='Hold', font='10pt')
    card1button.grid(row=3, column=0)
    card2button = Button(handFrame, text='Hold', font='10pt')
    card2button.grid(row=3, column=1)
    card3button = Button(handFrame, text='Hold', font='10pt')
    card3button.grid(row=3, column=2)
    card4button = Button(handFrame, text='Hold', font='10pt')
    card4button.grid(row=3, column=3)
    card5button = Button(handFrame, text='Hold', font='10pt')
    card5button.grid(row=3, column=4)
    buttonFrame = Frame(window, bg="green")
    buttonFrame.pack(pady=10)
    new_hand_button = Button(buttonFrame, text="Place New Bet", font="12pt")
    new_hand_button.grid(row=0, column=2, padx=25) 
    deal_hand_button = Button(buttonFrame, text="Deal Hand", font="12pt")
    deal_hand_button.grid(row=0, column=0, padx=25)
    draw_button = Button(buttonFrame, text="Draw Cards", font="12pt")
    draw_button.grid(row=0, column=1, padx=25)
    quit_button = Button(buttonFrame, text="Quit Game", font="12pt")
    quit_button.grid(row=0, column=3, padx=25)
    betFrame = Frame(window, bg='green')
    betFrame.pack(pady=10)
    payoutTable = Image.open('cards/payout-table.png')
    table = payoutTable.resize((472,300), Image.ANTIALIAS)
    sm_table = ImageTk.PhotoImage(table) 
    tableFrame = Label(betFrame, image=sm_table)
    tableFrame.image = sm_table
    tableFrame.grid(row=0, column=0)
    

    global bankroll
    bankroll = 100


    

    def deckShuffle():
        shuffled = shuffle(deckNoShuffle)

        return shuffled


            

    def loop(bankroll):       

        if bankroll > 0:

            global bet
            bet = 1
            shuffled = deckShuffle()
            playerHand = deal(shuffled)
        
            resultFrame.config(text='Draw Poker - Jacks or Better to Win')

            bankrollFrame = Frame(betFrame, bg='green')
            bankrollFrame.grid(row=0, column=1, padx=15)
            bankrollLabel = Label(bankrollFrame, text='Bankroll: ', font="12pt", bg='green')
            bankrollLabel.grid(row=0, column=0, padx=10)
            bankrollBox = Label(bankrollFrame, bg="white", text=bankroll - bet, font="11pt", width=6) 
            bankrollBox.grid(row=0, column=1)
            betLabel = Label(bankrollFrame, text='Bet Amount: ', font="12pt", bg='green')
            betLabel.grid(row=1, column=0, pady=5)
            betBox = Label(bankrollFrame, bg="white", text=bet, font="11pt", width=2) 
            betBox.grid(row=1, column=1, pady=5)
            betUpLabel = Label(bankrollFrame, text='Increase Bet: ', font="12pt", bg='green')
            betUpLabel.grid(row=2, column=0, padx=10)
            betUpBtn = Button(bankrollFrame, text="+", font="12pt", command=lambda: increaseBet())
            betUpBtn.grid(row=2, column=1, padx=10, pady=5)
            betDownLabel = Label(bankrollFrame, text='Decrease Bet: ', font="12pt", bg='green')
            betDownLabel.grid(row=3, column=0, padx=10, pady=5)
            betDownBtn = Button(bankrollFrame,text="-", font="12pt", command=lambda: decreaseBet())
            betDownBtn.grid(row=3, column=1, padx=10)

            handFrame.config = Frame(window, bg="green")

            card1button.config(state=DISABLED, text='Hold')
            card2button.config(state=DISABLED, text='Hold')
            card3button.config(state=DISABLED, text='Hold')
            card4button.config(state=DISABLED, text='Hold')
            card5button.config(state=DISABLED, text='Hold')

            deal_hand_button.config(command=lambda: showHand(resultFrame, card1_image, card2_image, card3_image, card4_image, card5_image, card1button, card2button, card3button, card4button, card5button, draw_button, deal_hand_button, new_hand_button, betUpBtn, betDownBtn, playerHand, shuffled))
            deal_hand_button.config(state=NORMAL)

            new_hand_button.config(state=DISABLED)  

            draw_button.config(state=DISABLED)

            quit_button.config(command=lambda: quit(betUpBtn, betDownBtn))

        else:
            quit(betUpBtn, betDownBtn)
            resultFrame.config(text="You're Busted! No Bankroll Remaining!")

            
        def increaseBet():
            global bet
            global bankroll
            if bet != 5 and bet < bankroll:
                bet = bet + 1
                betBox.config(text=bet)
                bankrollBox.config(text=bankroll - bet)    
            else:
                bet = bet
                betBox.config(text=bet)
                bankrollBox.config(text=bankroll - bet) 
                   


        def decreaseBet():
            global bet
            if bet != 1:
                bet = bet - 1
                betBox.config(text=bet)
                bankrollBox.config(text=bankroll - bet)
            else:
                bet = 1
                betBox.config(text=bet)
                bankrollBox.config(text=bankroll - bet)




    def quit(betUpBtn, betDownBtn):
        resultFrame.config(text='Thanks For Playing!')
        new_hand_button.config(state=DISABLED)  
        draw_button.config(state=DISABLED)
        deal_hand_button.config(state=DISABLED)
        card1button.config(state=DISABLED, text='Hold')
        card2button.config(state=DISABLED, text='Hold')
        card3button.config(state=DISABLED, text='Hold')
        card4button.config(state=DISABLED, text='Hold')
        card5button.config(state=DISABLED, text='Hold')
        betUpBtn.config(state=DISABLED)
        betDownBtn.config(state=DISABLED)


    def showHand(resultFrame, card1_image, card2_image, card3_image, card4_image, card5_image, card1button, card2button, card3button, card4button, card5button, draw_button, deal_hand_button, new_hand_button, betUpBtn, betDownBtn, playerHand, shuffled):   
        playerHand = playerHand
        shuffled = shuffled

        c1 = Image.open(playerHand[0].image)
        c1Image = ImageTk.PhotoImage(c1)
        card1_image.config(image=c1Image)
        card1_image.image = c1Image

        c2 = Image.open(playerHand[1].image)
        c2Image = ImageTk.PhotoImage(c2)
        card2_image.config(image=c2Image)
        card2_image.image = c2Image

        c3 = Image.open(playerHand[2].image)
        c3Image = ImageTk.PhotoImage(c3)
        card3_image.config(image=c3Image)
        card3_image.image = c3Image

        c4 = Image.open(playerHand[3].image)
        c4Image = ImageTk.PhotoImage(c4)
        card4_image.config(image=c4Image)
        card4_image.image = c4Image

        c5 = Image.open(playerHand[4].image)
        c5Image = ImageTk.PhotoImage(c5)
        card5_image.config(image=c5Image)
        card5_image.image = c5Image

        card1button.config(state=NORMAL, command=lambda: holdCards(1))
        card2button.config(state=NORMAL, command=lambda: holdCards(2))
        card3button.config(state=NORMAL, command=lambda: holdCards(3))
        card4button.config(state=NORMAL, command=lambda: holdCards(4))
        card5button.config(state=NORMAL, command=lambda: holdCards(5))
        draw_button.config(state=NORMAL, command=lambda: drawCards(resultFrame, new_hand_button, playerHand, shuffled))
        deal_hand_button.config(state=DISABLED)
        betDownBtn.config(state=DISABLED)
        betUpBtn.config(state=DISABLED)


        i = 0
        while i < 5:
            playerHand[i].clearHold()
            i = i + 1



        def holdCards(num):    
            hand = playerHand

            num = num - 1
            hand[num].setHold()

            if num == 0:
                if hand[num].getHold() == True:
                    card1button.config(text='HELD')
                else: 
                    card1button.config(text='Hold')

            elif num == 1:
                if hand[num].getHold()  == True:
                    card2button.config(text='HELD')
                else: 
                    card2button.config(text='Hold')

            elif num == 2:
                if hand[num].getHold()  == True:
                    card3button.config(text='HELD')
                else: 
                    card3button.config(text='Hold')        

            elif num == 3:
                if hand[num].getHold()  == True:
                    card4button.config(text='HELD')
                else: 
                    card4button.config(text='Hold')        
    
            elif num == 4:
                if hand[num].getHold() == True:
                    card5button.config(text='HELD')
                else: 
                    card5button.config(text='Hold')

            


        def drawCards(resultFrame, new_hand_button, playerHand, shuffled):
            playerHand = playerHand
            shuffled = shuffled
            next = 5
            i = 0
            while i < 5:
                if playerHand[i].getHold() == False:
                    playerHand[i] = shuffled[next]
                    i = i + 1
                    next = next + 1
                else:
                    i = i + 1

            showHand(resultFrame, card1_image, card2_image, card3_image, card4_image, card5_image, card1button, card2button, card3button, card4button, card5button, draw_button, deal_hand_button, new_hand_button, betUpBtn, betDownBtn, playerHand, shuffled)
            draw_button.config(state=DISABLED)
            deal_hand_button.config(state=DISABLED)
            card1button.config(state=DISABLED)     
            card2button.config(state=DISABLED) 
            card3button.config(state=DISABLED) 
            card4button.config(state=DISABLED) 
            card5button.config(state=DISABLED)
            global bankroll
            bankroll = bankroll - bet
            result = determineHand(playerHand, bet)
            resultFrame.config(text=result[0])
            payout = result[1]
            bankroll = bankroll + payout
            new_hand_button.config(state=NORMAL, command=lambda: loop(bankroll))  



    loop(bankroll)

    window.mainloop()

if __name__ == '__main__':
    main()
    