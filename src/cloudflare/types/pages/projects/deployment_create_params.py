# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DeploymentCreateParams"]


class DeploymentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    branch: str
    """The branch to build the new deployment from.

    The `HEAD` of the branch will be used. If omitted, the production branch will be
    used by default.
    """
