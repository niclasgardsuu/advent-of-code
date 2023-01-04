import requests
from bs4 import BeautifulSoup
import re
from collections import defaultdict
import matplotlib.pyplot as pl


days = []
for i in range(25):
    days.append(requests.get(f"https://adventofcode.com/2022/leaderboard/day/{i+1}"))
    print("day",i+1,"fetched")

def entry_to_score(html):
    a = re.findall(r'(?<=><\/span>)([^<]*)', str(html))
    b = re.findall(r'(?<="leaderboard-position">)([^)]*)', str(html))
    a = a[0]
    b = b[0].strip()
    if a == '':
        a = "anonymous"
    if b.isnumeric():
        b = 101 - int(b)
    return (a,b)

users = set()
score_days = [defaultdict(int)]
for day in days:
    soup = BeautifulSoup(day.content, 'html.parser')
    scores = soup.find_all(class_='leaderboard-entry')
    scores = list(map(entry_to_score,scores))
    scores = list(filter(lambda x: x[0] != 'anonymous', scores))
    score_days.append(defaultdict(int))
    for score in scores:
        users.add(score[0])
    
    for score in scores:
        if score_days[-1][score[0]] == 0:  
            score_days[-1][score[0]] = score_days[-2][score[0]]+score[1]
        else:
            score_days[-1][score[0]] = score_days[-1][score[0]]+score[1]

    for user in users:
        if score_days[-1][user] == 0:
            score_days[-1][user] = score_days[-2][user] 

fig, ax = pl.subplots()

for user in users:
    user_score = []
    for score_day in score_days:
        user_score.append(score_day[user])
    ax.plot(range(len(score_days)), user_score)

pl.show()