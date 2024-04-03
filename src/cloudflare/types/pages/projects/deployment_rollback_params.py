# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DeploymentRollbackParams"]


class DeploymentRollbackParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    project_name: Required[str]
    """Name of the project."""

    body: Required[object]
