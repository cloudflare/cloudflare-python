# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .unnamed_schema_ref_44e66100b948bfe723054c56b6144766 import UnnamedSchemaRef44e66100b948bfe723054c56b6144766
from .unnamed_schema_ref_767c0981cf47f45f0c766253dbd18669 import UnnamedSchemaRef767c0981cf47f45f0c766253dbd18669
from .unnamed_schema_ref_39419d70e2399b28b15cd660afd342fb import UnnamedSchemaRef39419d70e2399b28b15cd660afd342fb

__all__ = ["Submit"]


class Submit(BaseModel):
    excluded_urls: Optional[List[UnnamedSchemaRef767c0981cf47f45f0c766253dbd18669]] = None
    """
    URLs that were excluded from scanning because their domain is in our no-scan
    list.
    """

    skipped_urls: Optional[List[UnnamedSchemaRef44e66100b948bfe723054c56b6144766]] = None
    """URLs that were skipped because the same URL is currently being scanned"""

    submitted_urls: Optional[List[UnnamedSchemaRef39419d70e2399b28b15cd660afd342fb]] = None
    """URLs that were successfully submitted for scanning."""
