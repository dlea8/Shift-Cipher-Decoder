import string

common_letters = ['e', 't', 'a', 'i', 'o', 'n', 's', 'h']

''' 
iterate over the cipher text and create a dictionary of the letters and their frequency
return the dictionary of letters and frequencies
'''
def get_frequencies(inputText):

    letters = {}

    # remove spaces and punctuation from the cipher text in order to do frequency analysis
    noSpace = inputText.replace(" ", "").replace("\n", "").lower()
    noSpace = noSpace.translate(str.maketrans('', '', string.punctuation))

    # construct a dictionary of all lowercase letters in the cipher text and the frequency they appear
    for l in noSpace:
        if l not in letters.keys():
            letters[l] = 1
        else:
            letters[l] += 1

    return letters


'''
Calculate the shift by matching the most common letters in the cipher text to the most
common letters in the english alphabet
return the shift value
'''
def find_shift(letter_dict, letter):

    # find the letter in the cipher text that showed up the most
    max_letter = max(letter_dict, key=letter_dict.get)

    # conver both letters to ascii in order to find the shift between them
    return ord(max_letter) - ord(letter)


'''
iterate over the cipher text and apply the shift to alphabetic characters
return the decoded text
'''
def decode(cipher_text):
    decoded = False
    accuracyScore = 0
    letter_index = 0

    decoded_text = ''

    # verify there is no punctuation in the cipher text
    noPunc = cipher_text.lower().translate(str.maketrans('', '', string.punctuation))

    for letter in common_letters:

        shift = find_shift(letterDict, letter)

        # for each letter int he cipher text, if it is not a space character, apply the shift and append to the decoded text
        for letter in noPunc:
            if letter == " ":
                decoded_text += " "
            elif letter == "\n":
                decoded_text += "\n"
            else:
                # subtracting 97 form the character to get a value between 0 and 25. then apply the shift.
                # #then modulo 26 to deal with letters that may have wrapped around
                # finally add 97 again to get back into the ascii range
                decoded_text += chr((((ord(letter) - 97 - shift) % 26) + 97))

        # iterate over words in the common word list until you find at least 7 that are in the potentially decoded text
        for word in check_words:
            if word in decoded_text:
                accuracyScore += 1
            if accuracyScore >= 7:
                decoded = True
                break

        # if decoding was successful, break out of the loop. If not try the next most common letter
        if decoded:
            break
        else:
            accuracyScore = 0
            decoded_text = ''
            letter_index += 1

    return decoded_text, shift


'''
Opens CipherText.txt file and reads the contents to get the cipher text to decode.
'''
def read_cipher():
    with open('CipherText.txt') as f:
        text = f.read()
    return text


'''
Opens CommonWords.txt and reads in the 3000 most common words in the english language. 
This will be used to verify the accuracy of the decoder
'''
def read_common_words():
    with open('commonWords.txt') as f:
        words = f.readlines()
    return words


check_words = read_common_words()

print("\n\nDECRYPTING CIPHER TEXT BELOW")
print("==============================================")

cipher_text = read_cipher()

print("\nCipher Text: \n----------------------------------------------")
print(cipher_text)
print("\nDecrypting...\n")

letterDict = get_frequencies(cipher_text)

decoded_text, shift = decode(cipher_text)


print("DECRYPTION SUCCESSFUL! \n")
print("Shift: " + str(shift) + "\n")
print("Decrypted text: \n----------------------------------------------")
print(decoded_text)

