# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "EventNotificationGetResponse",
    "Conditions",
    "AbortMultipartUploadsTransition",
    "AbortMultipartUploadsTransitionCondition",
    "DeleteObjectsTransition",
    "DeleteObjectsTransitionCondition",
    "DeleteObjectsTransitionConditionR2LifecycleAgeCondition",
    "DeleteObjectsTransitionConditionR2LifecycleDateCondition",
    "StorageClassTransition",
    "StorageClassTransitionCondition",
    "StorageClassTransitionConditionR2LifecycleAgeCondition",
    "StorageClassTransitionConditionR2LifecycleDateCondition",
]


class Conditions(BaseModel):
    prefix: str
    """
    Transitions will only apply to objects/uploads in the bucket that start with the
    given prefix, an empty prefix can be provided to scope rule to all
    objects/uploads.
    """


class AbortMultipartUploadsTransitionCondition(BaseModel):
    max_age: int = FieldInfo(alias="maxAge")

    type: Literal["Age"]


class AbortMultipartUploadsTransition(BaseModel):
    condition: Optional[AbortMultipartUploadsTransitionCondition] = None
    """
    Condition for lifecycle transitions to apply after an object reaches an age in
    seconds.
    """


class DeleteObjectsTransitionConditionR2LifecycleAgeCondition(BaseModel):
    max_age: int = FieldInfo(alias="maxAge")

    type: Literal["Age"]


class DeleteObjectsTransitionConditionR2LifecycleDateCondition(BaseModel):
    date: datetime.date

    type: Literal["Date"]


DeleteObjectsTransitionCondition: TypeAlias = Union[
    DeleteObjectsTransitionConditionR2LifecycleAgeCondition, DeleteObjectsTransitionConditionR2LifecycleDateCondition
]


class DeleteObjectsTransition(BaseModel):
    condition: Optional[DeleteObjectsTransitionCondition] = None
    """
    Condition for lifecycle transitions to apply after an object reaches an age in
    seconds.
    """


class StorageClassTransitionConditionR2LifecycleAgeCondition(BaseModel):
    max_age: int = FieldInfo(alias="maxAge")

    type: Literal["Age"]


class StorageClassTransitionConditionR2LifecycleDateCondition(BaseModel):
    date: datetime.date

    type: Literal["Date"]


StorageClassTransitionCondition: TypeAlias = Union[
    StorageClassTransitionConditionR2LifecycleAgeCondition, StorageClassTransitionConditionR2LifecycleDateCondition
]


class StorageClassTransition(BaseModel):
    condition: StorageClassTransitionCondition
    """
    Condition for lifecycle transitions to apply after an object reaches an age in
    seconds.
    """

    storage_class: Literal["InfrequentAccess"] = FieldInfo(alias="storageClass")


class EventNotificationGetResponse(BaseModel):
    id: str
    """Unique identifier for this rule."""

    conditions: Conditions
    """Conditions that apply to all transitions of this rule."""

    enabled: bool
    """Whether or not this rule is in effect."""

    abort_multipart_uploads_transition: Optional[AbortMultipartUploadsTransition] = FieldInfo(
        alias="abortMultipartUploadsTransition", default=None
    )
    """Transition to abort ongoing multipart uploads."""

    delete_objects_transition: Optional[DeleteObjectsTransition] = FieldInfo(
        alias="deleteObjectsTransition", default=None
    )
    """Transition to delete objects."""

    storage_class_transitions: Optional[List[StorageClassTransition]] = FieldInfo(
        alias="storageClassTransitions", default=None
    )
    """Transitions to change the storage class of objects."""
