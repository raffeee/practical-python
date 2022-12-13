# bounce.py
#
# Exercise 1.5
bounce_count = 1
bounce_rate = 0.6
ball_height = 100

while bounce_count <= 10:
    ball_height *= bounce_rate
    print(bounce_count, round(ball_height, 4))
    bounce_count += 1
