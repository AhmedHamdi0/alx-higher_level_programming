#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with 2 new lines
    after each of these characters: ., ? and :.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    lines = []
    line = ''
    for char in text:
        if char in separators:
            lines.append(line.strip())
            line = ''
        else:
            line += char

    if line:
        lines.append(line.strip())

    for line in lines:
        print(line)
