# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, Dict

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Key"]

class Key(BaseModel):
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

    metadata: Optional[Dict[str, object]] = None
    """Arbitrary JSON that is associated with a key."""