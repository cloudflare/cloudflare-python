# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["IntegrationListResponse"]


class IntegrationListResponse(BaseModel):
    id: str
    """The id of the integration, a UUIDv4."""

    account_tag: str
    """The Cloudflare account tag."""

    active: bool
    """Whether this integration is enabled and should export changes in risk score."""

    created_at: datetime
    """When the integration was created in RFC3339 format."""

    integration_type: Literal["Okta"]

    reference_id: str
    """
    A reference ID defined by the client. Should be set to the Access-Okta IDP
    integration ID. Useful when the risk-score integration needs to be associated
    with a secondary asset and recalled using that ID.
    """

    tenant_url: str
    """The base URL for the tenant. E.g. "https://tenant.okta.com" """

    well_known_url: str
    """The URL for the Shared Signals Framework configuration, e.g.

    "/.well-known/sse-configuration/{integration_uuid}/".
    https://openid.net/specs/openid-sse-framework-1_0.html#rfc.section.6.2.1
    """
