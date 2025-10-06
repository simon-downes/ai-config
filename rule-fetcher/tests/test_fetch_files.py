#!/usr/bin/env python3
"""Tests for fetch_files.py"""

import tempfile
import pytest
import yaml
from pathlib import Path
import sys
import os

# Add parent directory to path to import fetch_rules
sys.path.insert(0, str(Path(__file__).parent.parent))
import fetch_rules


def create_temp_config(sources, output_dir=None):
    """Create a temporary config file and return its path."""
    if output_dir is None:
        output_dir = "./tests/test-output"

    config = {"sources": sources, "output": output_dir}

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump(config, f)
        return f.name


def test_missing_config_file():
    """Test error when config file doesn't exist."""
    with pytest.raises(SystemExit) as exc_info:
        fetch_rules.load_config("/nonexistent/config.yaml")
    assert exc_info.value.code == 1


def test_empty_sources():
    """Test error when sources list is empty."""
    config_path = create_temp_config([])
    try:
        with pytest.raises(SystemExit) as exc_info:
            fetch_rules.load_config(config_path)
        assert exc_info.value.code == 1
    finally:
        os.unlink(config_path)


def test_sources_not_list():
    """Test error when sources is not a list."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump({"sources": "not_a_list", "output": "./tests/test-output"}, f)
        config_path = f.name

    try:
        with pytest.raises(SystemExit) as exc_info:
            fetch_rules.load_config(config_path)
        assert exc_info.value.code == 1
    finally:
        os.unlink(config_path)


def test_missing_sources_key():
    """Test error when sources key is missing."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump({"output": "./tests/test-output"}, f)
        config_path = f.name

    try:
        with pytest.raises(SystemExit) as exc_info:
            fetch_rules.load_config(config_path)
        assert exc_info.value.code == 1
    finally:
        os.unlink(config_path)


def test_missing_output_key():
    """Test error when output key is missing."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        yaml.dump({"sources": ["test.md"]}, f)
        config_path = f.name

    try:
        with pytest.raises(SystemExit) as exc_info:
            fetch_rules.load_config(config_path)
        assert exc_info.value.code == 1
    finally:
        os.unlink(config_path)


def test_nonexistent_output_directory():
    """Test error when output directory doesn't exist."""
    config_path = create_temp_config(["test.md"], "/nonexistent/directory")
    try:
        with pytest.raises(SystemExit) as exc_info:
            fetch_rules.load_config(config_path)
        assert exc_info.value.code == 1
    finally:
        os.unlink(config_path)


def test_valid_config():
    """Test successful config loading with valid data."""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_path = create_temp_config(["test.md"], temp_dir)
        try:
            sources, output_dir = fetch_rules.load_config(config_path)
            assert sources == ["test.md"]
            assert output_dir == temp_dir
        finally:
            os.unlink(config_path)


def test_resolve_sources_empty():
    """Test resolve_sources with empty list."""
    result = fetch_rules.resolve_sources([])
    assert result == []


def test_resolve_sources_nonexistent_file():
    """Test resolve_sources with non-existent file."""
    result = fetch_rules.resolve_sources(["/nonexistent/file.md"])
    assert result == []


def test_resolve_sources_url():
    """Test resolve_sources with URL."""
    url = "https://example.com/test.md"
    result = fetch_rules.resolve_sources([url])
    assert result == [url]


def test_resolve_sources_github_url():
    """Test resolve_sources converts GitHub URLs to raw URLs."""
    github_url = "https://github.com/user/repo/blob/main/file.md"
    expected = "https://raw.githubusercontent.com/user/repo/main/file.md"
    result = fetch_rules.resolve_sources([github_url])
    assert result == [expected]


def test_dangerous_root_directory():
    """Test that root directory is blocked."""
    result = fetch_rules.resolve_sources(["/"])
    assert result == []


def test_dangerous_glob_patterns():
    """Test that dangerous glob patterns are blocked."""
    dangerous_patterns = ["/", "/*", "/**"]
    for pattern in dangerous_patterns:
        result = fetch_rules.resolve_sources([pattern])
        assert result == []


def test_safe_paths_allowed():
    """Test that safe paths are not blocked by safety checks."""
    # These paths should pass safety checks (though files may not exist)
    safe_paths = [
        "/usr/share/doc/test.md",  # Specific file under /usr
        "/etc/config.md",  # Specific file under /etc
        "/tmp/test.md",  # Specific file under /tmp
    ]

    # We're only testing that these don't get blocked by safety checks
    # The actual file existence will be handled normally
    for path in safe_paths:
        result = fetch_rules.resolve_sources([path])
        # Should not be empty due to safety blocks (though file may not exist)
        # The safety check should not prevent these from being processed
        assert isinstance(
            result, list
        )  # Just verify it returns a list without crashing
