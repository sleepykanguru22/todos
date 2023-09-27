
todos = []
while True:
    action = input("type add, show, or exit: ")
    match action:
        case "add":
            todo =input("enter a todo: ")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            print("bye 👋")
            break
    
  
#   match--> match this value
#   case--> if match is true then run this case