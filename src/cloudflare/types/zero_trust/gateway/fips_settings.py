# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["FipsSettings"]


class FipsSettings(BaseModel):
    tls: Optional[bool] = None
    """Enable only cipher suites and TLS versions compliant with FIPS 140-2."""
