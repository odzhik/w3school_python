# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#task 1
# def HighScoreMovie():
#     for i in range(len(movies)):
#         if movies[i]["imdb"] > 5.5:
#             return print(movies[i])
        
# HighScoreMovie()

#task 2
# def highScoreMov():
#     for i in range(len(movies)):
#         if movies[i]["imdb"] > 5.5:
#             movs.append(movies[i])
#     print(movs)

# movs = []

# highScoreMov()

#task3
# list = []
# def getCategory():
#     for i in range(len(movies)):
#         if movies[i]["category"] == "Crime":
#             print(movies[i])

# getCategory()

#task4
# average = 0
# def average_imdb():
#     total = sum(i["imdb"] for i in movies)
#     average = total / len(movies)
#     print(average)
# average_imdb()

#task 5
def imdbAvg():
    for i in range(len(movies)):
        if movies[i][category] == "Crime":
            total = sum(i[movies](["category == "Crime"]) for i in movies)
                                   av