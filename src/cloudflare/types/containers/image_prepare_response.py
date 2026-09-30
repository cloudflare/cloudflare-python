# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ImagePrepareResponse"]


class ImagePrepareResponse(BaseModel):
    """Durable preparation state for a container image."""

    image: str
    """Image url."""

    status: Literal["pending", "ready", "error"]
    """Current durable preparation state for a container image."""

    artifact_digest: Optional[str] = None
    """Digest of the prepared runtime artifact when status is ready."""

    reason: Optional[str] = None
    """Human-readable pending or terminal error detail."""
