# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.email_security.settings import (
    url_ignore_pattern_edit_params,
    url_ignore_pattern_list_params,
    url_ignore_pattern_create_params,
)
from ....types.email_security.settings.url_ignore_pattern_get_response import URLIgnorePatternGetResponse
from ....types.email_security.settings.url_ignore_pattern_edit_response import URLIgnorePatternEditResponse
from ....types.email_security.settings.url_ignore_pattern_list_response import URLIgnorePatternListResponse
from ....types.email_security.settings.url_ignore_pattern_create_response import URLIgnorePatternCreateResponse
from ....types.email_security.settings.url_ignore_pattern_delete_response import URLIgnorePatternDeleteResponse

__all__ = ["URLIgnorePatternsResource", "AsyncURLIgnorePatternsResource"]


class URLIgnorePatternsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLIgnorePatternsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return URLIgnorePatternsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLIgnorePatternsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return URLIgnorePatternsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        pattern: str,
        comments: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[URLIgnorePatternCreateResponse]:
        """Creates a new URL rewrite ignore pattern.

        URLs matching this pattern will not be
        rewritten.

        Args:
          account_id: Identifier.

          pattern: Regular expression matching URLs that should not be rewritten.

          comments: Optional note describing the reason for the ignore pattern.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/email-security/settings/url_ignore_patterns", account_id=account_id),
            body=maybe_transform(
                {
                    "pattern": pattern,
                    "comments": comments,
                },
                url_ignore_pattern_create_params.URLIgnorePatternCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[URLIgnorePatternCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[URLIgnorePatternCreateResponse]], ResultWrapper[URLIgnorePatternCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[URLIgnorePatternListResponse]:
        """Returns a paginated list of URL rewrite ignore patterns for the account.

        URLs
        matching these patterns will not be rewritten.

        Args:
          account_id: Identifier.

          page: Current page within paginated list of results.

          per_page: The number of results per page. Maximum value is 1000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/settings/url_ignore_patterns", account_id=account_id),
            page=SyncV4PagePaginationArray[URLIgnorePatternListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    url_ignore_pattern_list_params.URLIgnorePatternListParams,
                ),
            ),
            model=URLIgnorePatternListResponse,
        )

    def delete(
        self,
        pattern_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[URLIgnorePatternDeleteResponse]:
        """Removes a URL rewrite ignore pattern.

        After deletion, URLs matching this pattern
        will be rewritten again.

        Args:
          account_id: Identifier.

          pattern_id: URL ignore pattern identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pattern_id:
            raise ValueError(f"Expected a non-empty value for `pattern_id` but received {pattern_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/url_ignore_patterns/{pattern_id}",
                account_id=account_id,
                pattern_id=pattern_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[URLIgnorePatternDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[URLIgnorePatternDeleteResponse]], ResultWrapper[URLIgnorePatternDeleteResponse]),
        )

    def edit(
        self,
        pattern_id: str,
        *,
        account_id: str,
        comments: Optional[str] | Omit = omit,
        pattern: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[URLIgnorePatternEditResponse]:
        """Updates an existing URL rewrite ignore pattern.

        Only provided fields will be
        modified.

        Args:
          account_id: Identifier.

          pattern_id: URL ignore pattern identifier

          comments: Optional note describing the reason for the ignore pattern.

          pattern: Regular expression matching URLs that should not be rewritten.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pattern_id:
            raise ValueError(f"Expected a non-empty value for `pattern_id` but received {pattern_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/url_ignore_patterns/{pattern_id}",
                account_id=account_id,
                pattern_id=pattern_id,
            ),
            body=maybe_transform(
                {
                    "comments": comments,
                    "pattern": pattern,
                },
                url_ignore_pattern_edit_params.URLIgnorePatternEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[URLIgnorePatternEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[URLIgnorePatternEditResponse]], ResultWrapper[URLIgnorePatternEditResponse]),
        )

    def get(
        self,
        pattern_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[URLIgnorePatternGetResponse]:
        """
        Returns a single URL rewrite ignore pattern by its identifier.

        Args:
          account_id: Identifier.

          pattern_id: URL ignore pattern identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pattern_id:
            raise ValueError(f"Expected a non-empty value for `pattern_id` but received {pattern_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/url_ignore_patterns/{pattern_id}",
                account_id=account_id,
                pattern_id=pattern_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[URLIgnorePatternGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[URLIgnorePatternGetResponse]], ResultWrapper[URLIgnorePatternGetResponse]),
        )


class AsyncURLIgnorePatternsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLIgnorePatternsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncURLIgnorePatternsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLIgnorePatternsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncURLIgnorePatternsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        pattern: str,
        comments: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[URLIgnorePatternCreateResponse]:
        """Creates a new URL rewrite ignore pattern.

        URLs matching this pattern will not be
        rewritten.

        Args:
          account_id: Identifier.

          pattern: Regular expression matching URLs that should not be rewritten.

          comments: Optional note describing the reason for the ignore pattern.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/email-security/settings/url_ignore_patterns", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "pattern": pattern,
                    "comments": comments,
                },
                url_ignore_pattern_create_params.URLIgnorePatternCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[URLIgnorePatternCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[URLIgnorePatternCreateResponse]], ResultWrapper[URLIgnorePatternCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[URLIgnorePatternListResponse, AsyncV4PagePaginationArray[URLIgnorePatternListResponse]]:
        """Returns a paginated list of URL rewrite ignore patterns for the account.

        URLs
        matching these patterns will not be rewritten.

        Args:
          account_id: Identifier.

          page: Current page within paginated list of results.

          per_page: The number of results per page. Maximum value is 1000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/settings/url_ignore_patterns", account_id=account_id),
            page=AsyncV4PagePaginationArray[URLIgnorePatternListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    url_ignore_pattern_list_params.URLIgnorePatternListParams,
                ),
            ),
            model=URLIgnorePatternListResponse,
        )

    async def delete(
        self,
        pattern_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[URLIgnorePatternDeleteResponse]:
        """Removes a URL rewrite ignore pattern.

        After deletion, URLs matching this pattern
        will be rewritten again.

        Args:
          account_id: Identifier.

          pattern_id: URL ignore pattern identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pattern_id:
            raise ValueError(f"Expected a non-empty value for `pattern_id` but received {pattern_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/url_ignore_patterns/{pattern_id}",
                account_id=account_id,
                pattern_id=pattern_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[URLIgnorePatternDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[URLIgnorePatternDeleteResponse]], ResultWrapper[URLIgnorePatternDeleteResponse]),
        )

    async def edit(
        self,
        pattern_id: str,
        *,
        account_id: str,
        comments: Optional[str] | Omit = omit,
        pattern: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[URLIgnorePatternEditResponse]:
        """Updates an existing URL rewrite ignore pattern.

        Only provided fields will be
        modified.

        Args:
          account_id: Identifier.

          pattern_id: URL ignore pattern identifier

          comments: Optional note describing the reason for the ignore pattern.

          pattern: Regular expression matching URLs that should not be rewritten.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pattern_id:
            raise ValueError(f"Expected a non-empty value for `pattern_id` but received {pattern_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/url_ignore_patterns/{pattern_id}",
                account_id=account_id,
                pattern_id=pattern_id,
            ),
            body=await async_maybe_transform(
                {
                    "comments": comments,
                    "pattern": pattern,
                },
                url_ignore_pattern_edit_params.URLIgnorePatternEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[URLIgnorePatternEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[URLIgnorePatternEditResponse]], ResultWrapper[URLIgnorePatternEditResponse]),
        )

    async def get(
        self,
        pattern_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[URLIgnorePatternGetResponse]:
        """
        Returns a single URL rewrite ignore pattern by its identifier.

        Args:
          account_id: Identifier.

          pattern_id: URL ignore pattern identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pattern_id:
            raise ValueError(f"Expected a non-empty value for `pattern_id` but received {pattern_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/url_ignore_patterns/{pattern_id}",
                account_id=account_id,
                pattern_id=pattern_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[URLIgnorePatternGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[URLIgnorePatternGetResponse]], ResultWrapper[URLIgnorePatternGetResponse]),
        )


class URLIgnorePatternsResourceWithRawResponse:
    def __init__(self, url_ignore_patterns: URLIgnorePatternsResource) -> None:
        self._url_ignore_patterns = url_ignore_patterns

        self.create = to_raw_response_wrapper(
            url_ignore_patterns.create,
        )
        self.list = to_raw_response_wrapper(
            url_ignore_patterns.list,
        )
        self.delete = to_raw_response_wrapper(
            url_ignore_patterns.delete,
        )
        self.edit = to_raw_response_wrapper(
            url_ignore_patterns.edit,
        )
        self.get = to_raw_response_wrapper(
            url_ignore_patterns.get,
        )


class AsyncURLIgnorePatternsResourceWithRawResponse:
    def __init__(self, url_ignore_patterns: AsyncURLIgnorePatternsResource) -> None:
        self._url_ignore_patterns = url_ignore_patterns

        self.create = async_to_raw_response_wrapper(
            url_ignore_patterns.create,
        )
        self.list = async_to_raw_response_wrapper(
            url_ignore_patterns.list,
        )
        self.delete = async_to_raw_response_wrapper(
            url_ignore_patterns.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            url_ignore_patterns.edit,
        )
        self.get = async_to_raw_response_wrapper(
            url_ignore_patterns.get,
        )


class URLIgnorePatternsResourceWithStreamingResponse:
    def __init__(self, url_ignore_patterns: URLIgnorePatternsResource) -> None:
        self._url_ignore_patterns = url_ignore_patterns

        self.create = to_streamed_response_wrapper(
            url_ignore_patterns.create,
        )
        self.list = to_streamed_response_wrapper(
            url_ignore_patterns.list,
        )
        self.delete = to_streamed_response_wrapper(
            url_ignore_patterns.delete,
        )
        self.edit = to_streamed_response_wrapper(
            url_ignore_patterns.edit,
        )
        self.get = to_streamed_response_wrapper(
            url_ignore_patterns.get,
        )


class AsyncURLIgnorePatternsResourceWithStreamingResponse:
    def __init__(self, url_ignore_patterns: AsyncURLIgnorePatternsResource) -> None:
        self._url_ignore_patterns = url_ignore_patterns

        self.create = async_to_streamed_response_wrapper(
            url_ignore_patterns.create,
        )
        self.list = async_to_streamed_response_wrapper(
            url_ignore_patterns.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            url_ignore_patterns.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            url_ignore_patterns.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            url_ignore_patterns.get,
        )
