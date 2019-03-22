import facebook
import json
import requests


def req_facebook(req):
    r = requests.get()

if __name__ == '__main__':
    token = {"EAARf5K45TPkBAIUIEnVRZBHZCFvjsqjLmuc6taVYCPdxB2O3YZADwqZAmoWrhSs6clttPZC0PBjUAj0nJ0ZCAhHSwukzNn73ETHWD8Xt1vDMLwm7tZCZCNzPwAtNnlbYpzLNg4ZAUkXoOUjEUa7RBdbzHkfLmj3i8fzXcSYhZBSUAvSjkinNEBvXqaaSepOJq7KmSg6HZAS2C5ZBDgZDZD"}

    graph = facebook.GraphAPI(token)

    user = graph.get_object('me')

    friends = graph.get_connections(user["id"], 'friends')

    print(json.dumps(friends, indent=4))


