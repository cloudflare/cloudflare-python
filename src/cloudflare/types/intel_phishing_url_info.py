# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .shared import UnnamedSchemaRef13, UnnamedSchemaRef14, UnnamedSchemaRef15, UnnamedSchemaRef16
from .._models import BaseModel

__all__ = ["IntelPhishingURLInfo"]


class IntelPhishingURLInfo(BaseModel):
    categorizations: Optional[List[UnnamedSchemaRef13]] = None
    """List of categorizations applied to this submission."""

    ai_model_results: Optional[List[UnnamedSchemaRef14]] = FieldInfo(alias="model_results", default=None)
    """List of model results for completed scans."""

    rule_matches: Optional[List[UnnamedSchemaRef15]] = None
    """
    List of signatures that matched against site content found when crawling the
    URL.
    """

    scan_status: Optional[UnnamedSchemaRef16] = None
    """Status of the most recent scan found."""

    screenshot_download_signature: Optional[str] = None
    """For internal use."""

    screenshot_path: Optional[str] = None
    """For internal use."""

    url: Optional[str] = None
    """URL that was submitted."""
