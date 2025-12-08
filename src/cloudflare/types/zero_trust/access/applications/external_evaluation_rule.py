# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["ExternalEvaluationRule", "ExternalEvaluation"]


class ExternalEvaluation(BaseModel):
    evaluate_url: str
    """The API endpoint containing your business logic."""

    keys_url: str
    """
    The API endpoint containing the key that Access uses to verify that the response
    came from your API.
    """


class ExternalEvaluationRule(BaseModel):
    """
    Create Allow or Block policies which evaluate the user based on custom criteria.
    """

    external_evaluation: ExternalEvaluation
