# TDS_Project1
This project contains data on GitHub users based in Dublin with over 50 followers, as well as their repository information. The data was collected using the GitHub API through a custom Python script. 

####### SCRAPING DATA #######

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

####### DATA ANALYSIS(interesting insights)#######

1) A 0.315 correlation shows that repositories with projects enabled are somewhat likely to have wikis enabled as well, but the relationship isn’t strong.
2) A regression slope of 7.533 for followers on bio word count means that, on average, each additional word in a user's bio is associated with approximately 7.5 more followers.The positive slope indicates that longer bios tend to correlate with higher follower counts. It suggests that users who write more extensive bios are likely to attract more followers.
3) SURPRISING : A correlation of −0.099 suggests a very weak negative relationship between the account creation date (in terms of how long ago it was created) and the number of followers. Accounts created earlier or later don’t necessarily have more or fewer followers in any consistent way.

####### RECOMMENDATION TO DEVELOPERS #######

*Consistent Engagement, Regardless of Account Age*: The weak negative correlation between account age and follower count suggests that older accounts do not necessarily have more followers. Engagement, active contributions, and showcasing current work may matter more. Regularly share updates, work on open-source projects, and interact with others’ repositories to stay visible and maintain growth in followers.

