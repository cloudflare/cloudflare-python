# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["DeploymentGroupEditParams", "VersionConfig"]


class DeploymentGroupEditParams(TypedDict, total=False):
    account_id: Required[str]

    name: str
    """A user-friendly name for the deployment group."""

    policy_ids: SequenceNotStr[str]
    """Replaces the entire list of policy IDs."""

    version_config: Iterable[VersionConfig]
    """Replaces the entire version_config array."""


class VersionConfig(TypedDict, total=False):
    target_environment: Required[Optional[str]]
    """The target environment for the client version (e.g., windows, macos)."""

    version: Required[str]
    """The specific client version to deploy."""
