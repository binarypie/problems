class FileReader:
    def read_file(self, filename):
        with open(filename, 'r') as f:
            contents = f.read()

        return contents
