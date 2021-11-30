class Critter(object):
    def __init__(self, name, hunger = 0, boredom = 0):
        print('A new critter has been created')
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    
    def __str__(self):
        return f'''
        NAME: {self.name}
        HUNGER: {self.hunger}
        BOREDOM: {self.boredom}
        '''

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'Happy'
        elif 5 <= unhappiness <= 10:
            m = 'Okay'
        elif 11 <= unhappiness <= 15:
            m = 'frustrated'
        else:
            m = 'mad'
        return m

    def talk(self):
        print(f'Hi i am {self.name} and i am feeling {self.mood} now')
        self.__pass_time()

    def eat(self, food = 4):
        x = int(input('How much food would you like to give your critter: '))
        print('Burrrp, Thank you!')
        self.hunger -= x
        if self.hunger < 0:
            self.hunger = 0

        self.__pass_time()

    def play(self, fun = 4):
        time = int(input('How long would you like to play for: '))
        print('Wheeeee!')
        self.boredom -= time
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit = Critter(input('Please enter the name of your critter: '))
    choice = None
    while choice != "0":
        print('''
        Critter Caretaker

        0. Quit
        1. Listen to your Critter
        2. Feed your Critter
        3. Play with your Critter

        ''')
        choice = input('>>> ')

        if choice == "0":
            print('ByeBye')

        elif choice == "1":
            crit.talk()
        
        elif choice == "2":
            crit.eat()
        
        elif choice == "3":
            crit.play()
        
        elif choice == "19":
            print(str(crit))
        else:
            print('I dont understand that try again')

if __name__ == '__main__':
    main()

