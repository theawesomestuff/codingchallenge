class TriangularGlassStack:
    """
    A triangular stack of glasses, where you can pour liquid on the glasses
    """

    def __init__(self):
        self.glass_capacity = 250  # glass capacity in ml
        self.row = []

    def add_liquid(self, amount):
        """
        Pour liquid into top most glass
        :param amount: amount of liquid in ml
        :return:
        """
        pass

    def get_liquid(self, i, j):
        """
        Get how much liquid is in the j'th glass of the i'th row
        :param i: row index
        :param j: glasses index in the particular row
        :return:  amount of liquid in ml
        """
        return self.row[i][j]
