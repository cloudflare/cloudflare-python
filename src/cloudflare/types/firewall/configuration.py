# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .lockdown_ip_configuration import LockdownIPConfiguration

from .lockdown_cidr_configuration import LockdownCIDRConfiguration

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Configuration"]

Configuration: TypeAlias = Union[LockdownIPConfiguration, LockdownCIDRConfiguration]
