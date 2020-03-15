class Matrix:
    rows = []
    def __init__(self, matrix_string):
        self.rows = []
        srows = matrix_string.split("\n")
        for r in srows:
            e = r.split()
            self.rows.append(list(map(int, e)))

    def row(self, index):
        s = (self.rows[index - 1])
        return s

    def column(self, index):
        r = []
        for i in range(len(self.rows)):
            r.append(self.rows[i][index-1])
        return r
