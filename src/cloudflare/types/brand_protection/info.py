# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Info"]


class Info(BaseModel):
    categorizations: Optional[List[object]] = None
    """List of categorizations applied to this submission."""

    ai_model_results: Optional[List[object]] = FieldInfo(alias="model_results", default=None)
    """List of model results for completed scans."""

    rule_matches: Optional[List[object]] = None
    """
    List of signatures that matched against site content found when crawling the
    URL.
    """

    scan_status: Optional[object] = None

    screenshot_download_signature: Optional[str] = None
    """For internal use."""

    screenshot_path: Optional[str] = None
    """For internal use."""

    url: Optional[str] = None
    """URL that was submitted."""
