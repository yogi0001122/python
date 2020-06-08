import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import sys
import os
import sys
import getopt

args = sys.argv
if len(args) != 3:
    print ("""
    Usage: python archive_delete_git_repo.py -d <RepoName> or -a <RepoName>
    Options:
    -d or --delete    <RepoName>  : To delete  the repo
    -a or --archive   <RepoName>  : To archive the repo
    """)
    sys.exit(1)

#print ('ARGV      :', sys.argv[1:])
options, remainder = getopt.getopt(sys.argv[1:], 'da:', ['delete=',
                                                         'archive=',
                                                         ])
home_path = os.path.expanduser('~')
token_file = home_path + '/.tokenfile'
file = open(token_file)
org_name = "yogi1122"
for line in file:
    token = line.rstrip("\n").lstrip("\n")
token_code = 'token ' + token
headers={'Authorization': token_code,'content-type': 'application/vnd.github.nebula-preview+json'}

def yes_or_no(question):
    reply = str(raw_input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")

def archive_repo(url):
    payload = r'''{
        "archived": true
        }'''
    response = requests.patch(url,headers=headers,data=payload,verify=False)
    print (response.status_code)
    if response.status_code == 200:
        print ("Repo %s has been archived successfully" % (GIT_REPO_NAME))
    else:
        print ("Repo %s does not exist or already in archive state" % (GIT_REPO_NAME))

def delete_repo(url):
    flag = yes_or_no("Do you want to delete repo %s?" % (GIT_REPO_NAME))
    if flag == True:
        response = requests.delete(url,headers=headers)
        print (response.status_code)
        if response.status_code == 200 or response.status_code == 204:
                print ("Repo %s has been deleted successfully" % (GIT_REPO_NAME))
        else:
                print ("Repo %s does not exist " % (GIT_REPO_NAME))
    else:
        print ("No Action performed....")


if "main" in __name__:
    for opt, arg in options:
        if opt in ('-d', '--delete'):
            GIT_REPO_NAME = arg
            url = "https://api.github.com/repos/%s/%s" % (org_name, GIT_REPO_NAME)
            print (url)
            delete_repo(url)
        elif opt in ('-a', '--archive'):
            GIT_REPO_NAME = arg
            url = "https://api.github.com/repos/%s/%s" % (org_name, GIT_REPO_NAME)
            print (url)
            archive_repo(url)
