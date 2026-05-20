from faker import Faker
import random
import json

fake = Faker()

YEARS = list(range(1500, 2025))

def generate_event():

    return {
        "title": fake.sentence(nb_words=6),
        "description": fake.text(max_nb_chars=400),
        "event_year": random.choice(YEARS),
        "created_by": random.randint(1, 10)
    }

if __name__ == "__main__":

    for _ in range(5):
        print(json.dumps(generate_event()))
