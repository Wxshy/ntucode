import cards

class BJ_Card(cards.Card):
    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANK.index(self.rank) + 1
            if v > 10:
                v = 10

        else:
            v = None

class BJ_Deck(cards.Deck):
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

        
class BJ_Hand(cards.Hand):
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name
    
    def __str__(self):
        rep = self.name + ':\t' + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ')'
        
        return rep
    
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        
        t = 0
        for card in self.cards:
            t += card.value
        
        ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                ace = True
        
        if ace and t < 11:
            t += 10
        
        return t

    def is_busted(self):
        return self.total > 21
    

class BJ_Player(BJ_Hand):
    def is_hitting(self):
        response = games.ask_yes_no(f'\n {self.name} would you like to hit Y/N: ')
        return response == 'y'

    def bust(self):
        print(f'{self.name} busts')
        self.lose()

    def lose(self):
        print(f'{self.name} loses.')
    
    def win(self):
        print(f'{self.name} wins!')

    def push(self):
        print(f'{self.name} pushes.')

class BJ_Dealer(BJ_Hand):
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(f'{self.name} busts.')

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            self.players.append(BJ_Player(name))

        self.dealer = BJ_Dealer('Dealer')

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additonal_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust