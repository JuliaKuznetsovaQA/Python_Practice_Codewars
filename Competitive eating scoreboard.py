"""You are the judge at a competitive eating competition and you need to choose a winner!
There are three foods at the competition and each type of food is worth a different amount of points.
Points are as follows:
Chickenwings: 5 points
Hamburgers: 3 points
Hotdogs: 2 points

Write a function that helps you create a scoreboard.
It takes as a parameter a list of objects representing the participants, for example:

[
  {name: "Habanero Hillary", chickenwings: 5 , hamburgers: 17, hotdogs: 11},
  {name: "Big Bob" , chickenwings: 20, hamburgers: 4, hotdogs: 11}
]
It should return "name" and "score" properties sorted by score; if scores are equals, sort alphabetically by name.

[
  {name: "Big Bob", score: 134},
  {name: "Habanero Hillary", score: 98}
]
scoreboard([{"name": "Billy The Beast", "chickenwings": 17 , "hamburgers": 7, "hotdogs": 8},
                                       {"name": "Habanero Hillary", "chickenwings": 5 , "hamburgers": 17, "hotdogs": 11},
                                       {"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},
                                       {"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]),
                                       [{"name": "Big Bob", "score": 134},{"name": "Billy The Beast", "score": 122},
                                        {"name": "Habanero Hillary", "score": 98},{"name": "Joey Jaws", "score": 94}])"""


def scoreboard(who_ate_what):
    for person in who_ate_what:
        if 'chickenwings' not in person:
            person['chickenwings'] = 0
        if 'hamburgers' not in person:
            person['hamburgers'] = 0
        if 'hotdogs' not in person:
            person['hotdogs'] = 0
        person['score'] = person['chickenwings'] * 5 + person['hamburgers'] * 3 + person['hotdogs'] * 2
        del person['chickenwings'], person['hamburgers'], person['hotdogs']
    print(sorted(who_ate_what, key=lambda x: (-x['score'], x['name'])))


scoreboard([{"name": "Jack The Beast", "chickenwings": 17, "hamburgers": 7, "hotdogs": 8},
                                       {"name": "Habanero Hillary", "chickenwings": 5, "hotdogs": 11},
                                       {"name": "Joey Jaws", "hamburgers": 8}, {"name": "Lilian"},
                                       {"name": "Max Bob", "chickenwings": 17, "hamburgers": 7, "hotdogs": 8}])