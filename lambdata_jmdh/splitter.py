from sklearn.model_selection import train_test_split

class Split:

    """
    Performs a train-validate-test split on a dataframe.


    Parameters
    ---------------------------------------
    data : dataframe or array
        the data to be split
    test_float : float
        the size (percentage) of the data to be used as test data
    val_float : float
        the size (percentage) of the data to be used as validation data
    """

    def __init__(self, data, test_float=0.1, val_float=0.333):
        self.data = data
        self.test_per = test_float
        self.val_per = val_float

    def split_one(self):
        train_val, test = train_test_split(self.data, test_size=self.test_per)
        self.test = test
        self.train_val = train_val

    def split_two(self):
        train, val = train_test_split(self.train_val, test_size=self.val_per)
        self.train = train
        self.val = val

    def show(self):
        return self.train, self.val, self.test
