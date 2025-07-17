# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .ip_rule_param import IPRuleParam
from .email_rule_param import EmailRuleParam
from .group_rule_param import GroupRuleParam
from .domain_rule_param import DomainRuleParam
from .country_rule_param import CountryRuleParam
from .ip_list_rule_param import IPListRuleParam
from .everyone_rule_param import EveryoneRuleParam
from .email_list_rule_param import EmailListRuleParam
from .okta_group_rule_param import OktaGroupRuleParam
from .saml_group_rule_param import SAMLGroupRuleParam
from .azure_group_rule_param import AzureGroupRuleParam
from .certificate_rule_param import CertificateRuleParam
from .gsuite_group_rule_param import GSuiteGroupRuleParam
from .service_token_rule_param import ServiceTokenRuleParam
from .external_evaluation_rule_param import ExternalEvaluationRuleParam
from .github_organization_rule_param import GitHubOrganizationRuleParam
from .access_device_posture_rule_param import AccessDevicePostureRuleParam
from .authentication_method_rule_param import AuthenticationMethodRuleParam
from .any_valid_service_token_rule_param import AnyValidServiceTokenRuleParam

__all__ = [
    "AccessRuleParam",
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


class AccessAuthContextRuleAuthContext(TypedDict, total=False):
    id: Required[str]
    """The ID of an Authentication context."""

    ac_id: Required[str]
    """The ACID of an Authentication context."""

    identity_provider_id: Required[str]
    """The ID of your Azure identity provider."""


class AccessAuthContextRule(TypedDict, total=False):
    auth_context: Required[AccessAuthContextRuleAuthContext]


class AccessCommonNameRuleCommonName(TypedDict, total=False):
    common_name: Required[str]
    """The common name to match."""


class AccessCommonNameRule(TypedDict, total=False):
    common_name: Required[AccessCommonNameRuleCommonName]


class AccessLoginMethodRuleLoginMethod(TypedDict, total=False):
    id: Required[str]
    """The ID of an identity provider."""


class AccessLoginMethodRule(TypedDict, total=False):
    login_method: Required[AccessLoginMethodRuleLoginMethod]


class AccessOIDCClaimRuleOIDC(TypedDict, total=False):
    claim_name: Required[str]
    """The name of the OIDC claim."""

    claim_value: Required[str]
    """The OIDC claim value to look for."""

    identity_provider_id: Required[str]
    """The ID of your OIDC identity provider."""


class AccessOIDCClaimRule(TypedDict, total=False):
    oidc: Required[AccessOIDCClaimRuleOIDC]


class AccessLinkedAppTokenRuleLinkedAppToken(TypedDict, total=False):
    app_uid: Required[str]
    """The ID of an Access OIDC SaaS application"""


class AccessLinkedAppTokenRule(TypedDict, total=False):
    linked_app_token: Required[AccessLinkedAppTokenRuleLinkedAppToken]


AccessRuleParam: TypeAlias = Union[
    GroupRuleParam,
    AnyValidServiceTokenRuleParam,
    AccessAuthContextRule,
    AuthenticationMethodRuleParam,
    AzureGroupRuleParam,
    CertificateRuleParam,
    AccessCommonNameRule,
    CountryRuleParam,
    AccessDevicePostureRuleParam,
    DomainRuleParam,
    EmailListRuleParam,
    EmailRuleParam,
    EveryoneRuleParam,
    ExternalEvaluationRuleParam,
    GitHubOrganizationRuleParam,
    GSuiteGroupRuleParam,
    AccessLoginMethodRule,
    IPListRuleParam,
    IPRuleParam,
    OktaGroupRuleParam,
    SAMLGroupRuleParam,
    AccessOIDCClaimRule,
    ServiceTokenRuleParam,
    AccessLinkedAppTokenRule,
]
