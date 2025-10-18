# SuperClaude Framework MVP

### A Simplified CLI Tool for AI Development Assistance

## 🎯 Overview

This is a minimal viable product (MVP) version of the [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework). It demonstrates the core concept of a command-based CLI tool for enhancing development workflows.

## ✨ Features

This MVP includes:

- **CLI Interface**: Simple command-line tool built with Typer and Rich
- **Command System**: Extensible command structure
- **Help Command**: Built-in documentation
- **Version Management**: Version tracking and display

## 🚀 Quick Installation

### Using pip

```bash
pip install -e .
```

### Using pipx (Recommended)

```bash
pipx install .
```

## 📖 Usage

### Check Version

```bash
superclaude-mvp --version
```

### Get Help

```bash
superclaude-mvp --help
```

### Run Help Command

```bash
superclaude-mvp help
```

### Run Info Command

```bash
superclaude-mvp info
```

## 🏗️ Project Structure

```
superclaude-framework-mvp/
├── superclaude_mvp/
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # Entry point for python -m
│   ├── cli.py               # CLI application logic
│   └── commands/
│       ├── __init__.py
│       └── help.py          # Help command implementation
├── pyproject.toml           # Project configuration
├── setup.py                 # Setup file
├── VERSION                  # Version file
└── README.md               # This file
```

## 🔧 Technical Details

### Dependencies

This MVP uses the same core dependencies as the parent project:

- **typer>=0.9.0**: Modern CLI framework
- **rich>=13.0.0**: Beautiful terminal output
- **click>=8.0.0**: Command-line interface creation
- **pyyaml>=6.0.0**: YAML parsing

### Python Version

Requires Python 3.8 or higher

## 🎨 Differences from Full Framework

This MVP is simplified to focus on core concepts:

| Full Framework | MVP |
|----------------|-----|
| 26 commands | 2 commands (help, info) |
| 16 specialized agents | No agents |
| 7 behavioral modes | No modes |
| 8 MCP servers | No integrations |
| Complex installation | Simple pip install |
| Multi-file command system | Single command file |

## 🚀 Extending the MVP

To add new commands:

1. Create a new file in `superclaude_mvp/commands/`
2. Define your command function
3. Import and register it in `cli.py`

Example:

```python
# superclaude_mvp/commands/greet.py
import typer
from rich.console import Console

console = Console()

def greet_command(name: str = "World"):
    """Greet someone"""
    console.print(f"[green]Hello, {name}![/green]")
```

## 📝 License

MIT License - same as the original SuperClaude Framework

## 🙏 Acknowledgments

Based on the [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) by NomenAK and Mithun Gowda B.

## 🔗 Links

- Original Project: https://github.com/SuperClaude-Org/SuperClaude_Framework
- Documentation: https://superclaude.netlify.app/
