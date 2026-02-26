# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

from ..approval_group_param import ApprovalGroupParam

__all__ = ["PolicyCreateParams", "ConnectionRules", "ConnectionRulesRDP", "MfaConfig"]


class PolicyCreateParams(TypedDict, total=False):
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

    connection_rules: ConnectionRules
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

    mfa_config: MfaConfig
    """Configures multi-factor authentication (MFA) settings."""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: str
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: bool
    """Require users to enter a justification when they log in to the application."""

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


class ConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class ConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: ConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_bypass: bool
    """Indicates whether to bypass MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """
