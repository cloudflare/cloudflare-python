# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["IntegrationCreateParams"]


class IntegrationCreateParams(TypedDict, total=False):
    account_id: Required[str]

    integration_type: Required[Literal["Okta"]]

    tenant_url: Required[str]
    """The base url of the tenant, e.g. "https://tenant.okta.com" """

    reference_id: Optional[str]
    """A reference id that can be supplied by the client.

    Currently this should be set to the Access-Okta IDP ID (a UUIDv4).
    https://developers.cloudflare.com/api/operations/access-identity-providers-get-an-access-identity-provider
    """
