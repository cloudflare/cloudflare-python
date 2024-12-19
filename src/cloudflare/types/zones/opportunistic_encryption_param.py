# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OpportunisticEncryptionParam"]


class OpportunisticEncryptionParam(TypedDict, total=False):
    id: Literal["opportunistic_encryption"]
    """
    Opportunistic Encryption allows browsers to access HTTP URIs over an encrypted
    TLS channel. It's not a substitute for HTTPS, but provides additional security
    for otherwise vulnerable requests.
    """

    value: Literal["on", "off"]
    """The status of Opportunistic Encryption."""
