# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..decision import Decision
from ....._types import SequenceNotStr
from .access_rule_param import AccessRuleParam
from ..approval_group_param import ApprovalGroupParam

__all__ = [
    "PolicyCreateParams",
    "AccessAppPolicyRequest",
    "AccessAppPolicyRequestConnectionRules",
    "AccessAppPolicyRequestConnectionRulesRDP",
    "AccessAppPolicyRequestMfaConfig",
    "AccessInfraPolicyReq",
    "AccessInfraPolicyReqConnectionRules",
    "AccessInfraPolicyReqConnectionRulesSSH",
    "AccessInfraPolicyReqMfaConfig",
]


class AccessAppPolicyRequest(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: AccessAppPolicyRequestConnectionRules
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: AccessAppPolicyRequestMfaConfig
    """Configures multi-factor authentication (MFA) settings."""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: str
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: bool
    """Require users to enter a justification when they log in to the application."""

    session_duration: Optional[str]
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


class AccessAppPolicyRequestConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text", "file"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text", "file"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class AccessAppPolicyRequestConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: AccessAppPolicyRequestConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class AccessAppPolicyRequestMfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class AccessInfraPolicyReq(TypedDict, total=False):
    decision: Required[Decision]
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    include: Required[Iterable[AccessRuleParam]]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Required[str]
    """The name of the Access policy."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    connection_rules: AccessInfraPolicyReqConnectionRules
    """
    The rules that define how users may connect to the targets secured by your
    application.
    """

    exclude: Iterable[AccessRuleParam]
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    mfa_config: AccessInfraPolicyReqMfaConfig
    """
    Configures multi-factor authentication (MFA) settings for infrastructure
    applications.
    """

    require: Iterable[AccessRuleParam]
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """


class AccessInfraPolicyReqConnectionRulesSSH(TypedDict, total=False):
    """
    The SSH-specific rules that define how users may connect to the targets secured by your application.
    """

    usernames: Required[SequenceNotStr[str]]
    """Contains the Unix usernames that may be used when connecting over SSH."""

    allow_email_alias: bool
    """Enables using Identity Provider email alias as SSH username."""


class AccessInfraPolicyReqConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to the targets secured by your application.
    """

    ssh: AccessInfraPolicyReqConnectionRulesSSH
    """
    The SSH-specific rules that define how users may connect to the targets secured
    by your application.
    """


class AccessInfraPolicyReqMfaConfig(TypedDict, total=False):
    """
    Configures multi-factor authentication (MFA) settings for infrastructure applications.
    """

    allowed_authenticators: List[Literal["piv_key", "ssh_fido2_key"]]
    """Lists the MFA methods that users can authenticate with.

    For infrastructure applications, supported values are `piv_key` and
    `ssh_fido2_key`.
    """

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples: `5m` or `24h`.
    """


PolicyCreateParams: TypeAlias = Union[AccessAppPolicyRequest, AccessInfraPolicyReq]
