#!/usr/bin/env python

from data_utils import create_dataset

if __name__ == 'main':
    # create dataset for training
    create_dataset('config.json')
    print('dataset for training created')

