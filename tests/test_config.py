import os

import pytest

from src.config import get_required_env, mask, build_connection_label


def test_get_required_env_returns_value(monkeypatch):
    monkeypatch.setenv("TEAM", "platform")
    assert get_required_env("TEAM") == "platform"


def test_get_required_env_raises_when_missing(monkeypatch):
    monkeypatch.delenv("MISSING_VAR", raising=False)
    with pytest.raises(KeyError):
        get_required_env("MISSING_VAR")


def test_mask_hides_all_but_prefix():
    assert mask("supersecretvalue") == "supe************"


def test_mask_hides_short_values_entirely():
    assert mask("abc") == "***"


def test_build_connection_label_combines_env_and_region():
    assert build_connection_label("staging", "us-east-1") == "staging-us-east-1"
