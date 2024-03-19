# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntelPhishingURLInfo", "Categorization", "ModelResult", "RuleMatch", "ScanStatus"]


class Categorization(BaseModel):
    category: Optional[str] = None
    """Name of the category applied."""

    verification_status: Optional[str] = None
    """Result of human review for this categorization."""


class ModelResult(BaseModel):
    ai_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """Name of the model."""

    ai_model_score: Optional[float] = FieldInfo(alias="model_score", default=None)
    """Score output by the model for this submission."""


class RuleMatch(BaseModel):
    banning: Optional[bool] = None
    """For internal use."""

    blocking: Optional[bool] = None
    """For internal use."""

    description: Optional[str] = None
    """Description of the signature that matched."""

    name: Optional[str] = None
    """Name of the signature that matched."""


class ScanStatus(BaseModel):
    last_processed: Optional[str] = None
    """Timestamp of when the submission was processed."""

    scan_complete: Optional[bool] = None
    """For internal use."""

    status_code: Optional[int] = None
    """Status code that the crawler received when loading the submitted URL."""

    submission_id: Optional[int] = None
    """ID of the most recent submission."""


class IntelPhishingURLInfo(BaseModel):
    categorizations: Optional[List[Categorization]] = None
    """List of categorizations applied to this submission."""

    ai_model_results: Optional[List[ModelResult]] = FieldInfo(alias="model_results", default=None)
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
