import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
from scipy import interp
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
import statsmodels.api as sm
from scipy import stats
from sklearn.feature_selection import SelectKBest, chi2, f_classif, RFE, f_regression
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA 
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import StratifiedKFold, cross_val_score, learning_curve, validation_curve, GridSearchCV, train_test_split, KFold, cross_validate
from sklearn.svm import SVC, SVR
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import make_scorer, accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_curve, auc, mean_squared_error, r2_score

def fill_in_missing_values(data_frame, list_of_column_names):
    is_missing = False
    for col_name in list_of_column_names:
        if data_frame[col_name].isnull().sum() > 0:
            is_missing = True
            print (col_name)

    if not is_missing:
        print ('we dont see missing values for any of the columns')
        
    # fill NA with mean
    if is_missing:
        new_data_frame = data_frame.fillna(data_frame.mean())
        new_data_frame.to_csv('fill_in_missing_value_with_mean.csv')
        print ('some columns contain missing values and are filled with mean values.')

def plot_correlation_heat_map(data_frame, list_of_column_names):
    '''
        input: pandas dataframe
    '''
    df = data_frame[list_of_column_names]
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(12, 10))
    cmap = sns.diverging_palette(0, 230, 90, 60, as_cmap=True)
    sns.heatmap(corr, annot=True, fmt=".2f", 
               linewidths=5, cmap=cmap, vmin=-1, vmax=1, 
               cbar_kws={"shrink": .8}, square=True)
    yticks = [i for i in corr.index]
    xticks = [i for i in corr.columns]
    plt.yticks(plt.yticks()[0], labels=yticks, rotation=0)
    plt.xticks(plt.xticks()[0], labels=xticks)
    title = 'CORRELATION MATRIX\n'
    plt.title(title, loc='left', fontsize=18)
    fig.tight_layout()
    plt.show()

def plot_scatter_matrix(data_frame, list_of_column_names):
    pd.plotting.scatter_matrix(df, alpha=0.2, figsize = (10,10))
    plt.tight_layout()
    plt.show()
    
def calculate_variance_inflation_factor(data_frame, list_of_column_names):
    selected_dataframe = data_frame[list_of_column_names]
    X = add_constant(selected_dataframe)
    return pd.Series([variance_inflation_factor(X.values, i) for i in range(X.shape[1])], 
                      index=X.columns)

def principle_component_analysis(data, legend_size):

    '''
        data will be a stack of Raman curves, here 12 curves
        with a shape (12, 16801) 
    '''
    scaler = StandardScaler()
    pca = PCA()
    scaler.fit(data)
    scaled_data = scaler.transform(data)
    pca.fit(scaled_data)
    data_transform = pca.transform(scaled_data)
    variance_ratio = pca.explained_variance_ratio_
    print (variance_ratio)
    print (variance_ratio.cumsum())
    fig = plt.figure(figsize=(16, 6), dpi=100)
    ax1 = fig.add_subplot(131)
    
    for x_point, y_point in zip(data_transform[:,0], data_transform[:,1]):
        ax1.plot(x_point, y_point, 'bo', markersize = legend_size)

    ax1.set_xlabel('Principal Component 1 ({:.3f})'.format(variance_ratio[0]), fontsize = 12)
    ax1.set_ylabel('Principal Component 2 ({:.3f})'.format(variance_ratio[1]), fontsize = 12)
    ax1.axvline(x=0, linestyle = 'dotted', color = 'r', lw=2)
    ax1.axhline(y=0, linestyle = 'dotted', color = 'r', lw=2)
    ax1.legend(loc=0, prop = {'size': legend_size})
    ax1.set_title('Plot of first two principle components')

    ax2 = fig.add_subplot(132)
    ybar = variance_ratio*100
    xbar = ['PC' + str(x) for x in range(1, len(ybar) + 1)]
    ax2.bar(range(1, len(ybar)+1), ybar, tick_label = xbar)
    ax2.set_ylabel('Percentage of Explained Variance',fontsize = 12)
    ax2.set_xlabel('Principal Component',fontsize = 12)
    plt.xticks(rotation=90)
    ax2.set_title('Scree Plot')

    ax3 = fig.add_subplot(133)
    ax3.plot(xbar, variance_ratio.cumsum()*100, 'b-', lw =2, label = 'cumulative_explained_variance_ratio')
    ax3.set_ylabel('Cumulative Percentage of Explained Variance',fontsize = 12)
    ax3.set_xlabel('Principal Component',fontsize = 12)
    ax3.set_title('Cumulative Variance Explained')
    ax3.axhline(y=95, linestyle = 'dotted', color = 'r', lw=2)
    plt.xticks(rotation=90)
    fig.tight_layout()
    fig.show()


def statsmodel_linear_regression(X, y):
    X2 = sm.add_constant(X)
    est = sm.OLS(y, X2)
    est2 = est.fit()
    print(est2.summary())
    
def select_best_k(X, y, flag, k_best = 10):
    if flag == 'f_regression':
        selector = SelectKBest(f_regression, k=k_best)
    elif flag == 'tree':
        rf = RandomForestRegressor(n_estimators=100)
        rf.fit(X, y)
        sorted_idx = rf.feature_importances_.argsort()[::-1]
        plt.barh([list(X)[i] for i in sorted_idx][:k_best], rf.feature_importances_[sorted_idx][:k_best])
        plt.xlabel("Random Forest Feature Importance")
        plt.show()
        print ([list(X)[i] for i in sorted_idx][:k_best])
        return X[[list(X)[i] for i in sorted_idx][:k_best]]
    elif flag == 'rfe':
        rfe = RFE(estimator = RandomForestRegressor(n_estimators=100), n_features_to_select= k_best)
        rfe.fit(X, y)
        selected_columns = []
        for idx, boolean in enumerate(rfe.support_):
            if boolean:
                selected_columns.append(list(X)[idx])
        print (selected_columns)
        return rfe.transform(X)
    
    selector.fit(X, y)
    # Get columns to keep and create new dataframe with those only
    cols = selector.get_support(indices=True)
    X_new = X.iloc[:,cols]
    print ([list(X)[idx] for idx in selector.scores_.argsort()[::-1][:k_best]])
    return X_new 

def pipeline_performance(X_train, X_test, y_train, y_test, pipeline):
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    
    scoring = {'mse' : make_scorer(mean_squared_error), 
               'r2' : make_scorer(r2_score)}

    kfold = KFold(n_splits=10, random_state=42)
    scores = cross_validate(estimator = pipeline,
                             X = X_train,
                             y = y_train,
                             cv = kfold,
                             n_jobs = 1,
                             scoring = scoring,
                             return_train_score=True)

 
    print('Ten-fold CV train r2: %.3f +/- %.3f' % (np.mean(scores['train_r2']),np.std(scores['train_r2'])))
    print('Ten-fold CV test r2: %.3f +/- %.3f' % (np.mean(scores['test_r2']),np.std(scores['test_r2'])))
    print('Ten-fold CV train mse: %.3f +/- %.3f' % (np.mean(scores['train_mse']),np.std(scores['train_mse'])))
    print('Ten-fold CV test mse: %.3f +/- %.3f' % (np.mean(scores['test_mse']),np.std(scores['test_mse'])))

    print('Model performance on hold-out data: mse: %.3f' % mean_squared_error(y_true=y_test, y_pred=y_pred))
    print('Model performance on hold-out data: r2: %.3f' % r2_score(y_true=y_test, y_pred=y_pred))


def hyper_parameters_grid_search(X_train, y_train, X_test, y_test, pipeline, flag = 'rf'):
    if flag == 'rf':
        param_grid = {'randomforestregressor__n_estimators': [10, 25, 50, 100, 200]}

    elif flag == 'knn':
        param_grid = {'kneighborsregressor__n_neighbors': [i for i in range(1,15)]}

    elif flag == 'svr':
        param_grid = {'svr__C':[0.001, 0.01, 0.1, 1.0, 10, 100],
                      'svr__gamma':[0.001, 0.01, 0.1, 1.0, 10, 100],
                      'svr__kernel':['linear','rbf']}
        
    gs = GridSearchCV(estimator = pipeline,
                      param_grid = param_grid,
                      scoring = 'r2',
                      cv=10,
                      refit=True,
                      n_jobs = -1)
    gs = gs.fit(X_train, y_train)
    print(gs.best_score_)
    print(gs.best_params_)
    clf = gs.best_estimator_
    clf.fit(X_train, y_train)
    print('Test R2: %.3f' % clf.score(X_test, y_test))
    

def generate_learning_curves(X_train, y_train, pipeline):
    train_sizes, train_scores, test_scores = learning_curve(estimator=pipeline,
                                                            X = X_train,
                                                            y = y_train,
                                                            train_sizes=np.linspace(0.1, 1.0, 10),
                                                            cv=10,
                                                            n_jobs=1)
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    plt.plot(train_sizes, train_mean,color='blue', marker='o', markersize=5, label='Training R2')
    plt.fill_between(train_sizes,train_mean + train_std,train_mean - train_std,alpha=0.15, color='blue')
    plt.plot(train_sizes, test_mean,color='green', linestyle='--',marker='s', markersize=5,label='Validation R2')

    plt.fill_between(train_sizes,test_mean + test_std,test_mean - test_std,alpha=0.15, color='green')
    plt.grid()
    plt.title('Learning Curves', fontsize = 12)
    plt.xlabel('Number of training examples', fontsize = 12)
    plt.ylabel('R2', fontsize = 12)
    plt.legend(loc = 'lower right')
    plt.ylim([0.2, 1.03])
    plt.tight_layout()
    plt.show()

def generate_validation_curves(X_train, y_train, pipeline):
    param_range = [10, 50, 100, 200, 500]
    train_scores, test_scores = validation_curve(estimator=pipeline,
                                                 X=X_train,
                                                 y=y_train,
                                                 param_name='randomforestregressor__n_estimators',
                                                 param_range=param_range,
                                                 cv=10)
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    plt.plot(param_range, train_mean,color='blue', marker='o',markersize=5, label='Training R2')
    plt.fill_between(param_range, train_mean + train_std,train_mean - train_std, alpha=0.15,color='blue')
    plt.plot(param_range, test_mean,color='green', linestyle='--',marker='s', markersize=5,label='Validation R2')

    plt.fill_between(param_range,test_mean + test_std,test_mean - test_std,alpha=0.15, color='green')
    plt.grid()
    plt.xscale('log')
    plt.legend(loc='lower right')
    plt.title('Validation Curves', fontsize = 12)
    plt.xlabel('Number of estimators', fontsize = 12)
    plt.ylabel('R2', fontsize = 12)
    plt.ylim([0.2, 1.0])
    plt.tight_layout()
    plt.show()
     
if __name__ == '__main__':
    ### STEP - 0 LOAD DATA AS A DATAFRAME USING PANDAS; ADD COLUMN NAMES IF NECESSARY
    file_name = 'BostonHousing.csv'
    df = pd.read_csv(file_name)

    ### STEP - 1a CHECK IF THERE ARE MISSING VALUES ###
    #fill_in_missing_values(df, list_of_column_names = [i for i in range(32)])
    #df[col_name].fillna(df[col_name].mean(), inplace = True)
    #df['col_name'].value_counts()

    ### STEP - 1b PLOT CATEGORICAL LABELS
    def step_1b_plot_labels(label_col_name):
        df[label_col_name].value_counts().plot(kind = 'bar', rot = 0)
        plt.ylabel('value counts', fontsize = 15)
        plt.xticks(rotation=90)
        plt.show()
        
    ### STEP - 1c RELOAD DATA IF NECESSARY AND REPLACE CATEGORICAL VALUES WITH NUMERICAL ONES ###
    # df = pd.read_csv('fill_in_missing_value_with_mean.csv')
    X = df.iloc[:, :-1]
##    # X[col_name] = X[col_name].replace({'No': 0, 'Yes' : 1})
    y = df.iloc[:, -1]
##    y = y.replace({'M': 1, 'B': 0})
    y = np.array(y)

    ### STEP - 1d PLOT CORRELATION MAP ###
    def step_1d_plot_correlation_map():
        plot_correlation_heat_map(df, list_of_column_names = list(df))

    ### STEP - 1e PLOT SCATTER MATRIX ###
    def step_1e_plot_scatter_matrix():
        plot_scatter_matrix(df, list(df))

    ### STEP - 1f CALCULATE VIF ###
    def step_1f_calculate_vif():
        print (calculate_variance_inflation_factor(X, list(X)))
 
    ### STEP - 1g PLOT PCA PLOTS ###
    def step_1g_plot_pca():
        principle_component_analysis(X, legend_size = 8)

    '''
        RUN STEP 1 EXPERIMENTS
        (B) PLOT LABEL DISTRIBUTION
        (D) PLOT CORRELATION HEAT MAP
        (E) PLOT SCATTER MATRIX
        (F) CALCULATE VARIANCE INFLATION FACTOR
        (G) PLOT PCA
    '''
##    step_1b_plot_labels(label_col_name = 1)
##    step_1d_plot_correlation_map()
##    step_1e_plot_scatter_matrix()
##    step_1f_calculate_vif()
##    step_1g_plot_pca()

    ### STEP 2 Statsmodel multivariate linear regression ###
    def experiment_2():
        statsmodel_linear_regression(X, y)

##    experiment_2()

    ### STEP 2 SPECIFY TRAIN/TEST DATA AND PIPELINE ###
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
    pipeline_lr = make_pipeline(StandardScaler(),
                                PCA(n_components = 10),
                                LinearRegression())

    pipeline_rf = make_pipeline(StandardScaler(),
                                PCA(n_components = 10),
                                RandomForestRegressor(n_estimators = 100))

    pipeline_knn = make_pipeline(StandardScaler(),
                                 PCA(n_components = 10),
                                 KNeighborsRegressor(n_neighbors=5))

    pipeline_svr = make_pipeline(StandardScaler(),
                                 PCA(n_components = 10),
                                 SVR(gamma = 'scale'))

    ### STEP 3 MACHINE LEARNING ###
    def experiment_3a():
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_lr)

    def experiment_3b():
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_rf)

    def experiment_3c():
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_knn)

    def experiment_3d():
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_svc)

    '''
        RUN STEP 3 EXPERIMENTS
        CHECK PIPELINE MODEL PERFORMANCE OF (1) LOGISTIC REGRESSION (2) RANDOM FOREST (3) KNN (4) SUPPORT VECTOR MACHINE
    '''
##    experiment_3a()
##    experiment_3b()
##    experiment_3c()
##    experiment_3d()

    def experiment_4a():
        generate_learning_curves(X_train, y_train, pipeline = pipeline_lr)

    def experiment_4b():
        generate_validation_curves(X_train, y_train, pipeline = pipeline_rf)

    '''
        RUN STEP 3 EXPERIMENTS
        GENERATE (1) LEARNING CURVE (2) VALIDATION CURVE
    '''
##    experiment_4a()
##    experiment_4b()

    ### hyperparameters tuning ###        
    def experiment_5a():
        hyper_parameters_grid_search(X_train, y_train, X_test, y_test, pipeline_rf, flag = 'rf')
        
    def experiment_5b():
        hyper_parameters_grid_search(X_train, y_train, X_test, y_test, pipeline_knn, flag = 'knn')
        
    def experiment_5c():
        hyper_parameters_grid_search(X_train, y_train, X_test, y_test, pipeline_svr, flag = 'svr')

    '''
        RUN STEP 3 EXPERIMENTS
        GRID SEARCH ON HYPERPARAMETERS FOR (1) LOGISTIC REGRESSION (2) RANDOM FOREST (3) KNN (4) SUPPORT VECTOR MACHINE
    '''
##    experiment_5a()
##    experiment_5b()
##    experiment_5c()
        
    ### select K best features ###        
    def experiment_6a():
        new_X = select_best_k(X, y, flag = 'f_regression', k_best = 10)
        X_train, X_test, y_train, y_test = train_test_split(new_X, y, test_size=0.20, random_state=1)
        pipeline_rf = make_pipeline(StandardScaler(),
                                    RandomForestRegressor(n_estimators = 100))
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_rf)

    def experiment_6b():
        new_X = select_best_k(X, y, flag = 'tree', k_best = 10)
        X_train, X_test, y_train, y_test = train_test_split(new_X, y, test_size=0.20, random_state=1)
        pipeline_rf = make_pipeline(StandardScaler(),
                                    RandomForestRegressor(n_estimators = 100))
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_rf)

    def experiment_6c():
        new_X = select_best_k(X, y, flag = 'rfe', k_best = 10)
        X_train, X_test, y_train, y_test = train_test_split(new_X, y, test_size=0.20, random_state=1)
        pipeline_rf = make_pipeline(StandardScaler(),
                                    RandomForestRegressor(n_estimators = 100))
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_rf)
    
    '''
        RUN STEP 3 EXPERIMENTS
        SELECT K-BEST SUBSETS OF FEATURES USING (1) ANOVA (2) TREE (3) RFE
    '''
##    experiment_6a()
##    experiment_6b()
##    experiment_6c()

    
























