# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InterruptCreateParams", "Reboot", "Restart", "Shutdown"]


class InterruptCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier"""

    reboot: Reboot

    restart: Restart

    shutdown: Shutdown


class Reboot(TypedDict, total=False):
    purge: bool
    """Purge connector state."""


class Restart(TypedDict, total=False):
    purge: bool
    """Purge connector state."""


class Shutdown(TypedDict, total=False):
    purge: bool
    """Purge connector state."""
