# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DeploymentDeleteParams"]


class DeploymentDeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    project_name: Required[str]
    """Name of the Pages project.

    Must begin with a lowercase letter or digit and contain only lowercase letters,
    digits, and hyphens.
    """

    force: bool
    """Allow deletion when a non-production deployment has an active alias."""
