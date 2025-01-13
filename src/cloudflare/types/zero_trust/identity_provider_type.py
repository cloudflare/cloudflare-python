# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["IdentityProviderType"]

IdentityProviderType: TypeAlias = Literal[
    "onetimepin",
    "azureAD",
    "saml",
    "centrify",
    "facebook",
    "github",
    "google-apps",
    "google",
    "linkedin",
    "oidc",
    "okta",
    "onelogin",
    "pingone",
    "yandex",
]
