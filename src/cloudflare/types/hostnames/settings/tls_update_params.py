# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .setting_value_param import SettingValueParam

__all__ = ["TLSUpdateParams"]


class TLSUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    setting_id: Required[Literal["ciphers", "min_tls_version", "http2"]]
    """The TLS Setting name. The value type depends on the setting:

    - `ciphers`: value is an array of cipher suite strings (e.g.,
      `["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"]`)
    - `min_tls_version`: value is a TLS version string (`"1.0"`, `"1.1"`, `"1.2"`,
      or `"1.3"`)
    - `http2`: value is `"on"` or `"off"`
    """

    value: Required[SettingValueParam]
    """The TLS setting value.

    The type depends on the `setting_id` used in the request path:

    - `ciphers`: an array of allowed cipher suite strings in BoringSSL format (e.g.,
      `["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"]`)
    - `min_tls_version`: a string indicating the minimum TLS version — one of
      `"1.0"`, `"1.1"`, `"1.2"`, or `"1.3"` (e.g., `"1.2"`)
    - `http2`: a string indicating whether HTTP/2 is enabled — `"on"` or `"off"`
      (e.g., `"on"`)
    """
