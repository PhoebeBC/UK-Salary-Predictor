from __future__ import absolute_import, division, print_function, unicode_literals
from keras.layers import Normalization, Dense, Input
from keras.models import Model
import numpy as np
import pandas as pd
import tensorflow as tf
import keras

CSV_COLUMN_NAMES = ['Age', 'Region', 'Sex', 'Industry', 'Job_Title', 'Years_of_Experience', 'Number_of_Job_Moves',
                    'Level_of_Education', 'Salary', 'Salary_Band']
SALARY_BANDS = ['under 30K', '30K-50K', '50K-70K', '70K-90K', 'Over 90K']

train = pd.read_csv(r"C:\Users\phoeb\Documents\Software Learning\training_data.csv", names=CSV_COLUMN_NAMES, header=0)
test = pd.read_csv(r"C:\Users\phoeb\Documents\Software Learning\testing_data.csv", names=CSV_COLUMN_NAMES, header=0)

train_y = train.pop('Salary_Band')
test_y = test.pop('Salary_Band')
train = pd.read_csv(r"C:\Users\phoeb\Documents\Software Learning\training_data.csv", names=CSV_COLUMN_NAMES, header=0)
test = pd.read_csv(r"C:\Users\phoeb\Documents\Software Learning\testing_data.csv", names=CSV_COLUMN_NAMES, header=0)
print(train['Salary_Band'])

my_feature_columns = []
# For each feature, create a Normalization layer and adapt it to the data
for key in train.keys():
    normalizer = Normalization()
    normalizer.adapt(train[[key]].values)
    my_feature_columns.append(normalizer)
    print(f"feature columns: {my_feature_columns}")

# Create an input layer for each feature
inputs = {key: keras.Input(shape=(1,), name=key) for key in train.keys()}

# Apply normalization layers to the inputs
normalized_inputs = [my_feature_columns[i](inputs[key]) for i, key in enumerate(inputs.keys())]

# Concatenate the normalized inputs
concat = keras.layers.concatenate(normalized_inputs)

# Define the rest of the model
hidden_layer1 = Dense(128, activation='relu')(concat)
hidden_layer2 = Dense(64, activation='relu')(hidden_layer1)

# Update output layer for multi-class classification
num_classes = 5
outputs = Dense(num_classes, activation='softmax')(hidden_layer2)

# Create the model
model = Model(inputs=inputs, outputs=outputs)
# Compile the model for multi-class classification
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Prepare the inputs for training
# def prepare_inputs(data):
#     return {feature_name: data[feature_name].values for feature_name in data.columns if feature_name != 'Salary_Band'}
#
# train_inputs = prepare_inputs(train)
print(train['Salary_Band'])

# Train the model
model.fit(
    train_y,
    train['Salary_Band'],
    epochs=10)


# # Building a dnn classifier model as likly to be linear coorespondense in data
# classifier = tf.estimator.DNNClassifier(feature_columns=my_feature_columns, hidden_units=[30, 10], n_classes=5)
# # Training the model
# classifier.train(
#     input_fn=lambda: input_func(train, train_y, training=True),
#     steps=5000
# )
# # Testing the model
# eval_result = classifier.evaluate(input_fn=lambda: input_func(test, test_y, training=False))

#print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))
