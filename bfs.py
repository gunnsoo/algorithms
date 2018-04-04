#グラフアルゴリズム
#重みなしグラフ
#最短経路問題
#Breadh-first Search(幅優先探索)

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

mango_seller = ["alice", "thom"]


def person_is_seller(name):
    if name in mango_seller:
        return True
    else:
        return False


def bfs_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print("mango seller is not in your friends")
    return False


bfs_search("you")
