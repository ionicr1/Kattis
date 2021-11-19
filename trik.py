ball = [1, 2, 3]
position = ball[0]
for i in input():
    if i == 'A':
        if position == ball[0]:
            position = ball[1]
        elif position == ball[1]:
            position = ball[0]
    if i == 'B':
        if position == ball[1]:
            position = ball[2]
        elif position == ball[2]:
            position = ball[1]
    if i == 'C':
        if position == ball[0]:
            position = ball[2]
        elif position == ball[2]:
            position = ball[0]
print(position)
