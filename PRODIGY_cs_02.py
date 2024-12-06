from PIL import Image 
import numpy as np
import os

class ImageEncryptionTool:
    def _init_(self):
        self.encrypted_image_path = "encrypted_image.png"
        self.decrypted_image_path = "decrypted_image.png"

    def encrypt_image(self, image_path, key):
        """Encrypts the image with a key."""
        try:
            
            original_image = Image.open(image_path)
        except FileNotFoundError:
            print(f"Oops, we couldn't find the image at {image_path}. Please check the path.")
            return

        image_array = np.array(original_image)

        encrypted_image_array = (image_array * key) // (key + 1)

        encrypted_image = Image.fromarray(np.uint8(encrypted_image_array))

        encrypted_image.save(self.encrypted_image_path)
        print(f"Your image has been encrypted! You can find it here: {self.encrypted_image_path}")

    def decrypt_image(self, encrypted_image_path, key):
        """Decrypts the image using the same key."""
        try:
            encrypted_image = Image.open(encrypted_image_path)
        except FileNotFoundError:
            print(f"Couldn't find the encrypted image at {encrypted_image_path}. Please check the path.")
            return

        encrypted_image_array = np.array(encrypted_image)

        decrypted_image_array = (encrypted_image_array * (key + 1)) // key

        decrypted_image_array = np.clip(decrypted_image_array, 0, 255)

        decrypted_image = Image.fromarray(np.uint8(decrypted_image_array))
        decrypted_image.save(self.decrypted_image_path)
        print(f"Your image has been decrypted! You can find it here: {self.decrypted_image_path}")

    def get_key(self):
        """Gets a valid key from the user."""
        while True:
            try:
                key = int(input("Please enter the encryption/decryption key (positive integer): "))
                if key <= 0:
                    raise ValueError("The key must be a positive integer!")
                return key
            except ValueError as e:
                print(f"Oops! {e}. Try again.")

    def get_image_path(self, prompt):
        """Asks for a valid image file path."""
        while True:
            image_path = input(prompt)
            if os.path.isfile(image_path):
                return image_path
            else:
                print(f"Couldn't find a file at {image_path}. Please provide a valid path.")

    def encrypt_choice(self):
        """Handles encryption choice."""
        key = self.get_key()
        image_location = self.get_image_path("Enter the path of the image you want to encrypt: ")
        self.encrypt_image(image_location, key)

    def decrypt_choice(self):
        """Handles decryption choice."""
        key = self.get_key()
        encrypted_image_location = self.get_image_path("Enter the path of the encrypted image: ")
        self.decrypt_image(encrypted_image_location, key)

    def main(self):
        """Main loop to drive the program."""
        while True:
            print("\nWelcome to the Image Encryption Tool!")
            print("Choose an option:")
            print("e - Encrypt an image")
            print("d - Decrypt an image")
            print("q - Quit")
            choice = input("Your choice: ").lower()

            if choice == 'e':
                self.encrypt_choice()
            elif choice == 'd':
                self.decrypt_choice()
            elif choice == 'q':
                print("Goodbye!")
                break
            else:
                print("Sorry, that's not a valid choice. Please try again.")

if _name_ == "_main_":
    tool = ImageEncryptionTool()
    tool.main()
