import random
import string

class URLShortener:
    def __init__(self):
        self.url_to_short = {}
        self.short_to_url = {}

    def shorten_url(self, url):
        if url in self.url_to_short:
            return self.url_to_short[url]
        else:
            characters = string.ascii_letters + string.digits
            short_url = ''.join(random.choice(characters) for i in range(6))
            self.url_to_short[url] = short_url
            self.short_to_url[short_url] = url
            return short_url

    def get_original_url(self, short_url):
        if short_url in self.short_to_url:
            return self.short_to_url[short_url]
        else:
            return None
