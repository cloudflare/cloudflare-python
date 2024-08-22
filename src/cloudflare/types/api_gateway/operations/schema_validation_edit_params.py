# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .settings_multiple_request_param import SettingsMultipleRequestParam

__all__ = ["SchemaValidationEditParams"]


class SchemaValidationEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    settings_multiple_request: Required[SettingsMultipleRequestParam]
