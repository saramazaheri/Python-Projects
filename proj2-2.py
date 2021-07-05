filename = 'BB.txt'
try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    words = contents.split("Walter White")
    num_word = len(words)
    print(f"This {filename} file is talking about Walter White for {num_word}.")