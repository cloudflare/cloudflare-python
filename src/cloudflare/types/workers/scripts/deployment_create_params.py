# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .deployment_param import DeploymentParam

__all__ = ["DeploymentCreateParams"]


class DeploymentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    force: bool
    """
    If set to true, the deployment will be created even if normally blocked by
    something such rolling back to an older version when a secret has changed.
    """

    annotations: DeploymentParam

    strategy: str
