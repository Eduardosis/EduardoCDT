from django.conf import settings
from datetime import datetime, timedelta, timezone
import jwt

def generate_access_token(user):
    payload = {
        'idUsuario': user.idUsuario,  # Asegúrate de usar el nombre correcto del campo de ID del usuario
        'exp': datetime.now(timezone.utc) + timedelta(days=1),
        'iat': datetime.now(timezone.utc),
    }

    access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return access_token