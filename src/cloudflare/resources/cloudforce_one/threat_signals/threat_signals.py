# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .search import (
    SearchResource,
    AsyncSearchResource,
    SearchResourceWithRawResponse,
    AsyncSearchResourceWithRawResponse,
    SearchResourceWithStreamingResponse,
    AsyncSearchResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .categories import (
    CategoriesResource,
    AsyncCategoriesResource,
    CategoriesResourceWithRawResponse,
    AsyncCategoriesResourceWithRawResponse,
    CategoriesResourceWithStreamingResponse,
    AsyncCategoriesResourceWithStreamingResponse,
)
from .indicators import (
    IndicatorsResource,
    AsyncIndicatorsResource,
    IndicatorsResourceWithRawResponse,
    AsyncIndicatorsResourceWithRawResponse,
    IndicatorsResourceWithStreamingResponse,
    AsyncIndicatorsResourceWithStreamingResponse,
)
from .feeds.feeds import (
    FeedsResource,
    AsyncFeedsResource,
    FeedsResourceWithRawResponse,
    AsyncFeedsResourceWithRawResponse,
    FeedsResourceWithStreamingResponse,
    AsyncFeedsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .skills.skills import (
    SkillsResource,
    AsyncSkillsResource,
    SkillsResourceWithRawResponse,
    AsyncSkillsResourceWithRawResponse,
    SkillsResourceWithStreamingResponse,
    AsyncSkillsResourceWithStreamingResponse,
)
from .articles.articles import (
    ArticlesResource,
    AsyncArticlesResource,
    ArticlesResourceWithRawResponse,
    AsyncArticlesResourceWithRawResponse,
    ArticlesResourceWithStreamingResponse,
    AsyncArticlesResourceWithStreamingResponse,
)

__all__ = ["ThreatSignalsResource", "AsyncThreatSignalsResource"]


class ThreatSignalsResource(SyncAPIResource):
    """
    Threat Signals API for managing threat intelligence feeds, articles, indicators, and AI skills in Cloudforce One.

    ## Prerequisites

    1. **API token** — requests must use an API token with Cloudforce One permissions; write operations (creating, editing, or deleting feeds, skills, and tags) require write access.
    2. **Plan limits** — access on the Free plan is limited; feed quotas and managed default skills apply.
    """

    @cached_property
    def search(self) -> SearchResource:
        return SearchResource(self._client)

    @cached_property
    def categories(self) -> CategoriesResource:
        return CategoriesResource(self._client)

    @cached_property
    def feeds(self) -> FeedsResource:
        return FeedsResource(self._client)

    @cached_property
    def articles(self) -> ArticlesResource:
        return ArticlesResource(self._client)

    @cached_property
    def indicators(self) -> IndicatorsResource:
        return IndicatorsResource(self._client)

    @cached_property
    def skills(self) -> SkillsResource:
        return SkillsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ThreatSignalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ThreatSignalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ThreatSignalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ThreatSignalsResourceWithStreamingResponse(self)


class AsyncThreatSignalsResource(AsyncAPIResource):
    """
    Threat Signals API for managing threat intelligence feeds, articles, indicators, and AI skills in Cloudforce One.

    ## Prerequisites

    1. **API token** — requests must use an API token with Cloudforce One permissions; write operations (creating, editing, or deleting feeds, skills, and tags) require write access.
    2. **Plan limits** — access on the Free plan is limited; feed quotas and managed default skills apply.
    """

    @cached_property
    def search(self) -> AsyncSearchResource:
        return AsyncSearchResource(self._client)

    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        return AsyncCategoriesResource(self._client)

    @cached_property
    def feeds(self) -> AsyncFeedsResource:
        return AsyncFeedsResource(self._client)

    @cached_property
    def articles(self) -> AsyncArticlesResource:
        return AsyncArticlesResource(self._client)

    @cached_property
    def indicators(self) -> AsyncIndicatorsResource:
        return AsyncIndicatorsResource(self._client)

    @cached_property
    def skills(self) -> AsyncSkillsResource:
        return AsyncSkillsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncThreatSignalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncThreatSignalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncThreatSignalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncThreatSignalsResourceWithStreamingResponse(self)


class ThreatSignalsResourceWithRawResponse:
    def __init__(self, threat_signals: ThreatSignalsResource) -> None:
        self._threat_signals = threat_signals

    @cached_property
    def search(self) -> SearchResourceWithRawResponse:
        return SearchResourceWithRawResponse(self._threat_signals.search)

    @cached_property
    def categories(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self._threat_signals.categories)

    @cached_property
    def feeds(self) -> FeedsResourceWithRawResponse:
        return FeedsResourceWithRawResponse(self._threat_signals.feeds)

    @cached_property
    def articles(self) -> ArticlesResourceWithRawResponse:
        return ArticlesResourceWithRawResponse(self._threat_signals.articles)

    @cached_property
    def indicators(self) -> IndicatorsResourceWithRawResponse:
        return IndicatorsResourceWithRawResponse(self._threat_signals.indicators)

    @cached_property
    def skills(self) -> SkillsResourceWithRawResponse:
        return SkillsResourceWithRawResponse(self._threat_signals.skills)


class AsyncThreatSignalsResourceWithRawResponse:
    def __init__(self, threat_signals: AsyncThreatSignalsResource) -> None:
        self._threat_signals = threat_signals

    @cached_property
    def search(self) -> AsyncSearchResourceWithRawResponse:
        return AsyncSearchResourceWithRawResponse(self._threat_signals.search)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self._threat_signals.categories)

    @cached_property
    def feeds(self) -> AsyncFeedsResourceWithRawResponse:
        return AsyncFeedsResourceWithRawResponse(self._threat_signals.feeds)

    @cached_property
    def articles(self) -> AsyncArticlesResourceWithRawResponse:
        return AsyncArticlesResourceWithRawResponse(self._threat_signals.articles)

    @cached_property
    def indicators(self) -> AsyncIndicatorsResourceWithRawResponse:
        return AsyncIndicatorsResourceWithRawResponse(self._threat_signals.indicators)

    @cached_property
    def skills(self) -> AsyncSkillsResourceWithRawResponse:
        return AsyncSkillsResourceWithRawResponse(self._threat_signals.skills)


class ThreatSignalsResourceWithStreamingResponse:
    def __init__(self, threat_signals: ThreatSignalsResource) -> None:
        self._threat_signals = threat_signals

    @cached_property
    def search(self) -> SearchResourceWithStreamingResponse:
        return SearchResourceWithStreamingResponse(self._threat_signals.search)

    @cached_property
    def categories(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self._threat_signals.categories)

    @cached_property
    def feeds(self) -> FeedsResourceWithStreamingResponse:
        return FeedsResourceWithStreamingResponse(self._threat_signals.feeds)

    @cached_property
    def articles(self) -> ArticlesResourceWithStreamingResponse:
        return ArticlesResourceWithStreamingResponse(self._threat_signals.articles)

    @cached_property
    def indicators(self) -> IndicatorsResourceWithStreamingResponse:
        return IndicatorsResourceWithStreamingResponse(self._threat_signals.indicators)

    @cached_property
    def skills(self) -> SkillsResourceWithStreamingResponse:
        return SkillsResourceWithStreamingResponse(self._threat_signals.skills)


class AsyncThreatSignalsResourceWithStreamingResponse:
    def __init__(self, threat_signals: AsyncThreatSignalsResource) -> None:
        self._threat_signals = threat_signals

    @cached_property
    def search(self) -> AsyncSearchResourceWithStreamingResponse:
        return AsyncSearchResourceWithStreamingResponse(self._threat_signals.search)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self._threat_signals.categories)

    @cached_property
    def feeds(self) -> AsyncFeedsResourceWithStreamingResponse:
        return AsyncFeedsResourceWithStreamingResponse(self._threat_signals.feeds)

    @cached_property
    def articles(self) -> AsyncArticlesResourceWithStreamingResponse:
        return AsyncArticlesResourceWithStreamingResponse(self._threat_signals.articles)

    @cached_property
    def indicators(self) -> AsyncIndicatorsResourceWithStreamingResponse:
        return AsyncIndicatorsResourceWithStreamingResponse(self._threat_signals.indicators)

    @cached_property
    def skills(self) -> AsyncSkillsResourceWithStreamingResponse:
        return AsyncSkillsResourceWithStreamingResponse(self._threat_signals.skills)
