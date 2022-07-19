from sklearn.linear_model import LogisticRegression

my_log_reg = LogisticRegression()

cols = [
    "time_on_page",
    "pages_viewed",
    "interest_ski",
    "interest_climb",
]

my_log_reg.fit(train[cols], train["buy"])

predictions = my_log_reg.predict(test[cols])
