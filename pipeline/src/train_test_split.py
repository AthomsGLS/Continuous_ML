from sklearn.model_selection import train_test_split

def data_split(df, target_name, test_size, seed):

    # split into train and test sections
    y = df.pop(target_name) # remove target from dataframe
    X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=test_size, random_state=seed)

    return X_train, X_test, y_train, y_test