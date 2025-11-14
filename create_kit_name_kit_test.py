import pytest
from sender_stand_request import post_new_user, post_new_client_kit
from data import user_body


# Crear un nuevo usuario y obtener su token de autenticación
@pytest.fixture(scope="module")
def auth_token():
    response = post_new_user(user_body)
    assert response.status_code == 201, "❌ Error al crear el usuario"
    return response.json()["authToken"]

@pytest.mark.parametrize("kit_body, expected_status", [
   ({"name": "a"}, 201), # 1 carácter
   ({"name": "a" * 511}, 201), # 511 caracteres
   ({"name": ""}, 400), # 0 caracteres
   ({"name": "a" * 512}, 400), # 512 caracteres
   ({"name": "!№%@,"}, 201), # caracteres especiales
   ({"name": " A Aaa "}, 201), # espacios
   ({"name": "123"}, 201), # números
   ({}, 400), # sin parámetro name
   ({"name": 123}, 400), # tipo de dato incorrecto
 ])

def test_create_kit(auth_token, kit_body, expected_status):
    response = post_new_client_kit(kit_body, auth_token)
    # Verifica el código de estado
    assert response.status_code == expected_status, f"❌ Se esperaba {expected_status}, se obtuvo {response.status_code}"

# Si la creación fue exitosa, verifica que 'name' coincida
    if response.status_code == 201:
      response_json = response.json()
      assert response_json["name"] == kit_body["name"], "❌ El campo 'name' no coincide"