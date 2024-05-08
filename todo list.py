def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====\n1. Add Task\n2. Show Tasks\n3. Mark Task as Done\n4. Exit")
        
        c = input("Enter your choice: ")

        if c == '1':
            print()
            n = int(input("How may task you want to add: "))
            
            for i in range(n):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif c == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif c == '3':
            index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif c == '4':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()