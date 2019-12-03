from sklearn.model_selection import train_test_split

def train_val_test(df):
    train_val, test = train_test_split(df, test_size=0.1)
    train, val = train_test_split(train_val, test_size=0.8)

    return train, val, test
