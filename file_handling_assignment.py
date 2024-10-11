# file_handling_assignment.py

# File creation and writing
try:
    # Create a new text file in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("Hello, this is the first line.\n")
        file.write("Here is a number: 12345\n")
        file.write("This is the third line with some text.\n")
    print("File created and written successfully.")

except PermissionError:
    print("Error: You don't have permission to write to this file.")
except Exception as e:
    print(f"An error occurred: {e}")

# File reading and display
try:
    # Open the file in read mode ('r') and display the content
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nReading file content:")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# File appending
try:
    # Open the file in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text
        file.write("This is an appended line 1.\n")
        file.write("Appending another line with a number: 67890\n")
        file.write("Final appended line.\n")
    print("Content appended successfully.")

    # Re-read and display the updated content
    with open("my_file.txt", "r") as file:
        updated_content = file.read()
        print("\nUpdated file content:")
        print(updated_content)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You don't have permission to append to this file.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("File handling operations completed.")
