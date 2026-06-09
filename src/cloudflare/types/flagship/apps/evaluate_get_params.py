# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EvaluateGetParams"]


class EvaluateGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID."""

    flag_key: Required[Annotated[str, PropertyInfo(alias="flagKey")]]
    """The flag key to evaluate."""

    targeting_key: Annotated[str, PropertyInfo(alias="targetingKey")]
    """
    Context targeting key (per OpenFeature spec); used for percentage rollout
    bucketing.
    """
