import typer
import json
import os
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()
DB_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(DB_FILE): return []
    with open(DB_FILE, 'r') as f: return json.load(f)

def save_tasks(tasks):
    with open(DB_FILE, 'w') as f: json.dump(tasks, f, indent=2)

@app.command()
def add(title: str):
    """Add a new task"""
    tasks = load_tasks()
    new_id = 1 if not tasks else max(t['id'] for t in tasks) + 1
    tasks.append({'id': new_id, 'title': title, 'status': 'pending'})
    save_tasks(tasks)
    console.print(f'[green]Task added: {title}[/green]')

@app.command()
def list():
    """List all tasks"""
    tasks = load_tasks()
    table = Table('ID', 'Title', 'Status')
    for t in tasks:
        color = 'green' if t['status'] == 'completed' else 'yellow'
        table.add_row(str(t['id']), t['title'], f'[{color}]{t["status"]}[/{color}]')
    console.print(table)

@app.command()
def delete(id: int):
    """Delete a task"""
    tasks = load_tasks()  # <--- THIS WAS MISSING
    filtered = [t for t in tasks if t['id'] != id]
    if len(tasks) == len(filtered):
        console.print(f'[red]Task {id} not found.[/red]')
    else:
        save_tasks(filtered)
        console.print(f'[red]Deleted task {id}[/red]')

@app.command()
def complete(id: int):
    """Complete a task"""
    tasks = load_tasks()
    found = False
    for t in tasks:
        if t['id'] == id: 
            t['status'] = 'completed'
            found = True
    if found:
        save_tasks(tasks)
        console.print(f'[green]Task {id} completed[/green]')
    else:
        console.print(f'[red]Task {id} not found[/red]')

if __name__ == '__main__':
    app()
