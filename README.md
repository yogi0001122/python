---
Page_type: Python Use Cases
Languages: Python
Products:
  - iPaaS (IICS REST API) 
  - GitHub
  - Python Flask
---

# Python Code Samples for different-2 product's real time scenarios

These are code samples that show common scenario operations with the different-2 product's using Python different-2 libraries/module.

- [Agent-monitoring](./iics_secure_agent_monitoring/README.md) - Monitor the secure agent status and the status of seperate services in Informatica cloud using API:
    - Informatica Cloud users need a way to monitor whether the secure agent in their environment is up and running or shutdown.
    - To retrieve the status and service details of the Informatica cloud secure agent, you can make use of Rest API provided by Informatica Cloud using this Python script.
    - Read user/password/url from configuration file
    - Enabling Logging
   
- [archive_delete_git_repo](./git/README.md) - To Archive and Delete GitHub repo for user or for an organization:  
    -	Take parameters from user at the run time
   	 - Usage: python archive_delete_git_repo.py -d RepoName or -a RepoName
         - Options :
	     -  -d or --delete    <RepoName>  : To delete  the repo
	     - -a or --archive   <RepoName>  : To archive the repo

- [BuildFlaskAPI](./python-flask-app/README.md) - Build a Python Flask API
