import os
import shutil

import gc

import numpy as np
import pandas as pd

from src.utils.feat_args import fargs
from src.utils.path_args import pargs


def getUserData(train_type):
    if train_type == 'cv':
        #### train dataset
        if os.path.exists(pargs.tmp_data_path + '/tmp_train_data_user.npy'):
            X_train = np.load(pargs.tmp_data_path + '/tmp_train_data_user.npy')
        else:
            X_train = np.load(pargs.train_data_path + '/train_arr_user_age.npy')
            for n, i in enumerate(fargs.user_feat):
                if n == 0:
                    pass
                else:
                    X_train = np.concatenate((X_train, np.load(pargs.train_data_path + '/train_arr_%s.npy' % i)), axis=1)

            # save as tmp file
            np.save(pargs.tmp_data_path + '/tmp_train_data_user.npy', X_train)

        return X_train

    elif train_type == 'val':
        # load tmp file if exists
        if os.path.exists(pargs.tmp_data_path + '/tmp_tri_train_data.npy') \
                and os.path.exists(pargs.tmp_data_path + '/tmp_val_train_data.npy'):

            X_tri_data = np.load(pargs.tmp_data_path + '/tmp_tri_train_data_user.npy')
            X_val_data = np.load(pargs.tmp_data_path + '/tmp_val_train_data_user.npy')



        else:
            #### original train dataset
            if os.path.exists(pargs.tmp_data_path + '/tmp_train_data_user.npy'):
                X_train = np.load(pargs.tmp_data_path + '/tmp_train_data_user.npy')
            else:
                X_train = np.load(pargs.train_data_path + '/train_arr_user_age.npy')
                for n, i in enumerate(fargs.user_feat):
                    if n == 0:
                        pass
                    else:
                        X_train = np.concatenate((X_train, np.load(pargs.train_data_path + '/train_arr_%s.npy' % i)), axis=1)

                # save as tmp file
                np.save(pargs.tmp_data_path + '/tmp_train_data_user.npy', X_train)

            # train_df
            shutil.copy(pargs.train_data_path + '/train_origin_final.h5', './')
            test_df = pd.read_hdf('train_origin_final.h5')

            # pepare for dataset
            i = test_df.loc[test_df.日期 == 319].index
            m = test_df.loc[test_df.日期 != 319].index
            ### train dataset
            X_tri_data = X_train[m]
            # np.save(args.tmp_data_path + '/tmp_tri_train_data_user.npy', X_tri_data)

            ### test dataset
            X_val_data = X_train[i]
            # np.save(args.tmp_data_path + '/tmp_tri_train_data_user.npy', X_tri_data)

            ## collect
            del X_train
            gc.collect()

        return X_tri_data, X_val_data

    elif train_type == 'test':
        #### original rain dataset
        if os.path.exists(pargs.tmp_data_path + '/tmp_train_data_user.npy'):
            X_train = np.load(pargs.tmp_data_path + '/tmp_train_data_user.npy')
        else:
            X_train = np.load(pargs.train_data_path + '/train_arr_user_age.npy')
            for n, i in enumerate(fargs.ad_feat):
                if n == 0:
                    pass
                else:
                    X_train = np.concatenate((X_train, np.load(pargs.train_data_path + '/train_arr_%s.npy' % i)), axis=1)
            # save as tmp file
            np.save(pargs.tmp_data_path + '/tmp_train_data_user.npy', X_train)

        if os.path.exists(pargs.tmp_data_path + '/tmp_test_data_user.npy'):
            X_test = np.load(pargs.tmp_data_path + '/tmp_test_data_user.npy')
        else:
            X_test = np.load(pargs.test_data_path + '/test_arr_user_age.npy')
            for n, i in enumerate(fargs.user_feat):
                if n == 0:
                    pass
                else:
                    X_test = np.concatenate((X_test, np.load(pargs.test_data_path + '/test_arr_%s.npy' % i)), axis=1)

            np.save(pargs.tmp_data_path + '/tmp_test_data_user.npy', X_test)
        ###

        return X_train, X_test

    else:
        raise Exception('No Such Train Type')
