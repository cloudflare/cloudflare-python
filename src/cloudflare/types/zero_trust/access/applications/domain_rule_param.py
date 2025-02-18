# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DomainRuleParam", "EmailDomain"]


class EmailDomain(TypedDict, total=False):
    domain: Required[str]
    """The email domain to match."""


class DomainRuleParam(TypedDict, total=False):
    email_domain: Required[EmailDomain]
