import random
import string

# Input message and operation choice
st = input("Enter your message: ")
words = st.split(" ")

user = int(input("Enter 1 to encode or 0 to decode: "))

if user == 1:  # Encoding
    nwords = []
    for word in words:
        if len(word) >= 3:
            random_char = ''.join(random.choices(string.ascii_letters, k=3))
            new_word = random_char + word[1:] + word[0] + random_char
            nwords.append(new_word)
        else:
            nwords.append(word[::-1])  # Reverse words shorter than 3 characters
    print("Encoded message:", " ".join(nwords))

elif user == 0:  # Decoding
    nwords = []
    for word in words:
        if len(word) >= 9:  # Minimum length after encoding (3 + original length + 3)
            stripped_word = word[3:-3]  # Remove random characters
            decoded_word = stripped_word[-1] + stripped_word[:-1]  # Reverse the original encoding
            nwords.append(decoded_word)
        else:
            nwords.append(word[::-1])  # Reverse words shorter than 3 characters
    print("Decoded message:", " ".join(nwords))

else:
    print("Invalid choice. Please enter 1 for encoding or 0 for decoding.")
