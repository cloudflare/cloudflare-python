# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DeploymentCreateParams", "Annotations"]


class DeploymentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    annotations: Annotations

    strategy: str


class Annotations(TypedDict, total=False):
    workers_message: Annotated[str, PropertyInfo(alias="workers/message")]
    """Human-readable message about the deployment."""
