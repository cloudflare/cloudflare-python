# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OSVersionInputParam"]


class OSVersionInputParam(TypedDict, total=False):
    operating_system: Required[Literal["windows"]]
    """Operating System"""

    operator: Required[Literal["<", "<=", ">", ">=", "=="]]
    """operator"""

    version: Required[str]
    """Version of OS"""

    os_distro_name: str
    """Operating System Distribution Name (linux only)"""

    os_distro_revision: str
    """Version of OS Distribution (linux only)"""

    os_version_extra: str
    """Additional version data.

    For Mac or iOS, the Product Version Extra. For Linux, the kernel release
    version. (Mac, iOS, and Linux only)
    """
