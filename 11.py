# import pandas as pd
# from scipy.stats import chi2_contingency

# # Load the CSV file
# csv_file = 'repositories.csv'  # Replace with the correct path

# # Load the CSV into a DataFrame
# df = pd.read_csv(csv_file)

# # Convert 'has_projects' and 'has_wiki' to boolean if necessary
# df['has_projects'] = df['has_projects'].astype(bool)
# df['has_wiki'] = df['has_wiki'].astype(bool)

# # Create a contingency table
# contingency_table = pd.crosstab(df['has_projects'], df['has_wiki'])

# # Perform Chi-Square test
# chi2, p, dof, expected = chi2_contingency(contingency_table)

# print(f"Chi-Square Statistic: {chi2}")
# print(f"P-value: {p}")



# import pandas as pd

# # Load repository data from CSV file
# repo_df = pd.read_csv("repositories.csv")

# # Check if the necessary columns are present
# if 'has_projects' in repo_df.columns and 'has_wiki' in repo_df.columns:
#     # Calculate the correlation
#     correlation = repo_df['has_projects'].astype(int).corr(repo_df['has_wiki'].astype(int))

#     # Display the correlation rounded to 3 decimal places
#     print(f"Correlation between 'has_projects' and 'has_wiki' enabled: {correlation:.3f}")
# else:
#     print("The columns 'has_projects' and/or 'has_wiki' are missing in the CSV file.")





import pandas as pd

# Load repository data from CSV file
repo_df = pd.read_csv("repositories.csv")

# Ensure columns exist and contain only boolean values
if 'has_projects' in repo_df.columns and 'has_wiki' in repo_df.columns:
    # Handle any NaN values by filling them with False (assuming missing means not enabled)
    repo_df['has_projects'] = repo_df['has_projects'].fillna(False).astype(bool)
    repo_df['has_wiki'] = repo_df['has_wiki'].fillna(False).astype(bool)

    # Convert to integers for correlation calculation (True -> 1, False -> 0)
    repo_df['has_projects'] = repo_df['has_projects'].astype(int)
    repo_df['has_wiki'] = repo_df['has_wiki'].astype(int)

    # Calculate and print the correlation rounded to 3 decimal places
    correlation = repo_df['has_projects'].corr(repo_df['has_wiki'])
    print(f"Correlation between 'has_projects' and 'has_wiki' enabled: {correlation:.3f}")
else:
    print("The columns 'has_projects' and/or 'has_wiki' are missing in the CSV file.")
