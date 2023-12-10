contain = {}
five = []
four = []
house = []
three = []
two = []
one = []
high = []

def card_value(card):
    value = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    return value[card]

with open('day7.txt') as file:
    for line in file:
        card, point = line.split()
        contain[card] = point
        
for hand in contain:
    if hand.count(hand[0]) == 5:
        five.append(hand)
    elif hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4 or hand.count(hand[2]) == 4 or hand.count(hand[3]) == 4 or hand.count(hand[4]) == 4:
        four.append(hand)
    elif (hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3 or hand.count(hand[3]) == 3 or hand.count(hand[4]) == 3) and (hand.count(hand[0]) == 2 or hand.count(hand[1]) == 2 or hand.count(hand[2]) == 2 or hand.count(hand[3]) == 2  or hand.count(hand[4]) == 2):
        house.append(hand)
    elif (hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3 or hand.count(hand[3]) == 3 or hand.count(hand[4]) == 3) and (hand.count(hand[0]) == 1 or hand.count(hand[1]) == 1 or hand.count(hand[2]) == 1 or hand.count(hand[3]) == 1  or hand.count(hand[4]) == 1):
        three.append(hand)
    elif hand.count(hand[0]) == 1 and hand.count(hand[1]) == 1 and hand.count(hand[2]) == 1 and hand.count(hand[3]) == 1 and hand.count(hand[4]) == 1:
        high.append(hand)
    else:
        temp = hand
        hand = hand.replace(hand[0], '')
        hand = hand.replace(hand[0], '')
        hand = hand.replace(hand[0], '')
        if hand == '':
            two.append(temp)
        else:
            one.append(temp)

One = sorted(one, key = lambda x: [card_value(i) for i in x])
Two = sorted(two, key = lambda x: [card_value(i) for i in x])
Three = sorted(three, key = lambda x: [card_value(i) for i in x])
High = sorted(high, key = lambda x: [card_value(i) for i in x])
House = sorted(house, key = lambda x: [card_value(i) for i in x])
Four = sorted(four, key = lambda x: [card_value(i) for i in x])
Five = sorted(five, key = lambda x: [card_value(i) for i in x])

new = High + One + Two + Three + House + Four + Five
rank = 1

sum = 0
for element in new:
    sum += int(contain[element]) * rank
    rank += 1
print(sum)
    

