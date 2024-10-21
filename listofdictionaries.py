records = [
# Product
    {"name": "laptop", "price": 750},
    {"name": "desk chair", "price": 100},
    {"name": "smart watch", "price": 200},
    {"name": "notebook", "price": 5},
    {"name": "running shoes", "price": 80},
# Employee
    {"name": "john doe", "job title": "sales"},
    {"name": "jane smith", "job title": "human resources"},
    {"name": "mark johnson", "job title": "it"},
    {"name": "lisa wong", "job title": "marketing"},
    {"name": "paul mcdonald", "job title": "finance"},
# Books
    {"title": "the great gastby", "author": " f. scott fitzgerald"},
    {"title": "to kill a mockingbird", "author": "harper lee"},
    {"title": "1984", "author": "george orwell"},
    {"title": "the catcher in the rye", "author": "jd salinger"},
    {"title": "a brief history of time", "author": "stephen hawking"},
# University
    {"name": "university of the philippines", "location": "quezon city"},
    {"name": "ateneo de manila university", "location": "quezon city"},
    {"name": "de la salle university", "location": "manila"},
    {"name": "university of santo tomas", "location": "manila"},
    {"name": "polytechnic university of the philippines"},
# Restaurant
    {"name": "vikings luxury buffet", "cuisine type": "buffet"},
    {"name": "antonios restaurant", "cuisine type": "fine dining"},
    {"name": "mesa filipino moderne", "cuisine type": "filipino"},
    {"name"}: "manam comfort filipino", "cuisine type": "filipino"},
    {"name": "ramen nagi", "cuisine type": "japanese"}
]
for record in records:
    for key, value in record.items():
        print(f"{key}: {value}")
    print("-" * 30)