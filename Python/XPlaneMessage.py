class XPlaneMessage:
    def __init__(self):
        self.Id = -1
        self.Values = []

    def __str__(self):
        result = f'{self.Id} -> '
        for i in range(0, len(self.Values)):
            result += f'{self.Values[i]} , '
        return result
