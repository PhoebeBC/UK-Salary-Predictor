import pandas as pd
import numpy as np
import keras
import matplotlib.pyplot as plt
import seaborn as sns
from keras.layers import Dense, Input
from keras.models import Model

CSV_COLUMN_NAMES = ['Age', 'Region', 'Sex', 'Industry', 'Job_Title', 'Years_of_Experience', 'Number_of_Job_Moves',
                    'Level_of_Education', 'Salary_Band']
train = pd.read_csv(r"C:\Users\phoeb\Documents\Software Learning\training_data.csv", names=CSV_COLUMN_NAMES, header=0)
test = pd.read_csv(r"C:\Users\phoeb\Documents\Software Learning\testing_data.csv", names=CSV_COLUMN_NAMES, header=0)

# Separate features and target
features = train.drop(columns=['Salary_Band'])  # Features
target = train['Salary_Band']  # Target

# Separate features and target
features_test = test.drop(columns=['Salary_Band'])  # Features
target_test = test['Salary_Band']  # Target

# Input layer
inputs = keras.Input(shape=(8,))

dense_layer1 = keras.layers.Dense(64, activation="softmax")
output_layer1 = dense_layer1(inputs)

dense_layer2 = keras.layers.Dense(64, activation="softmax")(output_layer1)
outputs_layer2 = keras.layers.Dense(5)(dense_layer2)

model = keras.Model(inputs=inputs, outputs=outputs_layer2, name="my_model")

model.summary()

# (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
#
# x_train = x_train.reshape(60000, 784).astype("float32") / 255
# x_test = x_test.reshape(10000, 784).astype("float32") / 255

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.RMSprop(),
    metrics=[keras.metrics.SparseCategoricalAccuracy()],
)

history = model.fit(features, target, batch_size=64, epochs=50, validation_split=0.1)

test_scores = model.evaluate(features_test, target_test, verbose=2)
print("Test loss:", test_scores[0])
print("Test accuracy:", test_scores[1])
