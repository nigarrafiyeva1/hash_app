import sys
import os
import mmh3

# Check if n and s were provided
if len(sys.argv) != 3:
    print("Usage: python hash_app.py <n> <s>")
    exit()
    
# Get n and s from command line
n = int(sys.argv[1])
s = int(sys.argv[2])

# Check if n and s are positive
if n <= 0 or s <= 0:
    print("Error: n and s must be positive integers.")
    exit()


# Create a folder for bucket files
os.makedirs("buckets", exist_ok=True)


# Create n bucket files
for i in range(1, n + 1):
    file_path = f"buckets/{i}.txt"

    if not os.path.exists(file_path):
        open(file_path, "w").close()

# Add text to the bucket and its overflow files
def store_text(text, bucket_number):
    file_path = f"buckets/{bucket_number}.txt"
    overflow_number = 0

    # Find the last overflow file
    while os.path.exists(f"buckets/{bucket_number}_overflow_{overflow_number + 1}.txt"):
        overflow_number += 1
        file_path = f"buckets/{bucket_number}_overflow_{overflow_number}.txt"

    # Write text and create overflow when needed
    while text:
        with open(file_path, "r", encoding="utf-8") as file:
            available_space = s - len(file.read())

        if available_space > 0:
            with open(file_path, "a", encoding="utf-8") as file:
                file.write(text[:available_space])

            text = text[available_space:]

        if text:
            overflow_number += 1
            file_path = f"buckets/{bucket_number}_overflow_{overflow_number}.txt"
            open(file_path, "w").close()

print(f"hash_app {n} {s}")
print("Bucket files created successfully.")

# Keep accepting strings
try:
    while True:
        text = input("Please enter the string: ")

        # Calculate hash and find bucket
        hash_value = mmh3.hash(text, signed=False)
        bucket_number = (hash_value % n) + 1

        # Add string to the selected bucket
        store_text(text, bucket_number)

        print(f"{text} added to {bucket_number}.txt")

except KeyboardInterrupt:
    print("\nApp Stopped")
