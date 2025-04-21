from faker import Faker
from blog.models import Entry
from blog import db
from blog import create_app  # jeśli masz funkcję create_app, jak w klasycznym Flasku

fake = Faker()

app = create_app()  # tworzymy aplikację

with app.app_context():  # potrzebne do działania db w Flasku
    for _ in range(10):
        post = Entry(
            title=fake.sentence(),
            body='\n'.join(fake.paragraphs(15)),
            is_published=True
        )
        db.session.add(post)
    db.session.commit()
    print("Wygenerowano 10 przykładowych wpisów.")
