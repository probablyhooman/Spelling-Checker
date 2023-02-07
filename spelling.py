from textblob import TextBlob

#creating a conver function :

def Convert(string):
    li = list(string.split())
    return li

#taking the input from the user:
string1 = input ("Enter Your Word: ")
words = Convert(string1)

#appending the correct word in an empty list:
corrected_words = []

for i in words:
    corrected_words.append(TextBlob(i))   
print("Wrong words :", words)
print("Corrected Words are :")

#iterating for loop for the correct word:
for i in corrected_words:
    print(i.correct(), end= " ")