#!/usr/bin/env python3
"""
Help command implementation
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()


def show_help():
    """
    Display comprehensive help information
    """
    
    # Title
    console.print("\n[bold blue]SuperClaude MVP - Help[/bold blue]\n")
    
    # Overview
    overview = """
SuperClaude MVP is a simplified version of the SuperClaude Framework.
It demonstrates the core concept of a command-based CLI tool for development assistance.
"""
    console.print(Panel(overview.strip(), title="Overview", border_style="blue"))
    
    # Available Commands
    console.print("\n[bold cyan]Available Commands:[/bold cyan]\n")
    
    commands_table = Table(show_header=True, header_style="bold magenta", box=None)
    commands_table.add_column("Command", style="green", width=20)
    commands_table.add_column("Description", style="white")
    
    commands_table.add_row("help", "Show this help information")
    commands_table.add_row("info", "Display information about SuperClaude MVP")
    commands_table.add_row("--version, -v", "Show version and exit")
    commands_table.add_row("--help", "Show command-line help")
    
    console.print(commands_table)
    
    # Usage Examples
    console.print("\n[bold cyan]Usage Examples:[/bold cyan]\n")
    
    examples = [
        ("Show version", "superclaude-mvp --version"),
        ("Get help", "superclaude-mvp help"),
        ("Show info", "superclaude-mvp info"),
        ("Command help", "superclaude-mvp --help"),
    ]
    
    for description, command in examples:
        console.print(f"  [yellow]•[/yellow] {description}:")
        console.print(f"    [dim]$[/dim] [green]{command}[/green]\n")
    
    # Installation
    console.print("[bold cyan]Installation:[/bold cyan]\n")
    console.print("  [green]pip install -e .[/green]  # From source")
    console.print("  [green]pipx install .[/green]   # Using pipx (recommended)\n")
    
    # Links
    console.print("[bold cyan]Links:[/bold cyan]\n")
    console.print("  [blue]Original Project:[/blue] https://github.com/SuperClaude-Org/SuperClaude_Framework")
    console.print("  [blue]Documentation:[/blue] https://superclaude.netlify.app/\n")
