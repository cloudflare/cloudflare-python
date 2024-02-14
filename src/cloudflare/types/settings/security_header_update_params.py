# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["SecurityHeaderUpdateParams", "Value", "ValueStrictTransportSecurity"]


class SecurityHeaderUpdateParams(TypedDict, total=False):
    value: Required[Value]


class ValueStrictTransportSecurity(TypedDict, total=False):
    enabled: bool
    """Whether or not strict transport security is enabled."""

    include_subdomains: bool
    """Include all subdomains for strict transport security."""

    max_age: float
    """Max age in seconds of the strict transport security."""

    nosniff: bool
    """Whether or not to include 'X-Content-Type-Options: nosniff' header."""


class Value(TypedDict, total=False):
    strict_transport_security: ValueStrictTransportSecurity
    """Strict Transport Security."""
