from sklearn.metrics import confusion_matrix

tn, fp, fn, tp = confusion_matrix(
    test["buy"],
    predictions,
).ravel()

print(f"True  negatives: {tn}")
print(f"False positives: {fp}")
print(f"False negatives: {fn}")
print(f"True  Positives: {tp}")
