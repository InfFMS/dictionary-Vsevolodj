# Дан граф друзей в социальной сети, где:
# Ключ словаря — имя пользователя (вершина графа).
# Значение — список друзей (смежные вершины).
from operator import truediv

# Пример входных данных:
friends_graph = {
    "Анна": ["Борис", "Виктор", "Дарья"],
    "Борис": ["Анна", "Виктор"],
    "Виктор": ["Анна", "Борис", "Дарья"],
    "Дарья": ["Анна", "Виктор", "Елена"],
    "Елена": ["Дарья"],
    "Миша":[],
    "re3rewsd":[]
}

# Написать функции, которые выполняют следующие операции:
# 1. Поиск друзей (соседей) для заданного пользователя.
# 2. Проверка, являются ли два пользователя друзьями (есть ли ребро между вершинами).
# 3. Поиск изолированных пользователей (вершин без рёбер).
def find_friend(key,graph):
    return str(graph[key])[1:-1]
print(find_friend("Анна", friends_graph))

def check_friends(key1,key2,graph):
    i = 0
    for friend in graph[key1]:
        if friend == key2:
            return True
            i = 1
    if i == 0:
        return False
print(check_friends("Анна","Елена", friends_graph))

def friendless_users(graph):
    users = []
    keys = list(graph.keys())
    for user in keys:
        if graph[user]==[]:
            users = users+[user]
    return str(users)[1:-1]
print(friendless_users(friends_graph))

