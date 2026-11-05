# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["FindingTypeValidateResponse", "Error"]


class Error(BaseModel):
    detail: str
    """Description of the problem."""

    message: str
    """Deprecated: use `detail`."""

    code: Optional[str] = None
    """Machine-readable identifier for the class of problem, when one is available.

    Omitted otherwise.
    """

    column: Optional[int] = None
    """1-based column on `line`.

    Omitted when the problem could not be located in the submitted source.
    """

    field: Optional[str] = None
    """
    Request field the problem belongs to, matching the property names of
    `ValidateFindingTypeRequest`. Array properties are reported per entry with a
    zero-based index, for example `integration_ids[0]`. Empty when the problem
    cannot be attributed to a single submitted field.
    """

    line: Optional[int] = None
    """1-based line in `expression` where the problem was found.

    Omitted when the problem could not be located in the submitted source.
    """


class FindingTypeValidateResponse(BaseModel):
    errors: List[Error]
    """Every problem found with the candidate, so all of them can be surfaced at once.

    Empty when `valid` is true. Problems without a location come first, followed by
    located problems ordered by `line`, then `column`.
    """

    valid: bool
    """Whether the candidate finding type would be accepted as-is."""
