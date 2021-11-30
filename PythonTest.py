"""
s: Distance
t: Time
a: Acceleration - CONSTANT
u: Initial Speed
"""
a = 9.8
u = 10
t = 4

def calculate(a, u ,t):
    return (u*t)+(0.5*(a*(t**2)))

s = calculate(a,u,t)

print(f'Distance Travelled: {s}m')
if s > 100:
    output = 'Good going!'
elif 100 > s >= 50:
    output = 'Not bad'
else:
    output = 'Pathetic'

print(output)

