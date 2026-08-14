# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..decision import Decision
from ....._models import BaseModel
from .access_rule import AccessRule
from ..approval_group import ApprovalGroup

__all__ = [
    "PolicyCreateResponse",
    "UnionMember0",
    "UnionMember0ConnectionRules",
    "UnionMember0ConnectionRulesRDP",
    "UnionMember0MfaConfig",
    "UnionMember1",
    "UnionMember1ConnectionRules",
    "UnionMember1ConnectionRulesSSH",
    "UnionMember1MfaConfig",
]


class UnionMember0ConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text", "file"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text", "file"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class UnionMember0ConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[UnionMember0ConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class UnionMember0MfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class UnionMember0(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    account_id: Optional[str] = None
    """Identifier."""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[UnionMember0ConnectionRules] = None
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: Optional[UnionMember0MfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class UnionMember1ConnectionRulesSSH(BaseModel):
    """
    The SSH-specific rules that define how users may connect to the targets secured by your application.
    """

    usernames: List[str]
    """Contains the Unix usernames that may be used when connecting over SSH."""

    allow_email_alias: Optional[bool] = None
    """Enables using Identity Provider email alias as SSH username."""


class UnionMember1ConnectionRules(BaseModel):
    """
    The rules that define how users may connect to the targets secured by your application.
    """

    ssh: Optional[UnionMember1ConnectionRulesSSH] = None
    """
    The SSH-specific rules that define how users may connect to the targets secured
    by your application.
    """


class UnionMember1MfaConfig(BaseModel):
    """
    Configures multi-factor authentication (MFA) settings for infrastructure applications.
    """

    allowed_authenticators: Optional[List[Literal["piv_key", "ssh_fido2_key"]]] = None
    """Lists the MFA methods that users can authenticate with.

    For infrastructure applications, supported values are `piv_key` and
    `ssh_fido2_key`.
    """

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples: `5m` or `24h`.
    """


class UnionMember1(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    connection_rules: Optional[UnionMember1ConnectionRules] = None
    """
    The rules that define how users may connect to the targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    mfa_config: Optional[UnionMember1MfaConfig] = None
    """
    Configures multi-factor authentication (MFA) settings for infrastructure
    applications.
    """

    name: Optional[str] = None
    """The name of the Access policy."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    updated_at: Optional[datetime] = None


PolicyCreateResponse: TypeAlias = Union[UnionMember0, UnionMember1]
