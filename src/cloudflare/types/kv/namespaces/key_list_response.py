# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["KeyListResponse", "KeyListResponseItem"]


class KeyListResponseItem(BaseModel):
    name: str
    """A key's name.

    The name may be at most 512 bytes. All printable, non-whitespace characters are
    valid. Use percent-encoding to define key names as part of a URL.
    """

    expiration: Optional[float] = None
    """
    The time, measured in number of seconds since the UNIX epoch, at which the key
    will expire. This property is omitted for keys that will not expire.
    """

    metadata: Optional[object] = None
    """Arbitrary JSON that is associated with a key."""


KeyListResponse = List[KeyListResponseItem]
