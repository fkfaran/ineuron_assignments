import os
import keyword
import pickle
import shutil

# ---------------- 1. File status ----------------
def file_status(file_path, mode='r'):
    try:
        f = open(file_path, mode)
        print(f"File Name: {f.name}")
        print(f"File Closed: {f.closed}")
        print(f"File Mode: {f.mode}")
        print(f"File Readable: {f.readable()}")
        print(f"File Writable: {f.writable()}")
        f.close()
        print(f"After closing, File Closed: {f.closed}")
    except FileNotFoundError:
        print("File not found.")

# ---------------- 2. Create file and store user text ----------------
def create_file_user_text(file_path):
    text = input("Enter text to store in file: ")
    with open(file_path, 'w') as f:
        f.write(text)
    print(f"Text saved to {file_path}")

# ---------------- 3. Read file and display content ----------------
def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found.")

# ---------------- 4. Store list of cities ----------------
def store_cities(file_path, cities):
    with open(file_path, 'w') as f:
        for city in cities:
            f.write(city + "\n")
    print(f"Cities stored in {file_path}")

# ---------------- 5. Append cities ----------------
def append_cities(file_path, cities):
    with open(file_path, 'a') as f:
        for city in cities:
            f.write(city + "\n")
    print(f"Cities appended to {file_path}")

# ---------------- 6. Search city in file ----------------
def search_city(file_path, city):
    try:
        with open(file_path, 'r') as f:
            cities = [line.strip() for line in f]
        if city in cities:
            print(f"{city} is present in the file.")
        else:
            print(f"{city} is not present in the file.")
    except FileNotFoundError:
        print("File not found.")

# ---------------- 7. Count Python keywords in a source file ----------------
def count_keywords(file_path):
    try:
        with open(file_path, 'r') as f:
            code = f.read()
        kw_count = sum(code.count(kw) for kw in keyword.kwlist)
        print(f"Number of Python keywords in file: {kw_count}")
    except FileNotFoundError:
        print("File not found.")

# ---------------- 8. Copy a file ----------------
def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"Copied {src} to {dest}")
    except FileNotFoundError:
        print("Source file not found.")

# ---------------- 9. Store book data using pickle ----------------
def store_book_data(file_path, book_data):
    with open(file_path, 'wb') as f:
        pickle.dump(book_data, f)
    print(f"Book data stored in {file_path}")

# ---------------- 10. Extract book data using pickle ----------------
def extract_book_data(file_path):
    try:
        with open(file_path, 'rb') as f:
            book_data = pickle.load(f)
        print("Extracted book data:")
        for book, price in book_data.items():
            print(f"{book}: {price}")
    except FileNotFoundError:
        print("Book file not found.")


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    # 1
    file_status("myfile.txt")

    # 2 & 3
    create_file_user_text("myfile.txt")
    read_file("myfile.txt")

    # 4 & 5
    cities = ["New York", "London", "Tokyo"]
    store_cities("cities.txt", cities)
    append_cities("cities.txt", ["Paris", "Berlin"])

    # 6
    search_city("cities.txt", "Tokyo")
    search_city("cities.txt", "Sydney")

    # 7
    count_keywords("myfile.txt")

    # 8
    copy_file("myfile.txt", "myfile_copy.txt")

    # 9 & 10
    book_data = {"Python101": 300, "Java Basics": 250, "C++ Guide": 400}
    store_book_data("bookfile.pkl", book_data)
    extract_book_data("bookfile.pkl")
