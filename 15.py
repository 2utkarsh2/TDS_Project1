# import pandas as pd

# def analyze_email_sharing(users_csv_path='users.csv'):
#     # Read the complete CSV file
#     df = pd.read_csv(users_csv_path)
    
#     # Convert email column to boolean (True if email exists, False if NaN or empty)
#     df['has_email'] = df['email'].notna() & (df['email'] != '')
    
#     # Calculate for hireable users
#     hireable_mask = df['hireable'] == True
#     if hireable_mask.any():
#         hireable_email_fraction = df[hireable_mask]['has_email'].mean()
#     else:
#         hireable_email_fraction = 0
        
#     # Calculate for non-hireable users
#     non_hireable_mask = df['hireable'] != True
#     if non_hireable_mask.any():
#         non_hireable_email_fraction = df[non_hireable_mask]['has_email'].mean()
#     else:
#         non_hireable_email_fraction = 0
    
#     # Calculate difference and round to 3 decimal places
#     difference = round(hireable_email_fraction - non_hireable_email_fraction, 3)
    
#     # Print debug information
#     print(f"Total users: {len(df)}")
#     print(f"Hireable users with email: {df[hireable_mask]['has_email'].sum()}/{hireable_mask.sum()}")
#     print(f"Non-hireable users with email: {df[non_hireable_mask]['has_email'].sum()}/{non_hireable_mask.sum()}")
#     print(f"Hireable fraction: {hireable_email_fraction:.3f}")
#     print(f"Non-hireable fraction: {non_hireable_email_fraction:.3f}")
    
#     return difference

# # Read and analyze the complete dataset
# result = analyze_email_sharing()
# print(f"\nFinal result: {result:.3f}")

import pandas as pd

def analyze_email_sharing(users_csv_path='users.csv'):
    # Read the CSV file
    df = pd.read_csv(users_csv_path)

    # Replace NaN or empty values in 'hireable' with False
    df['hireable'] = df['hireable'].fillna(True).astype(bool)
    
    # Convert 'email' column to boolean indicating whether an email is present
    df['has_email'] = df['email'].notna() & (df['email'] != '')

    # Calculate the fraction of users with emails for hireable and non-hireable users
    hireable_email_fraction = df[df['hireable']]['has_email'].mean()
    non_hireable_email_fraction = df[~df['hireable']]['has_email'].mean()

    # Calculate difference and round to 3 decimal places
    difference = round(hireable_email_fraction - non_hireable_email_fraction, 3)

    # Print debug information
    print(f"Total users: {len(df)}")
    print(f"Hireable users with email: {df[df['hireable']]['has_email'].sum()}/{df['hireable'].sum()}")
    print(f"Non-hireable users with email: {df[~df['hireable']]['has_email'].sum()}/{(~df['hireable']).sum()}")
    print(f"Hireable fraction: {hireable_email_fraction:.3f}")
    print(f"Non-hireable fraction: {non_hireable_email_fraction:.3f}")

    return difference

# Read and analyze the dataset
result = analyze_email_sharing()
print(f"\nFinal result: {result:.3f}")
