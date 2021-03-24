from preprocess_and_split import load_and_preprocess, train_valid_splitting
from model import testModel, train_model

input_data, input_labels = load_and_preprocess()
test_model = testModel()
#test_model.summary()
X_train, X_valid, y_train, y_valid = train_valid_splitting(input_data, input_labels)
train_model(test_model, X_train, X_valid, y_train, y_valid)