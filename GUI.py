import tkinter as tk
import classcreation as cc
from PIL import Image,ImageTk

root = tk.Tk()

number_of_players = 1


def set_players(val):
    global number_of_players
    number_of_players = (int(val))


value_of_balance = 100


def set_balance(val):
    global value_of_balance
    value_of_balance = (int(val))


class Menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(fill=tk.BOTH)

        # Create menu buttons

        title_label = tk.Label(self, text='Nags Gaming')
        instructions1 = tk.Label(
            self, text='To play Blackjack please press the button below')
        window_one_button = tk.Button(self,
                                      text='BlackJack',
                                      command=self.window_one)
        close_button = tk.Button(self,
                                 text='Close',
                                 command=self.master.destroy)
        instruction_button = tk.Label(
            self, text='Press me to see the rules of blackjack!')

        # Attach to grid

        title_label.grid(row=0, column=0)
        instructions1.grid(row=1, column=0)
        window_one_button.grid(row=2, column=0)
        instruction_button.grid(row=3, column=0)

        close_button.grid(row=0, column=0, sticky="nw")

        # Describe grid

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        root.geometry("500x300")

    def window_one(self):
        self.destroy()
        Window_One(self.master)

    def window_two(self):
        self.destroy()
        Menu(self.master)


class Window_One(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # self.parent = parent
        self.pack(fill=tk.BOTH)

        # Create menu buttons

        self.title_label = tk.Label(self, text='BlackJack')
        self.menu_button = tk.Button(self,
                                     text='Back To Menu',
                                     command=self.menu)
        self.balance_val = tk.Label(self, text='Set your starting balance')
        self.balance_val_slider = tk.Scale(self,
                                           from_=100,
                                           to=1000,
                                           orient=tk.HORIZONTAL,
                                           bigincrement=10,
                                           command=set_balance)
        self.num_players = tk.Label(self, text='How many players are there?')
        self.num_players_slider = tk.Scale(self,
                                           from_=1,
                                           to=5,
                                           orient=tk.HORIZONTAL,
                                           command=set_players)
        self.num_players_button = tk.Button(self,
                                            text='Press this Button to Play',
                                            command=self.window_two)

        # Attach to grid

        self.title_label.grid(row=0, column=0, sticky='ew')
        self.menu_button.grid(row=0, column=0, sticky="nw")
        self.balance_val.grid(row=1, column=0)
        self.balance_val_slider.grid(row=2, column=0)
        self.num_players.grid(row=3, column=0)
        self.num_players_slider.grid(row=4, column=0)
        self.num_players_button.grid(row=5, column=0)

        # Describe grid

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)

    def window_two(self):
        self.destroy()
        Window_Two(self.master)

    def menu(self):
        self.destroy()
        Menu(self.master)

class Hand():
    def __init__(self, player, parent):
        # TODO: Store these tk objects that refer to specfic players in a way that means we can refer to them again later

        self.player = player

        print(player.playernum)

        self.card1_image = tk.Label(parent.middle_frame,
                                    text='Insert Image Card1',
                                    bg='blue',
                                    fg='white',
                                    font=('Times', 15))

        self.card2_image = tk.Label(parent.middle_frame,
                               text='Insert Image Card2',
                               bg='blue',
                               fg='white',
                               font=('Times', 15))
        self.balance_box = tk.Label(parent.bottom_frame,
                               text="{}: {}".format(
                                   player.name, player.balance),
                               bg='blue',
                               fg='white',
                               font=('Times', 15))
        # bet_size_box = tk.Label(bottom_frame, text=player.balance, bg='blue', fg='white', font=('Times', 15))
        self.hit_button = tk.Button(parent.bottom_frame,
                               text='HIT',
                               bg='blue',
                               fg='black',
                               font=('Times', 15))
        self.double_button = tk.Button(parent.bottom_frame,
                                  text='DOUBLE',
                                  bg='blue',
                                  fg='black',
                                  font=('Times', 15))
        self.stand_button = tk.Button(parent.bottom_frame,
                                 text='STAND',
                                 bg='blue',
                                 fg='black',
                                 font=('Times', 15))
        self.split_button = tk.Button(parent.bottom_frame,
                                 text='SPLIT',
                                 bg='blue',
                                 fg='black',
                                 font=('Times', 15))

        self.card1_image.grid(row=0,
                         column=self.player.position,
                         rowspan=20,
                         sticky='news',
                         padx=10,
                         pady=10)
        self.card2_image.grid(row=0,
                         column=self.player.position + 1,
                         rowspan=20,
                         sticky='news',
                         padx=10,
                         pady=10)
        self.balance_box.grid(row=0,
                         column=self.player.position,
                         sticky='news',
                         padx=10,
                         pady=10)
        self.hit_button.grid(row=1,
                        column=self.player.position,
                        sticky='news',
                        padx=10,
                        pady=10)
        self.double_button.grid(row=1,
                           column=self.player.position + 1,
                           sticky='news',
                           padx=10,
                           pady=10)
        self.stand_button.grid(row=2,
                          column=self.player.position,
                          sticky='news',
                          padx=10,
                          pady=10)
        self.split_button.grid(row=2,
                          column=self.player.position + 1,
                          sticky='news',
                          padx=10,
                          pady=10)

    def updateimages(self):

        self.card1_image.config(text=self.player.cards[0])
        self.card2_image.config(text=self.player.cards[1])

        # TODO: Change the .config to assign correct image file!


class Window_Two(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        root.geometry("1250x840")

        # This is my pack of cards

        self.deck = cc.Deck()

        self.configure(background="green")

        self.pack(fill=tk.BOTH)

        # Create a top and bottom frame

        self.bottom_frame = tk.Frame(self)
        self.middle_frame = tk.Frame(self)
        self.top_frame = tk.Frame(self)

        self.bottom_frame.grid(row=2, sticky="news")
        self.top_frame.grid(row=0, sticky='news')
        self.middle_frame.grid(row=1, sticky="news")

        self.bottom_frame.configure(background='green')
        self.middle_frame.configure(background='yellow')
        self.top_frame.configure(background='red')

        self.rowconfigure(0, minsize=280, weight=1)
        self.rowconfigure(1, minsize=280, weight=1)
        self.rowconfigure(2, minsize=280, weight=1)

        self.columnconfigure(0, weight=1)

        deal_button = tk.Button(self.top_frame, text='DEAL', bg='blue', fg='white', font=('Times', 15),
                                command=self.confirm_bet)

        deal_button.grid(row=0,
                         column=3,
                         sticky="e",
                         )

        self.players = []
        self.bet_sliders = []

        self.hands = []

        for i in range(number_of_players):
            self.players.append(
                cc.Players("Player {}".format(i + 1), i, value_of_balance))

        for player in self.players:
            if player.playernum == 0:
                player.position = 0
            else:
                player.position = (player.playernum + 1) * 2

            # Trying to make the hands accessible

            self.hands.append(Hand(player, self))


            self.bet_sliders.append(
                tk.Scale(self.bottom_frame,
                         from_=10,
                         to=player.balance,
                         orient=tk.HORIZONTAL,
                         bigincrement=10,
                         command=player.placebet))

            self.bet_sliders[player.playernum].grid(row=0,
                                                    column=player.position + 1,
                                                    sticky='news',
                                                    padx=10,
                                                    pady=10)

            self.bottom_frame.columnconfigure(player.position, weight=1)
            self.bottom_frame.columnconfigure(player.position + 1, weight=1)
            self.middle_frame.columnconfigure(player.position, weight=1)
            self.middle_frame.columnconfigure(player.position + 1, weight=1)

        self.bottom_frame.rowconfigure(0, weight=1)
        self.bottom_frame.rowconfigure(1, weight=1)
        self.bottom_frame.rowconfigure(2, weight=1)

        self.middle_frame.rowconfigure(0, weight=1)

        menu_button = tk.Button(self.top_frame,
                                text='Back To Menu',
                                command=self.menu)
        dealer_name = tk.Label(self.top_frame,
                               text='Dealer',
                               bg='blue',
                               fg='white',
                               font=('Times', 15))
        dealer_card1_image = tk.Label(self.top_frame,
                                      text='Insert Image Card1',
                                      bg='blue',
                                      fg='white',
                                      font=('Times', 15))
        dealer_card2_image = tk.Label(self.top_frame,
                                      text='Insert Image Card2',
                                      bg='blue',
                                      fg='white',
                                      font=('Times', 15))

        menu_button.grid(row=0, column=0, sticky="nw")
        dealer_name.grid(row=0,
                         column=1,
                         columnspan=2,
                         sticky="news",
                         padx=10,
                         pady=10)
        dealer_card1_image.grid(row=1,
                                column=1,
                                rowspan=20,
                                sticky='news',
                                padx=10,
                                pady=10)
        dealer_card2_image.grid(row=1,
                                column=2,
                                rowspan=20,
                                sticky='news',
                                padx=10,
                                pady=10)

        self.top_frame.rowconfigure(0, weight=1)
        self.top_frame.rowconfigure(1, weight=1, minsize=210)

        self.top_frame.columnconfigure(0, weight=1, minsize=400)
        self.top_frame.columnconfigure(1, weight=1)
        self.top_frame.columnconfigure(2, weight=1)
        self.top_frame.columnconfigure(3, weight=1, minsize=400)


    def menu(self):
        self.destroy()
        Menu(self.master)

    def window_one(self):
        self.destroy()
        Window_One(self.master)

    def confirm_bet(self):
        # First we reset the sliders

        for slider in self.bet_sliders:
            slider.grid_forget()

        # Create and shuffle the deck

        self.deck.reset()

        # Deal cards to players

        for hand in self.hands:
            hand.player.initialcards(self.deck)

            hand.updateimages()



root.geometry("500x300")
root.resizable(width=0, height=0)

menu = Menu(root)

root.mainloop()
