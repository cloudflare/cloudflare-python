# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .email_rule_param import EmailRuleParam

from .email_list_rule_param import EmailListRuleParam

from .domain_rule_param import DomainRuleParam

from .everyone_rule_param import EveryoneRuleParam

from .ip_rule_param import IPRuleParam

from .ip_list_rule_param import IPListRuleParam

from .certificate_rule_param import CertificateRuleParam

from .group_rule_param import GroupRuleParam

from .azure_group_rule_param import AzureGroupRuleParam

from .github_organization_rule_param import GitHubOrganizationRuleParam

from .gsuite_group_rule_param import GSuiteGroupRuleParam

from .okta_group_rule_param import OktaGroupRuleParam

from .saml_group_rule_param import SAMLGroupRuleParam

from .service_token_rule_param import ServiceTokenRuleParam

from .any_valid_service_token_rule_param import AnyValidServiceTokenRuleParam

from .external_evaluation_rule_param import ExternalEvaluationRuleParam

from .country_rule_param import CountryRuleParam

from .authentication_method_rule_param import AuthenticationMethodRuleParam

from .access_device_posture_rule_param import AccessDevicePostureRuleParam

from typing_extensions import TypeAlias

from typing import Union

__all__ = ["AccessRuleParam"]

AccessRuleParam: TypeAlias = Union[EmailRuleParam, EmailListRuleParam, DomainRuleParam, EveryoneRuleParam, IPRuleParam, IPListRuleParam, CertificateRuleParam, GroupRuleParam, AzureGroupRuleParam, GitHubOrganizationRuleParam, GSuiteGroupRuleParam, OktaGroupRuleParam, SAMLGroupRuleParam, ServiceTokenRuleParam, AnyValidServiceTokenRuleParam, ExternalEvaluationRuleParam, CountryRuleParam, AuthenticationMethodRuleParam, AccessDevicePostureRuleParam]