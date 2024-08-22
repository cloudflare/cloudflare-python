# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SingleStepMigration", "RenamedClass", "TransferredClass"]


class RenamedClass(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    to: Optional[str] = None


class TransferredClass(BaseModel):
    from_: Optional[str] = FieldInfo(alias="from", default=None)

    from_script: Optional[str] = None

    to: Optional[str] = None


class SingleStepMigration(BaseModel):
    deleted_classes: Optional[List[str]] = None
    """A list of classes to delete Durable Object namespaces from."""

    new_classes: Optional[List[str]] = None
    """A list of classes to create Durable Object namespaces from."""

    new_tag: Optional[str] = None
    """Tag to set as the latest migration tag."""

    old_tag: Optional[str] = None
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    renamed_classes: Optional[List[RenamedClass]] = None
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Optional[List[TransferredClass]] = None
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """
