# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PatternValidateParams"]


class PatternValidateParams(TypedDict, total=False):
    account_id: Required[str]

    regex: Required[str]

    max_match_bytes: Optional[int]
    """Maximum number of bytes that the regular expression can match.

    If this is `null` then there is no limit on the length. Patterns can use `*` and
    `+`. Otherwise repeats should use a range `{m,n}` to restrict patterns to the
    length. If this field is missing, then a default length limit is used.

    Note that the length is specified in bytes. Since regular expressions use UTF-8
    the pattern `.` can match up to 4 bytes. Hence `.{1,256}` has a maximum length
    of 1024 bytes.
    """
