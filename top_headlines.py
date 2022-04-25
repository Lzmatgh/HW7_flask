from flask import Flask, render_template
import requests
import json
import secrets2

app = Flask(__name__)


# 1. default home page
@app.route('/')
def index():
    return '<h1>Welcome!</h1>'


# 2. get users name
@app.route('/name/<nm>')
def hello_name(nm):
    apikey = secrets2.api_key
    params = {'api-key': apikey}

    baseurl = 'https://api.nytimes.com/svc/topstories/v2/technology.json?'
    response = requests.get(baseurl, params)
    nytimes_json = response.json()
    results = nytimes_json['results']
    top5 = results[0:5]
    titles = [x['title'] for x in top5]
    urls = [x['url'] for x in top5]
    thumbnails = [x['multimedia'][0]['url'] for x in top5]

    return render_template('name.html', name=nm, titles=titles, urls=urls, thumbnails=thumbnails)


# # 3. query new york times API
# def nytimes_api():
#     apikey = secrets2.api_key
#     params = {'api-key' : apikey}
#     # headers = {'Authorization': 'Bearer ' + apikey}
#     baseurl = 'https://api.nytimes.com/svc/topstories/v2/technology.json?'
#     response = requests.get(baseurl, params)
#     nytimes_json = response.json()
#     results = nytimes_json['results']
#     # print(nytimes_json)
#
#     return results
#
#
# results_list = nytimes_api()
# top5 = results_list[0:5]
# print('top5', top5)
# titles = [x['title'] for x in top5]
# urls = [x['url'] for x in top5]
# thumbnails = [x['multimedia'][0]['url'] for x in top5]
# print(urls)
# print(thumbnails)
# print(titles)
# print(len(titles))



if __name__ == '__main__':
    app.run(debug=True)