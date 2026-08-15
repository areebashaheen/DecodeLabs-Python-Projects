my_task = []
while True:
    print("1.Add Tasks")
    print("2.View Tasks")
    print("3.Exit")
    choice = input ("Choose an option:" )

    if choice =="1":
        task = input("Enter task name:")
        my_task.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(my_task) == 0:
            print("No tasks yet!")
        else:
            for index,task in enumerate(my_task):
                print(index + 1, "-",task)

    else:
                print("Goodbye!")
                break