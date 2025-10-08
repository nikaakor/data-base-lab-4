"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

import secrets
from typing import Dict, Any
from http import HTTPStatus

from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy

# --- Create SQLAlchemy instance ---
db = SQLAlchemy()

# --- Todo model for database table ---
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.String(50), primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# --- Function to create Flask app ---
def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    """Create Flask application, initialize DB and routes"""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config.update(app_config)

    _init_db(app)
    _init_routes(app)

    return app

def _init_db(app: Flask) -> None:
    """Initialize the database and create tables"""
    db.init_app(app)
    with app.app_context():
        db.create_all()

def _init_routes(app: Flask) -> None:
    """Initialize REST API routes with Flask-RESTX"""
    api = Api(app, title="Todo Backend", description="Simple backend with Azure MySQL")

    @api.route('/todos/<string:todo_id>')
    class TodoResource(Resource):
        def get(self, todo_id):
            """Get a todo by ID"""
            todo = Todo.query.get(todo_id)
            if todo:
                return {"id": todo.id, "title": todo.title, "done": todo.done}, HTTPStatus.OK
            return {"error": "Todo not found"}, HTTPStatus.NOT_FOUND

        def put(self, todo_id):
            """Add or update a todo by ID"""
            data = request.get_json()
            todo = Todo.query.get(todo_id)
            if todo:
                todo.title = data.get("title", todo.title)
                todo.done = data.get("done", todo.done)
            else:
                todo = Todo(id=todo_id, title=data.get("title", ""), done=data.get("done", False))
                db.session.add(todo)
            db.session.commit()
            return {"id": todo.id, "title": todo.title, "done": todo.done}, HTTPStatus.CREATED
