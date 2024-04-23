
    # Open "my_file.txt" in write mode ('w')
    file = open("my_file.txt", "w")

    # Write some content to the file
    file.write("This is line 1\n")
    file.write("12345\n")
    file.write("Another line with mixed data: abc123\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the file in finally block to ensure it's closed regardless of exceptions
    file.close()

    # File Creation
    file = open("my_file.txt", "w")
    file.write("This is line 1\n")
    file.write("12345\n")
    file.write("Another line with mixed data: abc123\n")
    file.close()

    # File Reading and Display
    file = open("my_file.txt", "r")
    print("Contents of my_file.txt:")
    for line in file:
        print(line.strip())
    file.close()

    # File Appending
    file = open("my_file.txt", "a")
    file.write("Line appended 1\n")
    file.write("54321\n")
    file.write("Yet another appended line\n")
    file.close()

    # File Reading and Display After Appending
    file = open("my_file.txt", "r")
    print("Contents of my_file.txt after appending:")
    for line in file:
        print(line.strip())
    file.close()

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the file in finally block to ensure it's closed regardless of exceptions
    if 'file' in locals() and not file.closed:
        file.close()