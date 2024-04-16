# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TCPConfigurationParam"]


class TCPConfigurationParam(TypedDict, total=False):
    method: Literal["connection_established"]
    """The TCP connection method to use for the health check."""

    port: int
    """Port number to connect to for the health check. Defaults to 80."""
