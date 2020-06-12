# Python Requests Library UseCase
 This code is for Python Requests Library using GitHub API
 

# HOW To: Archive or Delete GitHub repo for user or for an organization on GitHub?
# Solution:
     
     ## Prerequisite:
     
         pip install requests
     
     ## Step 1:  Create PAT for GitHub User account:
          
          User ---> Setting--->Developer settings--->Personal access tokens--->Generate new token
     
     ## Step 2:  Create a file with the name .tokenfile under user's home directory on system where you have this scrip and paste user's token in .tokenfile
     ## Step 3:  Change org name or user account name in script for variable org_name like this: org_name = "yogi1122"
     ## Step 4:  Now you can run script to Archive Repo on GitHub for user account or for an organization
      
                - python archive_delete_git_repo.py -a testrepo
      
     ## Step 4:  Now you can run script to Delete Repo on GitHub for user account or for an organization
     
                - python archive_delete_git_repo.py -d testrepo 
                
                ### Note: Repo deletion action will ask for confirmation like below : 
                
                - Do you want to delete repo ? (y/n):

