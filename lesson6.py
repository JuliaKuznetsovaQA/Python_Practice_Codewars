import re

text = 'Th1sf робот module provides regular expression matching operations similar to those found in Perl. ' \
       'Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). ' \
    'However, Unicode strings and 8-bit strings cannot be mixed: that is, you cannot match a Unicode s4tring ' \
    'with a bytes pattern or vice-versa; similarly, when asking for a substitution, the replacement string ' \
    'must be of the same type as both the pattern and the search string.'\
       'Regular expressions use the backslash character to indicate special forms or to allow special '\
       'characters to be used without invoking their special meaning. This collides with Python’s usage ' \
    'of the same character for the same purpose in string literals; for example, 5to match a literal backslash, ' \
    'one might have to write as the pattern string, because the regular expression must be ' \
    'and each 6 must be expressed as \\ \t inside a regular Python string literal. Also, please note ' \
    'that any invalid escape sequences in Python’s usage of the backslash in string literals now generate ' \
    'a SyntaxWarning and in the future this will become 2a SyntaxError. This behaviour will happen even if ' \
    'it is a valid22 escape sequence for a regular expression.'\
       'The solution is to use Python’s raw string notation for regular expression patterns; ' \
    'backslashes are not handled in any special 264way in a string literal prefixed with 'r'. ' \
    'So r"\n" is a two-character Google1\'s contain3ing while "\n" is a one-character string ' \
    'containing a newline. Usually patterns will be expressed in Python code using this raw string notation.'\
       'It is important to note that most regular expression operations are available as module-level functions ' \
    'and methods on compiled regular expressions. The functions are shortcuts that don’t require you ' \
    'to compile a regex object first, but miss some fine-tuning parameters.f a particular string ' \
    'matches a given regular expression (or if a given regular expression matches a particular string, ' \
    'which comes down to the same thing).'

# pattern = r'\d'
#
# result = re.split(pattern, text)
# print(result)
# print(len(result))


