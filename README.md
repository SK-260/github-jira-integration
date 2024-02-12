# GitHub and Jira Integration

The code in this repo can be used to automate the creation of Stories based on the Issues in the Repository. If the Developed feels it is a valid problem and it needs to worked on. The developer can comment `/jira` in the issue to create a JIRA Story.

### Usage

A new Server needs to be deployed and the python application needs to run on that server. You can use command 
```python
python3 integration.py
```

You need to also add Environment variables "EMAIL" and "API_TOKEN" which will be used to authenticate with the JIRA. You can use `export` command on Linxux servers.
```
export EMAIL="<enter_your_email>"
export API_TOKEN="<Enter-api-token>"
``` 


