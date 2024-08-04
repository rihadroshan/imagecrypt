from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class ImageEncryptor:
    def __init__(self, key):
        self.key = key

    def _apply_xor(self, pixels):
        return np.bitwise_xor(pixels, self.key)

    def encrypt(self, input_image_path, output_image_path):
        with Image.open(input_image_path) as img:
            img = img.convert('RGB')
            pixels = np.array(img)
            encrypted_pixels = self._apply_xor(pixels)
            encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
            encrypted_image.save(output_image_path)
            return encrypted_image

    def decrypt(self, input_image_path, output_image_path):
        with Image.open(input_image_path) as img:
            img = img.convert('RGB')
            pixels = np.array(img)
            decrypted_pixels = self._apply_xor(pixels)
            decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
            decrypted_image.save(output_image_path)
            return decrypted_image


class ImageEncryptorApp:
    def __init__(self):
        self.encryptor = None

    def run(self):
        key = self._get_encryption_key()
        self.encryptor = ImageEncryptor(key)
        choice = self._get_choice()
        input_image_path, output_image_path = self._get_image_paths()
        
        if choice == 'e':
            self._encrypt_image(input_image_path, output_image_path)
        elif choice == 'd':
            self._decrypt_image(input_image_path, output_image_path)
    
    def _get_encryption_key(self):
        while True:
            try:
                return int(input("\nPlease enter the encryption key (a number): "))
            except ValueError:
                print("Oops! That wasn't a valid number. Please try again.\n")

    def _get_choice(self):
        while True:
            choice = input("\nWould you like to encrypt or decrypt an image? Please type 'e' for encrypt or 'd' for decrypt: ").strip().lower()
            if choice in ['e', 'd']:
                return choice
            else:
                print("Oops! That was an invalid choice.\n Please type 'e' for encrypt or 'd' for decrypt.\n")
    
    def _get_image_paths(self):
        input_image_path = input("\nPlease enter the path of the input image: ")
        output_image_path = input("\nPlease enter the path where the output image will be saved: ")
        return input_image_path, output_image_path

    def _encrypt_image(self, input_image_path, output_image_path):
        self.encryptor.encrypt(input_image_path, output_image_path)
        print(f"\nThe image has been encrypted and saved to {output_image_path}.")
        self._display_images(input_image_path, output_image_path, "Original Image", "Encrypted Image")
    
    def _decrypt_image(self, input_image_path, output_image_path):
        self.encryptor.decrypt(input_image_path, output_image_path)
        print(f"\nThe image has been decrypted and saved to {output_image_path}.")
        self._display_images(input_image_path, output_image_path, "Encrypted Image", "Decrypted Image")

    def _display_images(self, input_image_path, output_image_path, input_title, output_title):
        self._display_image(input_image_path, input_title)
        self._display_image(output_image_path, output_title)

    def _display_image(self, image_path, title):
        img = Image.open(image_path)
        plt.imshow(img)
        plt.title(title)
        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    app = ImageEncryptorApp()
    app.run()
