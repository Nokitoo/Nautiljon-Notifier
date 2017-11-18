from config import config
import urllib.parse as urlparse

def getUrlParam(url, param):
    parsed = urlparse.urlparse(url)
    return urlparse.parse_qs(parsed.query)[param][0]

def getResourceUrl(url):
    # '/resource.png' => 'http://www.site/resource.png'
    if url and url[0] == '/':
        return config['site_domain'] + url;

    return url;
