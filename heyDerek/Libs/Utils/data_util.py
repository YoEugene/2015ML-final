import numpy as np
from sklearn import preprocessing


def normalize_data(data, norm='l2', axis=0):
    return preprocessing.normalize(data, norm=norm, axis=axis)


def normalize_data_minmax(data, axis=0):
    min_vec = np.min(data, axis=axis)
    max_vec = np.max(data, axis=axis)
    dif_vec = max_vec - min_vec
    if axis == 0:
        min_mat = np.tile(min_vec.reshape((1, data.shape[1])), (data.shape[0], 1))
        dif_mat = np.tile(dif_vec.reshape((1, data.shape[1])), (data.shape[0], 1))
    else:
        min_mat = np.tile(min_vec.reshape((data.shape[0], 1)), (1, data.shape[1]))
        dif_mat = np.tile(dif_vec.reshape((data.shape[0], 1)), (1, data.shape[1]))
    return (data - min_mat) / dif_mat


def standardize_data_var(data):
    data_mean = np.mean(data, axis=0)
    data_var = np.var(data, axis=0)
    return (data - data_mean) / data_var


def standardize_data_std(data):
    return preprocessing.scale(data)


def random_sample(data, sample_num):
    data_num = data.shape[0]
    sample_indices = np.random.choice(np.arange(data_num), sample_num)
    return data[sample_indices]


def shuffle_data(data):
    shuffled_data = np.array(data)
    np.random.shuffle(shuffled_data)
    return shuffled_data


def get_folded_data(data, fold_num, fold_index):
    data_size = data.shape[0]
    fold_size = int(data_size / fold_num)
    train_data = np.row_stack((data[0: fold_index * fold_size], data[(fold_index + 1) * fold_size:]))
    validation_data = data[fold_index * fold_size: (fold_index + 1) * fold_size]
    return train_data, validation_data
