

FILE_NAME=input("Enter file name: ")

try:
    with open(FILE_NAME,"r",encoding="utf-8") as f:
        tasks=[line.strip() for line in f]
except FileNotFoundError:
    tasks=[]

if tasks:
    print("To-Do список:")
    for task in tasks:
        print(task)
else:
    print("Список завдань порожній")

new_task = input("\n\nВвеcти нове завдання: ").strip()
if new_task:
    tasks.append(new_task)
    with open(FILE_NAME,"w",encoding="utf-8") as f:
        for task in tasks:
            f.write(task +"\n")
    print("Завдання додано")