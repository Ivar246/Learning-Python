message = input(">")
words = message.split(' ')
print(words)
emojis ={
    ":)" : "😊",                  # ->if the message is happy then type :) in order to print happy emoji                       
    ":(" : "😞"                   # ->if the message is sad type  then type :(in order to print sad emoji
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
