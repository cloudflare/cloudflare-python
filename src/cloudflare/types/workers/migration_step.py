# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["MigrationStep", "RenamedClass", "TransferredClass"]

class RenamedClass(BaseModel):
    from_: Optional[str] = FieldInfo(alias = "from", default = None)

    to: Optional[str] = None

class TransferredClass(BaseModel):
    from_: Optional[str] = FieldInfo(alias = "from", default = None)

    from_script: Optional[str] = None

    to: Optional[str] = None

class MigrationStep(BaseModel):
    deleted_classes: Optional[List[str]] = None
    """A list of classes to delete Durable Object namespaces from."""

    new_classes: Optional[List[str]] = None
    """A list of classes to create Durable Object namespaces from."""

    renamed_classes: Optional[List[RenamedClass]] = None
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Optional[List[TransferredClass]] = None
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """