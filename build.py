from pathlib import Path
from shutil import copytree

from app import app


def build():
    root = Path(__file__).resolve().parent
    output = root / "dist"
    output.mkdir(exist_ok=True)

    pages = {"/": "index.html", "/projects": "projects.html", "/resume": "resume.html"}
    with app.test_client() as client:
        for route, filename in pages.items():
            response = client.get(route)
            if response.status_code != 200:
                raise RuntimeError(f"Could not build {route}: HTTP {response.status_code}")
            (output / filename).write_bytes(response.data)

    copytree(app.static_folder, output / "static", dirs_exist_ok=True)


if __name__ == "__main__":
    build()
