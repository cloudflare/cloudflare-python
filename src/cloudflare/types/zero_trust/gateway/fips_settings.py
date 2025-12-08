# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["FipsSettings"]


class FipsSettings(BaseModel):
    """Specify FIPS settings."""

    tls: Optional[bool] = None
    """Enforce cipher suites and TLS versions compliant with FIPS 140-2."""
