# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .saas_app_name_id_format import SaaSAppNameIDFormat

__all__ = ["SAMLSaaSApp", "CustomAttribute", "CustomAttributeSource", "CustomAttributeSourceNameByIdP"]


class CustomAttributeSourceNameByIdP(BaseModel):
    idp_id: Optional[str] = None
    """The UID of the IdP."""

    source_name: Optional[str] = None
    """The name of the IdP provided attribute."""


class CustomAttributeSource(BaseModel):
    name: Optional[str] = None
    """The name of the IdP attribute."""

    name_by_idp: Optional[List[CustomAttributeSourceNameByIdP]] = None
    """A mapping from IdP ID to attribute name."""


class CustomAttribute(BaseModel):
    friendly_name: Optional[str] = None
    """The SAML FriendlyName of the attribute."""

    name: Optional[str] = None
    """The name of the attribute."""

    name_format: Optional[
        Literal[
            "urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified",
            "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
            "urn:oasis:names:tc:SAML:2.0:attrname-format:uri",
        ]
    ] = None
    """A globally unique name for an identity or service provider."""

    required: Optional[bool] = None
    """If the attribute is required when building a SAML assertion."""

    source: Optional[CustomAttributeSource] = None


class SAMLSaaSApp(BaseModel):
    auth_type: Optional[Literal["saml", "oidc"]] = None
    """Optional identifier indicating the authentication protocol used for the saas
    app.

    Required for OIDC. Default if unset is "saml"
    """

    consumer_service_url: Optional[str] = None
    """
    The service provider's endpoint that is responsible for receiving and parsing a
    SAML assertion.
    """

    created_at: Optional[datetime] = None

    custom_attributes: Optional[List[CustomAttribute]] = None

    default_relay_state: Optional[str] = None
    """
    The URL that the user will be redirected to after a successful login for IDP
    initiated logins.
    """

    idp_entity_id: Optional[str] = None
    """The unique identifier for your SaaS application."""

    name_id_format: Optional[SaaSAppNameIDFormat] = None
    """The format of the name identifier sent to the SaaS application."""

    name_id_transform_jsonata: Optional[str] = None
    """
    A [JSONata](https://jsonata.org/) expression that transforms an application's
    user identities into a NameID value for its SAML assertion. This expression
    should evaluate to a singular string. The output of this expression can override
    the `name_id_format` setting.
    """

    public_key: Optional[str] = None
    """The Access public certificate that will be used to verify your identity."""

    saml_attribute_transform_jsonata: Optional[str] = None
    """
    A [JSONata] (https://jsonata.org/) expression that transforms an application's
    user identities into attribute assertions in the SAML response. The expression
    can transform id, email, name, and groups values. It can also transform fields
    listed in the saml_attributes or oidc_fields of the identity provider used to
    authenticate. The output of this expression must be a JSON object.
    """

    sp_entity_id: Optional[str] = None
    """A globally unique name for an identity or service provider."""

    sso_endpoint: Optional[str] = None
    """The endpoint where your SaaS application will send login requests."""

    updated_at: Optional[datetime] = None
