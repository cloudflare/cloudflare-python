# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "PolicyAccessPoliciesListAccessPoliciesResponse",
    "PolicyAccessPoliciesListAccessPoliciesResponseItem",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemApprovalGroup",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExclude",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEmailRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEmailRuleEmail",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEmailListRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEmailListRuleEmailList",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessDomainRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessDomainRuleEmailDomain",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEveryoneRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessIPRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessIPRuleIP",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessIPListRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessIPListRuleIPList",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessCertificateRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAccessGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAccessGroupRuleGroup",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAzureGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAzureGroupRuleAzureAd",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessGitHubOrganizationRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessGitHubOrganizationRuleGitHubOrganization",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessGsuiteGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessGsuiteGroupRuleGsuite",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessOktaGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessOktaGroupRuleOkta",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessSamlGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessSamlGroupRuleSaml",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessServiceTokenRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessServiceTokenRuleServiceToken",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAnyValidServiceTokenRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessExternalEvaluationRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessExternalEvaluationRuleExternalEvaluation",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessCountryRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessCountryRuleGeo",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAuthenticationMethodRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAuthenticationMethodRuleAuthMethod",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessDevicePostureRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessDevicePostureRuleDevicePosture",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemInclude",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEmailRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEmailRuleEmail",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEmailListRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEmailListRuleEmailList",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessDomainRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessDomainRuleEmailDomain",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEveryoneRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessIPRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessIPRuleIP",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessIPListRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessIPListRuleIPList",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessCertificateRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAccessGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAccessGroupRuleGroup",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAzureGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAzureGroupRuleAzureAd",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessGitHubOrganizationRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessGitHubOrganizationRuleGitHubOrganization",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessGsuiteGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessGsuiteGroupRuleGsuite",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessOktaGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessOktaGroupRuleOkta",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessSamlGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessSamlGroupRuleSaml",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessServiceTokenRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessServiceTokenRuleServiceToken",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAnyValidServiceTokenRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessExternalEvaluationRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessExternalEvaluationRuleExternalEvaluation",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessCountryRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessCountryRuleGeo",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAuthenticationMethodRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAuthenticationMethodRuleAuthMethod",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessDevicePostureRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessDevicePostureRuleDevicePosture",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequire",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEmailRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEmailRuleEmail",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEmailListRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEmailListRuleEmailList",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessDomainRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessDomainRuleEmailDomain",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEveryoneRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessIPRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessIPRuleIP",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessIPListRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessIPListRuleIPList",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessCertificateRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAccessGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAccessGroupRuleGroup",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAzureGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAzureGroupRuleAzureAd",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessGitHubOrganizationRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessGitHubOrganizationRuleGitHubOrganization",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessGsuiteGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessGsuiteGroupRuleGsuite",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessOktaGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessOktaGroupRuleOkta",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessSamlGroupRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessSamlGroupRuleSaml",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessServiceTokenRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessServiceTokenRuleServiceToken",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAnyValidServiceTokenRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessExternalEvaluationRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessExternalEvaluationRuleExternalEvaluation",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessCountryRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessCountryRuleGeo",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAuthenticationMethodRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAuthenticationMethodRuleAuthMethod",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessDevicePostureRule",
    "PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessDevicePostureRuleDevicePosture",
]


class PolicyAccessPoliciesListAccessPoliciesResponseItemApprovalGroup(BaseModel):
    approvals_needed: float
    """The number of approvals needed to obtain access."""

    email_addresses: Optional[List[object]] = None
    """A list of emails that can approve the access request."""

    email_list_uuid: Optional[str] = None
    """The UUID of an re-usable email list."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEmailRule(BaseModel):
    email: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEmailRuleEmail


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEmailListRule(BaseModel):
    email_list: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEmailListRuleEmailList


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessDomainRule(BaseModel):
    email_domain: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessDomainRuleEmailDomain


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessIPRule(BaseModel):
    ip: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessIPRuleIP


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessIPListRule(BaseModel):
    ip_list: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessIPListRuleIPList


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessCertificateRule(BaseModel):
    certificate: object


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAccessGroupRule(BaseModel):
    group: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAccessGroupRuleGroup


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAzureGroupRule(BaseModel):
    azure_ad: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAzureGroupRuleAzureAd = FieldInfo(
        alias="azureAD"
    )


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessGitHubOrganizationRuleGitHubOrganization(
    BaseModel
):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessGitHubOrganizationRule(BaseModel):
    github_organization: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessGsuiteGroupRule(BaseModel):
    gsuite: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessGsuiteGroupRuleGsuite


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessOktaGroupRule(BaseModel):
    okta: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessOktaGroupRuleOkta


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessSamlGroupRule(BaseModel):
    saml: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessSamlGroupRuleSaml


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessServiceTokenRule(BaseModel):
    service_token: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessServiceTokenRuleServiceToken


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessExternalEvaluationRuleExternalEvaluation(
    BaseModel
):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessExternalEvaluationRule(BaseModel):
    external_evaluation: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessExternalEvaluationRuleExternalEvaluation


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessCountryRule(BaseModel):
    geo: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessCountryRuleGeo


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAuthenticationMethodRule(BaseModel):
    auth_method: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAuthenticationMethodRuleAuthMethod


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessDevicePostureRule(BaseModel):
    device_posture: PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessDevicePostureRuleDevicePosture


PolicyAccessPoliciesListAccessPoliciesResponseItemExclude = Union[
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEmailRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEmailListRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessDomainRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessEveryoneRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessIPRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessIPListRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessCertificateRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAccessGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAzureGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessGitHubOrganizationRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessGsuiteGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessOktaGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessSamlGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessServiceTokenRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAnyValidServiceTokenRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessExternalEvaluationRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessCountryRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessAuthenticationMethodRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemExcludeAccessDevicePostureRule,
]


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEmailRule(BaseModel):
    email: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEmailRuleEmail


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEmailListRule(BaseModel):
    email_list: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEmailListRuleEmailList


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessDomainRule(BaseModel):
    email_domain: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessDomainRuleEmailDomain


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessIPRule(BaseModel):
    ip: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessIPRuleIP


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessIPListRule(BaseModel):
    ip_list: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessIPListRuleIPList


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessCertificateRule(BaseModel):
    certificate: object


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAccessGroupRule(BaseModel):
    group: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAccessGroupRuleGroup


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAzureGroupRule(BaseModel):
    azure_ad: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAzureGroupRuleAzureAd = FieldInfo(
        alias="azureAD"
    )


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessGitHubOrganizationRuleGitHubOrganization(
    BaseModel
):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessGitHubOrganizationRule(BaseModel):
    github_organization: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessGsuiteGroupRule(BaseModel):
    gsuite: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessGsuiteGroupRuleGsuite


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessOktaGroupRule(BaseModel):
    okta: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessOktaGroupRuleOkta


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessSamlGroupRule(BaseModel):
    saml: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessSamlGroupRuleSaml


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessServiceTokenRule(BaseModel):
    service_token: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessServiceTokenRuleServiceToken


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessExternalEvaluationRuleExternalEvaluation(
    BaseModel
):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessExternalEvaluationRule(BaseModel):
    external_evaluation: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessExternalEvaluationRuleExternalEvaluation


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessCountryRule(BaseModel):
    geo: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessCountryRuleGeo


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAuthenticationMethodRule(BaseModel):
    auth_method: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAuthenticationMethodRuleAuthMethod


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessDevicePostureRule(BaseModel):
    device_posture: PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessDevicePostureRuleDevicePosture


PolicyAccessPoliciesListAccessPoliciesResponseItemInclude = Union[
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEmailRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEmailListRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessDomainRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessEveryoneRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessIPRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessIPListRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessCertificateRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAccessGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAzureGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessGitHubOrganizationRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessGsuiteGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessOktaGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessSamlGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessServiceTokenRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAnyValidServiceTokenRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessExternalEvaluationRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessCountryRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessAuthenticationMethodRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemIncludeAccessDevicePostureRule,
]


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEmailRule(BaseModel):
    email: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEmailRuleEmail


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEmailListRule(BaseModel):
    email_list: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEmailListRuleEmailList


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessDomainRule(BaseModel):
    email_domain: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessDomainRuleEmailDomain


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessIPRule(BaseModel):
    ip: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessIPRuleIP


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessIPListRule(BaseModel):
    ip_list: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessIPListRuleIPList


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessCertificateRule(BaseModel):
    certificate: object


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAccessGroupRule(BaseModel):
    group: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAccessGroupRuleGroup


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAzureGroupRule(BaseModel):
    azure_ad: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAzureGroupRuleAzureAd = FieldInfo(
        alias="azureAD"
    )


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessGitHubOrganizationRuleGitHubOrganization(
    BaseModel
):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessGitHubOrganizationRule(BaseModel):
    github_organization: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessGsuiteGroupRule(BaseModel):
    gsuite: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessGsuiteGroupRuleGsuite


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessOktaGroupRule(BaseModel):
    okta: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessOktaGroupRuleOkta


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessSamlGroupRule(BaseModel):
    saml: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessSamlGroupRuleSaml


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessServiceTokenRule(BaseModel):
    service_token: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessServiceTokenRuleServiceToken


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessExternalEvaluationRuleExternalEvaluation(
    BaseModel
):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessExternalEvaluationRule(BaseModel):
    external_evaluation: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessExternalEvaluationRuleExternalEvaluation


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessCountryRule(BaseModel):
    geo: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessCountryRuleGeo


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAuthenticationMethodRule(BaseModel):
    auth_method: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAuthenticationMethodRuleAuthMethod


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessDevicePostureRule(BaseModel):
    device_posture: PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessDevicePostureRuleDevicePosture


PolicyAccessPoliciesListAccessPoliciesResponseItemRequire = Union[
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEmailRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEmailListRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessDomainRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessEveryoneRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessIPRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessIPListRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessCertificateRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAccessGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAzureGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessGitHubOrganizationRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessGsuiteGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessOktaGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessSamlGroupRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessServiceTokenRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAnyValidServiceTokenRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessExternalEvaluationRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessCountryRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessAuthenticationMethodRule,
    PolicyAccessPoliciesListAccessPoliciesResponseItemRequireAccessDevicePostureRule,
]


class PolicyAccessPoliciesListAccessPoliciesResponseItem(BaseModel):
    id: Optional[str] = None
    """UUID"""

    approval_groups: Optional[List[PolicyAccessPoliciesListAccessPoliciesResponseItemApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Literal["allow", "deny", "non_identity", "bypass"]] = None
    """The action Access will take if a user matches this policy."""

    exclude: Optional[List[PolicyAccessPoliciesListAccessPoliciesResponseItemExclude]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[PolicyAccessPoliciesListAccessPoliciesResponseItemInclude]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy. Must be unique for each policy."""

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[PolicyAccessPoliciesListAccessPoliciesResponseItemRequire]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


PolicyAccessPoliciesListAccessPoliciesResponse = List[PolicyAccessPoliciesListAccessPoliciesResponseItem]
