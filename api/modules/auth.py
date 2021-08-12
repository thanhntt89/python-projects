from flask import Blueprint

class auth():
    
    auth_bp = Blueprint('auth',__name__)

    def __init__(self) -> None:
        pass

    @auth_bp.route('/')
    def login():
        return 'this auth login'