# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, TypeAlias

from typing import Union

__all__ = ["RewriteURIPartParam", "StaticValue", "DynamicValue"]

class StaticValue(TypedDict, total=False):
    value: Required[str]
    """Predefined replacement value."""

class DynamicValue(TypedDict, total=False):
    expression: Required[str]
    """Expression to evaluate for the replacement value."""

RewriteURIPartParam: TypeAlias = Union[StaticValue, DynamicValue]