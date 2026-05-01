# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["DeploymentGroupCreateParams", "VersionConfig"]


class DeploymentGroupCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """A user-friendly name for the deployment group."""

    version_config: Required[Iterable[VersionConfig]]
    """Contains at least one version configuration."""

    policy_ids: SequenceNotStr[str]
    """Contains an optional list of policy IDs assigned to a group."""


class VersionConfig(TypedDict, total=False):
    target_environment: Required[Optional[str]]
    """The target environment for the client version (e.g., windows, macos)."""

    version: Required[str]
    """The specific client version to deploy."""
