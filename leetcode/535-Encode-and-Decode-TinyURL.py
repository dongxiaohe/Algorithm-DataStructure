class Codec:

    characters = string.ascii_letters + '0123456789'
    size = 6

    def __init__(self):
        self.code_url = {}
        self.url_code = {}

    def encode(self, longUrl):
        if longUrl in self.url_code: return self.url_code[longUrl]
        while True:
            code = "".join(random.choice(Codec.characters) for _ in range(Codec.size))
            if code not in self.code_url:
                self.code_url[code] = longUrl
                self.url_code[longUrl] = code
                return "http://tinyurl.com/" + code

    def decode(self, shortUrl):
        return self.code_url[shortUrl[-Codec.size:]]

