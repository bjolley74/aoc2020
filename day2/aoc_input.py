class AOCInput:
    def init(self, filename):
        self.filename = filename
        self.file = self.get_input()

    def get_input(self) -> list:
        output = []
        with open(self.filename, 'r') as f:
            line = f.readline().strip()
            while line:
                output.append(int(line))
                line = f.readline().strip()
        return output