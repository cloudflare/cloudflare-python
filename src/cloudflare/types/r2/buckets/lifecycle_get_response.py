# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "LifecycleGetResponse",
    "Rule",
    "RuleConditions",
    "RuleAbortMultipartUploadsTransition",
    "RuleAbortMultipartUploadsTransitionCondition",
    "RuleDeleteObjectsTransition",
    "RuleDeleteObjectsTransitionCondition",
    "RuleDeleteObjectsTransitionConditionR2LifecycleAgeCondition",
    "RuleDeleteObjectsTransitionConditionR2LifecycleDateCondition",
    "RuleStorageClassTransition",
    "RuleStorageClassTransitionCondition",
    "RuleStorageClassTransitionConditionR2LifecycleAgeCondition",
    "RuleStorageClassTransitionConditionR2LifecycleDateCondition",
]


class RuleConditions(BaseModel):
    prefix: str
    """
    Transitions will only apply to objects/uploads in the bucket that start with the
    given prefix, an empty prefix can be provided to scope rule to all
    objects/uploads
    """


class RuleAbortMultipartUploadsTransitionCondition(BaseModel):
    max_age: int = FieldInfo(alias="maxAge")

    type: Literal["Age"]


class RuleAbortMultipartUploadsTransition(BaseModel):
    condition: Optional[RuleAbortMultipartUploadsTransitionCondition] = None
    """
    Condition for lifecycle transitions to apply after an object reaches an age in
    seconds
    """


class RuleDeleteObjectsTransitionConditionR2LifecycleAgeCondition(BaseModel):
    max_age: int = FieldInfo(alias="maxAge")

    type: Literal["Age"]


class RuleDeleteObjectsTransitionConditionR2LifecycleDateCondition(BaseModel):
    date: datetime.date

    type: Literal["Date"]


RuleDeleteObjectsTransitionCondition: TypeAlias = Union[
    RuleDeleteObjectsTransitionConditionR2LifecycleAgeCondition,
    RuleDeleteObjectsTransitionConditionR2LifecycleDateCondition,
]


class RuleDeleteObjectsTransition(BaseModel):
    condition: Optional[RuleDeleteObjectsTransitionCondition] = None
    """
    Condition for lifecycle transitions to apply after an object reaches an age in
    seconds
    """


class RuleStorageClassTransitionConditionR2LifecycleAgeCondition(BaseModel):
    max_age: int = FieldInfo(alias="maxAge")

    type: Literal["Age"]


class RuleStorageClassTransitionConditionR2LifecycleDateCondition(BaseModel):
    date: datetime.date

    type: Literal["Date"]


RuleStorageClassTransitionCondition: TypeAlias = Union[
    RuleStorageClassTransitionConditionR2LifecycleAgeCondition,
    RuleStorageClassTransitionConditionR2LifecycleDateCondition,
]


class RuleStorageClassTransition(BaseModel):
    condition: RuleStorageClassTransitionCondition
    """
    Condition for lifecycle transitions to apply after an object reaches an age in
    seconds
    """

    storage_class: Literal["InfrequentAccess"] = FieldInfo(alias="storageClass")


class Rule(BaseModel):
    id: str
    """Unique identifier for this rule"""

    conditions: RuleConditions
    """Conditions that apply to all transitions of this rule"""

    enabled: bool
    """Whether or not this rule is in effect"""

    abort_multipart_uploads_transition: Optional[RuleAbortMultipartUploadsTransition] = FieldInfo(
        alias="abortMultipartUploadsTransition", default=None
    )
    """Transition to abort ongoing multipart uploads"""

    delete_objects_transition: Optional[RuleDeleteObjectsTransition] = FieldInfo(
        alias="deleteObjectsTransition", default=None
    )
    """Transition to delete objects"""

    storage_class_transitions: Optional[List[RuleStorageClassTransition]] = FieldInfo(
        alias="storageClassTransitions", default=None
    )
    """Transitions to change the storage class of objects"""


class LifecycleGetResponse(BaseModel):
    rules: Optional[List[Rule]] = None
