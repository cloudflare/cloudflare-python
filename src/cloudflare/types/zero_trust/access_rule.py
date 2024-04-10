# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "AccessRule",
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
    "AccessAccessGroupRule",
    "AccessAccessGroupRuleGroup",
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


class AccessEmailRuleEmail(BaseModel):
    email: str
    """The email of the user."""


class AccessEmailRule(BaseModel):
    email: AccessEmailRuleEmail


class AccessEmailListRuleEmailList(BaseModel):
    id: str
    """The ID of a previously created email list."""


class AccessEmailListRule(BaseModel):
    email_list: AccessEmailListRuleEmailList


class AccessDomainRuleEmailDomain(BaseModel):
    domain: str
    """The email domain to match."""


class AccessDomainRule(BaseModel):
    email_domain: AccessDomainRuleEmailDomain


class AccessEveryoneRule(BaseModel):
    everyone: object
    """An empty object which matches on all users."""


class AccessIPRuleIP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class AccessIPRule(BaseModel):
    ip: AccessIPRuleIP


class AccessIPListRuleIPList(BaseModel):
    id: str
    """The ID of a previously created IP list."""


class AccessIPListRule(BaseModel):
    ip_list: AccessIPListRuleIPList


class AccessCertificateRule(BaseModel):
    certificate: object


class AccessAccessGroupRuleGroup(BaseModel):
    id: str
    """The ID of a previously created Access group."""


class AccessAccessGroupRule(BaseModel):
    group: AccessAccessGroupRuleGroup


class AccessAzureGroupRuleAzureAD(BaseModel):
    id: str
    """The ID of an Azure group."""

    connection_id: str
    """The ID of your Azure identity provider."""


class AccessAzureGroupRule(BaseModel):
    azure_ad: AccessAzureGroupRuleAzureAD = FieldInfo(alias="azureAD")


class AccessGitHubOrganizationRuleGitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class AccessGitHubOrganizationRule(BaseModel):
    github_organization: AccessGitHubOrganizationRuleGitHubOrganization = FieldInfo(alias="github-organization")


class AccessGSuiteGroupRuleGSuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class AccessGSuiteGroupRule(BaseModel):
    gsuite: AccessGSuiteGroupRuleGSuite


class AccessOktaGroupRuleOkta(BaseModel):
    connection_id: str
    """The ID of your Okta identity provider."""

    email: str
    """The email of the Okta group."""


class AccessOktaGroupRule(BaseModel):
    okta: AccessOktaGroupRuleOkta


class AccessSAMLGroupRuleSAML(BaseModel):
    attribute_name: str
    """The name of the SAML attribute."""

    attribute_value: str
    """The SAML attribute value to look for."""


class AccessSAMLGroupRule(BaseModel):
    saml: AccessSAMLGroupRuleSAML


class AccessServiceTokenRuleServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class AccessServiceTokenRule(BaseModel):
    service_token: AccessServiceTokenRuleServiceToken


class AccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


class AccessExternalEvaluationRuleExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class AccessExternalEvaluationRule(BaseModel):
    external_evaluation: AccessExternalEvaluationRuleExternalEvaluation


class AccessCountryRuleGeo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class AccessCountryRule(BaseModel):
    geo: AccessCountryRuleGeo


class AccessAuthenticationMethodRuleAuthMethod(BaseModel):
    auth_method: str
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """


class AccessAuthenticationMethodRule(BaseModel):
    auth_method: AccessAuthenticationMethodRuleAuthMethod


class AccessDevicePostureRuleDevicePosture(BaseModel):
    integration_uid: str
    """The ID of a device posture integration."""


class AccessDevicePostureRule(BaseModel):
    device_posture: AccessDevicePostureRuleDevicePosture


AccessRule = Union[
    AccessEmailRule,
    AccessEmailListRule,
    AccessDomainRule,
    AccessEveryoneRule,
    AccessIPRule,
    AccessIPListRule,
    AccessCertificateRule,
    AccessAccessGroupRule,
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
