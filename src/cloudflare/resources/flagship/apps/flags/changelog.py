# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncCursorPaginationAfter, AsyncCursorPaginationAfter
from ....._base_client import AsyncPaginator, make_request_options
from .....types.flagship.apps.flags import changelog_list_params
from .....types.flagship.apps.flags.changelog_list_response import ChangelogListResponse

__all__ = ["ChangelogResource", "AsyncChangelogResource"]


class ChangelogResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChangelogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ChangelogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChangelogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ChangelogResourceWithStreamingResponse(self)

    def list(
        self,
        flag_key: str,
        *,
        account_id: str,
        app_id: str,
        cursor: str | Omit = omit,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPaginationAfter[ChangelogListResponse]:
        """Returns the audit history for a flag, newest first.

        Each entry includes the
        event type and full flag state after the change; `update` entries include a
        field-level diff. Capped at 200 entries per flag.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          flag_key: Flag key (slug).

          cursor: Pagination cursor from a previous response.

          limit: Max items to return (1–200).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not flag_key:
            raise ValueError(f"Expected a non-empty value for `flag_key` but received {flag_key!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}/changelog",
                account_id=account_id,
                app_id=app_id,
                flag_key=flag_key,
            ),
            page=SyncCursorPaginationAfter[ChangelogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    changelog_list_params.ChangelogListParams,
                ),
            ),
            model=cast(Any, ChangelogListResponse),  # Union types cannot be passed in as arguments in the type system
        )


class AsyncChangelogResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChangelogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChangelogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChangelogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncChangelogResourceWithStreamingResponse(self)

    def list(
        self,
        flag_key: str,
        *,
        account_id: str,
        app_id: str,
        cursor: str | Omit = omit,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ChangelogListResponse, AsyncCursorPaginationAfter[ChangelogListResponse]]:
        """Returns the audit history for a flag, newest first.

        Each entry includes the
        event type and full flag state after the change; `update` entries include a
        field-level diff. Capped at 200 entries per flag.

        Args:
          account_id: Cloudflare account ID.

          app_id: App identifier.

          flag_key: Flag key (slug).

          cursor: Pagination cursor from a previous response.

          limit: Max items to return (1–200).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not flag_key:
            raise ValueError(f"Expected a non-empty value for `flag_key` but received {flag_key!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/flagship/apps/{app_id}/flags/{flag_key}/changelog",
                account_id=account_id,
                app_id=app_id,
                flag_key=flag_key,
            ),
            page=AsyncCursorPaginationAfter[ChangelogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    changelog_list_params.ChangelogListParams,
                ),
            ),
            model=cast(Any, ChangelogListResponse),  # Union types cannot be passed in as arguments in the type system
        )


class ChangelogResourceWithRawResponse:
    def __init__(self, changelog: ChangelogResource) -> None:
        self._changelog = changelog

        self.list = to_raw_response_wrapper(
            changelog.list,
        )


class AsyncChangelogResourceWithRawResponse:
    def __init__(self, changelog: AsyncChangelogResource) -> None:
        self._changelog = changelog

        self.list = async_to_raw_response_wrapper(
            changelog.list,
        )


class ChangelogResourceWithStreamingResponse:
    def __init__(self, changelog: ChangelogResource) -> None:
        self._changelog = changelog

        self.list = to_streamed_response_wrapper(
            changelog.list,
        )


class AsyncChangelogResourceWithStreamingResponse:
    def __init__(self, changelog: AsyncChangelogResource) -> None:
        self._changelog = changelog

        self.list = async_to_streamed_response_wrapper(
            changelog.list,
        )
