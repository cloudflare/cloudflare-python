# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from .skip_configuration import SkipConfiguration

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ContextAwareness"]


class ContextAwareness(BaseModel):
    enabled: bool
    """
    If true, scan the context of predefined entries to only return matches
    surrounded by keywords.
    """

    skip: SkipConfiguration
    """Content types to exclude from context analysis and return all matches."""
