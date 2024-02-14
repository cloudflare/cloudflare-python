# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = [
    "GroupAccessGroupsListAccessGroupsResponse",
    "GroupAccessGroupsListAccessGroupsResponseItem",
    "GroupAccessGroupsListAccessGroupsResponseItemExclude",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEmailRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEmailRuleEmail",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEmailListRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEmailListRuleEmailList",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessDomainRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessDomainRuleEmailDomain",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEveryoneRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessIPRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessIPRuleIP",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessIPListRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessIPListRuleIPList",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessCertificateRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAccessGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAccessGroupRuleGroup",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAzureGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAzureGroupRuleAzureAd",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessGitHubOrganizationRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessGitHubOrganizationRuleGitHubOrganization",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessGsuiteGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessGsuiteGroupRuleGsuite",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessOktaGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessOktaGroupRuleOkta",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessSamlGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessSamlGroupRuleSaml",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessServiceTokenRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessServiceTokenRuleServiceToken",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAnyValidServiceTokenRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessExternalEvaluationRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessExternalEvaluationRuleExternalEvaluation",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessCountryRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessCountryRuleGeo",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAuthenticationMethodRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAuthenticationMethodRuleAuthMethod",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessDevicePostureRule",
    "GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessDevicePostureRuleDevicePosture",
    "GroupAccessGroupsListAccessGroupsResponseItemInclude",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEmailRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEmailRuleEmail",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEmailListRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEmailListRuleEmailList",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessDomainRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessDomainRuleEmailDomain",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEveryoneRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessIPRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessIPRuleIP",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessIPListRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessIPListRuleIPList",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessCertificateRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAccessGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAccessGroupRuleGroup",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAzureGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAzureGroupRuleAzureAd",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessGitHubOrganizationRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessGitHubOrganizationRuleGitHubOrganization",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessGsuiteGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessGsuiteGroupRuleGsuite",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessOktaGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessOktaGroupRuleOkta",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessSamlGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessSamlGroupRuleSaml",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessServiceTokenRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessServiceTokenRuleServiceToken",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAnyValidServiceTokenRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessExternalEvaluationRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessExternalEvaluationRuleExternalEvaluation",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessCountryRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessCountryRuleGeo",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAuthenticationMethodRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAuthenticationMethodRuleAuthMethod",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessDevicePostureRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessDevicePostureRuleDevicePosture",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefault",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEmailRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEmailRuleEmail",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEmailListRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEmailListRuleEmailList",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessDomainRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessDomainRuleEmailDomain",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEveryoneRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessIPRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessIPRuleIP",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessIPListRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessIPListRuleIPList",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessCertificateRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAccessGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAccessGroupRuleGroup",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAzureGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAzureGroupRuleAzureAd",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessGitHubOrganizationRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessGitHubOrganizationRuleGitHubOrganization",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessGsuiteGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessGsuiteGroupRuleGsuite",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessOktaGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessOktaGroupRuleOkta",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessSamlGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessSamlGroupRuleSaml",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessServiceTokenRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessServiceTokenRuleServiceToken",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAnyValidServiceTokenRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessExternalEvaluationRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessExternalEvaluationRuleExternalEvaluation",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessCountryRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessCountryRuleGeo",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAuthenticationMethodRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAuthenticationMethodRuleAuthMethod",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessDevicePostureRule",
    "GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessDevicePostureRuleDevicePosture",
    "GroupAccessGroupsListAccessGroupsResponseItemRequire",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEmailRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEmailRuleEmail",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEmailListRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEmailListRuleEmailList",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessDomainRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessDomainRuleEmailDomain",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEveryoneRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessIPRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessIPRuleIP",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessIPListRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessIPListRuleIPList",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessCertificateRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAccessGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAccessGroupRuleGroup",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAzureGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAzureGroupRuleAzureAd",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessGitHubOrganizationRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessGitHubOrganizationRuleGitHubOrganization",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessGsuiteGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessGsuiteGroupRuleGsuite",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessOktaGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessOktaGroupRuleOkta",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessSamlGroupRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessSamlGroupRuleSaml",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessServiceTokenRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessServiceTokenRuleServiceToken",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAnyValidServiceTokenRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessExternalEvaluationRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessExternalEvaluationRuleExternalEvaluation",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessCountryRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessCountryRuleGeo",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAuthenticationMethodRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAuthenticationMethodRuleAuthMethod",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessDevicePostureRule",
    "GroupAccessGroupsListAccessGroupsResponseItemRequireAccessDevicePostureRuleDevicePosture",
]


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEmailRule(BaseModel):
    email: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEmailRuleEmail


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEmailListRule(BaseModel):
    email_list: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEmailListRuleEmailList


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessDomainRule(BaseModel):
    email_domain: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessDomainRuleEmailDomain


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessIPRule(BaseModel):
    ip: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessIPRuleIP


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessIPListRule(BaseModel):
    ip_list: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessIPListRuleIPList


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessCertificateRule(BaseModel):
    certificate: object


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAccessGroupRule(BaseModel):
    group: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAccessGroupRuleGroup


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAzureGroupRule(BaseModel):
    azure_ad: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAzureGroupRuleAzureAd = FieldInfo(
        alias="azureAD"
    )


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessGitHubOrganizationRule(BaseModel):
    github_organization: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessGsuiteGroupRule(BaseModel):
    gsuite: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessGsuiteGroupRuleGsuite


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessOktaGroupRule(BaseModel):
    okta: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessOktaGroupRuleOkta


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessSamlGroupRule(BaseModel):
    saml: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessSamlGroupRuleSaml


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessServiceTokenRule(BaseModel):
    service_token: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessServiceTokenRuleServiceToken


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessExternalEvaluationRule(BaseModel):
    external_evaluation: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessExternalEvaluationRuleExternalEvaluation


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessCountryRule(BaseModel):
    geo: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessCountryRuleGeo


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAuthenticationMethodRule(BaseModel):
    auth_method: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAuthenticationMethodRuleAuthMethod


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessDevicePostureRule(BaseModel):
    device_posture: GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessDevicePostureRuleDevicePosture


GroupAccessGroupsListAccessGroupsResponseItemExclude = Union[
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEmailRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEmailListRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessDomainRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessEveryoneRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessIPRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessIPListRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessCertificateRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAccessGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAzureGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessGitHubOrganizationRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessGsuiteGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessOktaGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessSamlGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessServiceTokenRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAnyValidServiceTokenRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessExternalEvaluationRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessCountryRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessAuthenticationMethodRule,
    GroupAccessGroupsListAccessGroupsResponseItemExcludeAccessDevicePostureRule,
]


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEmailRule(BaseModel):
    email: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEmailRuleEmail


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEmailListRule(BaseModel):
    email_list: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEmailListRuleEmailList


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessDomainRule(BaseModel):
    email_domain: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessDomainRuleEmailDomain


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessIPRule(BaseModel):
    ip: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessIPRuleIP


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessIPListRule(BaseModel):
    ip_list: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessIPListRuleIPList


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessCertificateRule(BaseModel):
    certificate: object


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAccessGroupRule(BaseModel):
    group: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAccessGroupRuleGroup


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAzureGroupRule(BaseModel):
    azure_ad: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAzureGroupRuleAzureAd = FieldInfo(
        alias="azureAD"
    )


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessGitHubOrganizationRule(BaseModel):
    github_organization: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessGsuiteGroupRule(BaseModel):
    gsuite: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessGsuiteGroupRuleGsuite


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessOktaGroupRule(BaseModel):
    okta: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessOktaGroupRuleOkta


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessSamlGroupRule(BaseModel):
    saml: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessSamlGroupRuleSaml


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessServiceTokenRule(BaseModel):
    service_token: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessServiceTokenRuleServiceToken


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessExternalEvaluationRule(BaseModel):
    external_evaluation: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessExternalEvaluationRuleExternalEvaluation


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessCountryRule(BaseModel):
    geo: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessCountryRuleGeo


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAuthenticationMethodRule(BaseModel):
    auth_method: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAuthenticationMethodRuleAuthMethod


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessDevicePostureRule(BaseModel):
    device_posture: GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessDevicePostureRuleDevicePosture


GroupAccessGroupsListAccessGroupsResponseItemInclude = Union[
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEmailRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEmailListRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessDomainRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessEveryoneRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessIPRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessIPListRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessCertificateRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAccessGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAzureGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessGitHubOrganizationRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessGsuiteGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessOktaGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessSamlGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessServiceTokenRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAnyValidServiceTokenRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessExternalEvaluationRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessCountryRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessAuthenticationMethodRule,
    GroupAccessGroupsListAccessGroupsResponseItemIncludeAccessDevicePostureRule,
]


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEmailRule(BaseModel):
    email: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEmailRuleEmail


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEmailListRule(BaseModel):
    email_list: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEmailListRuleEmailList


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessDomainRule(BaseModel):
    email_domain: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessDomainRuleEmailDomain


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessIPRule(BaseModel):
    ip: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessIPRuleIP


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessIPListRule(BaseModel):
    ip_list: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessIPListRuleIPList


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessCertificateRule(BaseModel):
    certificate: object


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAccessGroupRule(BaseModel):
    group: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAccessGroupRuleGroup


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAzureGroupRule(BaseModel):
    azure_ad: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAzureGroupRuleAzureAd = FieldInfo(
        alias="azureAD"
    )


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessGitHubOrganizationRule(BaseModel):
    github_organization: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessGsuiteGroupRule(BaseModel):
    gsuite: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessGsuiteGroupRuleGsuite


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessOktaGroupRule(BaseModel):
    okta: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessOktaGroupRuleOkta


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessSamlGroupRule(BaseModel):
    saml: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessSamlGroupRuleSaml


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessServiceTokenRule(BaseModel):
    service_token: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessServiceTokenRuleServiceToken


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessExternalEvaluationRule(BaseModel):
    external_evaluation: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessExternalEvaluationRuleExternalEvaluation


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessCountryRule(BaseModel):
    geo: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessCountryRuleGeo


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAuthenticationMethodRule(BaseModel):
    auth_method: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAuthenticationMethodRuleAuthMethod


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessDevicePostureRule(BaseModel):
    device_posture: GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessDevicePostureRuleDevicePosture


GroupAccessGroupsListAccessGroupsResponseItemIsDefault = Union[
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEmailRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEmailListRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessDomainRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessEveryoneRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessIPRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessIPListRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessCertificateRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAccessGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAzureGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessGitHubOrganizationRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessGsuiteGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessOktaGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessSamlGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessServiceTokenRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAnyValidServiceTokenRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessExternalEvaluationRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessCountryRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessAuthenticationMethodRule,
    GroupAccessGroupsListAccessGroupsResponseItemIsDefaultAccessDevicePostureRule,
]


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEmailRule(BaseModel):
    email: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEmailRuleEmail


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEmailListRule(BaseModel):
    email_list: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEmailListRuleEmailList


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessDomainRule(BaseModel):
    email_domain: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessDomainRuleEmailDomain


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessIPRule(BaseModel):
    ip: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessIPRuleIP


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessIPListRule(BaseModel):
    ip_list: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessIPListRuleIPList


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessCertificateRule(BaseModel):
    certificate: object


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAccessGroupRule(BaseModel):
    group: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAccessGroupRuleGroup


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAzureGroupRule(BaseModel):
    azure_ad: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAzureGroupRuleAzureAd = FieldInfo(
        alias="azureAD"
    )


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessGitHubOrganizationRule(BaseModel):
    github_organization: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessGsuiteGroupRule(BaseModel):
    gsuite: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessGsuiteGroupRuleGsuite


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessOktaGroupRule(BaseModel):
    okta: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessOktaGroupRuleOkta


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessSamlGroupRule(BaseModel):
    saml: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessSamlGroupRuleSaml


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessServiceTokenRule(BaseModel):
    service_token: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessServiceTokenRuleServiceToken


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessExternalEvaluationRule(BaseModel):
    external_evaluation: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessExternalEvaluationRuleExternalEvaluation


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessCountryRule(BaseModel):
    geo: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessCountryRuleGeo


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAuthenticationMethodRule(BaseModel):
    auth_method: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAuthenticationMethodRuleAuthMethod


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class GroupAccessGroupsListAccessGroupsResponseItemRequireAccessDevicePostureRule(BaseModel):
    device_posture: GroupAccessGroupsListAccessGroupsResponseItemRequireAccessDevicePostureRuleDevicePosture


GroupAccessGroupsListAccessGroupsResponseItemRequire = Union[
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEmailRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEmailListRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessDomainRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessEveryoneRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessIPRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessIPListRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessCertificateRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAccessGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAzureGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessGitHubOrganizationRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessGsuiteGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessOktaGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessSamlGroupRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessServiceTokenRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAnyValidServiceTokenRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessExternalEvaluationRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessCountryRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessAuthenticationMethodRule,
    GroupAccessGroupsListAccessGroupsResponseItemRequireAccessDevicePostureRule,
]


class GroupAccessGroupsListAccessGroupsResponseItem(BaseModel):
    id: Optional[str] = None
    """UUID"""

    created_at: Optional[datetime] = None

    exclude: Optional[List[GroupAccessGroupsListAccessGroupsResponseItemExclude]] = None
    """Rules evaluated with a NOT logical operator.

    To match a policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[GroupAccessGroupsListAccessGroupsResponseItemInclude]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    is_default: Optional[List[GroupAccessGroupsListAccessGroupsResponseItemIsDefault]] = None
    """Rules evaluated with an AND logical operator.

    To match a policy, a user must meet all of the Require rules.
    """

    name: Optional[str] = None
    """The name of the Access group."""

    require: Optional[List[GroupAccessGroupsListAccessGroupsResponseItemRequire]] = None
    """Rules evaluated with an AND logical operator.

    To match a policy, a user must meet all of the Require rules.
    """

    updated_at: Optional[datetime] = None


GroupAccessGroupsListAccessGroupsResponse = List[GroupAccessGroupsListAccessGroupsResponseItem]
