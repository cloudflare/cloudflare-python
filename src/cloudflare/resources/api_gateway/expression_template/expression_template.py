# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .fallthrough import (
    FallthroughResource,
    AsyncFallthroughResource,
    FallthroughResourceWithRawResponse,
    AsyncFallthroughResourceWithRawResponse,
    FallthroughResourceWithStreamingResponse,
    AsyncFallthroughResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ExpressionTemplateResource", "AsyncExpressionTemplateResource"]


class ExpressionTemplateResource(SyncAPIResource):
    @cached_property
    def fallthrough(self) -> FallthroughResource:
        return FallthroughResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExpressionTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ExpressionTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExpressionTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ExpressionTemplateResourceWithStreamingResponse(self)


class AsyncExpressionTemplateResource(AsyncAPIResource):
    @cached_property
    def fallthrough(self) -> AsyncFallthroughResource:
        return AsyncFallthroughResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExpressionTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExpressionTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExpressionTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncExpressionTemplateResourceWithStreamingResponse(self)


class ExpressionTemplateResourceWithRawResponse:
    def __init__(self, expression_template: ExpressionTemplateResource) -> None:
        self._expression_template = expression_template

    @cached_property
    def fallthrough(self) -> FallthroughResourceWithRawResponse:
        return FallthroughResourceWithRawResponse(self._expression_template.fallthrough)


class AsyncExpressionTemplateResourceWithRawResponse:
    def __init__(self, expression_template: AsyncExpressionTemplateResource) -> None:
        self._expression_template = expression_template

    @cached_property
    def fallthrough(self) -> AsyncFallthroughResourceWithRawResponse:
        return AsyncFallthroughResourceWithRawResponse(self._expression_template.fallthrough)


class ExpressionTemplateResourceWithStreamingResponse:
    def __init__(self, expression_template: ExpressionTemplateResource) -> None:
        self._expression_template = expression_template

    @cached_property
    def fallthrough(self) -> FallthroughResourceWithStreamingResponse:
        return FallthroughResourceWithStreamingResponse(self._expression_template.fallthrough)


class AsyncExpressionTemplateResourceWithStreamingResponse:
    def __init__(self, expression_template: AsyncExpressionTemplateResource) -> None:
        self._expression_template = expression_template

    @cached_property
    def fallthrough(self) -> AsyncFallthroughResourceWithStreamingResponse:
        return AsyncFallthroughResourceWithStreamingResponse(self._expression_template.fallthrough)
