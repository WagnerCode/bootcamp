from decorator import append


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        self.file = open(fr"/home/user/Desktop/bootcamp/bootcamp/module02/Ex03/{self.filename}", "r")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()



    def getdata(self):
        storage = []
        for line in self.file:
            storage.append(line.split(self.sep))

        return storage

    def getheader(self):
        pass


if __name__ == "__main__":
    with CsvReader('addresses.csv') as file:
        data = file.getdata()
        #header = file.getheader()
    i = 0
    for item in data:
        print(data[i][0])
        i += 1