def load_dictionary(filepath: str) -> list:
    """Loads words from a dictionary file and returns them as a list.
    
    Args:
        filepath (str): The path to the dictionary file containing words, one per line.
    
    Returns:
        list: A list of words from the dictionary file.
    """
    with open(filepath, 'r') as file:
        dictionary = file.read().splitlines()
    return dictionary