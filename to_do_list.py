# todo_list = []

# while True:
#     user_action = input("Type add, show or exit: ")
#     user_action = user_action.strip()

#     match user_action:
#         case "add":
#             todo = input("Enter an item to todo list: ")
#             todo_list.append(todo)
#         case "show":
#             for item in todo_list:
#                 item = item.title()
#                 print(item)
#         case "exit":
#             break
#         case x:
#             print("Error, please enter a known command: ")

# print("Good Bye!")


while True:
    user_input = input("Please enter what country you are from: ")

    match user_input:
        case "US":
            print("Hello")
        case "India":
            print("Namaste")
        case "Germany":
            print("Hallo")
        case "exit":
            break
