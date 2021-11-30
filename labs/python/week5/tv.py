class Television(object):
    def __init__(self):
        self.name = "Samsung TV"
        self.volume = 20
        self.channel = 1

    def change_volume(self):
        while True:
            volume = int(input('Please enter the new volume (0-100): '))
            if 0 <= volume <= 100:
                break
            else:
                print('Please enter a valid volume!')

        self.volume = volume

    def change_channel(self):
        while True:
            channel = int(input('Please enter the channel (0-999): '))
            if 0 <= channel <= 999:
                break
            else:
                print('Please enter a valid volume!')
        self.channel = channel

def main():
    tv = Television()
    while True:
        print(f'''
            SAMSUNG
        VOLUME: {tv.volume}
        CHANNEL: {tv.channel}

            TV REMOTE
        
        1. Power Off
        2. Adjust Volume
        3. Change Channel
        
        ''')
        choice = int(input(">>> "))

        if choice == 1:
            print('Beep Boop')
            break
        elif choice == 2:
            tv.change_volume
        elif choice == 3:
            tv.change_channel
        else:
            print('Error: Unknown choice! \n')

if __name__ == "__main__":
    main()