'''
test the obstruction class
'''

from main import Obstruction

# using point a, point b and real_time from example provided
point_a = [53.5872, -2.4138]
point_b = [53.474, -2.2388]
real_time = 78
speed = 15
distance = 26

obst =  Obstruction(speed, distance)

if obst.impenetrable(real_time):
    print("Impenetrable obstruction is found")
else:
    print("No Impenetrable obstruction")