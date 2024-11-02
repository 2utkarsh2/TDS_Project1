# import csv
# from collections import Counter

# # Counter to store surname frequencies
# surname_counter = Counter()

# # Open the users.csv file and read data
# with open('users.csv', 'r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         name = row.get('name', '').strip()
#         if name:  # Ignore missing names
#             # Split the name by whitespace and get the last word as the surname
#             surname = name.split()[-1]
#             surname_counter[surname] += 1

# # Find the maximum frequency of surnames
# if surname_counter:
#     max_count = max(surname_counter.values())
#     # Get all surnames with the maximum frequency
#     most_common_surnames = [surname for surname, count in surname_counter.items() if count == max_count]
#     # Sort surnames alphabetically
#     most_common_surnames.sort()
#     # Output the result
#     print(f"{', '.join(most_common_surnames)}: {max_count}")
# else:
#     print("No names found.")


import pandas as pd
from collections import Counter

# Load the users data
users_df = pd.read_csv("users.csv")

# Filter out rows with missing names and extract surnames
surnames = users_df['name'].dropna().apply(lambda x: x.strip().split()[-1])

# Count the occurrences of each surname
surname_counts = Counter(surnames)

# Find the maximum count
max_count = max(surname_counts.values())

# Get all surnames with the maximum count and sort them alphabetically
most_common_surnames = sorted([surname for surname, count in surname_counts.items() if count == max_count])

# Print the result as a comma-separated string
print("Most common surname(s):", ", ".join(most_common_surnames))
