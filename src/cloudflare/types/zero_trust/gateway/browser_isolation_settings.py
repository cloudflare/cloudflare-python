# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["BrowserIsolationSettings"]

class BrowserIsolationSettings(BaseModel):
    non_identity_enabled: Optional[bool] = None
    """Enable non-identity onramp support for Browser Isolation."""

    url_browser_isolation_enabled: Optional[bool] = None
    """Enable Clientless Browser Isolation."""