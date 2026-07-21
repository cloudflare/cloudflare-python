# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import datetime

import httpx

from .tokens import (
    TokensResource,
    AsyncTokensResource,
    TokensResourceWithRawResponse,
    AsyncTokensResourceWithRawResponse,
    TokensResourceWithStreamingResponse,
    AsyncTokensResourceWithStreamingResponse,
)
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
from ....types.moq import relay_list_params, relay_create_params, relay_update_params
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.moq.relay_get_response import RelayGetResponse
from ....types.moq.relay_list_response import RelayListResponse
from ....types.moq.relay_create_response import RelayCreateResponse
from ....types.moq.relay_update_response import RelayUpdateResponse

__all__ = ["RelaysResource", "AsyncRelaysResource"]


class RelaysResource(SyncAPIResource):
    @cached_property
    def tokens(self) -> TokensResource:
        return TokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> RelaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RelaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RelaysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[RelayCreateResponse]:
        """Provisions a new MoQ relay instance.

        Auto-creates a publish+subscribe token and
        a subscribe-only token. Token values are included in the response (shown once).
        Config is always set to defaults (upstreams off) and cannot be supplied here —
        sending a non-empty `config` is rejected (21014); `null` or `{}` is accepted as
        absent. Use PUT to configure the relay after it exists.

        Args:
          account_id: Cloudflare account identifier.

          name: Human-readable name for the relay.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/moq/relays", account_id=account_id),
            body=maybe_transform({"name": name}, relay_create_params.RelayCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RelayCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RelayCreateResponse]], ResultWrapper[RelayCreateResponse]),
        )

    def update(
        self,
        relay_id: str,
        *,
        account_id: str,
        config: relay_update_params.Config | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[RelayUpdateResponse]:
        """Updates a relay's name and/or configuration.

        The relay ID goes in the URL path —
        `PUT /accounts/{account_id}/moq/relays/{relay_id}` — not the request body; there
        is no collection-level update endpoint. This is also the only way to set a
        relay's config (config cannot be set at create time). Partial updates: omitted
        fields are preserved; config sub-objects replace as whole objects when present.

        Args:
          account_id: Cloudflare account identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not relay_id:
            raise ValueError(f"Expected a non-empty value for `relay_id` but received {relay_id!r}")
        return self._put(
            path_template("/accounts/{account_id}/moq/relays/{relay_id}", account_id=account_id, relay_id=relay_id),
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                },
                relay_update_params.RelayUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RelayUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RelayUpdateResponse]], ResultWrapper[RelayUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        asc: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[RelayListResponse]:
        """Lists all MoQ relays for the account.

        Returns only metadata. Config, status, and
        tokens are omitted.

        Results are cursor-paginated (keyset on the `created` timestamp). Use
        `created_before` / `created_after` with the `created` value of the first/last
        item in a page to fetch the adjacent page. `result_info` reports the page
        `count` and the `total` matching the cursor filters.

        Args:
          account_id: Cloudflare account identifier.

          asc: Sort order by `created`. When true, results are returned oldest-first
              (ascending); otherwise newest-first (descending, the default).

          created_after: Cursor for pagination. Returns relays created strictly after this RFC 3339
              timestamp (typically the `created` value of the last item on the current page,
              to fetch the next page).

          created_before: Cursor for pagination. Returns relays created strictly before this RFC 3339
              timestamp (typically the `created` value of the first item on the current page,
              to fetch the previous page).

          per_page: Maximum number of relays to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/moq/relays", account_id=account_id),
            page=SyncSinglePage[RelayListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asc": asc,
                        "created_after": created_after,
                        "created_before": created_before,
                        "per_page": per_page,
                    },
                    relay_list_params.RelayListParams,
                ),
            ),
            model=RelayListResponse,
        )

    def delete(
        self,
        relay_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Soft-deletes a MoQ relay.

        The relay ID goes in the URL path —
        `DELETE /accounts/{account_id}/moq/relays/{relay_id}` — not the request body;
        there is no collection-level delete endpoint.

        Args:
          account_id: Cloudflare account identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not relay_id:
            raise ValueError(f"Expected a non-empty value for `relay_id` but received {relay_id!r}")
        return self._delete(
            path_template("/accounts/{account_id}/moq/relays/{relay_id}", account_id=account_id, relay_id=relay_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(
        self,
        relay_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[RelayGetResponse]:
        """Retrieves a single MoQ relay including config and status.

        Tokens are NOT
        included.

        Args:
          account_id: Cloudflare account identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not relay_id:
            raise ValueError(f"Expected a non-empty value for `relay_id` but received {relay_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/moq/relays/{relay_id}", account_id=account_id, relay_id=relay_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RelayGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RelayGetResponse]], ResultWrapper[RelayGetResponse]),
        )


class AsyncRelaysResource(AsyncAPIResource):
    @cached_property
    def tokens(self) -> AsyncTokensResource:
        return AsyncTokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRelaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRelaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRelaysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[RelayCreateResponse]:
        """Provisions a new MoQ relay instance.

        Auto-creates a publish+subscribe token and
        a subscribe-only token. Token values are included in the response (shown once).
        Config is always set to defaults (upstreams off) and cannot be supplied here —
        sending a non-empty `config` is rejected (21014); `null` or `{}` is accepted as
        absent. Use PUT to configure the relay after it exists.

        Args:
          account_id: Cloudflare account identifier.

          name: Human-readable name for the relay.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/moq/relays", account_id=account_id),
            body=await async_maybe_transform({"name": name}, relay_create_params.RelayCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RelayCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RelayCreateResponse]], ResultWrapper[RelayCreateResponse]),
        )

    async def update(
        self,
        relay_id: str,
        *,
        account_id: str,
        config: relay_update_params.Config | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[RelayUpdateResponse]:
        """Updates a relay's name and/or configuration.

        The relay ID goes in the URL path —
        `PUT /accounts/{account_id}/moq/relays/{relay_id}` — not the request body; there
        is no collection-level update endpoint. This is also the only way to set a
        relay's config (config cannot be set at create time). Partial updates: omitted
        fields are preserved; config sub-objects replace as whole objects when present.

        Args:
          account_id: Cloudflare account identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not relay_id:
            raise ValueError(f"Expected a non-empty value for `relay_id` but received {relay_id!r}")
        return await self._put(
            path_template("/accounts/{account_id}/moq/relays/{relay_id}", account_id=account_id, relay_id=relay_id),
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                },
                relay_update_params.RelayUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RelayUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RelayUpdateResponse]], ResultWrapper[RelayUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        asc: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RelayListResponse, AsyncSinglePage[RelayListResponse]]:
        """Lists all MoQ relays for the account.

        Returns only metadata. Config, status, and
        tokens are omitted.

        Results are cursor-paginated (keyset on the `created` timestamp). Use
        `created_before` / `created_after` with the `created` value of the first/last
        item in a page to fetch the adjacent page. `result_info` reports the page
        `count` and the `total` matching the cursor filters.

        Args:
          account_id: Cloudflare account identifier.

          asc: Sort order by `created`. When true, results are returned oldest-first
              (ascending); otherwise newest-first (descending, the default).

          created_after: Cursor for pagination. Returns relays created strictly after this RFC 3339
              timestamp (typically the `created` value of the last item on the current page,
              to fetch the next page).

          created_before: Cursor for pagination. Returns relays created strictly before this RFC 3339
              timestamp (typically the `created` value of the first item on the current page,
              to fetch the previous page).

          per_page: Maximum number of relays to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/moq/relays", account_id=account_id),
            page=AsyncSinglePage[RelayListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asc": asc,
                        "created_after": created_after,
                        "created_before": created_before,
                        "per_page": per_page,
                    },
                    relay_list_params.RelayListParams,
                ),
            ),
            model=RelayListResponse,
        )

    async def delete(
        self,
        relay_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Soft-deletes a MoQ relay.

        The relay ID goes in the URL path —
        `DELETE /accounts/{account_id}/moq/relays/{relay_id}` — not the request body;
        there is no collection-level delete endpoint.

        Args:
          account_id: Cloudflare account identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not relay_id:
            raise ValueError(f"Expected a non-empty value for `relay_id` but received {relay_id!r}")
        return await self._delete(
            path_template("/accounts/{account_id}/moq/relays/{relay_id}", account_id=account_id, relay_id=relay_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(
        self,
        relay_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[RelayGetResponse]:
        """Retrieves a single MoQ relay including config and status.

        Tokens are NOT
        included.

        Args:
          account_id: Cloudflare account identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not relay_id:
            raise ValueError(f"Expected a non-empty value for `relay_id` but received {relay_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/moq/relays/{relay_id}", account_id=account_id, relay_id=relay_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RelayGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RelayGetResponse]], ResultWrapper[RelayGetResponse]),
        )


class RelaysResourceWithRawResponse:
    def __init__(self, relays: RelaysResource) -> None:
        self._relays = relays

        self.create = to_raw_response_wrapper(
            relays.create,
        )
        self.update = to_raw_response_wrapper(
            relays.update,
        )
        self.list = to_raw_response_wrapper(
            relays.list,
        )
        self.delete = to_raw_response_wrapper(
            relays.delete,
        )
        self.get = to_raw_response_wrapper(
            relays.get,
        )

    @cached_property
    def tokens(self) -> TokensResourceWithRawResponse:
        return TokensResourceWithRawResponse(self._relays.tokens)


class AsyncRelaysResourceWithRawResponse:
    def __init__(self, relays: AsyncRelaysResource) -> None:
        self._relays = relays

        self.create = async_to_raw_response_wrapper(
            relays.create,
        )
        self.update = async_to_raw_response_wrapper(
            relays.update,
        )
        self.list = async_to_raw_response_wrapper(
            relays.list,
        )
        self.delete = async_to_raw_response_wrapper(
            relays.delete,
        )
        self.get = async_to_raw_response_wrapper(
            relays.get,
        )

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithRawResponse:
        return AsyncTokensResourceWithRawResponse(self._relays.tokens)


class RelaysResourceWithStreamingResponse:
    def __init__(self, relays: RelaysResource) -> None:
        self._relays = relays

        self.create = to_streamed_response_wrapper(
            relays.create,
        )
        self.update = to_streamed_response_wrapper(
            relays.update,
        )
        self.list = to_streamed_response_wrapper(
            relays.list,
        )
        self.delete = to_streamed_response_wrapper(
            relays.delete,
        )
        self.get = to_streamed_response_wrapper(
            relays.get,
        )

    @cached_property
    def tokens(self) -> TokensResourceWithStreamingResponse:
        return TokensResourceWithStreamingResponse(self._relays.tokens)


class AsyncRelaysResourceWithStreamingResponse:
    def __init__(self, relays: AsyncRelaysResource) -> None:
        self._relays = relays

        self.create = async_to_streamed_response_wrapper(
            relays.create,
        )
        self.update = async_to_streamed_response_wrapper(
            relays.update,
        )
        self.list = async_to_streamed_response_wrapper(
            relays.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            relays.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            relays.get,
        )

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithStreamingResponse:
        return AsyncTokensResourceWithStreamingResponse(self._relays.tokens)
