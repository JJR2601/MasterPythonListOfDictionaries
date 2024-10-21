records = [
# Product
    {"Name": "Laptop", "Price": "750"},
    {"Name": "Desk chair", "Price": "100"},
    {"Name": "Smartwatch", "Price": "200"},
    {"Name": "Notebook", "Price": "5"},
    {"Name": "Running shoes", "Price": "80"},
# Employee
    {"Name": "John Doe", "Job title": "Sales"},
    {"Name": "Jane Smith", "Job title": "Human resources"},
    {"Name": "Mark Johnson", "Job title": "IT"},
    {"Name": "lisa Wong", "Job title": "Marketing"},
    {"Name": "Paul Mcdonald", "Job title": "Finance"},
# Books
    {"Title": "The Great Gastby", "Author": " F. Scott Fitzgerald"},
    {"Title": "To Kill a Mockingbird", "Author": "Harper Lee"},
    {"Title": "1984", "Author": "George Orwell"},
    {"Title": "The Catcher in the Rye", "Author": "J.D. Salinger"},
    {"Title": "A Brief History of Time", "Author": "Stephen Hawking"},
# University
    {"Name": "University of the Philippines", "Location": "Quezon city"},
    {"Name": "Ateneo de Manila University", "Location": "Quezon city"},
    {"Name": "De La Salle University", "Location": "Manila"},
    {"Name": "University of Santo Tomas", "Location": "Manila"},
    {"Name": "Polytechnic University of the Philippines", "Location": "Manila"},
# Restaurant
    {"Name": "Vikings Luxury Buffet", "Cuisine type": "Buffet"},
    {"Name": "Antonio's Restaurant", "Cuisine type": "Fine dining"},
    {"Name": "Mesa Filipino Moderne", "Cuisine type": "Filipino"},
    {"Name": "Manam Comfort Filipino", "Cuisine type": "Filipino"},
    {"Name": "Ramen Nagi", "Cuisine type": "Japanese"}
]
for record in records:
    for key, value in record.items():
        print(f"{key}: {value}")
    print("·" * 30)