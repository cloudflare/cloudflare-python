# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DeploymentListParams"]


class DeploymentListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    env: Literal["production", "preview"]
    """What type of deployments to fetch."""
