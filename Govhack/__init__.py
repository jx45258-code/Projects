from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv("keys.env")
    
    app = Flask(__name__, template_folder="../templates")
    app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "dev")
    
    # Import and register blueprints
    from .routes import main_bp   
    from .views  import  bp as chat_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(chat_bp, url_prefix="/chat") 
  
    
    return app
