def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    words = []
    string_stripped = s.strip()
    actual_word = []

    for letter in string_stripped:
        if letter != ' ':
            actual_word.append(letter)
        elif actual_word:  
            words.append(''.join(actual_word))
            actual_word = []

   
    if actual_word:
        words.append(''.join(actual_word))

    return ' '.join(words[::-1])  

if __name__ == '__main__':
    string = " ciao questa      frase deve essere reversata "
    reversed_string = reverseWords(string)
    print('Result:')
    print(reversed_string)
