# Storing the given input into a sentence variable
sentence = "I am a teacher and I love to inspire and teach people"

# Using Built in split() method to get all the individual elements. This split() method will return list of words
values = sentence.split()

# Using Built in set() to store list in Set. Set will add the unique words to it's Set unique_values.
unique_words = set(values)

no_unique_words = len(unique_words) # len() will give how many no.of unique words exists in the set

print("Unique Words:", unique_words)  # printing unique words

print("No of Unique Words: ", no_unique_words)