## ImageCrypt

**ImageCrypt** is a Python program that allows you to encrypt and decrypt images using a simple XOR-based pixel manipulation technique. This tool provides a basic form of image encryption by applying a bitwise XOR operation to the pixel values of an image.

## Usage

- **Encryption**: To encrypt an image, each pixel's value is XORed with a specified key, resulting in an encrypted image.
- **Decryption**: To decrypt an image, the encrypted image is processed again with the same key, restoring the original pixel values.

## Features

- **XOR Key**: Specify an integer key to XOR with each pixel's value, providing a basic form of encryption.
- **Supports**: Works with standard image formats such as PNG and JPEG.
- **Input Validation**: Validates user inputs for image paths and the encryption key.
- **Image Display**: Displays the original and processed images using Matplotlib.

## How to Use

### Clone the repository:

```bash
git clone https://github.com/rihadroshan/PRODIGY_CS_02.git
```

### Navigate into the project directory:

```bash
cd PRODIGY_CS_02
```

### Install required packages:

```bash
pip install -r requirements.txt
```

### Run the program:

```bash
python3 ImageCrypt.py
```

### Follow the prompts to encrypt or decrypt an image.

## Example

Here's an example of how to use the ImageCrypt tool:

```plaintext

Please enter the encryption key (a number): 1111

Would you like to encrypt or decrypt an image? Please type 'e' for encrypt or 'd' for decrypt: e

Please enter the path of the input image: img.png

Please enter the path where the output image will be saved: encrypted_img.png

The image has been encrypted and saved to encrypted_img.png.
```

## Notes

- **Educational Purpose**: This tool is for educational purposes only and should not be used for securing sensitive data, as the XOR method is not cryptographically secure.
