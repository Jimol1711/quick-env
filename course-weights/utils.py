def dict_average(d):
    """
    Calculate the average of the values in a dictionary.
    """
    return sum(d.values()) / len(d) if d else 0