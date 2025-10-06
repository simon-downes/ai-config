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

# ANSI color codes
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"


def resolve_sources(sources: List[str]) -> List[str]:
    """Resolve source patterns into actual file paths.

    Args:
        sources: List of source patterns (files, directories, URLs, globs).

    Returns:
        List of resolved file paths ready for fetching.
    """
    if not sources:
        print(f"{YELLOW}WARNING{RESET}: No sources specified in config")
        return []

    print(f"{CYAN}Processing sources...{RESET}")
    files = []
    for source in sources:
        print(f"- {source}")
        if source.startswith(("http://", "https://")):
            # Convert GitHub URLs to raw content URLs
            if "github.com" in source and "/blob/" in source:
                source = source.replace(
                    "github.com", "raw.githubusercontent.com"
                ).replace("/blob/", "/")
            files.append(source)
        else:
            path = Path(source).expanduser()
            if path.is_dir():
                count = 0
                for i, p in enumerate(path.rglob("*.md")):
                    if i >= DEFAULT_FILE_LIMIT:
                        print(
                            f"  {YELLOW}WARNING{RESET}: Directory hit file limit ({DEFAULT_FILE_LIMIT})"
                        )
                        break
                    files.append(str(p))
                    count += 1
                print(f"  Found {count} files in directory")
            elif "*" in source or "?" in source:
                count = 0
                for i, p in enumerate(glob.iglob(source, recursive=True)):
                    if i >= DEFAULT_FILE_LIMIT:
                        print(
                            f"  {YELLOW}WARNING{RESET}: Glob pattern hit file limit ({DEFAULT_FILE_LIMIT})"
                        )
                        break
                    files.append(p)
                    count += 1
                print(f"  Found {count} files matching pattern")
            else:
                if path.exists():
                    files.append(str(path))
                else:
                    print(f"  {YELLOW}WARNING{RESET}: File not found")

    if files:
        print(f"\n{GREEN}SUCCESS{RESET}: Resolved {len(files)} files total\n")
    else:
        print(f"{YELLOW}WARNING{RESET}: No files resolved from sources")

    return files


def fetch(files: List[str], output_dir: str) -> None:
    """Copy or download files to output directory.

    Args:
        files: List of file paths to copy/download.
        output_dir: Target directory for copied files.
    """

    if not files:
        return

    output_path = Path(output_dir).expanduser()
    output_path.mkdir(parents=True, exist_ok=True)
    print(f"{CYAN}Copying files to: {MAGENTA}{output_path}{RESET}")

    for file_path in files:
        if file_path.startswith(("http://", "https://")):
            filename = Path(file_path).name
            print(f"- {filename}")
            try:
                urlretrieve(file_path, output_path / filename)
            except Exception as e:
                print(f"  {YELLOW}WARNING{RESET}: Failed to download {file_path}: {e}")
        else:
            source_path = Path(file_path)
            print(f"- {source_path.name}")
            try:
                shutil.copy2(source_path, output_path / source_path.name)
            except Exception as e:
                print(f"  {YELLOW}WARNING{RESET}: Failed to copy {file_path}: {e}")


def load_config(config_path: str) -> tuple[List[str], str]:
    """Load configuration from YAML file.

    Args:
        config_path: Path to YAML configuration file.

    Returns:
        Tuple of (sources list, output directory path).

    Raises:
        SystemExit: If config is invalid or output directory is not writable.
    """
    try:
        with open(config_path) as f:
            config = yaml.safe_load(f)

        if not config["sources"]:
            print(f"{RED}ERROR{RESET}: No sources specified in config")
            sys.exit(1)

        if not isinstance(config["sources"], list):
            print(f"{RED}ERROR{RESET}: Sources must be a list")
            sys.exit(1)

        # Check output directory exists and is writable
        output_path = Path(config["output"]).expanduser()
        if not output_path.exists():
            print(f"{RED}ERROR{RESET}: Output directory does not exist: {output_path}")
            sys.exit(1)

        if not output_path.is_dir():
            print(f"{RED}ERROR{RESET}: Output path is not a directory: {output_path}")
            sys.exit(1)

        # Test write permission
        test_file = output_path / ".write_test"
        test_file.touch()
        test_file.unlink()

        return config["sources"], config["output"]

    except FileNotFoundError:
        print(f"{RED}ERROR{RESET}: Config file not found: {config_path}")
        sys.exit(1)
    except KeyError as e:
        print(f"{RED}ERROR{RESET}: Missing required key in config: {e}")
        sys.exit(1)
    except (PermissionError, OSError) as e:
        print(
            f"{RED}ERROR{RESET}: Cannot write to output directory: {output_path} ({e})"
        )
        sys.exit(1)


def main() -> None:
    """Main entry point for the fetch-rules command."""
    parser = argparse.ArgumentParser(description="Fetch files based on YAML config")
    parser.add_argument(
        "config",
        nargs="?",
        default=str(Path.home() / ".agent-rules.yaml"),
        help="Path to config file (default: ~/.agent-rules.yaml)",
    )
    args = parser.parse_args()

    sources, output_dir = load_config(args.config)
    files = resolve_sources(sources)
    fetch(files, output_dir)

    print(f"\n{GREEN}All Done!{RESET}")


if __name__ == "__main__":
    main()
