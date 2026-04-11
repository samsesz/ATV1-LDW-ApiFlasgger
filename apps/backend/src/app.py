from flask import Flask
from flasgger import Swagger
import os
from dotenv import load_dotenv

# SCHEMAS
from schemas.characters_schema import CharactersSchema
from schemas.dragons_schema import DragonsSchema
from schemas.houses_schema import HousesSchema
from schemas.swords_schema import SwordsSchema

load_dotenv()

def create_app():
    app = Flask(__name__)

    from database import init_db
    init_db(app)

    db_url = os.getenv('DATABASE_URL', '')
    env_label = 'Supabase' if 'supbase' in db_url else 'Local (Docker)'

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "API de GOT",
            "description": "API para atv1",
            "version": "1.0.0"
        },
        "definitions": {
            "Characters": CharactersSchema.model_json_schema(),
            "Dragons": DragonsSchema.model_json_schema(),
            "Houses": HousesSchema.model_json_schema(),
            "Swords": SwordsSchema.model_json_schema(),
            "Error": {
                "type": "object",
                "properties": {"error": {"type": "string"}}
            }
        }
    }

    Swagger(app, template=swagger_template)

    from routes.characters import characters_bp
    from routes.dragons import dragons_bp
    from routes.houses import houses_bp
    from routes.swords import swords_bp

    app.register_blueprint(characters_bp, url_prefix='/api/characters')
    app.register_blueprint(dragons_bp, url_prefix='/api/dragons')
    app.register_blueprint(houses_bp, url_prefix='/api/houses')
    app.register_blueprint(swords_bp, url_prefix='/api/swords')

    return app

app = create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)