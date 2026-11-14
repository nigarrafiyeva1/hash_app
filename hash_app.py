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
        file_path = f"buckets/{bucket_number}.txt"

        with open(file_path, "a", encoding="utf-8") as file:
            file.write(text)

        print(f"{text} added to {bucket_number}.txt")

except KeyboardInterrupt:
    print("\nApp Stopped")
