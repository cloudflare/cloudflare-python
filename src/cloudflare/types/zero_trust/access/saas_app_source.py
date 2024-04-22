# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel

__all__ = ["SaasAppSource"]


class SaasAppSource(BaseModel):
    name: Optional[str] = None
    """The name of the IdP attribute."""

    name_by_idp: Optional[Dict[str, str]] = None
    """A mapping from IdP ID to attribute name."""
