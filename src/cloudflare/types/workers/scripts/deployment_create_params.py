# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .unnamed_schema_ref_fda1c6f6758e763ae3b2964521f2fdd8_param import (
    UnnamedSchemaRefFda1c6f6758e763ae3b2964521f2fdd8Param,
)

__all__ = ["DeploymentCreateParams"]


class DeploymentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    annotations: UnnamedSchemaRefFda1c6f6758e763ae3b2964521f2fdd8Param

    strategy: str
