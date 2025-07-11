# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BotListParams"]


class BotListParams(TypedDict, total=False):
    bot_category: Annotated[
        Literal[
            "SEARCH_ENGINE_CRAWLER",
            "SEARCH_ENGINE_OPTIMIZATION",
            "MONITORING_AND_ANALYTICS",
            "ADVERTISING_AND_MARKETING",
            "SOCIAL_MEDIA_MARKETING",
            "PAGE_PREVIEW",
            "ACADEMIC_RESEARCH",
            "SECURITY",
            "ACCESSIBILITY",
            "WEBHOOKS",
            "FEED_FETCHER",
            "AI_CRAWLER",
            "AGGREGATOR",
            "AI_ASSISTANT",
            "AI_SEARCH",
            "ARCHIVER",
        ],
        PropertyInfo(alias="botCategory"),
    ]
    """Filters results by bot category."""

    bot_operator: Annotated[str, PropertyInfo(alias="botOperator")]
    """Filters results by bot operator."""

    bot_verification_status: Annotated[Literal["VERIFIED"], PropertyInfo(alias="botVerificationStatus")]
    """Filters results by bot verification status."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    limit: int
    """Limits the number of objects returned in the response."""

    offset: int
    """Skips the specified number of objects before fetching the results."""
