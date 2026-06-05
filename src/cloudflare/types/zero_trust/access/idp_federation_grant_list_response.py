# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .idp_federation_grant import IdPFederationGrant

__all__ = ["IdPFederationGrantListResponse"]

IdPFederationGrantListResponse: TypeAlias = List[IdPFederationGrant]
