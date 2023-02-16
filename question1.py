import numpy
import pandas as pd
import tensorflow as tf
import os 


def load_train(data_root):
    
    data_lst = []

    for p,d,files in os.walk(data_root):
        # print(p,d,files)
        
        for f in files:
            data_lst.append(pd.read_csv(os.path.join(p,f)))

    
    df= pd.concat(data_lst,axis=0)
    
    x = df.pop('X')
    y = df.pop('Y')
    
    x = tf.data.Dataset.from_tensor_slices(x.values)
    y = tf.data.Dataset.from_tensor_slices(y.values)


    X_train = list(x.as_numpy_iterator())
    y_train = list(y.as_numpy_iterator())


    return X_train , y_train




if __name__ == '__main__':
    print('q1')
    X_train, y_train = load_train('./temp')

    print(X_train)
    print(y_train)
