# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesParams"]


class ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesParams(TypedDict, total=False):
    properties: List[Literal["auth_id_characteristics"]]
    """Requests information about certain properties."""
