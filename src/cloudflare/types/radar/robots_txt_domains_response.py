# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RobotsTXTDomainsResponse", "Domain"]

class Domain(BaseModel):
    : str = FieldInfo(alias = "*")

    amazonbot: str

    categories_parent: str

    categories_sub: str

    domain: str

class RobotsTXTDomainsResponse(BaseModel):
    date: str

    domains: List[Domain]

    user_agents: List[str] = FieldInfo(alias = "userAgents")