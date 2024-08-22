# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from .url_info_model_results import URLInfoModelResults

from .rule_match import RuleMatch

from .scan_status import ScanStatus

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Info", "Categorization"]

class Categorization(BaseModel):
    category: Optional[str] = None
    """Name of the category applied."""

    verification_status: Optional[str] = None
    """Result of human review for this categorization."""

class Info(BaseModel):
    categorizations: Optional[List[Categorization]] = None
    """List of categorizations applied to this submission."""

    ai_model_results: Optional[List[URLInfoModelResults]] = FieldInfo(alias = "model_results", default = None)
    """List of model results for completed scans."""

    rule_matches: Optional[List[RuleMatch]] = None
    """
    List of signatures that matched against site content found when crawling the
    URL.
    """

    scan_status: Optional[ScanStatus] = None
    """Status of the most recent scan found."""

    screenshot_download_signature: Optional[str] = None
    """For internal use."""

    screenshot_path: Optional[str] = None
    """For internal use."""

    url: Optional[str] = None
    """URL that was submitted."""