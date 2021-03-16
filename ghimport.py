import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import json

with open('config.json', 'r') as j:
    config = json.load(j)
    print(config)

def make_github_issue(title, body=None, created_at=None, closed_at=None, updated_at=None, assignee=None, milestone=None, closed=None, labels=None):
    # Create an issue on github.com using the given parameters
    # Url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (config['REPO_OWNER'], config['REPO_NAME'])
    # https://api.github.com/repos/modyo/selenium-scripts/issues
    # Headers
    headers = {
        "Authorization": "token %s" % config['TOKEN'],
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "juak-modyo"
    }
    
    # Create our issue
    data = {
    'title': title,
    'body': body,
    'created_at': created_at,
    'closed_at': closed_at,
    'updated_at': updated_at,
    'milestone': milestone,
    'closed': closed,
    'labels': labels.split(",")
    }

    payload = json.dumps(data)

    # Add the issue to our repository
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 201:
        print 'Successfully created Issue "%s"' % title
        rData = json.loads(response.content)
        if closed == "closed":
          data2 = {
          'state': closed,
          }
          payload2 = json.dumps(data2)
          response2 = requests.request("PATCH", rData['url'], data=payload2, headers=headers)
          if response.status_code == 201:
            print 'Successfully closed Issue "%s"' % title
          else:
            print 'Could not close Issue "%s"' % title
            print 'status' + str(response.status_code)
            print 'Response:', response.content

    else:
        print 'Could not create Issue "%s"' % title
        print 'Response:', response.content
