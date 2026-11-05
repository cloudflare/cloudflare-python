# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ....._types import SequenceNotStr
from ..profiles.pattern_param import PatternParam

__all__ = ["CustomUpdateParams"]


class CustomUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    enabled: Required[bool]

    name: Required[str]

    pattern: Required[PatternParam]

    description: Optional[str]

    validator_ids: SequenceNotStr[str]
    """Validators this entry should reference, by id, at most 10.

    Replaces the current set.

    Optional, unlike the rest of this body: omitting it leaves the current
    attachments alone, so a client that predates validators cannot detach them by
    accident. Send `[]` to detach.
    """
