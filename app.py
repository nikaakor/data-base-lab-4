"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from my_project import create_app

DEVELOPMENT_PORT = 5000

config_data = {
    "SQLALCHEMY_DATABASE_URI": "sqlite:///my_db.sqlite",
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
}

additional_config = {}

app = create_app(config_data, additional_config)

if __name__ == "__main__":
    import os
    PORT = int(os.environ.get("PORT", DEVELOPMENT_PORT))
    app.run(host="0.0.0.0", port=PORT, debug=False)
