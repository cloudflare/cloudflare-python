# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExternalEvaluationRuleParam", "ExternalEvaluation"]


class ExternalEvaluation(TypedDict, total=False):
    evaluate_url: Required[str]
    """The API endpoint containing your business logic."""

    keys_url: Required[str]
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class ExternalEvaluationRuleParam(TypedDict, total=False):
    external_evaluation: Required[ExternalEvaluation]
