# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "GroupUpdateParams",
    "Include",
    "IncludeAccessEmailRule",
    "IncludeAccessEmailRuleEmail",
    "IncludeAccessEmailListRule",
    "IncludeAccessEmailListRuleEmailList",
    "IncludeAccessDomainRule",
    "IncludeAccessDomainRuleEmailDomain",
    "IncludeAccessEveryoneRule",
    "IncludeAccessIPRule",
    "IncludeAccessIPRuleIP",
    "IncludeAccessIPListRule",
    "IncludeAccessIPListRuleIPList",
    "IncludeAccessCertificateRule",
    "IncludeAccessAccessGroupRule",
    "IncludeAccessAccessGroupRuleGroup",
    "IncludeAccessAzureGroupRule",
    "IncludeAccessAzureGroupRuleAzureAd",
    "IncludeAccessGitHubOrganizationRule",
    "IncludeAccessGitHubOrganizationRuleGitHubOrganization",
    "IncludeAccessGsuiteGroupRule",
    "IncludeAccessGsuiteGroupRuleGsuite",
    "IncludeAccessOktaGroupRule",
    "IncludeAccessOktaGroupRuleOkta",
    "IncludeAccessSamlGroupRule",
    "IncludeAccessSamlGroupRuleSaml",
    "IncludeAccessServiceTokenRule",
    "IncludeAccessServiceTokenRuleServiceToken",
    "IncludeAccessAnyValidServiceTokenRule",
    "IncludeAccessExternalEvaluationRule",
    "IncludeAccessExternalEvaluationRuleExternalEvaluation",
    "IncludeAccessCountryRule",
    "IncludeAccessCountryRuleGeo",
    "IncludeAccessAuthenticationMethodRule",
    "IncludeAccessAuthenticationMethodRuleAuthMethod",
    "IncludeAccessDevicePostureRule",
    "IncludeAccessDevicePostureRuleDevicePosture",
    "Exclude",
    "ExcludeAccessEmailRule",
    "ExcludeAccessEmailRuleEmail",
    "ExcludeAccessEmailListRule",
    "ExcludeAccessEmailListRuleEmailList",
    "ExcludeAccessDomainRule",
    "ExcludeAccessDomainRuleEmailDomain",
    "ExcludeAccessEveryoneRule",
    "ExcludeAccessIPRule",
    "ExcludeAccessIPRuleIP",
    "ExcludeAccessIPListRule",
    "ExcludeAccessIPListRuleIPList",
    "ExcludeAccessCertificateRule",
    "ExcludeAccessAccessGroupRule",
    "ExcludeAccessAccessGroupRuleGroup",
    "ExcludeAccessAzureGroupRule",
    "ExcludeAccessAzureGroupRuleAzureAd",
    "ExcludeAccessGitHubOrganizationRule",
    "ExcludeAccessGitHubOrganizationRuleGitHubOrganization",
    "ExcludeAccessGsuiteGroupRule",
    "ExcludeAccessGsuiteGroupRuleGsuite",
    "ExcludeAccessOktaGroupRule",
    "ExcludeAccessOktaGroupRuleOkta",
    "ExcludeAccessSamlGroupRule",
    "ExcludeAccessSamlGroupRuleSaml",
    "ExcludeAccessServiceTokenRule",
    "ExcludeAccessServiceTokenRuleServiceToken",
    "ExcludeAccessAnyValidServiceTokenRule",
    "ExcludeAccessExternalEvaluationRule",
    "ExcludeAccessExternalEvaluationRuleExternalEvaluation",
    "ExcludeAccessCountryRule",
    "ExcludeAccessCountryRuleGeo",
    "ExcludeAccessAuthenticationMethodRule",
    "ExcludeAccessAuthenticationMethodRuleAuthMethod",
    "ExcludeAccessDevicePostureRule",
    "ExcludeAccessDevicePostureRuleDevicePosture",
    "Require",
    "RequireAccessEmailRule",
    "RequireAccessEmailRuleEmail",
    "RequireAccessEmailListRule",
    "RequireAccessEmailListRuleEmailList",
    "RequireAccessDomainRule",
    "RequireAccessDomainRuleEmailDomain",
    "RequireAccessEveryoneRule",
    "RequireAccessIPRule",
    "RequireAccessIPRuleIP",
    "RequireAccessIPListRule",
    "RequireAccessIPListRuleIPList",
    "RequireAccessCertificateRule",
    "RequireAccessAccessGroupRule",
    "RequireAccessAccessGroupRuleGroup",
    "RequireAccessAzureGroupRule",
    "RequireAccessAzureGroupRuleAzureAd",
    "RequireAccessGitHubOrganizationRule",
    "RequireAccessGitHubOrganizationRuleGitHubOrganization",
    "RequireAccessGsuiteGroupRule",
    "RequireAccessGsuiteGroupRuleGsuite",
    "RequireAccessOktaGroupRule",
    "RequireAccessOktaGroupRuleOkta",
    "RequireAccessSamlGroupRule",
    "RequireAccessSamlGroupRuleSaml",
    "RequireAccessServiceTokenRule",
    "RequireAccessServiceTokenRuleServiceToken",
    "RequireAccessAnyValidServiceTokenRule",
    "RequireAccessExternalEvaluationRule",
    "RequireAccessExternalEvaluationRuleExternalEvaluation",
    "RequireAccessCountryRule",
    "RequireAccessCountryRuleGeo",
    "RequireAccessAuthenticationMethodRule",
    "RequireAccessAuthenticationMethodRuleAuthMethod",
    "RequireAccessDevicePostureRule",
    "RequireAccessDevicePostureRuleDevicePosture",
]


class GroupUpdateParams(TypedDict, total=False):
    include: Required[Iterable[Include]]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Required[str]
    """The name of the Access group."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    exclude: Iterable[Exclude]
    """Rules evaluated with a NOT logical operator.

    To match a policy, a user cannot meet any of the Exclude rules.
    """

    is_default: bool
    """Whether this is the default group"""

    require: Iterable[Require]
    """Rules evaluated with an AND logical operator.

    To match a policy, a user must meet all of the Require rules.
    """


class IncludeAccessEmailRuleEmail(TypedDict, total=False):
    email: Required[str]
    """The email of the user."""


class IncludeAccessEmailRule(TypedDict, total=False):
    email: Required[IncludeAccessEmailRuleEmail]


class IncludeAccessEmailListRuleEmailList(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created email list."""


class IncludeAccessEmailListRule(TypedDict, total=False):
    email_list: Required[IncludeAccessEmailListRuleEmailList]


class IncludeAccessDomainRuleEmailDomain(TypedDict, total=False):
    domain: Required[str]
    """The email domain to match."""


class IncludeAccessDomainRule(TypedDict, total=False):
    email_domain: Required[IncludeAccessDomainRuleEmailDomain]


class IncludeAccessEveryoneRule(TypedDict, total=False):
    everyone: Required[object]
    """An empty object which matches on all users."""


class IncludeAccessIPRuleIP(TypedDict, total=False):
    ip: Required[str]
    """An IPv4 or IPv6 CIDR block."""


class IncludeAccessIPRule(TypedDict, total=False):
    ip: Required[IncludeAccessIPRuleIP]


class IncludeAccessIPListRuleIPList(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created IP list."""


class IncludeAccessIPListRule(TypedDict, total=False):
    ip_list: Required[IncludeAccessIPListRuleIPList]


class IncludeAccessCertificateRule(TypedDict, total=False):
    certificate: Required[object]


class IncludeAccessAccessGroupRuleGroup(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created Access group."""


class IncludeAccessAccessGroupRule(TypedDict, total=False):
    group: Required[IncludeAccessAccessGroupRuleGroup]


class IncludeAccessAzureGroupRuleAzureAd(TypedDict, total=False):
    id: Required[str]
    """The ID of an Azure group."""

    connection_id: Required[str]
    """The ID of your Azure identity provider."""


class IncludeAccessAzureGroupRule(TypedDict, total=False):
    azure_ad: Required[Annotated[IncludeAccessAzureGroupRuleAzureAd, PropertyInfo(alias="azureAD")]]


class IncludeAccessGitHubOrganizationRuleGitHubOrganization(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Github identity provider."""

    name: Required[str]
    """The name of the organization."""


class IncludeAccessGitHubOrganizationRule(TypedDict, total=False):
    github_organization: Required[
        Annotated[IncludeAccessGitHubOrganizationRuleGitHubOrganization, PropertyInfo(alias="github-organization")]
    ]


class IncludeAccessGsuiteGroupRuleGsuite(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Google Workspace identity provider."""

    email: Required[str]
    """The email of the Google Workspace group."""


class IncludeAccessGsuiteGroupRule(TypedDict, total=False):
    gsuite: Required[IncludeAccessGsuiteGroupRuleGsuite]


class IncludeAccessOktaGroupRuleOkta(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Okta identity provider."""

    email: Required[str]
    """The email of the Okta group."""


class IncludeAccessOktaGroupRule(TypedDict, total=False):
    okta: Required[IncludeAccessOktaGroupRuleOkta]


class IncludeAccessSamlGroupRuleSaml(TypedDict, total=False):
    attribute_name: Required[str]
    """The name of the SAML attribute."""

    attribute_value: Required[str]
    """The SAML attribute value to look for."""


class IncludeAccessSamlGroupRule(TypedDict, total=False):
    saml: Required[IncludeAccessSamlGroupRuleSaml]


class IncludeAccessServiceTokenRuleServiceToken(TypedDict, total=False):
    token_id: Required[str]
    """The ID of a Service Token."""


class IncludeAccessServiceTokenRule(TypedDict, total=False):
    service_token: Required[IncludeAccessServiceTokenRuleServiceToken]


class IncludeAccessAnyValidServiceTokenRule(TypedDict, total=False):
    any_valid_service_token: Required[object]
    """An empty object which matches on all service tokens."""


class IncludeAccessExternalEvaluationRuleExternalEvaluation(TypedDict, total=False):
    evaluate_url: Required[str]
    """The API endpoint containing your business logic."""

    keys_url: Required[str]
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class IncludeAccessExternalEvaluationRule(TypedDict, total=False):
    external_evaluation: Required[IncludeAccessExternalEvaluationRuleExternalEvaluation]


class IncludeAccessCountryRuleGeo(TypedDict, total=False):
    country_code: Required[str]
    """The country code that should be matched."""


class IncludeAccessCountryRule(TypedDict, total=False):
    geo: Required[IncludeAccessCountryRuleGeo]


class IncludeAccessAuthenticationMethodRuleAuthMethod(TypedDict, total=False):
    auth_method: Required[str]
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class IncludeAccessAuthenticationMethodRule(TypedDict, total=False):
    auth_method: Required[IncludeAccessAuthenticationMethodRuleAuthMethod]


class IncludeAccessDevicePostureRuleDevicePosture(TypedDict, total=False):
    integration_uid: Required[str]
    """The ID of a device posture integration."""


class IncludeAccessDevicePostureRule(TypedDict, total=False):
    device_posture: Required[IncludeAccessDevicePostureRuleDevicePosture]


Include = Union[
    IncludeAccessEmailRule,
    IncludeAccessEmailListRule,
    IncludeAccessDomainRule,
    IncludeAccessEveryoneRule,
    IncludeAccessIPRule,
    IncludeAccessIPListRule,
    IncludeAccessCertificateRule,
    IncludeAccessAccessGroupRule,
    IncludeAccessAzureGroupRule,
    IncludeAccessGitHubOrganizationRule,
    IncludeAccessGsuiteGroupRule,
    IncludeAccessOktaGroupRule,
    IncludeAccessSamlGroupRule,
    IncludeAccessServiceTokenRule,
    IncludeAccessAnyValidServiceTokenRule,
    IncludeAccessExternalEvaluationRule,
    IncludeAccessCountryRule,
    IncludeAccessAuthenticationMethodRule,
    IncludeAccessDevicePostureRule,
]


class ExcludeAccessEmailRuleEmail(TypedDict, total=False):
    email: Required[str]
    """The email of the user."""


class ExcludeAccessEmailRule(TypedDict, total=False):
    email: Required[ExcludeAccessEmailRuleEmail]


class ExcludeAccessEmailListRuleEmailList(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created email list."""


class ExcludeAccessEmailListRule(TypedDict, total=False):
    email_list: Required[ExcludeAccessEmailListRuleEmailList]


class ExcludeAccessDomainRuleEmailDomain(TypedDict, total=False):
    domain: Required[str]
    """The email domain to match."""


class ExcludeAccessDomainRule(TypedDict, total=False):
    email_domain: Required[ExcludeAccessDomainRuleEmailDomain]


class ExcludeAccessEveryoneRule(TypedDict, total=False):
    everyone: Required[object]
    """An empty object which matches on all users."""


class ExcludeAccessIPRuleIP(TypedDict, total=False):
    ip: Required[str]
    """An IPv4 or IPv6 CIDR block."""


class ExcludeAccessIPRule(TypedDict, total=False):
    ip: Required[ExcludeAccessIPRuleIP]


class ExcludeAccessIPListRuleIPList(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created IP list."""


class ExcludeAccessIPListRule(TypedDict, total=False):
    ip_list: Required[ExcludeAccessIPListRuleIPList]


class ExcludeAccessCertificateRule(TypedDict, total=False):
    certificate: Required[object]


class ExcludeAccessAccessGroupRuleGroup(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created Access group."""


class ExcludeAccessAccessGroupRule(TypedDict, total=False):
    group: Required[ExcludeAccessAccessGroupRuleGroup]


class ExcludeAccessAzureGroupRuleAzureAd(TypedDict, total=False):
    id: Required[str]
    """The ID of an Azure group."""

    connection_id: Required[str]
    """The ID of your Azure identity provider."""


class ExcludeAccessAzureGroupRule(TypedDict, total=False):
    azure_ad: Required[Annotated[ExcludeAccessAzureGroupRuleAzureAd, PropertyInfo(alias="azureAD")]]


class ExcludeAccessGitHubOrganizationRuleGitHubOrganization(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Github identity provider."""

    name: Required[str]
    """The name of the organization."""


class ExcludeAccessGitHubOrganizationRule(TypedDict, total=False):
    github_organization: Required[
        Annotated[ExcludeAccessGitHubOrganizationRuleGitHubOrganization, PropertyInfo(alias="github-organization")]
    ]


class ExcludeAccessGsuiteGroupRuleGsuite(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Google Workspace identity provider."""

    email: Required[str]
    """The email of the Google Workspace group."""


class ExcludeAccessGsuiteGroupRule(TypedDict, total=False):
    gsuite: Required[ExcludeAccessGsuiteGroupRuleGsuite]


class ExcludeAccessOktaGroupRuleOkta(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Okta identity provider."""

    email: Required[str]
    """The email of the Okta group."""


class ExcludeAccessOktaGroupRule(TypedDict, total=False):
    okta: Required[ExcludeAccessOktaGroupRuleOkta]


class ExcludeAccessSamlGroupRuleSaml(TypedDict, total=False):
    attribute_name: Required[str]
    """The name of the SAML attribute."""

    attribute_value: Required[str]
    """The SAML attribute value to look for."""


class ExcludeAccessSamlGroupRule(TypedDict, total=False):
    saml: Required[ExcludeAccessSamlGroupRuleSaml]


class ExcludeAccessServiceTokenRuleServiceToken(TypedDict, total=False):
    token_id: Required[str]
    """The ID of a Service Token."""


class ExcludeAccessServiceTokenRule(TypedDict, total=False):
    service_token: Required[ExcludeAccessServiceTokenRuleServiceToken]


class ExcludeAccessAnyValidServiceTokenRule(TypedDict, total=False):
    any_valid_service_token: Required[object]
    """An empty object which matches on all service tokens."""


class ExcludeAccessExternalEvaluationRuleExternalEvaluation(TypedDict, total=False):
    evaluate_url: Required[str]
    """The API endpoint containing your business logic."""

    keys_url: Required[str]
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class ExcludeAccessExternalEvaluationRule(TypedDict, total=False):
    external_evaluation: Required[ExcludeAccessExternalEvaluationRuleExternalEvaluation]


class ExcludeAccessCountryRuleGeo(TypedDict, total=False):
    country_code: Required[str]
    """The country code that should be matched."""


class ExcludeAccessCountryRule(TypedDict, total=False):
    geo: Required[ExcludeAccessCountryRuleGeo]


class ExcludeAccessAuthenticationMethodRuleAuthMethod(TypedDict, total=False):
    auth_method: Required[str]
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class ExcludeAccessAuthenticationMethodRule(TypedDict, total=False):
    auth_method: Required[ExcludeAccessAuthenticationMethodRuleAuthMethod]


class ExcludeAccessDevicePostureRuleDevicePosture(TypedDict, total=False):
    integration_uid: Required[str]
    """The ID of a device posture integration."""


class ExcludeAccessDevicePostureRule(TypedDict, total=False):
    device_posture: Required[ExcludeAccessDevicePostureRuleDevicePosture]


Exclude = Union[
    ExcludeAccessEmailRule,
    ExcludeAccessEmailListRule,
    ExcludeAccessDomainRule,
    ExcludeAccessEveryoneRule,
    ExcludeAccessIPRule,
    ExcludeAccessIPListRule,
    ExcludeAccessCertificateRule,
    ExcludeAccessAccessGroupRule,
    ExcludeAccessAzureGroupRule,
    ExcludeAccessGitHubOrganizationRule,
    ExcludeAccessGsuiteGroupRule,
    ExcludeAccessOktaGroupRule,
    ExcludeAccessSamlGroupRule,
    ExcludeAccessServiceTokenRule,
    ExcludeAccessAnyValidServiceTokenRule,
    ExcludeAccessExternalEvaluationRule,
    ExcludeAccessCountryRule,
    ExcludeAccessAuthenticationMethodRule,
    ExcludeAccessDevicePostureRule,
]


class RequireAccessEmailRuleEmail(TypedDict, total=False):
    email: Required[str]
    """The email of the user."""


class RequireAccessEmailRule(TypedDict, total=False):
    email: Required[RequireAccessEmailRuleEmail]


class RequireAccessEmailListRuleEmailList(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created email list."""


class RequireAccessEmailListRule(TypedDict, total=False):
    email_list: Required[RequireAccessEmailListRuleEmailList]


class RequireAccessDomainRuleEmailDomain(TypedDict, total=False):
    domain: Required[str]
    """The email domain to match."""


class RequireAccessDomainRule(TypedDict, total=False):
    email_domain: Required[RequireAccessDomainRuleEmailDomain]


class RequireAccessEveryoneRule(TypedDict, total=False):
    everyone: Required[object]
    """An empty object which matches on all users."""


class RequireAccessIPRuleIP(TypedDict, total=False):
    ip: Required[str]
    """An IPv4 or IPv6 CIDR block."""


class RequireAccessIPRule(TypedDict, total=False):
    ip: Required[RequireAccessIPRuleIP]


class RequireAccessIPListRuleIPList(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created IP list."""


class RequireAccessIPListRule(TypedDict, total=False):
    ip_list: Required[RequireAccessIPListRuleIPList]


class RequireAccessCertificateRule(TypedDict, total=False):
    certificate: Required[object]


class RequireAccessAccessGroupRuleGroup(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created Access group."""


class RequireAccessAccessGroupRule(TypedDict, total=False):
    group: Required[RequireAccessAccessGroupRuleGroup]


class RequireAccessAzureGroupRuleAzureAd(TypedDict, total=False):
    id: Required[str]
    """The ID of an Azure group."""

    connection_id: Required[str]
    """The ID of your Azure identity provider."""


class RequireAccessAzureGroupRule(TypedDict, total=False):
    azure_ad: Required[Annotated[RequireAccessAzureGroupRuleAzureAd, PropertyInfo(alias="azureAD")]]


class RequireAccessGitHubOrganizationRuleGitHubOrganization(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Github identity provider."""

    name: Required[str]
    """The name of the organization."""


class RequireAccessGitHubOrganizationRule(TypedDict, total=False):
    github_organization: Required[
        Annotated[RequireAccessGitHubOrganizationRuleGitHubOrganization, PropertyInfo(alias="github-organization")]
    ]


class RequireAccessGsuiteGroupRuleGsuite(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Google Workspace identity provider."""

    email: Required[str]
    """The email of the Google Workspace group."""


class RequireAccessGsuiteGroupRule(TypedDict, total=False):
    gsuite: Required[RequireAccessGsuiteGroupRuleGsuite]


class RequireAccessOktaGroupRuleOkta(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Okta identity provider."""

    email: Required[str]
    """The email of the Okta group."""


class RequireAccessOktaGroupRule(TypedDict, total=False):
    okta: Required[RequireAccessOktaGroupRuleOkta]


class RequireAccessSamlGroupRuleSaml(TypedDict, total=False):
    attribute_name: Required[str]
    """The name of the SAML attribute."""

    attribute_value: Required[str]
    """The SAML attribute value to look for."""


class RequireAccessSamlGroupRule(TypedDict, total=False):
    saml: Required[RequireAccessSamlGroupRuleSaml]


class RequireAccessServiceTokenRuleServiceToken(TypedDict, total=False):
    token_id: Required[str]
    """The ID of a Service Token."""


class RequireAccessServiceTokenRule(TypedDict, total=False):
    service_token: Required[RequireAccessServiceTokenRuleServiceToken]


class RequireAccessAnyValidServiceTokenRule(TypedDict, total=False):
    any_valid_service_token: Required[object]
    """An empty object which matches on all service tokens."""


class RequireAccessExternalEvaluationRuleExternalEvaluation(TypedDict, total=False):
    evaluate_url: Required[str]
    """The API endpoint containing your business logic."""

    keys_url: Required[str]
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class RequireAccessExternalEvaluationRule(TypedDict, total=False):
    external_evaluation: Required[RequireAccessExternalEvaluationRuleExternalEvaluation]


class RequireAccessCountryRuleGeo(TypedDict, total=False):
    country_code: Required[str]
    """The country code that should be matched."""


class RequireAccessCountryRule(TypedDict, total=False):
    geo: Required[RequireAccessCountryRuleGeo]


class RequireAccessAuthenticationMethodRuleAuthMethod(TypedDict, total=False):
    auth_method: Required[str]
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class RequireAccessAuthenticationMethodRule(TypedDict, total=False):
    auth_method: Required[RequireAccessAuthenticationMethodRuleAuthMethod]


class RequireAccessDevicePostureRuleDevicePosture(TypedDict, total=False):
    integration_uid: Required[str]
    """The ID of a device posture integration."""


class RequireAccessDevicePostureRule(TypedDict, total=False):
    device_posture: Required[RequireAccessDevicePostureRuleDevicePosture]


Require = Union[
    RequireAccessEmailRule,
    RequireAccessEmailListRule,
    RequireAccessDomainRule,
    RequireAccessEveryoneRule,
    RequireAccessIPRule,
    RequireAccessIPListRule,
    RequireAccessCertificateRule,
    RequireAccessAccessGroupRule,
    RequireAccessAzureGroupRule,
    RequireAccessGitHubOrganizationRule,
    RequireAccessGsuiteGroupRule,
    RequireAccessOktaGroupRule,
    RequireAccessSamlGroupRule,
    RequireAccessServiceTokenRule,
    RequireAccessAnyValidServiceTokenRule,
    RequireAccessExternalEvaluationRule,
    RequireAccessCountryRule,
    RequireAccessAuthenticationMethodRule,
    RequireAccessDevicePostureRule,
]
