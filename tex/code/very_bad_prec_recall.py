from sklearn.metrics import precision_score, recall_score

print("Precision is: ", precision_score(test.buy, predictions))
print("Recall is: ", recall_score(test.buy, predictions))
