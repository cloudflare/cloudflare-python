# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

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

__all__ = ["AccessRuleParam"]

AccessRuleParam: TypeAlias = Union[
    EmailRuleParam,
    EmailListRuleParam,
    DomainRuleParam,
    EveryoneRuleParam,
    IPRuleParam,
    IPListRuleParam,
    CertificateRuleParam,
    GroupRuleParam,
    AzureGroupRuleParam,
    GitHubOrganizationRuleParam,
    GSuiteGroupRuleParam,
    OktaGroupRuleParam,
    SAMLGroupRuleParam,
    ServiceTokenRuleParam,
    AnyValidServiceTokenRuleParam,
    ExternalEvaluationRuleParam,
    CountryRuleParam,
    AuthenticationMethodRuleParam,
    AccessDevicePostureRuleParam,
]
