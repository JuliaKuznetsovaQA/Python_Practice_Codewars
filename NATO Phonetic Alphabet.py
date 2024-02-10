"""Complete the function nato that takes a word in parameter and returns a string
that spells the word using the NATO phonetic alphabet.

There should be a space between each word in the returned string, and the first letter of each word
should be capitalized.

For those of you that don't want your fingers to bleed, this kata already has a dictionary typed out for you."""

# LETTERS is preloaded


def nato(word):
    s = []
    for i in word:
        s.append(LETTERS[i.upper()])
    return ' '.join(s)
