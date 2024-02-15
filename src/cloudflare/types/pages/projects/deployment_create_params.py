# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["DeploymentCreateParams"]


class DeploymentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    branch: str
    """The branch to build the new deployment from.

    The `HEAD` of the branch will be used. If omitted, the production branch will be
    used by default.
    """
