import json
import urllib.request

with open('versions.json') as versions:
    data = json.load(versions)
    for v in data:
        version = v['version']
        url = 'https://submissions.dcc.icgc.org/ws/dictionaries/%s'%version
        urllib.request.urlretrieve(url, './%s.json'%version)
