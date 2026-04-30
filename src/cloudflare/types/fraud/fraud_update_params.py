# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "FraudUpdateParams",
    "AuthenticationSettings",
    "AuthenticationSettingsFailureCriteria",
    "AuthenticationSettingsSuccessCriteria",
]


class FraudUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    authentication_settings: AuthenticationSettings
    """
    Configuration for classifying login authentication outcomes based on the origin
    response. Requires `user_profiles` to be enabled.

    - Success and failure criteria are independently updatable — sending only
      `success_criteria` leaves failure codes untouched, and vice versa.
    - Omit `authentication_settings` entirely to leave both unchanged.
    - Status codes must not overlap between success and failure criteria.
    """

    user_profiles: Literal["enabled", "disabled"]
    """Whether Fraud User Profiles is enabled for the zone."""

    username_expressions: SequenceNotStr[str]
    """List of expressions to detect usernames in write HTTP requests.

    - Maximum of 10 expressions.
    - Omit or set to null to leave unchanged on update.
    - Provide an empty array `[]` to clear all expressions on update.
    - Invalid expressions will result in a 10400 Bad Request with details in the
      `messages` array.
    """


class AuthenticationSettingsFailureCriteria(TypedDict, total=False):
    """Criterion for identifying failed login responses."""

    kind: Required[Literal["status_code"]]
    """The type of criterion. Currently only `status_code` is supported."""

    status_codes: Iterable[int]
    """HTTP status codes to match against the origin response.

    - Maximum of 10 codes per criterion.
    - Each code must be a valid HTTP status code (100-599).
    - Codes are deduplicated and sorted on save.
    - Omit to leave unchanged on update.
    - Provide an empty array `[]` to clear codes on update.
    """


class AuthenticationSettingsSuccessCriteria(TypedDict, total=False):
    """Criterion for identifying successful login responses."""

    kind: Required[Literal["status_code"]]
    """The type of criterion. Currently only `status_code` is supported."""

    status_codes: Iterable[int]
    """HTTP status codes to match against the origin response.

    - Maximum of 10 codes per criterion.
    - Each code must be a valid HTTP status code (100-599).
    - Codes are deduplicated and sorted on save.
    - Omit to leave unchanged on update.
    - Provide an empty array `[]` to clear codes on update.
    """


class AuthenticationSettings(TypedDict, total=False):
    """
    Configuration for classifying login authentication outcomes based on the origin response.
    Requires `user_profiles` to be enabled.

    - Success and failure criteria are independently updatable — sending only `success_criteria`
      leaves failure codes untouched, and vice versa.
    - Omit `authentication_settings` entirely to leave both unchanged.
    - Status codes must not overlap between success and failure criteria.
    """

    failure_criteria: AuthenticationSettingsFailureCriteria
    """Criterion for identifying failed login responses."""

    success_criteria: AuthenticationSettingsSuccessCriteria
    """Criterion for identifying successful login responses."""
