import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
from scipy import interp
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from sklearn.feature_selection import SelectKBest, chi2, f_classif, RFE
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA 
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score, learning_curve, validation_curve, GridSearchCV, train_test_split, KFold, cross_validate
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import make_scorer, accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_curve, auc

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

def select_best_k(X, y, flag, k_best = 10):
    if flag == 'chi2':
        selector = SelectKBest(chi2, k=k_best)
    elif flag == 'anova':
        selector = SelectKBest(f_classif, k=k_best)
    elif flag == 'tree':
        rf = RandomForestClassifier(n_estimators=100)
        rf.fit(X, y)
        sorted_idx = rf.feature_importances_.argsort()[::-1]
        plt.barh([list(X)[i] for i in sorted_idx][:k_best], rf.feature_importances_[sorted_idx][:k_best])
        plt.xlabel("Random Forest Feature Importance")
        plt.show()
        print ([list(X)[i] for i in sorted_idx][:k_best])
        return X[[list(X)[i] for i in sorted_idx][:k_best]]
    elif flag == 'rfe':
        rfe = RFE(estimator = RandomForestClassifier(n_estimators=100), n_features_to_select= k_best)
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
    print (selector.scores_.argsort()[::-1][:k_best])
    return X_new 

def pipeline_performance(X_train, X_test, y_train, y_test, pipeline):
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    
    scoring = {'accuracy' : make_scorer(accuracy_score), 
               'precision' : make_scorer(precision_score),
               'recall' : make_scorer(recall_score), 
               'f1_score' : make_scorer(f1_score)}

    kfold = KFold(n_splits=10, random_state=42)
    scores = cross_validate(estimator = pipeline,
                             X = X_train,
                             y = y_train,
                             cv = kfold,
                             n_jobs = 1,
                             scoring = scoring,
                             return_train_score=True)
    
    print('Ten-fold CV train accuracy: %.3f +/- %.3f' % (np.mean(scores['train_accuracy']),np.std(scores['train_accuracy'])))
    print('Ten-fold CV test accuracy: %.3f +/- %.3f' % (np.mean(scores['test_accuracy']),np.std(scores['test_accuracy'])))
    print('Ten-fold CV train recall: %.3f +/- %.3f' % (np.mean(scores['train_recall']),np.std(scores['train_recall'])))
    print('Ten-fold CV test recall: %.3f +/- %.3f' % (np.mean(scores['test_recall']),np.std(scores['test_recall'])))
    print('Ten-fold CV train precision: %.3f +/- %.3f' % (np.mean(scores['train_precision']),np.std(scores['train_precision'])))
    print('Ten-fold CV test precision: %.3f +/- %.3f' % (np.mean(scores['test_precision']),np.std(scores['test_precision'])))
    print('Ten-fold CV train f1: %.3f +/- %.3f' % (np.mean(scores['train_f1_score']),np.std(scores['train_f1_score'])))
    print('Ten-fold CV test f1: %.3f +/- %.3f' % (np.mean(scores['test_f1_score']),np.std(scores['test_f1_score'])))

    confmat = confusion_matrix(y_true = y_test, y_pred = y_pred)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
    for i in range(confmat.shape[0]):
        for j in range(confmat.shape[1]):
            ax.text(x = j, y = i,s = confmat[i, j], va = 'center', ha = 'center')
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.show()
    print('Model performance on hold-out data: Accuracy: %.3f' % accuracy_score(y_true=y_test, y_pred=y_pred))
    print('Model performance on hold-out data: Precision: %.3f' % precision_score(y_true=y_test, y_pred=y_pred))
    print('Model performance on hold-out data: Recall: %.3f' % recall_score(y_true=y_test, y_pred=y_pred))
    print('Model performance on hold-out data: F1: %.3f' % f1_score(y_true=y_test, y_pred=y_pred))


def hyper_parameters_grid_search(X_train, y_train, X_test, y_test, pipeline, flag = 'lr'):
    if flag == 'lr':
        param_grid = {'logisticregression__C': [0.001, 0.01, 0.1, 1.0, 10, 100]}
        
    elif flag == 'rf':
        param_grid = {'randomforestclassifier__n_estimators': [10, 25, 50, 100, 200]}
    
    elif flag == 'svc':
        param_grid = {'svc__C':[0.001, 0.01, 0.1, 1.0, 10, 100],
                      'svc__gamma':[0.001, 0.01, 0.1, 1.0, 10, 100],
                      'svc__kernel':['linear','rbf']}

    elif flag == 'knn':
        param_grid = {'kneighborsclassifier__n_neighbors': [i for i in range(1,15)]}
        
    gs = GridSearchCV(estimator = pipeline,
                      param_grid = param_grid,
                      scoring = 'accuracy',
                      cv=10,
                      refit=True,
                      n_jobs = -1)
    gs = gs.fit(X_train, y_train)
    print(gs.best_score_)
    print(gs.best_params_)
    clf = gs.best_estimator_
    clf.fit(X_train, y_train)
    print('Test accuracy: %.3f' % clf.score(X_test, y_test))
    

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
    plt.plot(train_sizes, train_mean,color='blue', marker='o', markersize=5, label='Training accuracy')
    plt.fill_between(train_sizes,train_mean + train_std,train_mean - train_std,alpha=0.15, color='blue')
    plt.plot(train_sizes, test_mean,color='green', linestyle='--',marker='s', markersize=5,label='Validation accuracy')

    plt.fill_between(train_sizes,test_mean + test_std,test_mean - test_std,alpha=0.15, color='green')
    plt.grid()
    plt.title('Learning Curves', fontsize = 12)
    plt.xlabel('Number of training examples', fontsize = 12)
    plt.ylabel('Accuracy', fontsize = 12)
    plt.legend(loc = 'lower right')
    plt.ylim([0.8, 1.03])
    plt.tight_layout()
    plt.show()

def generate_validation_curves(X_train, y_train, pipeline):
    param_range = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]
    train_scores, test_scores = validation_curve(estimator=pipeline,
                                                 X=X_train,
                                                 y=y_train,
                                                 param_name='logisticregression__C',
                                                 param_range=param_range,
                                                 cv=10)
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    plt.plot(param_range, train_mean,color='blue', marker='o',markersize=5, label='Training accuracy')
    plt.fill_between(param_range, train_mean + train_std,train_mean - train_std, alpha=0.15,color='blue')
    plt.plot(param_range, test_mean,color='green', linestyle='--',marker='s', markersize=5,label='Validation accuracy')

    plt.fill_between(param_range,test_mean + test_std,test_mean - test_std,alpha=0.15, color='green')
    plt.grid()
    plt.xscale('log')
    plt.legend(loc='lower right')
    plt.title('Validation Curves', fontsize = 12)
    plt.xlabel('Parameter C', fontsize = 12)
    plt.ylabel('Accuracy', fontsize = 12)
    plt.ylim([0.8, 1.0])
    plt.tight_layout()
    plt.show()

def generate_ROC_curve(X_train, y_train, pipeline, kfold):
    cv = list(StratifiedKFold(n_splits=kfold, random_state=1).split(X_train, y_train))
    fig = plt.figure(figsize=(7, 5))
    mean_tpr = 0.0
    mean_fpr = np.linspace(0, 1, 100)
    all_tpr = []
    for i, (train, test) in enumerate(cv):
        probas = pipeline.fit(X_train.iloc[train, :], y_train[train]).predict_proba(X_train.iloc[test, :])
        fpr, tpr, thresholds = roc_curve(y_train[test], probas[:, 1], pos_label=1)
        mean_tpr += interp(mean_fpr, fpr, tpr)
        mean_tpr[0] = 0.0
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr,
                 tpr,
                 label='ROC fold %d (area = %0.2f)'% (i+1, roc_auc))
        
    plt.plot([0, 1],
             [0, 1],
             linestyle='--',
             color=(0.6, 0.6, 0.6),
             label='Random guessing')
    mean_tpr /= len(cv)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    plt.plot(mean_fpr, mean_tpr, 'k--', label='Mean ROC (area = %0.2f)' % mean_auc, lw=2)
    plt.plot([0, 0, 1],
             [0, 1, 1],
             linestyle=':',
             color='black',
             label='Perfect performance')
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False positive rate', fontsize = 12)
    plt.ylabel('True positive rate', fontsize = 12)
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.show()
     
if __name__ == '__main__':
    ### STEP - 0 LOAD DATA AS A DATAFRAME USING PANDAS; ADD COLUMN NAMES IF NECESSARY
    file_name = 'wdbc.data'
    df = pd.read_csv(file_name, header = None)

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
    X = df.iloc[:, 2:]
    # X[col_name] = X[col_name].replace({'No': 0, 'Yes' : 1})
    y = df.iloc[:, 1]
    y = y.replace({'M': 1, 'B': 0})
    y = np.array(y)

    ### STEP - 1d PLOT CORRELATION MAP ###
    def step_1d_plot_correlation_map():
        plot_correlation_heat_map(df, list_of_column_names = [i for i in range(2, 32)])

    ### STEP - 1e CALCULATE VIF ###
    def step_1e_calculate_vif():
        print (calculate_variance_inflation_factor(X, list(X)))
 
    ### STEP - 1f PLOT PCA PLOTS ###
    def step_1f_plot_pca():
        principle_component_analysis(X, legend_size = 8)

    '''
        RUN STEP 1 EXPERIMENTS
        (B) PLOT LABEL DISTRIBUTION
        (C) PLOT CORRELATION HEAT MAP
        (E) CALCULATE VARIANCE INFLATION FACTOR
        (F) PLOT PCA
    '''
##    step_1b_plot_labels(label_col_name = 1)
##    step_1d_plot_correlation_map()
##    step_1e_calculate_vif()
##    step_1f_plot_pca()


    ### STEP 2 SPECIFY TRAIN/TEST DATA AND PIPELINE ###
##    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, stratify=y, random_state=1)
##    pipeline_lr = make_pipeline(StandardScaler(),
##                                PCA(n_components = 10),
##                                LogisticRegression(solver = 'lbfgs'))
##
##    pipeline_rf = make_pipeline(StandardScaler(),
##                                PCA(n_components = 10),
##                                RandomForestClassifier(n_estimators = 100))
##
##    pipeline_knn = make_pipeline(StandardScaler(),
##                                 PCA(n_components = 10),
##                                 KNeighborsClassifier(n_neighbors=5))
##
##    pipeline_svc = make_pipeline(StandardScaler(),
##                                 PCA(n_components = 10),
##                                 SVC(gamma = 'scale'))

    ### STEP 3 MACHINE LEARNING ###
    def experiment_1a():
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_lr)

    def experiment_1b():
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_rf)

    def experiment_1c():
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_knn)

    def experiment_1d():
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_svc)

    '''
        RUN STEP 3 EXPERIMENTS
        CHECK PIPELINE MODEL PERFORMANCE OF (1) LOGISTIC REGRESSION (2) RANDOM FOREST (3) KNN (4) SUPPORT VECTOR MACHINE
    '''
##    experiment_1a()
##    experiment_1b()
##    experiment_1c()
##    experiment_1d()

    def experiment_2a():
        generate_learning_curves(X_train, y_train, pipeline = pipeline_lr)

    def experiment_2b():
        generate_validation_curves(X_train, y_train, pipeline = pipeline_lr)

    '''
        RUN STEP 3 EXPERIMENTS
        GENERATE (1) LEARNING CURVE (2) VALIDATION CURVE
    '''
##    experiment_2a()
##    experiment_2b()

    ### hyperparameters tuning ###
    def experiment_3a():
        hyper_parameters_grid_search(X_train, y_train, X_test, y_test, pipeline_lr, flag = 'lr')
        
    def experiment_3b():
        hyper_parameters_grid_search(X_train, y_train, X_test, y_test, pipeline_rf, flag = 'rf')
        
    def experiment_3c():
        hyper_parameters_grid_search(X_train, y_train, X_test, y_test, pipeline_knn, flag = 'knn')
        
    def experiment_3d():
        hyper_parameters_grid_search(X_train, y_train, X_test, y_test, pipeline_svc, flag = 'svc')

    '''
        RUN STEP 3 EXPERIMENTS
        GRID SEARCH ON HYPERPARAMETERS FOR (1) LOGISTIC REGRESSION (2) RANDOM FOREST (3) KNN (4) SUPPORT VECTOR MACHINE
    '''
##    experiment_3a()
##    experiment_3b()
##    experiment_3c()
##    experiment_3d()

    '''
        RUN STEP 3 EXPERIMENTS
        GENERATE ROC CURVE FOR LOGISTIC REGRESSION WITH K-FOLD CROSS VALIDATION
    '''
    def experiment_4():
        generate_ROC_curve(X_train, y_train, pipeline = pipeline_lr, kfold = 5)

##    experiment_4()
        
    ### select K best features ###
    def experiment_5a():
        new_X = select_best_k(X, y, flag = 'chi2', k_best = 10)
        X_train, X_test, y_train, y_test = train_test_split(new_X, y, test_size=0.20, stratify=y, random_state=1)
        pipeline_lr = make_pipeline(StandardScaler(),
                                    LogisticRegression(solver = 'lbfgs'))
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_lr)
        
    def experiment_5b():
        new_X = select_best_k(X, y, flag = 'anova', k_best = 10)
        X_train, X_test, y_train, y_test = train_test_split(new_X, y, test_size=0.20, stratify=y, random_state=1)
        pipeline_lr = make_pipeline(StandardScaler(),
                                    LogisticRegression(solver = 'lbfgs'))
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_lr)

    def experiment_5c():
        new_X = select_best_k(X, y, flag = 'tree', k_best = 10)
        X_train, X_test, y_train, y_test = train_test_split(new_X, y, test_size=0.20, stratify=y, random_state=1)
        pipeline_lr = make_pipeline(StandardScaler(),
                                    LogisticRegression(solver = 'lbfgs'))
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_lr)

    def experiment_5d():
        new_X = select_best_k(X, y, flag = 'rfe', k_best = 10)
        X_train, X_test, y_train, y_test = train_test_split(new_X, y, test_size=0.20, stratify=y, random_state=1)
        pipeline_lr = make_pipeline(StandardScaler(),
                                    LogisticRegression(solver = 'lbfgs'))
        pipeline_performance(X_train, X_test, y_train, y_test, pipeline_lr)
    
    '''
        RUN STEP 3 EXPERIMENTS
        SELECT K-BEST SUBSETS OF FEATURES USING (1) ANOVA (2) CHI2 (3) TREE (4) RFE
    '''
##    experiment_5a()
##    experiment_5b()
##    experiment_5c()
##    experiment_5d()
    
























