# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Setting", "Value"]


class Value(BaseModel):
    """The NEL configuration value."""

    enabled: bool
    """Whether Network Error Logging is enabled for the zone.

    When enabled, browsers report network errors to Cloudflare's NEL endpoint.
    """


class Setting(BaseModel):
    """A zone-scoped NEL configuration setting."""

    id: Literal["nel"]
    """Zone setting identifier."""

    editable: bool
    """Whether the setting is editable.

    This is false when the zone's plan does not include NEL or the NEL product
    feature is not enabled.
    """

    modified_on: datetime
    """When the setting was last modified.

    A zero value (0001-01-01T00:00:00Z) indicates the setting has never been
    explicitly set and is using the default value.
    """

    value: Value
    """The NEL configuration value."""
