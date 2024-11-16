from urllib.parse import urlparse


def get_url_hash(short_url: str) -> str:
    """
    Extracts the hash code from the given short URL.

    Args:
        short_url (str): The short URL from which to extract the hash.

    Returns:
        str: The hash code extracted from the short URL.
    """
    parsed_url = urlparse(short_url)
    path = parsed_url.path  # e.g., '/url/3UxbHC'
    return path.rstrip('/').split('/')[-1]



