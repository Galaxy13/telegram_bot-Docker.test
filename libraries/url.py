from urllib.parse import urlparse


def url_validate(link):
    try:
        result = urlparse(link)
        return all([result.scheme, result.netloc])
    except:
        return False
