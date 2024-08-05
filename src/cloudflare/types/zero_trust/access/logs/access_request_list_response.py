# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .access_requests import AccessRequests

__all__ = ["AccessRequestListResponse"]

AccessRequestListResponse: TypeAlias = List[AccessRequests]
