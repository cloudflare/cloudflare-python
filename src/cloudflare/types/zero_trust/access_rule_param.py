# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .group_rule_param import GroupRuleParam

__all__ = [
    "AccessRuleParam",
    "AccessEmailRule",
    "AccessEmailRuleEmail",
    "AccessEmailListRule",
    "AccessEmailListRuleEmailList",
    "AccessDomainRule",
    "AccessDomainRuleEmailDomain",
    "AccessEveryoneRule",
    "AccessIPRule",
    "AccessIPRuleIP",
    "AccessIPListRule",
    "AccessIPListRuleIPList",
    "AccessCertificateRule",
    "AccessAzureGroupRule",
    "AccessAzureGroupRuleAzureAD",
    "AccessGitHubOrganizationRule",
    "AccessGitHubOrganizationRuleGitHubOrganization",
    "AccessGSuiteGroupRule",
    "AccessGSuiteGroupRuleGSuite",
    "AccessOktaGroupRule",
    "AccessOktaGroupRuleOkta",
    "AccessSAMLGroupRule",
    "AccessSAMLGroupRuleSAML",
    "AccessServiceTokenRule",
    "AccessServiceTokenRuleServiceToken",
    "AccessAnyValidServiceTokenRule",
    "AccessExternalEvaluationRule",
    "AccessExternalEvaluationRuleExternalEvaluation",
    "AccessCountryRule",
    "AccessCountryRuleGeo",
    "AccessAuthenticationMethodRule",
    "AccessAuthenticationMethodRuleAuthMethod",
    "AccessDevicePostureRule",
    "AccessDevicePostureRuleDevicePosture",
]


class AccessEmailRuleEmail(TypedDict, total=False):
    email: Required[str]
    """The email of the user."""


class AccessEmailRule(TypedDict, total=False):
    email: Required[AccessEmailRuleEmail]


class AccessEmailListRuleEmailList(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created email list."""


class AccessEmailListRule(TypedDict, total=False):
    email_list: Required[AccessEmailListRuleEmailList]


class AccessDomainRuleEmailDomain(TypedDict, total=False):
    domain: Required[str]
    """The email domain to match."""


class AccessDomainRule(TypedDict, total=False):
    email_domain: Required[AccessDomainRuleEmailDomain]


class AccessEveryoneRule(TypedDict, total=False):
    everyone: Required[object]
    """An empty object which matches on all users."""


class AccessIPRuleIP(TypedDict, total=False):
    ip: Required[str]
    """An IPv4 or IPv6 CIDR block."""


class AccessIPRule(TypedDict, total=False):
    ip: Required[AccessIPRuleIP]


class AccessIPListRuleIPList(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created IP list."""


class AccessIPListRule(TypedDict, total=False):
    ip_list: Required[AccessIPListRuleIPList]


class AccessCertificateRule(TypedDict, total=False):
    certificate: Required[object]


class AccessAzureGroupRuleAzureAD(TypedDict, total=False):
    id: Required[str]
    """The ID of an Azure group."""

    connection_id: Required[str]
    """The ID of your Azure identity provider."""


class AccessAzureGroupRule(TypedDict, total=False):
    azure_ad: Required[Annotated[AccessAzureGroupRuleAzureAD, PropertyInfo(alias="azureAD")]]


class AccessGitHubOrganizationRuleGitHubOrganization(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Github identity provider."""

    name: Required[str]
    """The name of the organization."""


class AccessGitHubOrganizationRule(TypedDict, total=False):
    github_organization: Required[
        Annotated[AccessGitHubOrganizationRuleGitHubOrganization, PropertyInfo(alias="github-organization")]
    ]


class AccessGSuiteGroupRuleGSuite(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Google Workspace identity provider."""

    email: Required[str]
    """The email of the Google Workspace group."""


class AccessGSuiteGroupRule(TypedDict, total=False):
    gsuite: Required[AccessGSuiteGroupRuleGSuite]


class AccessOktaGroupRuleOkta(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Okta identity provider."""

    email: Required[str]
    """The email of the Okta group."""


class AccessOktaGroupRule(TypedDict, total=False):
    okta: Required[AccessOktaGroupRuleOkta]


class AccessSAMLGroupRuleSAML(TypedDict, total=False):
    attribute_name: Required[str]
    """The name of the SAML attribute."""

    attribute_value: Required[str]
    """The SAML attribute value to look for."""


class AccessSAMLGroupRule(TypedDict, total=False):
    saml: Required[AccessSAMLGroupRuleSAML]


class AccessServiceTokenRuleServiceToken(TypedDict, total=False):
    token_id: Required[str]
    """The ID of a Service Token."""


class AccessServiceTokenRule(TypedDict, total=False):
    service_token: Required[AccessServiceTokenRuleServiceToken]


class AccessAnyValidServiceTokenRule(TypedDict, total=False):
    any_valid_service_token: Required[object]
    """An empty object which matches on all service tokens."""


class AccessExternalEvaluationRuleExternalEvaluation(TypedDict, total=False):
    evaluate_url: Required[str]
    """The API endpoint containing your business logic."""

    keys_url: Required[str]
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class AccessExternalEvaluationRule(TypedDict, total=False):
    external_evaluation: Required[AccessExternalEvaluationRuleExternalEvaluation]


class AccessCountryRuleGeo(TypedDict, total=False):
    country_code: Required[str]
    """The country code that should be matched."""


class AccessCountryRule(TypedDict, total=False):
    geo: Required[AccessCountryRuleGeo]


class AccessAuthenticationMethodRuleAuthMethod(TypedDict, total=False):
    auth_method: Required[str]
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class AccessAuthenticationMethodRule(TypedDict, total=False):
    auth_method: Required[AccessAuthenticationMethodRuleAuthMethod]


class AccessDevicePostureRuleDevicePosture(TypedDict, total=False):
    integration_uid: Required[str]
    """The ID of a device posture integration."""


class AccessDevicePostureRule(TypedDict, total=False):
    device_posture: Required[AccessDevicePostureRuleDevicePosture]


AccessRuleParam = Union[
    AccessEmailRule,
    AccessEmailListRule,
    AccessDomainRule,
    AccessEveryoneRule,
    AccessIPRule,
    AccessIPListRule,
    AccessCertificateRule,
    GroupRuleParam,
    AccessAzureGroupRule,
    AccessGitHubOrganizationRule,
    AccessGSuiteGroupRule,
    AccessOktaGroupRule,
    AccessSAMLGroupRule,
    AccessServiceTokenRule,
    AccessAnyValidServiceTokenRule,
    AccessExternalEvaluationRule,
    AccessCountryRule,
    AccessAuthenticationMethodRule,
    AccessDevicePostureRule,
]
