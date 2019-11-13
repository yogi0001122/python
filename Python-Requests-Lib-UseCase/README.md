# Python-Requests-Lib-UseCase
 This code is for Python-Requests-Lib-UseCase

# HOW TO: Monitor the secure agent status and the status of seperate services in Informatica cloud using API?
# Solution:

To retrieve the status and service details of the Informatica cloud secure agent, you can make use of Rest API provided by Informatica Cloud.

REST API that can be used is :- 

GET <serverUrl>/api/v2/agent/details/{agent_id}
Accept:application/json
icSessionId: <icSessionId>


To invoke most of the APIs, the icSessionId and serverUrl is required which is obtained by invoking first invoking the Login() API

Below is REST Login API that can be used is to get icSessionId:

POST https://dm-us.informaticacloud.com/ma/api/v2/user/login

Accept:application/json

{
    "@type" : "login",

    "username" : "XXXXXX@gmail.com",
    
    "password" : "XXXXXX"
}
