# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CertificateRuleParam", "Certificate"]


class Certificate(TypedDict, total=False):
    pass


class CertificateRuleParam(TypedDict, total=False):
    certificate: Required[Certificate]
