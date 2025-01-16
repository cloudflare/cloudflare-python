# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "LifecycleUpdateParams",
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


class LifecycleUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    rules: Iterable[Rule]

    jurisdiction: Annotated[Literal["default", "eu", "fedramp"], PropertyInfo(alias="cf-r2-jurisdiction")]
    """The bucket jurisdiction"""


class RuleConditions(TypedDict, total=False):
    prefix: Required[str]
    """
    Transitions will only apply to objects/uploads in the bucket that start with the
    given prefix, an empty prefix can be provided to scope rule to all
    objects/uploads
    """


class RuleAbortMultipartUploadsTransitionCondition(TypedDict, total=False):
    max_age: Required[Annotated[int, PropertyInfo(alias="maxAge")]]

    type: Required[Literal["Age"]]


class RuleAbortMultipartUploadsTransition(TypedDict, total=False):
    condition: RuleAbortMultipartUploadsTransitionCondition
    """
    Condition for lifecycle transitions to apply after an object reaches an age in
    seconds
    """


class RuleDeleteObjectsTransitionConditionR2LifecycleAgeCondition(TypedDict, total=False):
    max_age: Required[Annotated[int, PropertyInfo(alias="maxAge")]]

    type: Required[Literal["Age"]]


class RuleDeleteObjectsTransitionConditionR2LifecycleDateCondition(TypedDict, total=False):
    date: Required[Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]]

    type: Required[Literal["Date"]]


RuleDeleteObjectsTransitionCondition: TypeAlias = Union[
    RuleDeleteObjectsTransitionConditionR2LifecycleAgeCondition,
    RuleDeleteObjectsTransitionConditionR2LifecycleDateCondition,
]


class RuleDeleteObjectsTransition(TypedDict, total=False):
    condition: RuleDeleteObjectsTransitionCondition
    """
    Condition for lifecycle transitions to apply after an object reaches an age in
    seconds
    """


class RuleStorageClassTransitionConditionR2LifecycleAgeCondition(TypedDict, total=False):
    max_age: Required[Annotated[int, PropertyInfo(alias="maxAge")]]

    type: Required[Literal["Age"]]


class RuleStorageClassTransitionConditionR2LifecycleDateCondition(TypedDict, total=False):
    date: Required[Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]]

    type: Required[Literal["Date"]]


RuleStorageClassTransitionCondition: TypeAlias = Union[
    RuleStorageClassTransitionConditionR2LifecycleAgeCondition,
    RuleStorageClassTransitionConditionR2LifecycleDateCondition,
]


class RuleStorageClassTransition(TypedDict, total=False):
    condition: Required[RuleStorageClassTransitionCondition]
    """
    Condition for lifecycle transitions to apply after an object reaches an age in
    seconds
    """

    storage_class: Required[Annotated[Literal["InfrequentAccess"], PropertyInfo(alias="storageClass")]]


class Rule(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for this rule"""

    conditions: Required[RuleConditions]
    """Conditions that apply to all transitions of this rule"""

    enabled: Required[bool]
    """Whether or not this rule is in effect"""

    abort_multipart_uploads_transition: Annotated[
        RuleAbortMultipartUploadsTransition, PropertyInfo(alias="abortMultipartUploadsTransition")
    ]
    """Transition to abort ongoing multipart uploads"""

    delete_objects_transition: Annotated[RuleDeleteObjectsTransition, PropertyInfo(alias="deleteObjectsTransition")]
    """Transition to delete objects"""

    storage_class_transitions: Annotated[
        Iterable[RuleStorageClassTransition], PropertyInfo(alias="storageClassTransitions")
    ]
    """Transitions to change the storage class of objects"""
