# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

__all__ = ["AllowedMethods"]

AllowedMethods = Literal["GET", "POST", "HEAD", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]

AllowedHTTPMethodsParam = List[AllowedMethods]
