from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt

def LogRegr(X, y, X_test, y_test):
    print("\n\n  ________________________________ ")
    print("\n Logistic Regression:\n")

    clf = LogisticRegression()
    clf.fit(X, y)

    y_pred = clf.predict(X_test) #defualt - 96.73%

    # confusion matrix
    labels = ["anger", "fear", "joy"]
    cm = confusion_matrix(y_test, y_pred)
    cmd_obj = ConfusionMatrixDisplay(cm, display_labels=labels)
    cmd_obj.plot()
    cmd_obj.ax_.set(
        title='Confusion Matrix (Logistic Regression)',
        xlabel='Predicted Emotion',
        ylabel='Actual Emotion')
    print("Confusion matrix:")
    plt.show()

    # accuracy
    print("\nAccuracy:")
    print(accuracy_score(y_test, y_pred))

    # precision
    print("\nPrecision:")
    print(precision_score(y_test, y_pred, average=None))

    # recall
    print("\nRecall:")
    print(recall_score(y_test, y_pred, average=None))

    # f1
    print("\nf1:")
    print(f1_score(y_test, y_pred, average=None))