import sys
import os

# Adiciona a pasta src ao path
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
))

from dotenv import load_dotenv
load_dotenv()

from app import create_app
from database import db
from models import Characters, Dragons, Houses, Swords


CHARACTERS = [
    {
        "id": 1,
        "title": "Theon Greyjoy",
        "description": " Protegido de Ned Stark, Herdeiro das ilhas de ferro",
    },
]

DRAGONS = [
    {
        "id": 1,
        "title": "Caraxes",
        "description": "Dragão de Daemon Targaryen",
    },
]

HOUSES = [
    {
        "id": 1,
        "title": "Stark",
        "description": "O inverno está chegando.",
    },
]

SWORDS = [
    {
        "id": 1,
        "title": "Neddle",
        "description": "Espada de arya stark",
    },
]

def seed():
    """Popula o banco de dados com os dados iniciais."""
    app = create_app()

    with app.app_context():
        # Verifica se já existem dados
        if Characters.query.first():
            print("Banco já possui dados. Pulando seed.")
            return

        print("Populando banco de dados...")

        for c in CHARACTERS:
            db.session.add(Characters(**c))
        print(f"  {len(CHARACTERS)} personagens inseridos")

        for d in DRAGONS:
            db.session.add(Dragons(**d))
        print(f"  {len(DRAGONS)} dragões inseridos")

        for h in HOUSES:
            db.session.add(Houses(**h))
        print(f"  {len(HOUSES)} casas inseridas")

        for s in SWORDS:
            db.session.add(Swords(**s))
        print(f"  {len(SWORDS)} espadas inseridas")

        db.session.commit()
        print("Seed concluído com sucesso!")


if __name__ == '__main__':
    seed()