import facebook
import json
import requests

if __name__ == '__main__':
    token = {'EAARf5K45TPkBAPWXiroyANIV8geVECRWvetUZAFGcYUaYTi2d2NZCsHcU0dpRAWQNZC5DhcWbVmY4jGPsaZAjvzBdS9orhvBHf8ZB2VLaVuNFiBvaniXXK97jTiRTL8gQN3YiZBfpp6ZAuPDBZBc2a5CmgFXcwvcprMaLbypfPuU2uN9oQFQfRLNVksXK95ynNoTq83SkktUrAZDZD'}

    graph = facebook.GraphAPI(token)

    user = graph.get_object('me')

    posts = graph.get_connections(user['id'], 'posts')

    while True:
        try:
            with open('my_posts.jsonl', 'a', encoding='utf8') as file:
                for post in posts['data']:
                    file.write(json.dumps(post, ensure_ascii=False) + '\n')
                print("***********")
                posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            break
