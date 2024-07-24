from PIL import Image
import stepic

def encode_image():
    image_path = input("Enter the path of the image to encode: ")
    output_name = input("Enter the name for the new encoded image (e.g., encoded_image.png): ")
    secret_message = input("Enter the secret message: ")
    password = input("Enter the password: ")
    
    # Convert secret message and password to bytes
    secret_message_bytes = secret_message.encode('utf-8')
    password_bytes = password.encode('utf-8')
    
    # Combine message and password
    combined_message = secret_message_bytes + b':' + password_bytes
    
    # Open image and encode
    image = Image.open(image_path)
    encoded_image = stepic.encode(image, combined_message)
    
    # Save the encoded image
    encoded_image.save(output_name)
    print(f"Encoded image saved as {output_name}")

### Decoding with stepic Library

def decode_image():
    image_path = input("Enter the path of the image to decode: ")
    password = input("Enter the password: ")
    
    # Open the encoded image and decode
    encoded_image = Image.open(image_path)
    decoded_message = stepic.decode(encoded_image)
    
    # Convert the decoded message to bytes
    decoded_bytes = decoded_message.encode('utf-8')
    
    # Split the combined message
    decoded_message_bytes, decoded_password = decoded_bytes.rsplit(b':', 1)
    
    # Check if the password matches
    if decoded_password.decode('utf-8') == password:
        print(f"The secret message is: {decoded_message_bytes.decode('utf-8')}")
    else:
        print("Incorrect password! Decryption failed.")

### Main Function

def main():
    choice = input("Enter 'e' to encode a message or 'd' to decode a message: ").lower()
    if choice == 'e':
        encode_image()
    elif choice == 'd':
        decode_image()
    else:
        print("Invalid choice. Please enter 'e' to encode or 'd' to decode.")

if __name__ == "__main__":
    

    main()