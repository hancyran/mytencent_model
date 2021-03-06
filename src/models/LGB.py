import lightgbm as lgb


def createLGB(max_depth=7, learning_rate=0.1, n_estimators=1500, feature_fraction=1.0, objective='fair', num_leaves=31,
              reg_alpha=0, reg_lambda=0):
    model = lgb.LGBMRegressor(max_depth=max_depth,
                              learning_rate=learning_rate,
                              num_leaves=num_leaves,
                              n_estimators=n_estimators,
                              subsample=0.8,
                              colsample_bytree=0.7,
                              #                               subsample_for_bin=50000,
                              min_child_weight=1,
                              reg_alpha=reg_alpha,

                              reg_lambda=reg_lambda,
                              scale_pos_weight=1,
                              #                               min_split_gain=0,
                              #                               max_bin=425,
                              #                               subsample_freq=1,
                              seed=2019,
                              boosting_type='gbdt',
                              feature_fraction=feature_fraction,
                              #                               boosting_type='dart',
                              objective=objective,
                              nthread=32, silent=True)
    #     model.set_params(**{'objective': custom_sample_train}, metrics = ["mse", 'mae'])

    return model
