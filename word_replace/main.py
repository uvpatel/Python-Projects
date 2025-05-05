def replace_word_at_index():
    text = "hi,guys,i am tomi, and hi hi hi hi"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    index = int(input("Enter which occurrence to replace (1 for first, 2 for second, etc.): "))

    # Split the text into a list of words
    words = text.split()
    
    # Count occurrences of the word and replace the one at the given index
    count = 0
    for i in range(len(words)):
        if words[i] == word_to_replace:
            count += 1
            if count == index:
                words[i] = word_replacement
                break
    
    # Join the words back into a single string
    modified_text = ' '.join(words)
    print(modified_text)

replace_word_at_index()
