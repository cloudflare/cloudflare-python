# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "GroupListResponse",
    "GroupListResponseItem",
    "GroupListResponseItemExclude",
    "GroupListResponseItemExcludeAccessEmailRule",
    "GroupListResponseItemExcludeAccessEmailRuleEmail",
    "GroupListResponseItemExcludeAccessEmailListRule",
    "GroupListResponseItemExcludeAccessEmailListRuleEmailList",
    "GroupListResponseItemExcludeAccessDomainRule",
    "GroupListResponseItemExcludeAccessDomainRuleEmailDomain",
    "GroupListResponseItemExcludeAccessEveryoneRule",
    "GroupListResponseItemExcludeAccessIPRule",
    "GroupListResponseItemExcludeAccessIPRuleIP",
    "GroupListResponseItemExcludeAccessIPListRule",
    "GroupListResponseItemExcludeAccessIPListRuleIPList",
    "GroupListResponseItemExcludeAccessCertificateRule",
    "GroupListResponseItemExcludeAccessAccessGroupRule",
    "GroupListResponseItemExcludeAccessAccessGroupRuleGroup",
    "GroupListResponseItemExcludeAccessAzureGroupRule",
    "GroupListResponseItemExcludeAccessAzureGroupRuleAzureAd",
    "GroupListResponseItemExcludeAccessGitHubOrganizationRule",
    "GroupListResponseItemExcludeAccessGitHubOrganizationRuleGitHubOrganization",
    "GroupListResponseItemExcludeAccessGsuiteGroupRule",
    "GroupListResponseItemExcludeAccessGsuiteGroupRuleGsuite",
    "GroupListResponseItemExcludeAccessOktaGroupRule",
    "GroupListResponseItemExcludeAccessOktaGroupRuleOkta",
    "GroupListResponseItemExcludeAccessSamlGroupRule",
    "GroupListResponseItemExcludeAccessSamlGroupRuleSaml",
    "GroupListResponseItemExcludeAccessServiceTokenRule",
    "GroupListResponseItemExcludeAccessServiceTokenRuleServiceToken",
    "GroupListResponseItemExcludeAccessAnyValidServiceTokenRule",
    "GroupListResponseItemExcludeAccessExternalEvaluationRule",
    "GroupListResponseItemExcludeAccessExternalEvaluationRuleExternalEvaluation",
    "GroupListResponseItemExcludeAccessCountryRule",
    "GroupListResponseItemExcludeAccessCountryRuleGeo",
    "GroupListResponseItemExcludeAccessAuthenticationMethodRule",
    "GroupListResponseItemExcludeAccessAuthenticationMethodRuleAuthMethod",
    "GroupListResponseItemExcludeAccessDevicePostureRule",
    "GroupListResponseItemExcludeAccessDevicePostureRuleDevicePosture",
    "GroupListResponseItemInclude",
    "GroupListResponseItemIncludeAccessEmailRule",
    "GroupListResponseItemIncludeAccessEmailRuleEmail",
    "GroupListResponseItemIncludeAccessEmailListRule",
    "GroupListResponseItemIncludeAccessEmailListRuleEmailList",
    "GroupListResponseItemIncludeAccessDomainRule",
    "GroupListResponseItemIncludeAccessDomainRuleEmailDomain",
    "GroupListResponseItemIncludeAccessEveryoneRule",
    "GroupListResponseItemIncludeAccessIPRule",
    "GroupListResponseItemIncludeAccessIPRuleIP",
    "GroupListResponseItemIncludeAccessIPListRule",
    "GroupListResponseItemIncludeAccessIPListRuleIPList",
    "GroupListResponseItemIncludeAccessCertificateRule",
    "GroupListResponseItemIncludeAccessAccessGroupRule",
    "GroupListResponseItemIncludeAccessAccessGroupRuleGroup",
    "GroupListResponseItemIncludeAccessAzureGroupRule",
    "GroupListResponseItemIncludeAccessAzureGroupRuleAzureAd",
    "GroupListResponseItemIncludeAccessGitHubOrganizationRule",
    "GroupListResponseItemIncludeAccessGitHubOrganizationRuleGitHubOrganization",
    "GroupListResponseItemIncludeAccessGsuiteGroupRule",
    "GroupListResponseItemIncludeAccessGsuiteGroupRuleGsuite",
    "GroupListResponseItemIncludeAccessOktaGroupRule",
    "GroupListResponseItemIncludeAccessOktaGroupRuleOkta",
    "GroupListResponseItemIncludeAccessSamlGroupRule",
    "GroupListResponseItemIncludeAccessSamlGroupRuleSaml",
    "GroupListResponseItemIncludeAccessServiceTokenRule",
    "GroupListResponseItemIncludeAccessServiceTokenRuleServiceToken",
    "GroupListResponseItemIncludeAccessAnyValidServiceTokenRule",
    "GroupListResponseItemIncludeAccessExternalEvaluationRule",
    "GroupListResponseItemIncludeAccessExternalEvaluationRuleExternalEvaluation",
    "GroupListResponseItemIncludeAccessCountryRule",
    "GroupListResponseItemIncludeAccessCountryRuleGeo",
    "GroupListResponseItemIncludeAccessAuthenticationMethodRule",
    "GroupListResponseItemIncludeAccessAuthenticationMethodRuleAuthMethod",
    "GroupListResponseItemIncludeAccessDevicePostureRule",
    "GroupListResponseItemIncludeAccessDevicePostureRuleDevicePosture",
    "GroupListResponseItemIsDefault",
    "GroupListResponseItemIsDefaultAccessEmailRule",
    "GroupListResponseItemIsDefaultAccessEmailRuleEmail",
    "GroupListResponseItemIsDefaultAccessEmailListRule",
    "GroupListResponseItemIsDefaultAccessEmailListRuleEmailList",
    "GroupListResponseItemIsDefaultAccessDomainRule",
    "GroupListResponseItemIsDefaultAccessDomainRuleEmailDomain",
    "GroupListResponseItemIsDefaultAccessEveryoneRule",
    "GroupListResponseItemIsDefaultAccessIPRule",
    "GroupListResponseItemIsDefaultAccessIPRuleIP",
    "GroupListResponseItemIsDefaultAccessIPListRule",
    "GroupListResponseItemIsDefaultAccessIPListRuleIPList",
    "GroupListResponseItemIsDefaultAccessCertificateRule",
    "GroupListResponseItemIsDefaultAccessAccessGroupRule",
    "GroupListResponseItemIsDefaultAccessAccessGroupRuleGroup",
    "GroupListResponseItemIsDefaultAccessAzureGroupRule",
    "GroupListResponseItemIsDefaultAccessAzureGroupRuleAzureAd",
    "GroupListResponseItemIsDefaultAccessGitHubOrganizationRule",
    "GroupListResponseItemIsDefaultAccessGitHubOrganizationRuleGitHubOrganization",
    "GroupListResponseItemIsDefaultAccessGsuiteGroupRule",
    "GroupListResponseItemIsDefaultAccessGsuiteGroupRuleGsuite",
    "GroupListResponseItemIsDefaultAccessOktaGroupRule",
    "GroupListResponseItemIsDefaultAccessOktaGroupRuleOkta",
    "GroupListResponseItemIsDefaultAccessSamlGroupRule",
    "GroupListResponseItemIsDefaultAccessSamlGroupRuleSaml",
    "GroupListResponseItemIsDefaultAccessServiceTokenRule",
    "GroupListResponseItemIsDefaultAccessServiceTokenRuleServiceToken",
    "GroupListResponseItemIsDefaultAccessAnyValidServiceTokenRule",
    "GroupListResponseItemIsDefaultAccessExternalEvaluationRule",
    "GroupListResponseItemIsDefaultAccessExternalEvaluationRuleExternalEvaluation",
    "GroupListResponseItemIsDefaultAccessCountryRule",
    "GroupListResponseItemIsDefaultAccessCountryRuleGeo",
    "GroupListResponseItemIsDefaultAccessAuthenticationMethodRule",
    "GroupListResponseItemIsDefaultAccessAuthenticationMethodRuleAuthMethod",
    "GroupListResponseItemIsDefaultAccessDevicePostureRule",
    "GroupListResponseItemIsDefaultAccessDevicePostureRuleDevicePosture",
    "GroupListResponseItemRequire",
    "GroupListResponseItemRequireAccessEmailRule",
    "GroupListResponseItemRequireAccessEmailRuleEmail",
    "GroupListResponseItemRequireAccessEmailListRule",
    "GroupListResponseItemRequireAccessEmailListRuleEmailList",
    "GroupListResponseItemRequireAccessDomainRule",
    "GroupListResponseItemRequireAccessDomainRuleEmailDomain",
    "GroupListResponseItemRequireAccessEveryoneRule",
    "GroupListResponseItemRequireAccessIPRule",
    "GroupListResponseItemRequireAccessIPRuleIP",
    "GroupListResponseItemRequireAccessIPListRule",
    "GroupListResponseItemRequireAccessIPListRuleIPList",
    "GroupListResponseItemRequireAccessCertificateRule",
    "GroupListResponseItemRequireAccessAccessGroupRule",
    "GroupListResponseItemRequireAccessAccessGroupRuleGroup",
    "GroupListResponseItemRequireAccessAzureGroupRule",
    "GroupListResponseItemRequireAccessAzureGroupRuleAzureAd",
    "GroupListResponseItemRequireAccessGitHubOrganizationRule",
    "GroupListResponseItemRequireAccessGitHubOrganizationRuleGitHubOrganization",
    "GroupListResponseItemRequireAccessGsuiteGroupRule",
    "GroupListResponseItemRequireAccessGsuiteGroupRuleGsuite",
    "GroupListResponseItemRequireAccessOktaGroupRule",
    "GroupListResponseItemRequireAccessOktaGroupRuleOkta",
    "GroupListResponseItemRequireAccessSamlGroupRule",
    "GroupListResponseItemRequireAccessSamlGroupRuleSaml",
    "GroupListResponseItemRequireAccessServiceTokenRule",
    "GroupListResponseItemRequireAccessServiceTokenRuleServiceToken",
    "GroupListResponseItemRequireAccessAnyValidServiceTokenRule",
    "GroupListResponseItemRequireAccessExternalEvaluationRule",
    "GroupListResponseItemRequireAccessExternalEvaluationRuleExternalEvaluation",
    "GroupListResponseItemRequireAccessCountryRule",
    "GroupListResponseItemRequireAccessCountryRuleGeo",
    "GroupListResponseItemRequireAccessAuthenticationMethodRule",
    "GroupListResponseItemRequireAccessAuthenticationMethodRuleAuthMethod",
    "GroupListResponseItemRequireAccessDevicePostureRule",
    "GroupListResponseItemRequireAccessDevicePostureRuleDevicePosture",
]


class GroupListResponseItemExcludeAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class GroupListResponseItemExcludeAccessEmailRule(BaseModel):
    email: GroupListResponseItemExcludeAccessEmailRuleEmail


class GroupListResponseItemExcludeAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class GroupListResponseItemExcludeAccessEmailListRule(BaseModel):
    email_list: GroupListResponseItemExcludeAccessEmailListRuleEmailList


class GroupListResponseItemExcludeAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class GroupListResponseItemExcludeAccessDomainRule(BaseModel):
    email_domain: GroupListResponseItemExcludeAccessDomainRuleEmailDomain


class GroupListResponseItemExcludeAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class GroupListResponseItemExcludeAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class GroupListResponseItemExcludeAccessIPRule(BaseModel):
    ip: GroupListResponseItemExcludeAccessIPRuleIP


class GroupListResponseItemExcludeAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class GroupListResponseItemExcludeAccessIPListRule(BaseModel):
    ip_list: GroupListResponseItemExcludeAccessIPListRuleIPList


class GroupListResponseItemExcludeAccessCertificateRule(BaseModel):
    certificate: object


class GroupListResponseItemExcludeAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class GroupListResponseItemExcludeAccessAccessGroupRule(BaseModel):
    group: GroupListResponseItemExcludeAccessAccessGroupRuleGroup


class GroupListResponseItemExcludeAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class GroupListResponseItemExcludeAccessAzureGroupRule(BaseModel):
    azure_ad: GroupListResponseItemExcludeAccessAzureGroupRuleAzureAd = FieldInfo(alias="azureAD")


class GroupListResponseItemExcludeAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class GroupListResponseItemExcludeAccessGitHubOrganizationRule(BaseModel):
    github_organization: GroupListResponseItemExcludeAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class GroupListResponseItemExcludeAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class GroupListResponseItemExcludeAccessGsuiteGroupRule(BaseModel):
    gsuite: GroupListResponseItemExcludeAccessGsuiteGroupRuleGsuite


class GroupListResponseItemExcludeAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class GroupListResponseItemExcludeAccessOktaGroupRule(BaseModel):
    okta: GroupListResponseItemExcludeAccessOktaGroupRuleOkta


class GroupListResponseItemExcludeAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class GroupListResponseItemExcludeAccessSamlGroupRule(BaseModel):
    saml: GroupListResponseItemExcludeAccessSamlGroupRuleSaml


class GroupListResponseItemExcludeAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class GroupListResponseItemExcludeAccessServiceTokenRule(BaseModel):
    service_token: GroupListResponseItemExcludeAccessServiceTokenRuleServiceToken


class GroupListResponseItemExcludeAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class GroupListResponseItemExcludeAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class GroupListResponseItemExcludeAccessExternalEvaluationRule(BaseModel):
    external_evaluation: GroupListResponseItemExcludeAccessExternalEvaluationRuleExternalEvaluation


class GroupListResponseItemExcludeAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class GroupListResponseItemExcludeAccessCountryRule(BaseModel):
    geo: GroupListResponseItemExcludeAccessCountryRuleGeo


class GroupListResponseItemExcludeAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class GroupListResponseItemExcludeAccessAuthenticationMethodRule(BaseModel):
    auth_method: GroupListResponseItemExcludeAccessAuthenticationMethodRuleAuthMethod


class GroupListResponseItemExcludeAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class GroupListResponseItemExcludeAccessDevicePostureRule(BaseModel):
    device_posture: GroupListResponseItemExcludeAccessDevicePostureRuleDevicePosture


GroupListResponseItemExclude = Union[
    GroupListResponseItemExcludeAccessEmailRule,
    GroupListResponseItemExcludeAccessEmailListRule,
    GroupListResponseItemExcludeAccessDomainRule,
    GroupListResponseItemExcludeAccessEveryoneRule,
    GroupListResponseItemExcludeAccessIPRule,
    GroupListResponseItemExcludeAccessIPListRule,
    GroupListResponseItemExcludeAccessCertificateRule,
    GroupListResponseItemExcludeAccessAccessGroupRule,
    GroupListResponseItemExcludeAccessAzureGroupRule,
    GroupListResponseItemExcludeAccessGitHubOrganizationRule,
    GroupListResponseItemExcludeAccessGsuiteGroupRule,
    GroupListResponseItemExcludeAccessOktaGroupRule,
    GroupListResponseItemExcludeAccessSamlGroupRule,
    GroupListResponseItemExcludeAccessServiceTokenRule,
    GroupListResponseItemExcludeAccessAnyValidServiceTokenRule,
    GroupListResponseItemExcludeAccessExternalEvaluationRule,
    GroupListResponseItemExcludeAccessCountryRule,
    GroupListResponseItemExcludeAccessAuthenticationMethodRule,
    GroupListResponseItemExcludeAccessDevicePostureRule,
]


class GroupListResponseItemIncludeAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class GroupListResponseItemIncludeAccessEmailRule(BaseModel):
    email: GroupListResponseItemIncludeAccessEmailRuleEmail


class GroupListResponseItemIncludeAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class GroupListResponseItemIncludeAccessEmailListRule(BaseModel):
    email_list: GroupListResponseItemIncludeAccessEmailListRuleEmailList


class GroupListResponseItemIncludeAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class GroupListResponseItemIncludeAccessDomainRule(BaseModel):
    email_domain: GroupListResponseItemIncludeAccessDomainRuleEmailDomain


class GroupListResponseItemIncludeAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class GroupListResponseItemIncludeAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class GroupListResponseItemIncludeAccessIPRule(BaseModel):
    ip: GroupListResponseItemIncludeAccessIPRuleIP


class GroupListResponseItemIncludeAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class GroupListResponseItemIncludeAccessIPListRule(BaseModel):
    ip_list: GroupListResponseItemIncludeAccessIPListRuleIPList


class GroupListResponseItemIncludeAccessCertificateRule(BaseModel):
    certificate: object


class GroupListResponseItemIncludeAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class GroupListResponseItemIncludeAccessAccessGroupRule(BaseModel):
    group: GroupListResponseItemIncludeAccessAccessGroupRuleGroup


class GroupListResponseItemIncludeAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class GroupListResponseItemIncludeAccessAzureGroupRule(BaseModel):
    azure_ad: GroupListResponseItemIncludeAccessAzureGroupRuleAzureAd = FieldInfo(alias="azureAD")


class GroupListResponseItemIncludeAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class GroupListResponseItemIncludeAccessGitHubOrganizationRule(BaseModel):
    github_organization: GroupListResponseItemIncludeAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class GroupListResponseItemIncludeAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class GroupListResponseItemIncludeAccessGsuiteGroupRule(BaseModel):
    gsuite: GroupListResponseItemIncludeAccessGsuiteGroupRuleGsuite


class GroupListResponseItemIncludeAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class GroupListResponseItemIncludeAccessOktaGroupRule(BaseModel):
    okta: GroupListResponseItemIncludeAccessOktaGroupRuleOkta


class GroupListResponseItemIncludeAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class GroupListResponseItemIncludeAccessSamlGroupRule(BaseModel):
    saml: GroupListResponseItemIncludeAccessSamlGroupRuleSaml


class GroupListResponseItemIncludeAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class GroupListResponseItemIncludeAccessServiceTokenRule(BaseModel):
    service_token: GroupListResponseItemIncludeAccessServiceTokenRuleServiceToken


class GroupListResponseItemIncludeAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class GroupListResponseItemIncludeAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class GroupListResponseItemIncludeAccessExternalEvaluationRule(BaseModel):
    external_evaluation: GroupListResponseItemIncludeAccessExternalEvaluationRuleExternalEvaluation


class GroupListResponseItemIncludeAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class GroupListResponseItemIncludeAccessCountryRule(BaseModel):
    geo: GroupListResponseItemIncludeAccessCountryRuleGeo


class GroupListResponseItemIncludeAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class GroupListResponseItemIncludeAccessAuthenticationMethodRule(BaseModel):
    auth_method: GroupListResponseItemIncludeAccessAuthenticationMethodRuleAuthMethod


class GroupListResponseItemIncludeAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class GroupListResponseItemIncludeAccessDevicePostureRule(BaseModel):
    device_posture: GroupListResponseItemIncludeAccessDevicePostureRuleDevicePosture


GroupListResponseItemInclude = Union[
    GroupListResponseItemIncludeAccessEmailRule,
    GroupListResponseItemIncludeAccessEmailListRule,
    GroupListResponseItemIncludeAccessDomainRule,
    GroupListResponseItemIncludeAccessEveryoneRule,
    GroupListResponseItemIncludeAccessIPRule,
    GroupListResponseItemIncludeAccessIPListRule,
    GroupListResponseItemIncludeAccessCertificateRule,
    GroupListResponseItemIncludeAccessAccessGroupRule,
    GroupListResponseItemIncludeAccessAzureGroupRule,
    GroupListResponseItemIncludeAccessGitHubOrganizationRule,
    GroupListResponseItemIncludeAccessGsuiteGroupRule,
    GroupListResponseItemIncludeAccessOktaGroupRule,
    GroupListResponseItemIncludeAccessSamlGroupRule,
    GroupListResponseItemIncludeAccessServiceTokenRule,
    GroupListResponseItemIncludeAccessAnyValidServiceTokenRule,
    GroupListResponseItemIncludeAccessExternalEvaluationRule,
    GroupListResponseItemIncludeAccessCountryRule,
    GroupListResponseItemIncludeAccessAuthenticationMethodRule,
    GroupListResponseItemIncludeAccessDevicePostureRule,
]


class GroupListResponseItemIsDefaultAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class GroupListResponseItemIsDefaultAccessEmailRule(BaseModel):
    email: GroupListResponseItemIsDefaultAccessEmailRuleEmail


class GroupListResponseItemIsDefaultAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class GroupListResponseItemIsDefaultAccessEmailListRule(BaseModel):
    email_list: GroupListResponseItemIsDefaultAccessEmailListRuleEmailList


class GroupListResponseItemIsDefaultAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class GroupListResponseItemIsDefaultAccessDomainRule(BaseModel):
    email_domain: GroupListResponseItemIsDefaultAccessDomainRuleEmailDomain


class GroupListResponseItemIsDefaultAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class GroupListResponseItemIsDefaultAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class GroupListResponseItemIsDefaultAccessIPRule(BaseModel):
    ip: GroupListResponseItemIsDefaultAccessIPRuleIP


class GroupListResponseItemIsDefaultAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class GroupListResponseItemIsDefaultAccessIPListRule(BaseModel):
    ip_list: GroupListResponseItemIsDefaultAccessIPListRuleIPList


class GroupListResponseItemIsDefaultAccessCertificateRule(BaseModel):
    certificate: object


class GroupListResponseItemIsDefaultAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class GroupListResponseItemIsDefaultAccessAccessGroupRule(BaseModel):
    group: GroupListResponseItemIsDefaultAccessAccessGroupRuleGroup


class GroupListResponseItemIsDefaultAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class GroupListResponseItemIsDefaultAccessAzureGroupRule(BaseModel):
    azure_ad: GroupListResponseItemIsDefaultAccessAzureGroupRuleAzureAd = FieldInfo(alias="azureAD")


class GroupListResponseItemIsDefaultAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class GroupListResponseItemIsDefaultAccessGitHubOrganizationRule(BaseModel):
    github_organization: GroupListResponseItemIsDefaultAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class GroupListResponseItemIsDefaultAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class GroupListResponseItemIsDefaultAccessGsuiteGroupRule(BaseModel):
    gsuite: GroupListResponseItemIsDefaultAccessGsuiteGroupRuleGsuite


class GroupListResponseItemIsDefaultAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class GroupListResponseItemIsDefaultAccessOktaGroupRule(BaseModel):
    okta: GroupListResponseItemIsDefaultAccessOktaGroupRuleOkta


class GroupListResponseItemIsDefaultAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class GroupListResponseItemIsDefaultAccessSamlGroupRule(BaseModel):
    saml: GroupListResponseItemIsDefaultAccessSamlGroupRuleSaml


class GroupListResponseItemIsDefaultAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class GroupListResponseItemIsDefaultAccessServiceTokenRule(BaseModel):
    service_token: GroupListResponseItemIsDefaultAccessServiceTokenRuleServiceToken


class GroupListResponseItemIsDefaultAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class GroupListResponseItemIsDefaultAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class GroupListResponseItemIsDefaultAccessExternalEvaluationRule(BaseModel):
    external_evaluation: GroupListResponseItemIsDefaultAccessExternalEvaluationRuleExternalEvaluation


class GroupListResponseItemIsDefaultAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class GroupListResponseItemIsDefaultAccessCountryRule(BaseModel):
    geo: GroupListResponseItemIsDefaultAccessCountryRuleGeo


class GroupListResponseItemIsDefaultAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class GroupListResponseItemIsDefaultAccessAuthenticationMethodRule(BaseModel):
    auth_method: GroupListResponseItemIsDefaultAccessAuthenticationMethodRuleAuthMethod


class GroupListResponseItemIsDefaultAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class GroupListResponseItemIsDefaultAccessDevicePostureRule(BaseModel):
    device_posture: GroupListResponseItemIsDefaultAccessDevicePostureRuleDevicePosture


GroupListResponseItemIsDefault = Union[
    GroupListResponseItemIsDefaultAccessEmailRule,
    GroupListResponseItemIsDefaultAccessEmailListRule,
    GroupListResponseItemIsDefaultAccessDomainRule,
    GroupListResponseItemIsDefaultAccessEveryoneRule,
    GroupListResponseItemIsDefaultAccessIPRule,
    GroupListResponseItemIsDefaultAccessIPListRule,
    GroupListResponseItemIsDefaultAccessCertificateRule,
    GroupListResponseItemIsDefaultAccessAccessGroupRule,
    GroupListResponseItemIsDefaultAccessAzureGroupRule,
    GroupListResponseItemIsDefaultAccessGitHubOrganizationRule,
    GroupListResponseItemIsDefaultAccessGsuiteGroupRule,
    GroupListResponseItemIsDefaultAccessOktaGroupRule,
    GroupListResponseItemIsDefaultAccessSamlGroupRule,
    GroupListResponseItemIsDefaultAccessServiceTokenRule,
    GroupListResponseItemIsDefaultAccessAnyValidServiceTokenRule,
    GroupListResponseItemIsDefaultAccessExternalEvaluationRule,
    GroupListResponseItemIsDefaultAccessCountryRule,
    GroupListResponseItemIsDefaultAccessAuthenticationMethodRule,
    GroupListResponseItemIsDefaultAccessDevicePostureRule,
]


class GroupListResponseItemRequireAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class GroupListResponseItemRequireAccessEmailRule(BaseModel):
    email: GroupListResponseItemRequireAccessEmailRuleEmail


class GroupListResponseItemRequireAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class GroupListResponseItemRequireAccessEmailListRule(BaseModel):
    email_list: GroupListResponseItemRequireAccessEmailListRuleEmailList


class GroupListResponseItemRequireAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class GroupListResponseItemRequireAccessDomainRule(BaseModel):
    email_domain: GroupListResponseItemRequireAccessDomainRuleEmailDomain


class GroupListResponseItemRequireAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class GroupListResponseItemRequireAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class GroupListResponseItemRequireAccessIPRule(BaseModel):
    ip: GroupListResponseItemRequireAccessIPRuleIP


class GroupListResponseItemRequireAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class GroupListResponseItemRequireAccessIPListRule(BaseModel):
    ip_list: GroupListResponseItemRequireAccessIPListRuleIPList


class GroupListResponseItemRequireAccessCertificateRule(BaseModel):
    certificate: object


class GroupListResponseItemRequireAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class GroupListResponseItemRequireAccessAccessGroupRule(BaseModel):
    group: GroupListResponseItemRequireAccessAccessGroupRuleGroup


class GroupListResponseItemRequireAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class GroupListResponseItemRequireAccessAzureGroupRule(BaseModel):
    azure_ad: GroupListResponseItemRequireAccessAzureGroupRuleAzureAd = FieldInfo(alias="azureAD")


class GroupListResponseItemRequireAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class GroupListResponseItemRequireAccessGitHubOrganizationRule(BaseModel):
    github_organization: GroupListResponseItemRequireAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class GroupListResponseItemRequireAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class GroupListResponseItemRequireAccessGsuiteGroupRule(BaseModel):
    gsuite: GroupListResponseItemRequireAccessGsuiteGroupRuleGsuite


class GroupListResponseItemRequireAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class GroupListResponseItemRequireAccessOktaGroupRule(BaseModel):
    okta: GroupListResponseItemRequireAccessOktaGroupRuleOkta


class GroupListResponseItemRequireAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class GroupListResponseItemRequireAccessSamlGroupRule(BaseModel):
    saml: GroupListResponseItemRequireAccessSamlGroupRuleSaml


class GroupListResponseItemRequireAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class GroupListResponseItemRequireAccessServiceTokenRule(BaseModel):
    service_token: GroupListResponseItemRequireAccessServiceTokenRuleServiceToken


class GroupListResponseItemRequireAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class GroupListResponseItemRequireAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class GroupListResponseItemRequireAccessExternalEvaluationRule(BaseModel):
    external_evaluation: GroupListResponseItemRequireAccessExternalEvaluationRuleExternalEvaluation


class GroupListResponseItemRequireAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class GroupListResponseItemRequireAccessCountryRule(BaseModel):
    geo: GroupListResponseItemRequireAccessCountryRuleGeo


class GroupListResponseItemRequireAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class GroupListResponseItemRequireAccessAuthenticationMethodRule(BaseModel):
    auth_method: GroupListResponseItemRequireAccessAuthenticationMethodRuleAuthMethod


class GroupListResponseItemRequireAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class GroupListResponseItemRequireAccessDevicePostureRule(BaseModel):
    device_posture: GroupListResponseItemRequireAccessDevicePostureRuleDevicePosture


GroupListResponseItemRequire = Union[
    GroupListResponseItemRequireAccessEmailRule,
    GroupListResponseItemRequireAccessEmailListRule,
    GroupListResponseItemRequireAccessDomainRule,
    GroupListResponseItemRequireAccessEveryoneRule,
    GroupListResponseItemRequireAccessIPRule,
    GroupListResponseItemRequireAccessIPListRule,
    GroupListResponseItemRequireAccessCertificateRule,
    GroupListResponseItemRequireAccessAccessGroupRule,
    GroupListResponseItemRequireAccessAzureGroupRule,
    GroupListResponseItemRequireAccessGitHubOrganizationRule,
    GroupListResponseItemRequireAccessGsuiteGroupRule,
    GroupListResponseItemRequireAccessOktaGroupRule,
    GroupListResponseItemRequireAccessSamlGroupRule,
    GroupListResponseItemRequireAccessServiceTokenRule,
    GroupListResponseItemRequireAccessAnyValidServiceTokenRule,
    GroupListResponseItemRequireAccessExternalEvaluationRule,
    GroupListResponseItemRequireAccessCountryRule,
    GroupListResponseItemRequireAccessAuthenticationMethodRule,
    GroupListResponseItemRequireAccessDevicePostureRule,
]


class GroupListResponseItem(BaseModel):
    id: Optional[str] = None
    """UUID"""

    created_at: Optional[datetime] = None

    exclude: Optional[List[GroupListResponseItemExclude]] = None
    """Rules evaluated with a NOT logical operator.

    To match a policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[GroupListResponseItemInclude]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    is_default: Optional[List[GroupListResponseItemIsDefault]] = None
    """Rules evaluated with an AND logical operator.

    To match a policy, a user must meet all of the Require rules.
    """

    name: Optional[str] = None
    """The name of the Access group."""

    require: Optional[List[GroupListResponseItemRequire]] = None
    """Rules evaluated with an AND logical operator.

    To match a policy, a user must meet all of the Require rules.
    """

    updated_at: Optional[datetime] = None


GroupListResponse = List[GroupListResponseItem]
