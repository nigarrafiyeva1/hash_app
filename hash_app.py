import sys
import os

# Check if n and s were provided
if len(sys.argv) != 3:
    print("Usage: python hash_app.py <n> <s>")
    exit()
    
# Get n and s from command line
n = int(sys.argv[1])
s = int(sys.argv[2])


# Create a folder for bucket files
os.makedirs("buckets", exist_ok=True)


# Create n bucket files
for i in range(1, n + 1):
    file_path = f"buckets/{i}.txt"

    if not os.path.exists(file_path):
        open(file_path, "w").close()


print(f"hash_app {n} {s}")
print("Bucket files created successfully.")