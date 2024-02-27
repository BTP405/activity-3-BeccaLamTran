import pickle

def pickle_obj(obj, file_path):
    """
    Pickles the given object and saves it to the specified file.

    Parameters:
    obj: The object to pickle.
    file_path: The path to save the pickled data.

    Returns:
    None
    """
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f)
    print(f"Object pickled and saved to {file_path}")

def unpickle_obj(file_path):
    """
    Unpickles an object from the specified file.

    Parameters:
    file_path: The path to the pickled data file.

    Returns:
    The unpickled object.
    """
    with open(file_path, 'rb') as f:
        obj = pickle.load(f)
    return obj
