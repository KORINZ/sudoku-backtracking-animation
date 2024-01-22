import keras

# Use MNIST handwriting dataset
mnist = keras.datasets.mnist

# Prepare data for training
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)
x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)

# Create a convolutional neural network
model = keras.models.Sequential(
    [
        # Convolutional layer. Learn 64 filters using a 3x3 kernel
        keras.layers.Conv2D(64, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        # Max-pooling layer, using 2x2 pool size
        keras.layers.MaxPooling2D(pool_size=(2, 2)),
        # Flatten units
        keras.layers.Flatten(),
        # Add a hidden layer with dropout
        keras.layers.Dense(128, activation="relu"),
        keras.layers.Dropout(0.5),
        # Add an output layer with output units for all 10 digits
        keras.layers.Dense(10, activation="softmax"),
    ]
)

# Train neural network
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(x_train, y_train, epochs=10)

# Evaluate neural network performance
model.evaluate(x_test, y_test, verbose="2")

# Save model to file
model.save(r"handwriting_keras/model.keras")
