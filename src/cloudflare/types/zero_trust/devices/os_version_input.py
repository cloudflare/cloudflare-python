# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["OSVersionInput"]


class OSVersionInput(BaseModel):
    operating_system: Literal["windows"]
    """Operating System"""

    operator: Literal["<", "<=", ">", ">=", "=="]
    """operator"""

    version: str
    """Version of OS"""

    os_distro_name: Optional[str] = None
    """Operating System Distribution Name (linux only)"""

    os_distro_revision: Optional[str] = None
    """Version of OS Distribution (linux only)"""

    os_version_extra: Optional[str] = None
    """Additional version data.

    For Mac or iOS, the Product Version Extra. For Linux, the kernel release
    version. (Mac, iOS, and Linux only)
    """
