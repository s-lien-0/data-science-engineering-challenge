import pytest
import subprocess
import os

def test_cli_runs_with_default_config():
    result = subprocess.run(
        ["python", "cli.py", "--config", "config/default_config.json"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
