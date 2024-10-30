# TDS_Project1
This project contains data on GitHub users based in Dublin with over 50 followers, as well as their repository information. The data was collected using the GitHub API through a custom Python script. 

#######SCRAPING DATA#######

***********Search for Users***********--->
The GitHub API was used to search for users with:
Location set to "Dublin"
Minimum followers set to 50
For each user returned by the search, the script retrieved detailed profile information, including username, name, company, email, bio, number of followers, number of public repositories, and account creation date.

***************Repository Data Collection*************** --->
For each user meeting the search criteria, the script collected data on up to 500 of their public repositories. 
The repository data includes:
Repository name
Creation date
Number of stars and watchers
Main programming language used
Additional repository attributes such as whether it has projects and a wiki enabled, and the license type (if any).

*********Output*********--->
The data is saved in two CSV files:

users.csv: Contains profile information for each GitHub user in Dublin with over 50 followers.
repositories.csv: Contains data for up to 500 public repositories for each of these users.

#######DATA ANALYSIS#######

