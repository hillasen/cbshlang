class Parser:
    def __init__(self, code):
        self.code = (code.replace(' ', '')).replace('\n', 'f');
        self.parsed = []

    def getParsed(self):
        return self.code + "f"
