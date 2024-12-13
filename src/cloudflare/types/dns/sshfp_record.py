# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SSHFPRecord", "Data"]


class Data(BaseModel):
    algorithm: Optional[float] = None
    """algorithm."""

    fingerprint: Optional[str] = None
    """fingerprint."""

    type: Optional[float] = None
    """type."""


class SSHFPRecord(BaseModel):
    content: Optional[str] = None
    """Formatted SSHFP content. See 'data' to set SSHFP properties."""

    data: Optional[Data] = None
    """Components of a SSHFP record."""

    type: Optional[Literal["SSHFP"]] = None
    """Record type."""
