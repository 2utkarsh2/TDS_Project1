# import pandas as pd

# def analyze_following_difference(users_csv_path='users.csv'):
#     # Read the data
#     df = pd.read_csv(users_csv_path)
    
#     # Calculate average following for hireable users
#     hireable_following = df[df['hireable'] == True]['following'].mean()
    
#     # Calculate average following for non-hireable users
#     non_hireable_following = df[df['hireable'] != True]['following'].mean()
    
#     # Calculate the difference rounded to 3 decimal places
#     difference = round(hireable_following - non_hireable_following, 3)
    
#     # Print debug information
#     print(f"Number of hireable users: {len(df[df['hireable'] == True])}")
#     print(f"Number of non-hireable users: {len(df[df['hireable'] != True])}")
#     print(f"Average following for hireable users: {hireable_following:.3f}")
#     print(f"Average following for non-hireable users: {non_hireable_following:.3f}")
    
#     return difference

# # Calculate the difference
# result = analyze_following_difference()
# print(f"\nDifference in average following: {result:.3f}")




import pandas as pd

# Load user data from CSV file
users_df = pd.read_csv("users.csv")

# Ensure 'hireable' and 'following' columns exist
if 'hireable' in users_df.columns and 'following' in users_df.columns:
    # Handle any NaN values in 'hireable' by filling them with False (assuming missing means not hireable)
    users_df['hireable'] = users_df['hireable'].fillna(True).astype(bool)
    
    # Calculate the average following for hireable and non-hireable users
    avg_following_hireable = users_df[users_df['hireable']]['following'].mean()
    avg_following_non_hireable = users_df[~users_df['hireable']]['following'].mean()

    # Calculate the difference and round to 3 decimal places
    difference = round(avg_following_hireable - avg_following_non_hireable, 3)
    print(f"Difference in average following: {difference}")
else:
    print("The columns 'hireable' and/or 'following' are missing in the CSV file.")
