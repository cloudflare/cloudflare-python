# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .setting_value import SettingValue

__all__ = ["TLSGetResponse"]


class TLSGetResponse(BaseModel):
    created_at: Optional[datetime] = None
    """This is the time the tls setting was originally created for this hostname."""

    hostname: Optional[str] = None
    """The hostname for which the tls settings are set."""

    status: Optional[str] = None
    """Deployment status for the given tls setting."""

    updated_at: Optional[datetime] = None
    """This is the time the tls setting was updated."""

    value: Optional[SettingValue] = None
    """The TLS setting value.

    The type depends on the `setting_id` used in the request path:

    - `ciphers`: an array of allowed cipher suite strings in BoringSSL format (e.g.,
      `["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"]`)
    - `min_tls_version`: a string indicating the minimum TLS version — one of
      `"1.0"`, `"1.1"`, `"1.2"`, or `"1.3"` (e.g., `"1.2"`)
    - `http2`: a string indicating whether HTTP/2 is enabled — `"on"` or `"off"`
      (e.g., `"on"`)
    """
