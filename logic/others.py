def parse_to_string_list(text: str) -> list[str]:
    """
    Parse a string to a list of strings.
    "[arroz, feijão, batata]" -> ["arroz", "feijão", "batata"]
    """
    
    return text[1:-1].replace(' ', '').split(',') # Remove the brackets and split by ", "