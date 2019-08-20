class TriangularGlassStack:
    """
    A triangular stack of glasses, where you can pour liquid on the glasses
    """

    def __init__(self):
        self.glass_capacity = 250  # glass capacity in ml
        self.rows = []  # Contains glass capacity of each glasses in each row

    def add_liquid(self, amount):
        """
        Pour liquid into top most glass
        :param amount: amount of liquid in ml
        :return:
        """
        remaining_liquid = amount
        curr_row_index = 0

        if amount < 0:
            raise ValueError(f"Amount added cannot be negative :{amount}")

        while remaining_liquid > 0:
            curr_row_glasses_count = curr_row_index + 1
            curr_row_capacity = curr_row_glasses_count * self.glass_capacity

            if remaining_liquid <= curr_row_capacity:
                # Handle case where there is NO overflow
                curr_row = [remaining_liquid/curr_row_glasses_count
                            for i in range(curr_row_glasses_count)]
                self.rows.append(curr_row)
                remaining_liquid = 0
            else:
                # Handle case where there is an overflow
                curr_row = [curr_row_capacity / curr_row_glasses_count
                            for i in range(curr_row_glasses_count)]
                self.rows.append(curr_row)
                remaining_liquid -= curr_row_capacity

            curr_row_index += 1

    def get_liquid(self, i, j):
        """
        Get how much liquid is in the j'th glass of the i'th row

        Assume that if the given i and/or j indexes are invalid,
        then return None
        :param i: row index
        :param j: glasses index in the particular row
        :return:  amount of liquid in ml
        """
        try:
            return self.rows[i][j]
        except IndexError:
            return None
