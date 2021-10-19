from random import randrange

sweet_amount = int(input("hoeveel kleuren (M&M’s) moeten er aan de zak worden toegevoegd? "))


def bag(sweet_amount: int):
    colors = ("oranje", "blauw", "groen", "bruin")
    bag  = {}

    for i in range(0, sweet_amount):
        num = randrange(0, (len(colors) -1) )
        color = colors[num]

        try:
            bag[color] += 1
        
        except KeyError: 
            bag[color] = 1

    else:
        return bag


bag = bag(sweet_amount)

print(bag)