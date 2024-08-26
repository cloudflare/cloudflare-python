# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from .associated_hostnames import AssociatedHostnames

__all__ = ["Certificate"]


class Certificate(BaseModel):
    id: Optional[str] = None
    """The ID of the application that will use this certificate."""

    associated_hostnames: Optional[List[AssociatedHostnames]] = None
    """The hostnames of the applications that will use this certificate."""

    created_at: Optional[datetime] = None

    expires_on: Optional[datetime] = None

    fingerprint: Optional[str] = None
    """The MD5 fingerprint of the certificate."""

    name: Optional[str] = None
    """The name of the certificate."""

    updated_at: Optional[datetime] = None
