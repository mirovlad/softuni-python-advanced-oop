def palindrome(word, idx):
    def get_string(is_palindrome):
        if is_palindrome:
            return f"{word} is a palindrome"
        return f"{word} is not a palindrome"

    # ""[0:0] is safe to do
    sub_word = word[idx:len(word) - idx:]
    sub_word_len = len(sub_word)
    if sub_word_len < 2:
        return get_string(True)
    # From here on sub_word_len >=2

    if sub_word[0] != sub_word[sub_word_len - 1]:
        return get_string(False)

    return palindrome(word, idx + 1)


print(palindrome("abcba", 0))
# abcba is a palindrome

print(palindrome("peter", 0))
# peter is not a palindrome
