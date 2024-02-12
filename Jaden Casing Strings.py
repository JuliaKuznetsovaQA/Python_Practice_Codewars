def to_jaden_case(string):
    words = string.split()
    result = []
    for word in words:
        result.append(word.capitalize())
    return ' '.join(result)