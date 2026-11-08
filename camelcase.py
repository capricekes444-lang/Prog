
def convert(s: str) -> str:
    """
    >>> convert("check")
    'check'
    >>> convert("convertInput")
    'convert_input'
    >>> convert("readFromFile")
    'read_from_file'
    >>> convert("helloWorld")
    'hello_world'
    >>> convert("myVariableName")
    'my_variable_name'
    """
    result = ""

    for char in s:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char

    return result


if __name__ == "__main__":
    tekst = input("camelCase: ")
    print("snake_case:", convert(tekst))
