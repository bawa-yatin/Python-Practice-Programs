
# Given a string, reverse all the words which have odd length.
# The even length words are not changed.

def odd_words_reverse(text):
    word_list = text.split()
    result = ""
    for val in word_list:
        if len(val) % 2 == 1:
            result += "".join(val[::-1]) + " "
        else:
            result += val + " "
    return result


str_val = input("Enter a string: ")

if str_val.isnumeric():
    print("Provide a string only!")
else:
    res = odd_words_reverse(str_val)
    print("After reversing words with odd length", end="\n")
    print(res)