#!/usr/bin/env -S uv run python
"""Watch for changes in Jupyter notebooks and convert them to Markdown."""

import sys
import time
import subprocess
from pathlib import Path
import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

console = Console()
app = typer.Typer(help="Watch and convert Jupyter notebooks to Markdown")


class NotebookHandler(FileSystemEventHandler):
    def __init__(self, output_dir):
        self.last_modified = {}
        self.output_dir = output_dir
        
    def on_modified(self, event):
        if event.is_directory:
            return
            
        path = Path(event.src_path)
        if path.suffix == '.ipynb' and not path.name.startswith('.'):
            # Debounce - ignore if modified within last 2 seconds
            current_time = time.time()
            if path in self.last_modified:
                if current_time - self.last_modified[path] < 2:
                    return
            self.last_modified[path] = current_time
            
            self.convert_notebook(path)
    
    def convert_notebook(self, notebook_path, show_status=True):
        """Convert a notebook to markdown using the convert.py script."""
        output_path = self.output_dir / notebook_path.with_suffix('.md').name
        
        if show_status:
            with console.status(f"[cyan]Converting {notebook_path.name}...[/cyan]"):
                try:
                    result = subprocess.run(
                        [sys.executable, "convert.py", "file", str(notebook_path), "-o", str(output_path)],
                        capture_output=True,
                        text=True
                    )
                    if result.returncode == 0:
                        console.print(f"[green]✓[/green] Converted [blue]{notebook_path.name}[/blue] → [green]{output_path.relative_to(notebook_path.parent)}[/green]")
                    else:
                        console.print(f"[red]✗[/red] Error converting [blue]{notebook_path.name}[/blue]: {result.stderr}")
                except Exception as e:
                    console.print(f"[red]✗[/red] Error converting [blue]{notebook_path.name}[/blue]: {e}")
        else:
            try:
                result = subprocess.run(
                    [sys.executable, "convert.py", "file", str(notebook_path), "-o", str(output_path)],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    console.print(f"[green]✓[/green] Converted [blue]{notebook_path.name}[/blue] → [green]{output_path.relative_to(notebook_path.parent)}[/green]")
                else:
                    console.print(f"[red]✗[/red] Error converting [blue]{notebook_path.name}[/blue]: {result.stderr}")
            except Exception as e:
                console.print(f"[red]✗[/red] Error converting [blue]{notebook_path.name}[/blue]: {e}")


@app.command()
def watch(
    directory: Path = typer.Argument(Path("."), help="Directory to watch for notebook changes"),
    output: Path = typer.Option(None, "--output", "-o", help="Output directory for markdown files (default: <directory>/md)")
):
    """Watch for Jupyter notebook changes and convert them to Markdown."""
    watch_dir = directory.resolve()
    output_dir = output if output else watch_dir / 'md'
    output_dir.mkdir(exist_ok=True)
    
    # Display header
    console.print(Panel.fit(
        f"[bold cyan]Notebook Watcher[/bold cyan]\n"
        f"Watching: [yellow]{watch_dir}[/yellow]\n"
        f"Output: [green]{output_dir}[/green]",
        border_style="cyan"
    ))
    
    # Convert existing notebooks
    notebooks = list(watch_dir.glob('*.ipynb'))
    notebooks = [nb for nb in notebooks if not nb.name.startswith('.')]
    
    if notebooks:
        console.print(f"\n[cyan]Found {len(notebooks)} existing notebook(s)[/cyan]")
        handler = NotebookHandler(output_dir)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Converting notebooks...", total=len(notebooks))
            for notebook in notebooks:
                handler.convert_notebook(notebook, show_status=False)
                progress.advance(task)
    
    # Set up file watcher
    console.print("\n[cyan]Watching for changes... Press [bold]Ctrl+C[/bold] to stop[/cyan]\n")
    
    event_handler = NotebookHandler(output_dir)
    observer = Observer()
    observer.schedule(event_handler, str(watch_dir), recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        console.print("\n[yellow]Stopped watching for changes.[/yellow]")
    observer.join()


if __name__ == "__main__":
    app()