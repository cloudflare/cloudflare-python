# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .deployment_param import DeploymentParam

__all__ = ["DeploymentCreateParams", "Version"]


class DeploymentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    strategy: Required[Literal["percentage"]]

    versions: Required[Iterable[Version]]

    force: bool
    """
    If set to true, the deployment will be created even if normally blocked by
    something such rolling back to an older version when a secret has changed.
    """

    annotations: DeploymentParam


class Version(TypedDict, total=False):
    percentage: Required[float]

    version_id: Required[str]
