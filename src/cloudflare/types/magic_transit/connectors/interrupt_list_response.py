# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["InterruptListResponse", "Reboot", "Restart", "Shutdown"]


class Reboot(BaseModel):
    purge: Optional[bool] = None
    """Purge connector state."""


class Restart(BaseModel):
    purge: Optional[bool] = None
    """Purge connector state."""


class Shutdown(BaseModel):
    purge: Optional[bool] = None
    """Purge connector state."""


class InterruptListResponse(BaseModel):
    """Interrupt action for a connector."""

    submitted_at: str

    reboot: Optional[Reboot] = None

    restart: Optional[Restart] = None

    shutdown: Optional[Shutdown] = None

    triggered_at: Optional[str] = None
