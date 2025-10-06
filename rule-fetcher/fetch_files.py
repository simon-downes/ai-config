#!/usr/bin/env python3
"""File fetcher script that copies/downloads files based on YAML configuration."""

import argparse
import glob
import shutil
import sys
from pathlib import Path
from typing import List
from urllib.request import urlretrieve

import yaml

DEFAULT_FILE_LIMIT = 25


def resolve_sources(sources: List[str]) -> List[str]:
    """Resolve source patterns into actual file paths."""
    files = []
    for source in sources:
        if source.startswith(("http://", "https://")):
            # Convert GitHub URLs to raw content URLs
            if "github.com" in source and "/blob/" in source:
                source = source.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            files.append(source)
        else:
            path = Path(source).expanduser()
            if path.is_dir():
                for i, p in enumerate(path.rglob("*.md")):
                    if i >= DEFAULT_FILE_LIMIT:
                        break
                    files.append(str(p))
            elif "*" in source or "?" in source:
                for i, p in enumerate(glob.iglob(source, recursive=True)):
                    if i >= DEFAULT_FILE_LIMIT:
                        break
                    files.append(p)
            else:
                files.append(str(path))
    return files


def fetch(files: List[str], output_dir: str) -> None:
    """Copy or download files to output directory."""
    output_path = Path(output_dir).expanduser()
    output_path.mkdir(parents=True, exist_ok=True)
    
    for file_path in files:
        if file_path.startswith(("http://", "https://")):
            filename = Path(file_path).name
            urlretrieve(file_path, output_path / filename)
        else:
            source_path = Path(file_path)
            if source_path.exists():
                shutil.copy2(source_path, output_path / source_path.name)


def load_config(config_path: str) -> tuple[List[str], str]:
    """Load configuration from YAML file."""
    try:
        with open(config_path) as f:
            config = yaml.safe_load(f)
        return config["sources"], config["output"]
    except FileNotFoundError:
        print(f"Config file not found: {config_path}", file=sys.stderr)
        sys.exit(1)
    except KeyError as e:
        print(f"Missing required key in config: {e}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Fetch files based on YAML config")
    parser.add_argument(
        "config", 
        nargs="?", 
        default=str(Path.home() / ".agent-rules.yaml"),
        help="Path to config file (default: ~/.agent-rules.yaml)"
    )
    args = parser.parse_args()
    
    sources, output_dir = load_config(args.config)
    files = resolve_sources(sources)
    fetch(files, output_dir)


if __name__ == "__main__":
    main()
