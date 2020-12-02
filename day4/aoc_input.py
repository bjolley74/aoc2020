class AOCInput:
    def __init__(self, **kwargs):
        if kwargs.get('filename') == None:
            filename = 'puzzle_input.txt'
        else:
            filename = kwargs.get('filename')
        self.filename = filename
    
    @property
    def get_input(self) -> list:
        output = []
        with open(self.filename, 'r') as f:
            line = f.readline().strip()
            while line:
                output.append(line)
                line = f.readline().strip()
        return output

if __name__ == '__main__':
    test = AOCInput(filename='puzzle_input.txt')
    print(f'filename = {test.filename}')
    for line in test.get_input:
        print(line)