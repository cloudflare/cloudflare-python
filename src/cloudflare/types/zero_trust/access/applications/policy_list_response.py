# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "PolicyListResponse",
    "PolicyListResponseItem",
    "PolicyListResponseItemApprovalGroup",
    "PolicyListResponseItemExclude",
    "PolicyListResponseItemExcludeAccessEmailRule",
    "PolicyListResponseItemExcludeAccessEmailRuleEmail",
    "PolicyListResponseItemExcludeAccessEmailListRule",
    "PolicyListResponseItemExcludeAccessEmailListRuleEmailList",
    "PolicyListResponseItemExcludeAccessDomainRule",
    "PolicyListResponseItemExcludeAccessDomainRuleEmailDomain",
    "PolicyListResponseItemExcludeAccessEveryoneRule",
    "PolicyListResponseItemExcludeAccessIPRule",
    "PolicyListResponseItemExcludeAccessIPRuleIP",
    "PolicyListResponseItemExcludeAccessIPListRule",
    "PolicyListResponseItemExcludeAccessIPListRuleIPList",
    "PolicyListResponseItemExcludeAccessCertificateRule",
    "PolicyListResponseItemExcludeAccessAccessGroupRule",
    "PolicyListResponseItemExcludeAccessAccessGroupRuleGroup",
    "PolicyListResponseItemExcludeAccessAzureGroupRule",
    "PolicyListResponseItemExcludeAccessAzureGroupRuleAzureAd",
    "PolicyListResponseItemExcludeAccessGitHubOrganizationRule",
    "PolicyListResponseItemExcludeAccessGitHubOrganizationRuleGitHubOrganization",
    "PolicyListResponseItemExcludeAccessGsuiteGroupRule",
    "PolicyListResponseItemExcludeAccessGsuiteGroupRuleGsuite",
    "PolicyListResponseItemExcludeAccessOktaGroupRule",
    "PolicyListResponseItemExcludeAccessOktaGroupRuleOkta",
    "PolicyListResponseItemExcludeAccessSamlGroupRule",
    "PolicyListResponseItemExcludeAccessSamlGroupRuleSaml",
    "PolicyListResponseItemExcludeAccessServiceTokenRule",
    "PolicyListResponseItemExcludeAccessServiceTokenRuleServiceToken",
    "PolicyListResponseItemExcludeAccessAnyValidServiceTokenRule",
    "PolicyListResponseItemExcludeAccessExternalEvaluationRule",
    "PolicyListResponseItemExcludeAccessExternalEvaluationRuleExternalEvaluation",
    "PolicyListResponseItemExcludeAccessCountryRule",
    "PolicyListResponseItemExcludeAccessCountryRuleGeo",
    "PolicyListResponseItemExcludeAccessAuthenticationMethodRule",
    "PolicyListResponseItemExcludeAccessAuthenticationMethodRuleAuthMethod",
    "PolicyListResponseItemExcludeAccessDevicePostureRule",
    "PolicyListResponseItemExcludeAccessDevicePostureRuleDevicePosture",
    "PolicyListResponseItemInclude",
    "PolicyListResponseItemIncludeAccessEmailRule",
    "PolicyListResponseItemIncludeAccessEmailRuleEmail",
    "PolicyListResponseItemIncludeAccessEmailListRule",
    "PolicyListResponseItemIncludeAccessEmailListRuleEmailList",
    "PolicyListResponseItemIncludeAccessDomainRule",
    "PolicyListResponseItemIncludeAccessDomainRuleEmailDomain",
    "PolicyListResponseItemIncludeAccessEveryoneRule",
    "PolicyListResponseItemIncludeAccessIPRule",
    "PolicyListResponseItemIncludeAccessIPRuleIP",
    "PolicyListResponseItemIncludeAccessIPListRule",
    "PolicyListResponseItemIncludeAccessIPListRuleIPList",
    "PolicyListResponseItemIncludeAccessCertificateRule",
    "PolicyListResponseItemIncludeAccessAccessGroupRule",
    "PolicyListResponseItemIncludeAccessAccessGroupRuleGroup",
    "PolicyListResponseItemIncludeAccessAzureGroupRule",
    "PolicyListResponseItemIncludeAccessAzureGroupRuleAzureAd",
    "PolicyListResponseItemIncludeAccessGitHubOrganizationRule",
    "PolicyListResponseItemIncludeAccessGitHubOrganizationRuleGitHubOrganization",
    "PolicyListResponseItemIncludeAccessGsuiteGroupRule",
    "PolicyListResponseItemIncludeAccessGsuiteGroupRuleGsuite",
    "PolicyListResponseItemIncludeAccessOktaGroupRule",
    "PolicyListResponseItemIncludeAccessOktaGroupRuleOkta",
    "PolicyListResponseItemIncludeAccessSamlGroupRule",
    "PolicyListResponseItemIncludeAccessSamlGroupRuleSaml",
    "PolicyListResponseItemIncludeAccessServiceTokenRule",
    "PolicyListResponseItemIncludeAccessServiceTokenRuleServiceToken",
    "PolicyListResponseItemIncludeAccessAnyValidServiceTokenRule",
    "PolicyListResponseItemIncludeAccessExternalEvaluationRule",
    "PolicyListResponseItemIncludeAccessExternalEvaluationRuleExternalEvaluation",
    "PolicyListResponseItemIncludeAccessCountryRule",
    "PolicyListResponseItemIncludeAccessCountryRuleGeo",
    "PolicyListResponseItemIncludeAccessAuthenticationMethodRule",
    "PolicyListResponseItemIncludeAccessAuthenticationMethodRuleAuthMethod",
    "PolicyListResponseItemIncludeAccessDevicePostureRule",
    "PolicyListResponseItemIncludeAccessDevicePostureRuleDevicePosture",
    "PolicyListResponseItemRequire",
    "PolicyListResponseItemRequireAccessEmailRule",
    "PolicyListResponseItemRequireAccessEmailRuleEmail",
    "PolicyListResponseItemRequireAccessEmailListRule",
    "PolicyListResponseItemRequireAccessEmailListRuleEmailList",
    "PolicyListResponseItemRequireAccessDomainRule",
    "PolicyListResponseItemRequireAccessDomainRuleEmailDomain",
    "PolicyListResponseItemRequireAccessEveryoneRule",
    "PolicyListResponseItemRequireAccessIPRule",
    "PolicyListResponseItemRequireAccessIPRuleIP",
    "PolicyListResponseItemRequireAccessIPListRule",
    "PolicyListResponseItemRequireAccessIPListRuleIPList",
    "PolicyListResponseItemRequireAccessCertificateRule",
    "PolicyListResponseItemRequireAccessAccessGroupRule",
    "PolicyListResponseItemRequireAccessAccessGroupRuleGroup",
    "PolicyListResponseItemRequireAccessAzureGroupRule",
    "PolicyListResponseItemRequireAccessAzureGroupRuleAzureAd",
    "PolicyListResponseItemRequireAccessGitHubOrganizationRule",
    "PolicyListResponseItemRequireAccessGitHubOrganizationRuleGitHubOrganization",
    "PolicyListResponseItemRequireAccessGsuiteGroupRule",
    "PolicyListResponseItemRequireAccessGsuiteGroupRuleGsuite",
    "PolicyListResponseItemRequireAccessOktaGroupRule",
    "PolicyListResponseItemRequireAccessOktaGroupRuleOkta",
    "PolicyListResponseItemRequireAccessSamlGroupRule",
    "PolicyListResponseItemRequireAccessSamlGroupRuleSaml",
    "PolicyListResponseItemRequireAccessServiceTokenRule",
    "PolicyListResponseItemRequireAccessServiceTokenRuleServiceToken",
    "PolicyListResponseItemRequireAccessAnyValidServiceTokenRule",
    "PolicyListResponseItemRequireAccessExternalEvaluationRule",
    "PolicyListResponseItemRequireAccessExternalEvaluationRuleExternalEvaluation",
    "PolicyListResponseItemRequireAccessCountryRule",
    "PolicyListResponseItemRequireAccessCountryRuleGeo",
    "PolicyListResponseItemRequireAccessAuthenticationMethodRule",
    "PolicyListResponseItemRequireAccessAuthenticationMethodRuleAuthMethod",
    "PolicyListResponseItemRequireAccessDevicePostureRule",
    "PolicyListResponseItemRequireAccessDevicePostureRuleDevicePosture",
]


class PolicyListResponseItemApprovalGroup(BaseModel):
    approvals_needed: float
    """The number of approvals needed to obtain access."""

    email_addresses: Optional[List[object]] = None
    """A list of emails that can approve the access request."""

    email_list_uuid: Optional[str] = None
    """The UUID of an re-usable email list."""


class PolicyListResponseItemExcludeAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class PolicyListResponseItemExcludeAccessEmailRule(BaseModel):
    email: PolicyListResponseItemExcludeAccessEmailRuleEmail


class PolicyListResponseItemExcludeAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class PolicyListResponseItemExcludeAccessEmailListRule(BaseModel):
    email_list: PolicyListResponseItemExcludeAccessEmailListRuleEmailList


class PolicyListResponseItemExcludeAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class PolicyListResponseItemExcludeAccessDomainRule(BaseModel):
    email_domain: PolicyListResponseItemExcludeAccessDomainRuleEmailDomain


class PolicyListResponseItemExcludeAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class PolicyListResponseItemExcludeAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class PolicyListResponseItemExcludeAccessIPRule(BaseModel):
    ip: PolicyListResponseItemExcludeAccessIPRuleIP


class PolicyListResponseItemExcludeAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class PolicyListResponseItemExcludeAccessIPListRule(BaseModel):
    ip_list: PolicyListResponseItemExcludeAccessIPListRuleIPList


class PolicyListResponseItemExcludeAccessCertificateRule(BaseModel):
    certificate: object


class PolicyListResponseItemExcludeAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class PolicyListResponseItemExcludeAccessAccessGroupRule(BaseModel):
    group: PolicyListResponseItemExcludeAccessAccessGroupRuleGroup


class PolicyListResponseItemExcludeAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class PolicyListResponseItemExcludeAccessAzureGroupRule(BaseModel):
    azure_ad: PolicyListResponseItemExcludeAccessAzureGroupRuleAzureAd = FieldInfo(alias="azureAD")


class PolicyListResponseItemExcludeAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class PolicyListResponseItemExcludeAccessGitHubOrganizationRule(BaseModel):
    github_organization: PolicyListResponseItemExcludeAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class PolicyListResponseItemExcludeAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class PolicyListResponseItemExcludeAccessGsuiteGroupRule(BaseModel):
    gsuite: PolicyListResponseItemExcludeAccessGsuiteGroupRuleGsuite


class PolicyListResponseItemExcludeAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class PolicyListResponseItemExcludeAccessOktaGroupRule(BaseModel):
    okta: PolicyListResponseItemExcludeAccessOktaGroupRuleOkta


class PolicyListResponseItemExcludeAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class PolicyListResponseItemExcludeAccessSamlGroupRule(BaseModel):
    saml: PolicyListResponseItemExcludeAccessSamlGroupRuleSaml


class PolicyListResponseItemExcludeAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class PolicyListResponseItemExcludeAccessServiceTokenRule(BaseModel):
    service_token: PolicyListResponseItemExcludeAccessServiceTokenRuleServiceToken


class PolicyListResponseItemExcludeAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class PolicyListResponseItemExcludeAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class PolicyListResponseItemExcludeAccessExternalEvaluationRule(BaseModel):
    external_evaluation: PolicyListResponseItemExcludeAccessExternalEvaluationRuleExternalEvaluation


class PolicyListResponseItemExcludeAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class PolicyListResponseItemExcludeAccessCountryRule(BaseModel):
    geo: PolicyListResponseItemExcludeAccessCountryRuleGeo


class PolicyListResponseItemExcludeAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class PolicyListResponseItemExcludeAccessAuthenticationMethodRule(BaseModel):
    auth_method: PolicyListResponseItemExcludeAccessAuthenticationMethodRuleAuthMethod


class PolicyListResponseItemExcludeAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class PolicyListResponseItemExcludeAccessDevicePostureRule(BaseModel):
    device_posture: PolicyListResponseItemExcludeAccessDevicePostureRuleDevicePosture


PolicyListResponseItemExclude = Union[
    PolicyListResponseItemExcludeAccessEmailRule,
    PolicyListResponseItemExcludeAccessEmailListRule,
    PolicyListResponseItemExcludeAccessDomainRule,
    PolicyListResponseItemExcludeAccessEveryoneRule,
    PolicyListResponseItemExcludeAccessIPRule,
    PolicyListResponseItemExcludeAccessIPListRule,
    PolicyListResponseItemExcludeAccessCertificateRule,
    PolicyListResponseItemExcludeAccessAccessGroupRule,
    PolicyListResponseItemExcludeAccessAzureGroupRule,
    PolicyListResponseItemExcludeAccessGitHubOrganizationRule,
    PolicyListResponseItemExcludeAccessGsuiteGroupRule,
    PolicyListResponseItemExcludeAccessOktaGroupRule,
    PolicyListResponseItemExcludeAccessSamlGroupRule,
    PolicyListResponseItemExcludeAccessServiceTokenRule,
    PolicyListResponseItemExcludeAccessAnyValidServiceTokenRule,
    PolicyListResponseItemExcludeAccessExternalEvaluationRule,
    PolicyListResponseItemExcludeAccessCountryRule,
    PolicyListResponseItemExcludeAccessAuthenticationMethodRule,
    PolicyListResponseItemExcludeAccessDevicePostureRule,
]


class PolicyListResponseItemIncludeAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class PolicyListResponseItemIncludeAccessEmailRule(BaseModel):
    email: PolicyListResponseItemIncludeAccessEmailRuleEmail


class PolicyListResponseItemIncludeAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class PolicyListResponseItemIncludeAccessEmailListRule(BaseModel):
    email_list: PolicyListResponseItemIncludeAccessEmailListRuleEmailList


class PolicyListResponseItemIncludeAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class PolicyListResponseItemIncludeAccessDomainRule(BaseModel):
    email_domain: PolicyListResponseItemIncludeAccessDomainRuleEmailDomain


class PolicyListResponseItemIncludeAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class PolicyListResponseItemIncludeAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class PolicyListResponseItemIncludeAccessIPRule(BaseModel):
    ip: PolicyListResponseItemIncludeAccessIPRuleIP


class PolicyListResponseItemIncludeAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class PolicyListResponseItemIncludeAccessIPListRule(BaseModel):
    ip_list: PolicyListResponseItemIncludeAccessIPListRuleIPList


class PolicyListResponseItemIncludeAccessCertificateRule(BaseModel):
    certificate: object


class PolicyListResponseItemIncludeAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class PolicyListResponseItemIncludeAccessAccessGroupRule(BaseModel):
    group: PolicyListResponseItemIncludeAccessAccessGroupRuleGroup


class PolicyListResponseItemIncludeAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class PolicyListResponseItemIncludeAccessAzureGroupRule(BaseModel):
    azure_ad: PolicyListResponseItemIncludeAccessAzureGroupRuleAzureAd = FieldInfo(alias="azureAD")


class PolicyListResponseItemIncludeAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class PolicyListResponseItemIncludeAccessGitHubOrganizationRule(BaseModel):
    github_organization: PolicyListResponseItemIncludeAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class PolicyListResponseItemIncludeAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class PolicyListResponseItemIncludeAccessGsuiteGroupRule(BaseModel):
    gsuite: PolicyListResponseItemIncludeAccessGsuiteGroupRuleGsuite


class PolicyListResponseItemIncludeAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class PolicyListResponseItemIncludeAccessOktaGroupRule(BaseModel):
    okta: PolicyListResponseItemIncludeAccessOktaGroupRuleOkta


class PolicyListResponseItemIncludeAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class PolicyListResponseItemIncludeAccessSamlGroupRule(BaseModel):
    saml: PolicyListResponseItemIncludeAccessSamlGroupRuleSaml


class PolicyListResponseItemIncludeAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class PolicyListResponseItemIncludeAccessServiceTokenRule(BaseModel):
    service_token: PolicyListResponseItemIncludeAccessServiceTokenRuleServiceToken


class PolicyListResponseItemIncludeAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class PolicyListResponseItemIncludeAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class PolicyListResponseItemIncludeAccessExternalEvaluationRule(BaseModel):
    external_evaluation: PolicyListResponseItemIncludeAccessExternalEvaluationRuleExternalEvaluation


class PolicyListResponseItemIncludeAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class PolicyListResponseItemIncludeAccessCountryRule(BaseModel):
    geo: PolicyListResponseItemIncludeAccessCountryRuleGeo


class PolicyListResponseItemIncludeAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class PolicyListResponseItemIncludeAccessAuthenticationMethodRule(BaseModel):
    auth_method: PolicyListResponseItemIncludeAccessAuthenticationMethodRuleAuthMethod


class PolicyListResponseItemIncludeAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class PolicyListResponseItemIncludeAccessDevicePostureRule(BaseModel):
    device_posture: PolicyListResponseItemIncludeAccessDevicePostureRuleDevicePosture


PolicyListResponseItemInclude = Union[
    PolicyListResponseItemIncludeAccessEmailRule,
    PolicyListResponseItemIncludeAccessEmailListRule,
    PolicyListResponseItemIncludeAccessDomainRule,
    PolicyListResponseItemIncludeAccessEveryoneRule,
    PolicyListResponseItemIncludeAccessIPRule,
    PolicyListResponseItemIncludeAccessIPListRule,
    PolicyListResponseItemIncludeAccessCertificateRule,
    PolicyListResponseItemIncludeAccessAccessGroupRule,
    PolicyListResponseItemIncludeAccessAzureGroupRule,
    PolicyListResponseItemIncludeAccessGitHubOrganizationRule,
    PolicyListResponseItemIncludeAccessGsuiteGroupRule,
    PolicyListResponseItemIncludeAccessOktaGroupRule,
    PolicyListResponseItemIncludeAccessSamlGroupRule,
    PolicyListResponseItemIncludeAccessServiceTokenRule,
    PolicyListResponseItemIncludeAccessAnyValidServiceTokenRule,
    PolicyListResponseItemIncludeAccessExternalEvaluationRule,
    PolicyListResponseItemIncludeAccessCountryRule,
    PolicyListResponseItemIncludeAccessAuthenticationMethodRule,
    PolicyListResponseItemIncludeAccessDevicePostureRule,
]


class PolicyListResponseItemRequireAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class PolicyListResponseItemRequireAccessEmailRule(BaseModel):
    email: PolicyListResponseItemRequireAccessEmailRuleEmail


class PolicyListResponseItemRequireAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class PolicyListResponseItemRequireAccessEmailListRule(BaseModel):
    email_list: PolicyListResponseItemRequireAccessEmailListRuleEmailList


class PolicyListResponseItemRequireAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class PolicyListResponseItemRequireAccessDomainRule(BaseModel):
    email_domain: PolicyListResponseItemRequireAccessDomainRuleEmailDomain


class PolicyListResponseItemRequireAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class PolicyListResponseItemRequireAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class PolicyListResponseItemRequireAccessIPRule(BaseModel):
    ip: PolicyListResponseItemRequireAccessIPRuleIP


class PolicyListResponseItemRequireAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class PolicyListResponseItemRequireAccessIPListRule(BaseModel):
    ip_list: PolicyListResponseItemRequireAccessIPListRuleIPList


class PolicyListResponseItemRequireAccessCertificateRule(BaseModel):
    certificate: object


class PolicyListResponseItemRequireAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class PolicyListResponseItemRequireAccessAccessGroupRule(BaseModel):
    group: PolicyListResponseItemRequireAccessAccessGroupRuleGroup


class PolicyListResponseItemRequireAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class PolicyListResponseItemRequireAccessAzureGroupRule(BaseModel):
    azure_ad: PolicyListResponseItemRequireAccessAzureGroupRuleAzureAd = FieldInfo(alias="azureAD")


class PolicyListResponseItemRequireAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class PolicyListResponseItemRequireAccessGitHubOrganizationRule(BaseModel):
    github_organization: PolicyListResponseItemRequireAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(
        alias="github-organization"
    )


class PolicyListResponseItemRequireAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class PolicyListResponseItemRequireAccessGsuiteGroupRule(BaseModel):
    gsuite: PolicyListResponseItemRequireAccessGsuiteGroupRuleGsuite


class PolicyListResponseItemRequireAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class PolicyListResponseItemRequireAccessOktaGroupRule(BaseModel):
    okta: PolicyListResponseItemRequireAccessOktaGroupRuleOkta


class PolicyListResponseItemRequireAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class PolicyListResponseItemRequireAccessSamlGroupRule(BaseModel):
    saml: PolicyListResponseItemRequireAccessSamlGroupRuleSaml


class PolicyListResponseItemRequireAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class PolicyListResponseItemRequireAccessServiceTokenRule(BaseModel):
    service_token: PolicyListResponseItemRequireAccessServiceTokenRuleServiceToken


class PolicyListResponseItemRequireAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class PolicyListResponseItemRequireAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class PolicyListResponseItemRequireAccessExternalEvaluationRule(BaseModel):
    external_evaluation: PolicyListResponseItemRequireAccessExternalEvaluationRuleExternalEvaluation


class PolicyListResponseItemRequireAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class PolicyListResponseItemRequireAccessCountryRule(BaseModel):
    geo: PolicyListResponseItemRequireAccessCountryRuleGeo


class PolicyListResponseItemRequireAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class PolicyListResponseItemRequireAccessAuthenticationMethodRule(BaseModel):
    auth_method: PolicyListResponseItemRequireAccessAuthenticationMethodRuleAuthMethod


class PolicyListResponseItemRequireAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class PolicyListResponseItemRequireAccessDevicePostureRule(BaseModel):
    device_posture: PolicyListResponseItemRequireAccessDevicePostureRuleDevicePosture


PolicyListResponseItemRequire = Union[
    PolicyListResponseItemRequireAccessEmailRule,
    PolicyListResponseItemRequireAccessEmailListRule,
    PolicyListResponseItemRequireAccessDomainRule,
    PolicyListResponseItemRequireAccessEveryoneRule,
    PolicyListResponseItemRequireAccessIPRule,
    PolicyListResponseItemRequireAccessIPListRule,
    PolicyListResponseItemRequireAccessCertificateRule,
    PolicyListResponseItemRequireAccessAccessGroupRule,
    PolicyListResponseItemRequireAccessAzureGroupRule,
    PolicyListResponseItemRequireAccessGitHubOrganizationRule,
    PolicyListResponseItemRequireAccessGsuiteGroupRule,
    PolicyListResponseItemRequireAccessOktaGroupRule,
    PolicyListResponseItemRequireAccessSamlGroupRule,
    PolicyListResponseItemRequireAccessServiceTokenRule,
    PolicyListResponseItemRequireAccessAnyValidServiceTokenRule,
    PolicyListResponseItemRequireAccessExternalEvaluationRule,
    PolicyListResponseItemRequireAccessCountryRule,
    PolicyListResponseItemRequireAccessAuthenticationMethodRule,
    PolicyListResponseItemRequireAccessDevicePostureRule,
]


class PolicyListResponseItem(BaseModel):
    id: Optional[str] = None
    """UUID"""

    approval_groups: Optional[List[PolicyListResponseItemApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Literal["allow", "deny", "non_identity", "bypass"]] = None
    """The action Access will take if a user matches this policy."""

    exclude: Optional[List[PolicyListResponseItemExclude]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[PolicyListResponseItemInclude]] = None
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

    require: Optional[List[PolicyListResponseItemRequire]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


PolicyListResponse = List[PolicyListResponseItem]
