import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def model_evaluation(model, X_train, y_train, X_test, y_test, output_dir):
    # Report training set score
    train_score = model.score(X_train, y_train) * 100
    # Report test set score
    test_score = model.score(X_test, y_test) * 100

    # Write scores to a file
    with open(output_dir + "/metrics.txt", 'w') as outfile:
        outfile.write("Training variance explained: %2.1f%%\n" % train_score)
        outfile.write("Test variance explained: %2.1f%%\n" % test_score)

    ##########################################
    ##### PLOT FEATURE IMPORTANCE ############
    ##########################################
    # Calculate feature importance in random forest
    importances = model.feature_importances_
    labels = X_train.columns
    feature_df = pd.DataFrame(list(zip(labels, importances)), columns = ["feature","importance"])
    feature_df = feature_df.sort_values(by='importance', ascending=False,)

    # image formatting
    axis_fs = 18 #fontsize
    title_fs = 22 #fontsize
    sns.set_theme(style="whitegrid")

    ax = sns.barplot(x="importance", y="feature", data=feature_df)
    ax.set_xlabel('Importance',fontsize = axis_fs) 
    ax.set_ylabel('Feature', fontsize = axis_fs)#ylabel
    ax.set_title('Random forest\nfeature importance', fontsize = title_fs)

    plt.tight_layout()
    plt.savefig(output_dir + "/feature_importance.png",dpi=120) 
    plt.close()


    ##########################################
    ############ PLOT RESIDUALS  #############
    ##########################################
    # Calculate residuals
    y_pred = model.predict(X_test)
    residuals = y_test - y_pred

    # Plotting residuals
    fig, ax = plt.subplots()
    ax.scatter(y_test, residuals)
    ax.axhline(lw=2,color='black')
    ax.set_xlabel('Observed', fontsize = axis_fs)
    ax.set_ylabel('Residual', fontsize = axis_fs)
    ax.set_title('Residual vs. Observed', fontsize = title_fs)
    plt.tight_layout()
    plt.savefig(output_dir + "/residuals.png", dpi=120) 
    plt.close()