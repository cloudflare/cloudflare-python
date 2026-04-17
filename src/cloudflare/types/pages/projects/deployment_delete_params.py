# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DeploymentDeleteParams"]


class DeploymentDeleteParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    project_name: Required[str]
    """Name of the project."""

    force: bool
    """
    Allow deletion of aliased non-production deployments when a normal delete would
    be rejected.
    """
