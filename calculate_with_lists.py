listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo =[2,4,6,8,10,12,14,16,18,20]



def addAndDisplayLists(list1, list2):
    print("------------")
    print("Add lists")

    for num, val in enumerate(list1):
        string = str(val) + " + " + str(list2[num]) + " = " + str(val + list2[num])

        print(string)


def substractAndDisplayLists(list1, list2):
    print("------------")
    print("Substract lists")

    for num, val in enumerate(list1):
        string = str(val) + " - " + str(list2[num]) + " = " + str(val - list2[num])

        print(string)


def multiplyAndDisplayLists(list1, list2):
    print("------------")
    print("Multiply lists")

    for num, val in enumerate(list1):
        string = str(val) + " * " + str(list2[num]) + " = " + str(val * list2[num])

        print(string)    


def divideAndDisplayLists(list1, list2):
    print("------------")
    print("Divide lists")

    for num, val in enumerate(list1):
        string = str(val) + " / " + str(list2[num]) + " = " + str(val / list2[num])

        print(string)  



addAndDisplayLists(listOne, listTwo)

substractAndDisplayLists(listOne, listTwo)

multiplyAndDisplayLists(listOne, listTwo)

divideAndDisplayLists (listOne, listTwo)