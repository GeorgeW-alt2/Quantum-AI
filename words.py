with open("test.txt", 'r', encoding = 'utf=8') as file:
    content = file.read()

# Split the content into words
words = content.split()

with open("words.txt", 'w', encoding = 'utf=8') as file:
    for word in words:
        file.write(word + "\n")