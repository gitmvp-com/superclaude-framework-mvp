#!/usr/bin/env python3
"""
SuperClaude MVP CLI
Main command-line interface
"""

import typer
from rich.console import Console
from rich.table import Table
from pathlib import Path
from typing import Optional

from superclaude_mvp.commands.help import show_help
from superclaude_mvp import __version__

# Initialize CLI app and console
app = typer.Typer(
    name="superclaude-mvp",
    help="SuperClaude MVP - A simplified CLI framework for development assistance",
    add_completion=False,
)
console = Console()


def version_callback(value: bool):
    """Display version information"""
    if value:
        console.print(f"[bold blue]SuperClaude MVP[/bold blue] version [green]{__version__}[/green]")
        console.print("[dim]Based on SuperClaude Framework[/dim]")
        raise typer.Exit()


@app.callback()
def callback(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit"
    )
):
    """SuperClaude MVP - A simplified CLI framework"""
    pass


@app.command()
def help():
    """
    Show detailed help information
    """
    show_help()


@app.command()
def info():
    """
    Display information about SuperClaude MVP
    """
    console.print("\n[bold blue]SuperClaude MVP[/bold blue]\n")
    
    # Create info table
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="white")
    
    table.add_row("Version", __version__)
    table.add_row("Type", "Minimal Viable Product")
    table.add_row("Based On", "SuperClaude Framework")
    table.add_row("License", "MIT")
    
    console.print(table)
    console.print("\n[dim]This is a simplified demonstration of the SuperClaude Framework concept.[/dim]\n")
    console.print("[yellow]Original Project:[/yellow] https://github.com/SuperClaude-Org/SuperClaude_Framework\n")


def main():
    """Main entry point"""
    app()


if __name__ == "__main__":
    main()
