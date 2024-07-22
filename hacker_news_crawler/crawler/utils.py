import re


def remove_symbols(text: str) -> str:
    """Removes symbols from a given string"""
    pattern = r"[^\w\s]"
    return re.sub(pattern, "", text)


def get_title_length(title: str) -> int:
    """Takes in a string and returns it's word length"""
    title = remove_symbols(title)
    title = title.split(' ')
    title = [word for word in title if word]

    return len(title)
