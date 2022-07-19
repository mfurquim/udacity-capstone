# Checking best parameters
print(gbc_clf.best_params_)
{
    "clf__max_depth": 3,
    "clf__max_features": None,
    "clf__min_samples_split": 2,
}

# Checking best score
print("Best ROC_AUC score: {:.2f}".format(gbc_clf.best_score_))
Best ROC_AUC score: 0.76
