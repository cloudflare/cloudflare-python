# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["BrowserProtocolResponse", "Domain", "Version"]


class Domain(BaseModel):
    domain: str
    """Domain name."""

    commands: Optional[List[Dict[str, Optional[object]]]] = None
    """Available commands."""

    dependencies: Optional[List[str]] = None
    """Domain dependencies."""

    events: Optional[List[Dict[str, Optional[object]]]] = None
    """Available events."""

    experimental: Optional[bool] = None
    """Whether this domain is experimental."""

    types: Optional[List[Dict[str, Optional[object]]]] = None
    """Type definitions."""


class Version(BaseModel):
    """Protocol version."""

    major: str
    """Major version."""

    minor: str
    """Minor version."""


class BrowserProtocolResponse(BaseModel):
    domains: List[Domain]
    """List of protocol domains."""

    version: Optional[Version] = None
    """Protocol version."""
