import reflex as rx
import requests
from rxconfig import config

class State(rx.State):
    """El estado de la aplicación."""
    pass  # Aquí puedes agregar atributos de estado si es necesario

def index() -> rx.Component:
    # Página de bienvenida (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to !", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

def fetch_movies():
    response = requests.get("http://localhost:8000/movies")  # Cambia la URL según tu API
    print(response.json())  # Agrega esta línea para verificar la respuesta
    return response.json()  # Devuelve la respuesta en formato JSON



def table_movies() -> rx.Component:
    movies = fetch_movies()  # Llama a la función para obtener películas
    if movies:
        # Define los encabezados de la tabla
        headers = ["Title", "Description", "Length", "Director"]
        # Crea la fila de encabezado
        header_row = rx.hstack(*[rx.text(header, font_weight="bold") for header in headers])
        # Crea las filas de la tabla
        table_rows = [
            rx.hstack(
                rx.text(movie['title']),
                rx.text(movie['Description']),
                rx.text(movie['length']),
                rx.text(movie['director']),
            )
            for movie in movies
        ]
        # Retorna el componente de la tabla
        return rx.vstack(
            header_row,  # Agrega la fila de encabezado
            *table_rows,  # Agrega todas las filas de películas
            spacing="2",  # Espaciado entre filas
        )
    else:
        return rx.text("No se pudieron cargar las películas.")


app = rx.App()

# Agregar una página para mostrar películas
app.add_page(table_movies, route="/")

# Comenzar la aplicación
if __name__ == "__main__":
    app.run()

