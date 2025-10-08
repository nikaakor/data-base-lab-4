from my_project import create_app

# --- Development server port ---
DEVELOPMENT_PORT = 5000

# --- Database configuration ---
config_data = {
    "SQLALCHEMY_DATABASE_URI": (
        "mysql+pymysql://veronika:Andriy2405@clouds-mysql.mysql.database.azure.com:3306/footboom"
        "?ssl_ca=/home/Veronika-Korchahin/clouds/azure/DigiCertGlobalRootG2.crt.pem"
    ),
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
}

additional_config = {}

if __name__ == "__main__":
    app = create_app(config_data, additional_config)
    app.run(host="0.0.0.0", port=DEVELOPMENT_PORT, debug=True)
