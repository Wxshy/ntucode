import random
import threading
import time
import os
import signal

c = threading.Condition()
num = random.randint(1,100)

class Timer(threading.Thread):
    def run(self, *args):
        self.my_timer = time.time() + 10
        while True:
            time.sleep(0.1)
            if time.time() >= self.my_timer:
                break
        print()

        global num
        c.acquire()

        print('Unlucky you ran out of time!')
        print(f'The Number was {num}')
        os.kill(os.getpid(), signal.SIGINT)
        

print('You have 10 seconds and 8 attempts')
print('GO!!!')

t = Timer()
t.daemon = True
t.start()

try:
    guess = int(input('Please enter your guess: '))

    attempts = 1

    while guess != num and attempts < 8:
        print()
        print(f'Guess No.: {attempts} attempts')
        print('Your guess is too high') if guess > num else print('Your guess is too low')
        guess = int(input('Please enter your new guess: '))
        attempts += 1
except KeyboardInterrupt:
    pass
