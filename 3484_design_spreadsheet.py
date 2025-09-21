


"""
2484. Design SpreadSheet (https://leetcode.com/problems/design-spreadsheet/?envType=daily-question&envId=2025-09-21)

literally just use a hashmap that takes in pairs of cell codes and values

setCell():
    set the key of cell to the value

resetCell():
    set cell to 0

getValue():
    split string by the '+' symbol
    check first character of each split string
        if is an integer, use that
        if is a letter, use the hashmap to get the value at that cell
            if the letter doesn't exist in the hashmap, use 0

runtime: O(1)
space: O(1)
"""

class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = {}

    def setCell(self, cell: str, value: int) -> None:
        self.spreadsheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)
    
    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split("+")
        return self.formulaHelper(a) + self.formulaHelper(b)
    
    def formulaHelper(self, cell):
        if cell[0].isalpha():
            if cell in self.spreadsheet:
                return self.spreadsheet[cell]
            return 0
        return int(cell)

sheet = Spreadsheet(3)
print(sheet.getValue('=5+7'))
sheet.setCell('A1', 10)
print(sheet.getValue('=A1+6'))



"""
idk why i did this
like this is just way worse
"""

class worseSpreadsheet:
    def __init__(self, rows: int):
        self.spreadsheet = [[0 for _ in range(26)] for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        i, j = self.getCell(cell)
        self.spreadsheet[i][j] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)
    
    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split("+")
        return self.formulaHelper(a) + self.formulaHelper(b)

    def getCell(self, cell):
        return [int(cell[1:]), ord(cell[0])-65]
    
    def formulaHelper(self, cell):
        if cell[0].isalpha():
            i, j = self.getCell(cell)
            return self.spreadsheet[i][j]
        return int(cell)
    
