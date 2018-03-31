"""Tests for `qnet_qsd` package."""

import pytest
from pkg_resources import parse_version

import qnet_qsd


def test_valid_version():
    """Check that the package defines a valid __version__"""
    assert parse_version(qnet_qsd.__version__) >= parse_version("0.1.0")
