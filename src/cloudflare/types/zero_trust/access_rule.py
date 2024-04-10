# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .ip_rule import IPRule
from ..._models import BaseModel
from .email_rule import EmailRule
from .group_rule import GroupRule
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

__all__ = [
    "AccessRule",
    "AccessAnyValidServiceTokenRule",
    "AccessAuthenticationMethodRule",
    "AccessAuthenticationMethodRuleAuthMethod",
    "AccessDevicePostureRule",
    "AccessDevicePostureRuleDevicePosture",
]


class AccessAnyValidServiceTokenRule(BaseModel):
    any_valid_service_token: object
    """An empty object which matches on all service tokens."""


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
    EmailRule,
    EmailListRule,
    DomainRule,
    EveryoneRule,
    IPRule,
    IPListRule,
    CertificateRule,
    GroupRule,
    AzureGroupRule,
    GitHubOrganizationRule,
    GSuiteGroupRule,
    OktaGroupRule,
    SAMLGroupRule,
    ServiceTokenRule,
    AccessAnyValidServiceTokenRule,
    ExternalEvaluationRule,
    CountryRule,
    AccessAuthenticationMethodRule,
    AccessDevicePostureRule,
]
