# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Logging"]


class Logging(BaseModel):
    """An object configuring the rule's logging behavior."""

    enabled: bool
    """Whether to generate a log when the rule matches."""
