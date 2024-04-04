# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UnnamedSchemaRefFda1c6f6758e763ae3b2964521f2fdd8Param"]


class UnnamedSchemaRefFda1c6f6758e763ae3b2964521f2fdd8Param(TypedDict, total=False):
    workers_message: Annotated[str, PropertyInfo(alias="workers/message")]
    """Human-readable message about the deployment."""
