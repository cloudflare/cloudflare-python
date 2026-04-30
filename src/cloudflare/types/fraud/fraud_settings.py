# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "FraudSettings",
    "AuthenticationSettings",
    "AuthenticationSettingsFailureCriteria",
    "AuthenticationSettingsSuccessCriteria",
]


class AuthenticationSettingsFailureCriteria(BaseModel):
    """Criterion for identifying failed login responses."""

    kind: Literal["status_code"]
    """The type of criterion. Currently only `status_code` is supported."""

    status_codes: Optional[List[int]] = None
    """HTTP status codes to match against the origin response.

    - Maximum of 10 codes per criterion.
    - Each code must be a valid HTTP status code (100-599).
    - Codes are deduplicated and sorted on save.
    - Omit to leave unchanged on update.
    - Provide an empty array `[]` to clear codes on update.
    """


class AuthenticationSettingsSuccessCriteria(BaseModel):
    """Criterion for identifying successful login responses."""

    kind: Literal["status_code"]
    """The type of criterion. Currently only `status_code` is supported."""

    status_codes: Optional[List[int]] = None
    """HTTP status codes to match against the origin response.

    - Maximum of 10 codes per criterion.
    - Each code must be a valid HTTP status code (100-599).
    - Codes are deduplicated and sorted on save.
    - Omit to leave unchanged on update.
    - Provide an empty array `[]` to clear codes on update.
    """


class AuthenticationSettings(BaseModel):
    """
    Configuration for classifying login authentication outcomes based on the origin response.
    Requires `user_profiles` to be enabled.

    - Success and failure criteria are independently updatable — sending only `success_criteria`
      leaves failure codes untouched, and vice versa.
    - Omit `authentication_settings` entirely to leave both unchanged.
    - Status codes must not overlap between success and failure criteria.
    """

    failure_criteria: Optional[AuthenticationSettingsFailureCriteria] = None
    """Criterion for identifying failed login responses."""

    success_criteria: Optional[AuthenticationSettingsSuccessCriteria] = None
    """Criterion for identifying successful login responses."""


class FraudSettings(BaseModel):
    authentication_settings: Optional[AuthenticationSettings] = None
    """
    Configuration for classifying login authentication outcomes based on the origin
    response. Requires `user_profiles` to be enabled.

    - Success and failure criteria are independently updatable — sending only
      `success_criteria` leaves failure codes untouched, and vice versa.
    - Omit `authentication_settings` entirely to leave both unchanged.
    - Status codes must not overlap between success and failure criteria.
    """

    user_profiles: Optional[Literal["enabled", "disabled"]] = None
    """Whether Fraud User Profiles is enabled for the zone."""

    username_expressions: Optional[List[str]] = None
    """List of expressions to detect usernames in write HTTP requests.

    - Maximum of 10 expressions.
    - Omit or set to null to leave unchanged on update.
    - Provide an empty array `[]` to clear all expressions on update.
    - Invalid expressions will result in a 10400 Bad Request with details in the
      `messages` array.
    """
