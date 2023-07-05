import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, UpSampling2D
from tensorflow.keras.models import Sequential

# Define the CNN model architecture
model = Sequential()
model.add(Conv2D(16, (3, 3), activation='relu', padding='same', input_shape=(128, 128, 3)))
model.add(MaxPooling2D((2, 2), padding='same'))
model.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D((2, 2), padding='same'))
model.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D((2, 2), padding='same'))

# Load and preprocess the image
def load_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_image(image, channels=3)
    image = tf.image.resize(image, (128, 128))
    image = image / 255.0  # Normalize pixel values to the range [0, 1]
    return image

# Save and visualize the encrypted image
def save_image(image, output_path):
    image = image * 255.0  # Convert back to the range [0, 255]
    image = tf.cast(image, tf.uint8)
    image = tf.image.encode_png(image)
    tf.io.write_file(output_path, image)

# Encrypt an image using the trained CNN model
def encrypt_image(image):
    # Preprocess the image if needed
    image = tf.expand_dims(image, axis=0)

    # Perform encryption using the CNN model
    encrypted_image = model.predict(image)

    return encrypted_image

# Decrypt an encrypted image using the trained CNN model
def decrypt_image(encrypted_image):
    # Perform decryption using the CNN model
    decrypted_image = model.predict(encrypted_image)

    # Postprocess the decrypted image if needed

    return decrypted_image

# Example usage
image_path = "path/to/input/image.png"
output_path = "path/to/output/encrypted_image.png"

# Load the image
image = load_image(image_path)

# Encrypt the image
encrypted = encrypt_image(image)

# Save and visualize the encrypted image
save_image(encrypted[0], output_path)

# Decrypt the encrypted image
decrypted = decrypt_image(encrypted)

# Save and visualize the decrypted image
save_image(decrypted[0], "path/to/output/decrypted_image.png")
