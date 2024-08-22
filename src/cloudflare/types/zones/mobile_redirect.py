# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["MobileRedirect", "Value"]

class Value(BaseModel):
    mobile_subdomain: Optional[str] = None
    """
    Which subdomain prefix you wish to redirect visitors on mobile devices to
    (subdomain must already exist).
    """

    status: Optional[Literal["on", "off"]] = None
    """
    Deprecated: Use Single Redirects instead
    https://developers.cloudflare.com/rules/url-forwarding/single-redirects/examples/#perform-mobile-redirects.
    Whether or not mobile redirect is enabled.
    """

    strip_uri: Optional[bool] = None
    """
    Whether to drop the current page path and redirect to the mobile subdomain URL
    root, or keep the path and redirect to the same page on the mobile subdomain.
    """

class MobileRedirect(BaseModel):
    id: Literal["mobile_redirect"]
    """Identifier of the zone setting."""

    value: Value
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""