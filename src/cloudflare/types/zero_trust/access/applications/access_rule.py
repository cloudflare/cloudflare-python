# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .ip_rule import IPRule
from .email_rule import EmailRule
from .group_rule import GroupRule
from ....._models import BaseModel
from .domain_rule import DomainRule
from .country_rule import CountryRule
from .ip_list_rule import IPListRule
from .everyone_rule import EveryoneRule
from .email_list_rule import EmailListRule
from .okta_group_rule import OktaGroupRule
from .saml_group_rule import SAMLGroupRule
from .azure_group_rule import AzureGroupRule
from .certificate_rule import CertificateRule
from .gsuite_group_rule import GSuiteGroupRule
from .service_token_rule import ServiceTokenRule
from .external_evaluation_rule import ExternalEvaluationRule
from .github_organization_rule import GitHubOrganizationRule
from .access_device_posture_rule import AccessDevicePostureRule
from .authentication_method_rule import AuthenticationMethodRule
from .any_valid_service_token_rule import AnyValidServiceTokenRule

__all__ = [
    "AccessRule",
    "AccessAuthContextRule",
    "AccessAuthContextRuleAuthContext",
    "AccessCommonNameRule",
    "AccessCommonNameRuleCommonName",
    "AccessLoginMethodRule",
    "AccessLoginMethodRuleLoginMethod",
    "AccessOIDCClaimRule",
    "AccessOIDCClaimRuleOIDC",
    "AccessLinkedAppTokenRule",
    "AccessLinkedAppTokenRuleLinkedAppToken",
]


class AccessAuthContextRuleAuthContext(BaseModel):
    id: str
    """The ID of an Authentication context."""

    ac_id: str
    """The ACID of an Authentication context."""

    identity_provider_id: str
    """The ID of your Azure identity provider."""


class AccessAuthContextRule(BaseModel):
    """
    Matches an Azure Authentication Context.
    Requires an Azure identity provider.
    """

    auth_context: AccessAuthContextRuleAuthContext


class AccessCommonNameRuleCommonName(BaseModel):
    common_name: str
    """The common name to match."""


class AccessCommonNameRule(BaseModel):
    """Matches a specific common name."""

    common_name: AccessCommonNameRuleCommonName


class AccessLoginMethodRuleLoginMethod(BaseModel):
    id: str
    """The ID of an identity provider."""


class AccessLoginMethodRule(BaseModel):
    """Matches a specific identity provider id."""

    login_method: AccessLoginMethodRuleLoginMethod


class AccessOIDCClaimRuleOIDC(BaseModel):
    claim_name: str
    """The name of the OIDC claim."""

    claim_value: str
    """The OIDC claim value to look for."""

    identity_provider_id: str
    """The ID of your OIDC identity provider."""


class AccessOIDCClaimRule(BaseModel):
    """
    Matches an OIDC claim.
    Requires an OIDC identity provider.
    """

    oidc: AccessOIDCClaimRuleOIDC


class AccessLinkedAppTokenRuleLinkedAppToken(BaseModel):
    app_uid: str
    """The ID of an Access OIDC SaaS application"""


class AccessLinkedAppTokenRule(BaseModel):
    """
    Matches OAuth 2.0 access tokens issued by the specified Access OIDC SaaS application. Only compatible with non_identity and bypass decisions.
    """

    linked_app_token: AccessLinkedAppTokenRuleLinkedAppToken


AccessRule: TypeAlias = Union[
    GroupRule,
    AnyValidServiceTokenRule,
    AccessAuthContextRule,
    AuthenticationMethodRule,
    AzureGroupRule,
    CertificateRule,
    AccessCommonNameRule,
    CountryRule,
    AccessDevicePostureRule,
    DomainRule,
    EmailListRule,
    EmailRule,
    EveryoneRule,
    ExternalEvaluationRule,
    GitHubOrganizationRule,
    GSuiteGroupRule,
    AccessLoginMethodRule,
    IPListRule,
    IPRule,
    OktaGroupRule,
    SAMLGroupRule,
    AccessOIDCClaimRule,
    ServiceTokenRule,
    AccessLinkedAppTokenRule,
]
