# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .authenticated_origin_pull import AuthenticatedOriginPull

__all__ = ["HostnameUpdateResponse"]

HostnameUpdateResponse: TypeAlias = List[AuthenticatedOriginPull]
