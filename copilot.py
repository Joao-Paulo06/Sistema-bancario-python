import shutil
from pathlib import Path
import typer

app = typer.Typer()

TEMPLATES_DIR = Path("project_templates")

@app.command()
def criar(projeto: str, destino: str = "."):
    modelo = TEMPLATES_DIR / projeto
    if not modelo.exists():
        typer.echo(f"Modelo '{projeto}' não encontrado.")
        raise typer.Exit()
    
    destino_path = Path(destino) / projeto
    shutil.copytree(modelo, destino_path)
    typer.echo(f"Projeto '{projeto}' criado em: {destino_path.resolve()}")

if __name__ == "__main__":
    app()
