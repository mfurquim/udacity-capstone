# Defining machine learning pipeline:
gbc_ml_pipe = Pipeline(
    steps=[
        ("preprocessing", preproc),
        (
            "clf",
            GradientBoostingClassifier(
                learning_rate=0.1,
                n_estimators=150,
                random_state=310,
            ),
        ),
    ]
)

# Setting parameters to be tested:
params = {
    "clf__min_samples_split": [2, 4],
    "clf__max_depth": [3, 5],
    "clf__max_features": [None, "auto"],
}
