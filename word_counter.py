
words=[]

with open("demofile.txt") as f:
    lines = f.read().split("\n")

    for line in lines:
        words.extend(line.split(' '))


print(f"Number of words in file is {len(words)}.")