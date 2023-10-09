from flask import Flask
from src.main.routes.rotas import user_route_bp

app = Flask(
    __name__, static_folder="/app/src/static", template_folder="/app/src/templates"
)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB

# Register Blueprints
app.register_blueprint(user_route_bp)
