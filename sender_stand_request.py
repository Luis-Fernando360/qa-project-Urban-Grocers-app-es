import requests
import configuration



# Paso 1: Crear usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body)

# Paso 2: Crear un Kit personal
def post_new_client_kit(kit_body, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH, headers=headers, json=kit_body)