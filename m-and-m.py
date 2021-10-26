from random import choice

bag_chosen = False

amount = int(input("hoeveel kleuren (M&M’s) moeten er aan de zak worden toegevoegd? "))

colors = ["oranje", "blauw", "groen", "bruin"]


def color_bag(amount: int):
    colors_bag = []

    for i in range(amount):
        color = choice(colors)

        colors_bag.append(color)
    
    else:
        return colors_bag


def dict_color_bag(amount: int):
    dict_colors_bag  = {}

    for i in range(amount):
        color = choice(colors)

        try:
            dict_colors_bag[color] += 1
        
        except KeyError: 
            dict_colors_bag[color] = 1

    else:
        return dict_colors_bag


def sort_bag(bag, colors):
    if isinstance(bag, list):
        new_bag = sorted(bag)
    else:
        new_bag = {}

        for color in bag:            
            new_bag[color] = bag[color]

    return new_bag

color_bag = color_bag(amount)
dict_color_bag = dict_color_bag(amount)


while not bag_chosen:
    choice = input("wilt u de zak meegeven als L )list of als D) dictionary?: ").upper()

    if choice == "L":
        bag_must_sort = color_bag
        bag_chosen = True

    elif choice == "D":
        bag_must_sort = dict_color_bag
        bag_chosen = True

    else:
        print("Kies opnieuw")   

else:
    new_bag = sort_bag(bag_must_sort, colors)

    print(new_bag)