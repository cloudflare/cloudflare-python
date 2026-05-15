# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ......_models import BaseModel

__all__ = ["ItemEditResponse"]


class ItemEditResponse(BaseModel):
    id: str
    """The unique ID of the TCP Flow Protection rule."""

    burst_sensitivity: str
    """The burst sensitivity. Must be one of 'low', 'medium', 'high'."""

    created_on: datetime
    """The creation timestamp of the TCP Flow Protection rule."""

    mode: str
    """The mode for TCP Flow Protection.

    Must be one of 'enabled', 'disabled', 'monitoring'.
    """

    modified_on: datetime
    """The last modification timestamp of the TCP Flow Protection rule."""

    name: str
    """The name of the TCP Flow Protection rule.

    Value is relative to the 'scope' setting. For 'global' scope, name should be
    'global'. For either the 'region' or 'datacenter' scope, name should be the
    actual name of the region or datacenter, e.g., 'wnam' or 'lax'.
    """

    rate_sensitivity: str
    """The rate sensitivity. Must be one of 'low', 'medium', 'high'."""

    scope: str
    """The scope for the TCP Flow Protection rule.

    Must be one of 'global', 'region', or 'datacenter'.
    """
