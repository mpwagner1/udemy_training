todo_list = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter an item to todo list: ")
            todo_list.append(todo)
        case "show":
            for item in todo_list:
                item = item.title()
                print(item)
        case "edit":
            number = int(input("Please enter the number you would like to edit: "))
            number = number - 1
            new_todo_list = input("Please enter the edited item: ")
            todo_list[number] = new_todo_list
        case "exit":
            break
        case x:
            print("Error, please enter a known command: ")

print("Good Bye!")
