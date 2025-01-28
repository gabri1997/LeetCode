import os

"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only."""

def lengthOfLastWord(input):
        """
        :type s: str
        :rtype: int
        """
        input = input.strip()
        length_last_word = 0
        input = list(input)
        for c in input[::-1]:
            if c != ' ':
                length_last_word += 1
            else: 
                break

        return length_last_word

if __name__ == '__main__':

    input = '   want to fly to the moon  '
    lenght = lengthOfLastWord(input)
    print('La lunghezza dell\'ultima parole è: ', lenght)

