# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "AccessPolicies",
    "ApprovalGroup",
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


class ApprovalGroup(BaseModel):
    approvals_needed: float
    """The number of approvals needed to obtain access."""

    email_addresses: Optional[List[object]] = None
    """A list of emails that can approve the access request."""

    email_list_uuid: Optional[str] = None
    """The UUID of an re-usable email list."""


class ExcludeAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class ExcludeAccessEmailRule(BaseModel):
    email: ExcludeAccessEmailRuleEmail


class ExcludeAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class ExcludeAccessEmailListRule(BaseModel):
    email_list: ExcludeAccessEmailListRuleEmailList


class ExcludeAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class ExcludeAccessDomainRule(BaseModel):
    email_domain: ExcludeAccessDomainRuleEmailDomain


class ExcludeAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class ExcludeAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class ExcludeAccessIPRule(BaseModel):
    ip: ExcludeAccessIPRuleIP


class ExcludeAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class ExcludeAccessIPListRule(BaseModel):
    ip_list: ExcludeAccessIPListRuleIPList


class ExcludeAccessCertificateRule(BaseModel):
    certificate: object


class ExcludeAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class ExcludeAccessAccessGroupRule(BaseModel):
    group: ExcludeAccessAccessGroupRuleGroup


class ExcludeAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class ExcludeAccessAzureGroupRule(BaseModel):
    azure_ad: ExcludeAccessAzureGroupRuleAzureAd = FieldInfo(alias="azureAD")


class ExcludeAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class ExcludeAccessGitHubOrganizationRule(BaseModel):
    github_organization: ExcludeAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(alias="github-organization")


class ExcludeAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class ExcludeAccessGsuiteGroupRule(BaseModel):
    gsuite: ExcludeAccessGsuiteGroupRuleGsuite


class ExcludeAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class ExcludeAccessOktaGroupRule(BaseModel):
    okta: ExcludeAccessOktaGroupRuleOkta


class ExcludeAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class ExcludeAccessSamlGroupRule(BaseModel):
    saml: ExcludeAccessSamlGroupRuleSaml


class ExcludeAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class ExcludeAccessServiceTokenRule(BaseModel):
    service_token: ExcludeAccessServiceTokenRuleServiceToken


class ExcludeAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class ExcludeAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class ExcludeAccessExternalEvaluationRule(BaseModel):
    external_evaluation: ExcludeAccessExternalEvaluationRuleExternalEvaluation


class ExcludeAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class ExcludeAccessCountryRule(BaseModel):
    geo: ExcludeAccessCountryRuleGeo


class ExcludeAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class ExcludeAccessAuthenticationMethodRule(BaseModel):
    auth_method: ExcludeAccessAuthenticationMethodRuleAuthMethod


class ExcludeAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class ExcludeAccessDevicePostureRule(BaseModel):
    device_posture: ExcludeAccessDevicePostureRuleDevicePosture


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


class IncludeAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class IncludeAccessEmailRule(BaseModel):
    email: IncludeAccessEmailRuleEmail


class IncludeAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class IncludeAccessEmailListRule(BaseModel):
    email_list: IncludeAccessEmailListRuleEmailList


class IncludeAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class IncludeAccessDomainRule(BaseModel):
    email_domain: IncludeAccessDomainRuleEmailDomain


class IncludeAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class IncludeAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class IncludeAccessIPRule(BaseModel):
    ip: IncludeAccessIPRuleIP


class IncludeAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class IncludeAccessIPListRule(BaseModel):
    ip_list: IncludeAccessIPListRuleIPList


class IncludeAccessCertificateRule(BaseModel):
    certificate: object


class IncludeAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class IncludeAccessAccessGroupRule(BaseModel):
    group: IncludeAccessAccessGroupRuleGroup


class IncludeAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class IncludeAccessAzureGroupRule(BaseModel):
    azure_ad: IncludeAccessAzureGroupRuleAzureAd = FieldInfo(alias="azureAD")


class IncludeAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class IncludeAccessGitHubOrganizationRule(BaseModel):
    github_organization: IncludeAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(alias="github-organization")


class IncludeAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class IncludeAccessGsuiteGroupRule(BaseModel):
    gsuite: IncludeAccessGsuiteGroupRuleGsuite


class IncludeAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class IncludeAccessOktaGroupRule(BaseModel):
    okta: IncludeAccessOktaGroupRuleOkta


class IncludeAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class IncludeAccessSamlGroupRule(BaseModel):
    saml: IncludeAccessSamlGroupRuleSaml


class IncludeAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class IncludeAccessServiceTokenRule(BaseModel):
    service_token: IncludeAccessServiceTokenRuleServiceToken


class IncludeAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class IncludeAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class IncludeAccessExternalEvaluationRule(BaseModel):
    external_evaluation: IncludeAccessExternalEvaluationRuleExternalEvaluation


class IncludeAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class IncludeAccessCountryRule(BaseModel):
    geo: IncludeAccessCountryRuleGeo


class IncludeAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class IncludeAccessAuthenticationMethodRule(BaseModel):
    auth_method: IncludeAccessAuthenticationMethodRuleAuthMethod


class IncludeAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class IncludeAccessDevicePostureRule(BaseModel):
    device_posture: IncludeAccessDevicePostureRuleDevicePosture


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


class RequireAccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class RequireAccessEmailRule(BaseModel):
    email: RequireAccessEmailRuleEmail


class RequireAccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class RequireAccessEmailListRule(BaseModel):
    email_list: RequireAccessEmailListRuleEmailList


class RequireAccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class RequireAccessDomainRule(BaseModel):
    email_domain: RequireAccessDomainRuleEmailDomain


class RequireAccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class RequireAccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class RequireAccessIPRule(BaseModel):
    ip: RequireAccessIPRuleIP


class RequireAccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class RequireAccessIPListRule(BaseModel):
    ip_list: RequireAccessIPListRuleIPList


class RequireAccessCertificateRule(BaseModel):
    certificate: object


class RequireAccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class RequireAccessAccessGroupRule(BaseModel):
    group: RequireAccessAccessGroupRuleGroup


class RequireAccessAzureGroupRuleAzureAd(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class RequireAccessAzureGroupRule(BaseModel):
    azure_ad: RequireAccessAzureGroupRuleAzureAd = FieldInfo(alias="azureAD")


class RequireAccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class RequireAccessGitHubOrganizationRule(BaseModel):
    github_organization: RequireAccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(alias="github-organization")


class RequireAccessGsuiteGroupRuleGsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class RequireAccessGsuiteGroupRule(BaseModel):
    gsuite: RequireAccessGsuiteGroupRuleGsuite


class RequireAccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class RequireAccessOktaGroupRule(BaseModel):
    okta: RequireAccessOktaGroupRuleOkta


class RequireAccessSamlGroupRuleSaml(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class RequireAccessSamlGroupRule(BaseModel):
    saml: RequireAccessSamlGroupRuleSaml


class RequireAccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class RequireAccessServiceTokenRule(BaseModel):
    service_token: RequireAccessServiceTokenRuleServiceToken


class RequireAccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class RequireAccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class RequireAccessExternalEvaluationRule(BaseModel):
    external_evaluation: RequireAccessExternalEvaluationRuleExternalEvaluation


class RequireAccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class RequireAccessCountryRule(BaseModel):
    geo: RequireAccessCountryRuleGeo


class RequireAccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class RequireAccessAuthenticationMethodRule(BaseModel):
    auth_method: RequireAccessAuthenticationMethodRuleAuthMethod


class RequireAccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class RequireAccessDevicePostureRule(BaseModel):
    device_posture: RequireAccessDevicePostureRuleDevicePosture


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


class AccessPolicies(BaseModel):
    id: Optional[str] = None
    """UUID"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Literal["allow", "deny", "non_identity", "bypass"]] = None
    """The action Access will take if a user matches this policy."""

    exclude: Optional[List[Exclude]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[Include]] = None
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

    require: Optional[List[Require]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None
