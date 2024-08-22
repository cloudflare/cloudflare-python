# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .email_rule import EmailRule

from .email_list_rule import EmailListRule

from .domain_rule import DomainRule

from .everyone_rule import EveryoneRule

from .ip_rule import IPRule

from .ip_list_rule import IPListRule

from .certificate_rule import CertificateRule

from .group_rule import GroupRule

from .azure_group_rule import AzureGroupRule

from .github_organization_rule import GitHubOrganizationRule

from .gsuite_group_rule import GSuiteGroupRule

from .okta_group_rule import OktaGroupRule

from .saml_group_rule import SAMLGroupRule

from .service_token_rule import ServiceTokenRule

from .any_valid_service_token_rule import AnyValidServiceTokenRule

from .external_evaluation_rule import ExternalEvaluationRule

from .country_rule import CountryRule

from .authentication_method_rule import AuthenticationMethodRule

from .access_device_posture_rule import AccessDevicePostureRule

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AccessRule"]

AccessRule: TypeAlias = Union[EmailRule, EmailListRule, DomainRule, EveryoneRule, IPRule, IPListRule, CertificateRule, GroupRule, AzureGroupRule, GitHubOrganizationRule, GSuiteGroupRule, OktaGroupRule, SAMLGroupRule, ServiceTokenRule, AnyValidServiceTokenRule, ExternalEvaluationRule, CountryRule, AuthenticationMethodRule, AccessDevicePostureRule]