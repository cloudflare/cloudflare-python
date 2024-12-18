# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["EvaluationCreateParams"]


class EvaluationCreateParams(TypedDict, total=False):
    account_id: Required[str]

    dataset_ids: Required[List[str]]

    evaluation_type_ids: Required[List[str]]

    name: Required[str]
