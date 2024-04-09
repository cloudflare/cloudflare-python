# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .unnamed_schema_ref_3e10ea08deb8102a27500f986488c1e8 import UnnamedSchemaRef3e10ea08deb8102a27500f986488c1e8
from .unnamed_schema_ref_9b4c9779a35b172cb69c71389ebc7014 import UnnamedSchemaRef9b4c9779a35b172cb69c71389ebc7014
from .unnamed_schema_ref_209db30ed499548152d6f3bccf720b54 import UnnamedSchemaRef209db30ed499548152d6f3bccf720b54
from .unnamed_schema_ref_a64e2a18a86750b6bd72cdf37ecfd869 import UnnamedSchemaRefA64e2a18a86750b6bd72cdf37ecfd869

__all__ = ["Info"]


class Info(BaseModel):
    categorizations: Optional[List[UnnamedSchemaRef209db30ed499548152d6f3bccf720b54]] = None
    """List of categorizations applied to this submission."""

    ai_model_results: Optional[List[UnnamedSchemaRef9b4c9779a35b172cb69c71389ebc7014]] = FieldInfo(
        alias="model_results", default=None
    )
    """List of model results for completed scans."""

    rule_matches: Optional[List[UnnamedSchemaRef3e10ea08deb8102a27500f986488c1e8]] = None
    """
    List of signatures that matched against site content found when crawling the
    URL.
    """

    scan_status: Optional[UnnamedSchemaRefA64e2a18a86750b6bd72cdf37ecfd869] = None
    """Status of the most recent scan found."""

    screenshot_download_signature: Optional[str] = None
    """For internal use."""

    screenshot_path: Optional[str] = None
    """For internal use."""

    url: Optional[str] = None
    """URL that was submitted."""
