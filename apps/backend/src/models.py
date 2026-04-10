from database import db
from sqlalchemy.dialects.postgresql import JSONB

class Characters(db.Model):
    """Modelo SQLAlchemy para a tabela de personagens."""

    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)


class Dragons(db.Model):
    """Modelo SQLAlchemy para a tabela de dragões."""

    __tablename__ = 'dragons'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)


class Houses(db.Model):
    """Modelo SQLAlchemy para a tabela de casas."""

    __tablename__ = 'houses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

class Swords(db.Model):
    """Modelo SQLAlchemy para tabela de espadas."""

    __tablename__ = 'swords'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)