# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.iam.oauth_scope_list_response import OAuthScopeListResponse

__all__ = ["OAuthScopesResource", "AsyncOAuthScopesResource"]


class OAuthScopesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthScopesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OAuthScopesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthScopesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OAuthScopesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[OAuthScopeListResponse]:
        """List all available OAuth scopes.

        This endpoint requires authentication but has
        no authorization role requirements.
        """
        return self._get_api_list(
            "/oauth/scopes",
            page=SyncSinglePage[OAuthScopeListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=OAuthScopeListResponse,
        )


class AsyncOAuthScopesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthScopesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthScopesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthScopesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOAuthScopesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[OAuthScopeListResponse, AsyncSinglePage[OAuthScopeListResponse]]:
        """List all available OAuth scopes.

        This endpoint requires authentication but has
        no authorization role requirements.
        """
        return self._get_api_list(
            "/oauth/scopes",
            page=AsyncSinglePage[OAuthScopeListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=OAuthScopeListResponse,
        )


class OAuthScopesResourceWithRawResponse:
    def __init__(self, oauth_scopes: OAuthScopesResource) -> None:
        self._oauth_scopes = oauth_scopes

        self.list = to_raw_response_wrapper(
            oauth_scopes.list,
        )


class AsyncOAuthScopesResourceWithRawResponse:
    def __init__(self, oauth_scopes: AsyncOAuthScopesResource) -> None:
        self._oauth_scopes = oauth_scopes

        self.list = async_to_raw_response_wrapper(
            oauth_scopes.list,
        )


class OAuthScopesResourceWithStreamingResponse:
    def __init__(self, oauth_scopes: OAuthScopesResource) -> None:
        self._oauth_scopes = oauth_scopes

        self.list = to_streamed_response_wrapper(
            oauth_scopes.list,
        )


class AsyncOAuthScopesResourceWithStreamingResponse:
    def __init__(self, oauth_scopes: AsyncOAuthScopesResource) -> None:
        self._oauth_scopes = oauth_scopes

        self.list = async_to_streamed_response_wrapper(
            oauth_scopes.list,
        )
