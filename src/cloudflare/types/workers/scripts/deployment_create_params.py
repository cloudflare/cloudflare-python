# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Iterable

from .deployment_param import DeploymentParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

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
