# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .decision import Decision
from ...._models import BaseModel
from .approval_group import ApprovalGroup
from .applications.access_rule import AccessRule

__all__ = ["PolicyGetResponse", "ConnectionRules", "ConnectionRulesRDP", "MfaConfig"]


class ConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class ConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[ConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class MfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_bypass: Optional[bool] = None
    """Indicates whether to bypass MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class PolicyGetResponse(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    app_count: Optional[int] = None
    """Number of access applications currently using this policy."""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[ConnectionRules] = None
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

    mfa_config: Optional[MfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    reusable: Optional[Literal[True]] = None

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None
