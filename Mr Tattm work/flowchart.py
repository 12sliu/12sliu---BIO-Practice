shopping_list = []
while True:
    item = input("add item")
    if item == "done":
        break
    shopping_list.append(item)

while True:
    print("Menu: ")
    print("1: Print list")
    print("2: Add more items")
    print("3: Remove items")
    print("4: Quit")
    choice = input()
    match choice:
        case "1":
            for item in shopping_list:
                print(item)
        case "2":
            item = input("Add your item: ")
            shopping_list.append(item)
        case "3":
            shopping_list.pop(int(input("Remove index?"))-1)
        case "4":
            break
        case _:
            print("No.")
