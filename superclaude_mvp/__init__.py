#!/usr/bin/env python3
"""
SuperClaude MVP - Minimal Viable Product
A simplified version demonstrating core CLI concepts
"""

from pathlib import Path

# Read version from VERSION file
try:
    __version__ = (Path(__file__).parent.parent / "VERSION").read_text().strip()
except Exception:
    __version__ = "1.0.0"  # Fallback

__author__ = "SuperClaude MVP"
__license__ = "MIT"
