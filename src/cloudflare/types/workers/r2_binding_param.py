# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

__all__ = ["R2BindingParam"]

class R2BindingParam(TypedDict, total=False):
    bucket_name: Required[str]
    """R2 bucket to bind to"""

    type: Required[Literal["r2_bucket"]]
    """The class of resource that the binding provides."""