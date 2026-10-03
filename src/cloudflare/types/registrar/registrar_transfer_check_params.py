# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo
from ..._models import set_pydantic_config

__all__ = ["RegistrarTransferCheckParams", "Domain"]


class RegistrarTransferCheckParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    domains: Required[Iterable[Domain]]
    """List of domain objects to evaluate for transfer eligibility."""


class Domain(TypedDict, total=False):
    domain_name: Required[str]
    """Fully qualified domain name (FQDN) to check for transfer eligibility."""

    auth_code: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Base64-encoded auth/EPP code from the current registrar. Required for most TLDs.

    `.uk` namespaces do not use auth codes.
    """


set_pydantic_config(Domain, {"arbitrary_types_allowed": True})
