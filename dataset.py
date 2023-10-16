from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()

# Access the features and target variable
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Target variable (species)

print(X,y)