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
]


class AccessAuthContextRuleAuthContext(BaseModel):
    id: str
    """The ID of an Authentication context."""

    ac_id: str
    """The ACID of an Authentication context."""

    identity_provider_id: str
    """The ID of your Azure identity provider."""


class AccessAuthContextRule(BaseModel):
    auth_context: AccessAuthContextRuleAuthContext


class AccessCommonNameRuleCommonName(BaseModel):
    common_name: str
    """The common name to match."""


class AccessCommonNameRule(BaseModel):
    common_name: AccessCommonNameRuleCommonName


class AccessLoginMethodRuleLoginMethod(BaseModel):
    id: str
    """The ID of an identity provider."""


class AccessLoginMethodRule(BaseModel):
    login_method: AccessLoginMethodRuleLoginMethod


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
    ServiceTokenRule,
]
