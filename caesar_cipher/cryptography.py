import nltk
import re

cipher_text = "UPJL AVWPJ"
# print(encrypt("Nice Topic",7))

def encrypt(m, k):
    m=m.upper()
    offset = 65 # A
    words = m.split()
    cipher_words = []
    for word in words:
        cipher = ""
        for char in word:
            char_num = ord(char.upper())
            shifted_num = char_num + k - offset
            mod_num = shifted_num % 26 + offset
            cipher += chr(mod_num)
        cipher_words.append(cipher.lower())
    return " ".join(cipher_words)


def decrypt(c, k):
    return encrypt(c, -k)

# print(decrypt("LNRRJ F PZ",5))
for i in range(28):
    results = decrypt(cipher_text, i).split()
    for word in results:
        if word == "Nice".upper():
            print(results, i)




nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

def count_words(m):
    candidate_words = m.split()
    count = 0
    for i in candidate_words:
        word = re.sub(r'[^A-Za-z]',' ', i)
        if word.lower() in word_list or word in name_list:
            count += 1

    return count

def crack(m):
    text = ''
    for i in range(26):
         total_words = decrypt(m, i) 
         word_count = count_words(total_words) 
         ratio = word_count / len(total_words.split()) 
         percentage = int(ratio * 100) 
         if percentage > 50: 
             text += total_words 
         return text      

print(crack("It was the best of times, it was the worst of times."))
             