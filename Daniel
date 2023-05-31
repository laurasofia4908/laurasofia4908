import requests

def obtener_capital(pais):
    url = f"https://restcountries.com/v2/name/{pais}?fullText=true"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()
            capital = datos[0]['capital']
            return capital
        else:
            print("Error en la solicitud. Código de estado:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", e)

# Ejemplo de uso
pais = input("Ingresa el nombre del país: ")
capital = obtener_capital(pais)

if capital is not None:
    print(f"La capital de {pais} es {capital}.")
