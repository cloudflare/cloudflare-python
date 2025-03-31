# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .saas_app_name_id_format import SaaSAppNameIDFormat

__all__ = ["SAMLSaaSAppParam", "CustomAttribute", "CustomAttributeSource", "CustomAttributeSourceNameByIdP"]


class CustomAttributeSourceNameByIdP(TypedDict, total=False):
    idp_id: str
    """The UID of the IdP."""

    source_name: str
    """The name of the IdP provided attribute."""


class CustomAttributeSource(TypedDict, total=False):
    name: str
    """The name of the IdP attribute."""

    name_by_idp: Iterable[CustomAttributeSourceNameByIdP]
    """A mapping from IdP ID to attribute name."""


class CustomAttribute(TypedDict, total=False):
    friendly_name: str
    """The SAML FriendlyName of the attribute."""

    name: str
    """The name of the attribute."""

    name_format: Literal[
        "urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified",
        "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
        "urn:oasis:names:tc:SAML:2.0:attrname-format:uri",
    ]
    """A globally unique name for an identity or service provider."""

    required: bool
    """If the attribute is required when building a SAML assertion."""

    source: CustomAttributeSource


class SAMLSaaSAppParam(TypedDict, total=False):
    auth_type: Literal["saml", "oidc"]
    """Optional identifier indicating the authentication protocol used for the saas
    app.

    Required for OIDC. Default if unset is "saml"
    """

    consumer_service_url: str
    """
    The service provider's endpoint that is responsible for receiving and parsing a
    SAML assertion.
    """

    custom_attributes: Iterable[CustomAttribute]

    default_relay_state: str
    """
    The URL that the user will be redirected to after a successful login for IDP
    initiated logins.
    """

    idp_entity_id: str
    """The unique identifier for your SaaS application."""

    name_id_format: SaaSAppNameIDFormat
    """The format of the name identifier sent to the SaaS application."""

    name_id_transform_jsonata: str
    """
    A [JSONata](https://jsonata.org/) expression that transforms an application's
    user identities into a NameID value for its SAML assertion. This expression
    should evaluate to a singular string. The output of this expression can override
    the `name_id_format` setting.
    """

    public_key: str
    """The Access public certificate that will be used to verify your identity."""

    saml_attribute_transform_jsonata: str
    """
    A [JSONata] (https://jsonata.org/) expression that transforms an application's
    user identities into attribute assertions in the SAML response. The expression
    can transform id, email, name, and groups values. It can also transform fields
    listed in the saml_attributes or oidc_fields of the identity provider used to
    authenticate. The output of this expression must be a JSON object.
    """

    sp_entity_id: str
    """A globally unique name for an identity or service provider."""

    sso_endpoint: str
    """The endpoint where your SaaS application will send login requests."""
