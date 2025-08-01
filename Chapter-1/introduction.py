"""
Find key connectors from an example social network.
"""

from collections import Counter, defaultdict

def create_friends_dict(friendship_pairs, users):
    friendships = {user["id"]: [] for user in users}

    for i, j in friendship_pairs:
        friendships[i].append(j)
        friendships[j].append(i)
    
    return friendships

def number_of_friends(user):
    user_id = user["id"]
    friend_id = friendships[user_id]

    return len(friend_id)

#users and friendship_pairs would be given or gettable.
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship_pairs = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
                    (4,5),(5,6),(5,7),(6,8),(7,8),(8,9),]

#Create the friends dict once instead of iterating over everytime we have a question.
friendships = create_friends_dict(
    users=users,
    friendship_pairs=friendship_pairs)

#print(friendships)

#Answers, how many friends does user[0] have?
user_friends = number_of_friends(user=users[0])
#print(user_friends)

#Other useful stats
total_connections = sum(number_of_friends(user=user) for user in users)
#print("The total number of connections are:", total_connections)

num_users = len(users)
#print("The total number of users are:", num_users)

avg_connections = total_connections / num_users
#print("The average number of connections per user:", avg_connections)

#Create a list of friends and sort.
num_friends_list = [(user["id"], number_of_friends(user)) for user in users]
num_friends_list.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)

#print(num_friends_list)
#Output: [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]


"""
Connections you may know suggestions for social networks.
"""

def foaf_ids_flaw(user):
    return [foaf_id
        for friend_id in friendships[user["id"]]
        for foaf_id in friendships[friend_id]]

foaf_user0 = foaf_ids_flaw(user=users[0])
#print(foaf_user0)

#Output: [0, 2, 3, 0, 1, 3]
#Explanation:
# 0 is friends with 2 people (since it is bidirectional both those connections are valid)
# 3 is reachable from two paths (1 and 2), which is why it appears twice. 

def friends_of_friends(user):
    user_id = user['id']
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )
#print(friends_of_friends(users[3]))

#Output: Counter({0: 2, 5: 1})
#Explanation:
# Id=3 has two mutual friends with id=0 and only one with id=5


interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
    (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"),
    (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machin learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"), 
    (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages"),
    (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"),
    (8, "Big Data"), (8, "artificial intelligence"), (8, "deep learning"), (8, "neural networks"),
    (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_that_like(interest):
    return [
        user_id
        for user_id, user_interest in interests
        if user_interest == interest
    ]

#Above will require a search of every item in the list.

user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

#print(user_ids_by_interest)

interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

#print(interests_by_user_id)

def most_common_interest_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )

#print(most_common_interest_with(user=users[0]))


"""
Salaries and Experience
"""

salaries_and_tenures = [
    (83000,8.7), (88000, 8.1), (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2)]

salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

#print(average_salary_by_tenure)
#Output: {8.7: 83000.0, 8.1: 88000.0, 0.7: 48000.0, 6: 76000.0, 6.5: 69000.0, 7.5: 76000.0, 2.5: 60000.0, 10: 83000.0, 1.9: 48000.0, 4.2: 63000.0}
#Explanation: This is not helpful as there is not a lot of data with the same tenure.

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

#print(average_salary_bucket)
#Output: {'more than five': 79166.66666666667, 'less than two': 48000.0, 'between two and five': 61500.0}
#Explanation: Buckets are better for this type of data.

"""
Paid Accounts

Here is the tenure and paid vs unpaid accounts as we know:
0.7 paid
1.9 unpaid
2.5 paid
4.2 unpaid
6.0 unpaid
6.5 unpaid
7.5 unpaid
8.1 unpaid
8.7 paid
10.0 paid
"""

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"

#The above was totally eyeballed and is not a reliable way to calculate, 
# especially as more data becomes available.

"""
Topics of Interest

Reusing the interests tuples from earlier.
"""

#Find the most popular interests.
words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())
#print(words_and_counts)
#Output: Counter({'big': 3, 'data': 3, 'java': 3, 'python': 3, 'learning': 3, 'hadoop': 2, 'cassandra': 2, 'scikit-learn': 2, 'r': 2, 'statistics': 2, 'regression': 2, 'probability': 2, 'neural': 2, 'networks': 2, 'spark': 1, 'storm': 1, 'nosql': 1, 'mongodb': 1, 'hbase': 1, 'postgres': 1, 'scipy': 1, 'numpy': 1, 'statsmodels': 1, 'pandas': 1, 'machin': 1, 'decision': 1, 'trees': 1, 'libsvm': 1, 'c++': 1, 'haskell': 1, 'programming': 1, 'languages': 1, 'mathematics': 1, 'theory': 1, 'machine': 1, 'mahout': 1, 'artificial': 1, 'intelligence': 1, 'deep': 1, 'mapreduce': 1})

#Here is a way to output the words that occur more than once.
for word, count in words_and_counts.most_common():
    if count > 1:
        done = True
        #print(word, count)
"""Output:
big 3
data 3
java 3
python 3
learning 3
hadoop 2
cassandra 2
scikit-learn 2
r 2
statistics 2
regression 2
probability 2
neural 2
networks 2
"""
