import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics

digits = datasets.load_digits()
images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.title('Training: %i' % label)
    plt.imshow(image, cmap='binary', interpolation='nearest')

X, y = digits['data'], digits['target']
X.shape
print(X.shape)

print(X[0])
print(y[0])