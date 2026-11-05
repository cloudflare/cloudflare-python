# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["UserPopulationUpdateResponse"]


class UserPopulationUpdateResponse(BaseModel):
    id: str
    """UUID."""

    name: str
    """The name of the user population.

    Leading and trailing whitespace is trimmed before validation. After trimming,
    the name must contain at least one non-whitespace character and must not exceed
    128 UTF-8 bytes.
    """
