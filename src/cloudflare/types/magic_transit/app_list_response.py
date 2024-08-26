# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AppListResponse", "MagicAccountApp", "MagicManagedApp"]

class MagicAccountApp(BaseModel):
    account_app_id: str
    """Magic account app ID."""

    hostnames: Optional[List[str]] = None
    """FQDNs to associate with traffic decisions."""

    ip_subnets: Optional[List[str]] = None
    """CIDRs to associate with traffic decisions."""

    name: Optional[str] = None
    """Display name for the app."""

    type: Optional[str] = None
    """Category of the app."""

class MagicManagedApp(BaseModel):
    managed_app_id: str
    """Managed app ID."""

    hostnames: Optional[List[str]] = None
    """FQDNs to associate with traffic decisions."""

    ip_subnets: Optional[List[str]] = None
    """CIDRs to associate with traffic decisions."""

    name: Optional[str] = None
    """Display name for the app."""

    type: Optional[str] = None
    """Category of the app."""

AppListResponse: TypeAlias = Union[MagicAccountApp, MagicManagedApp]