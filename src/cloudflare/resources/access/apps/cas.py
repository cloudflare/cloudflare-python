# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.access.apps import CaGetResponse, CaListResponse, CaCreateResponse, CaDeleteResponse

__all__ = ["Cas", "AsyncCas"]


class Cas(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CasWithRawResponse:
        return CasWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CasWithStreamingResponse:
        return CasWithStreamingResponse(self)

    def create(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CaCreateResponse:
        """
        Generates a new short-lived certificate CA and public key.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return cast(
            CaCreateResponse,
            self._post(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/ca",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CaCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CaListResponse]:
        """
        Lists short-lived certificate CAs and their public keys.

        Args:
          account_or_zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/ca",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CaListResponse]], ResultWrapper[CaListResponse]),
        )

    def delete(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CaDeleteResponse:
        """
        Deletes a short-lived certificate CA.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/ca",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CaDeleteResponse], ResultWrapper[CaDeleteResponse]),
        )

    def get(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CaGetResponse:
        """
        Fetches a short-lived certificate CA and its public key.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return cast(
            CaGetResponse,
            self._get(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/ca",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CaGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncCas(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCasWithRawResponse:
        return AsyncCasWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCasWithStreamingResponse:
        return AsyncCasWithStreamingResponse(self)

    async def create(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CaCreateResponse:
        """
        Generates a new short-lived certificate CA and public key.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return cast(
            CaCreateResponse,
            await self._post(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/ca",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CaCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CaListResponse]:
        """
        Lists short-lived certificate CAs and their public keys.

        Args:
          account_or_zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/ca",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CaListResponse]], ResultWrapper[CaListResponse]),
        )

    async def delete(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CaDeleteResponse:
        """
        Deletes a short-lived certificate CA.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/ca",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CaDeleteResponse], ResultWrapper[CaDeleteResponse]),
        )

    async def get(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CaGetResponse:
        """
        Fetches a short-lived certificate CA and its public key.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return cast(
            CaGetResponse,
            await self._get(
                f"/{account_or_zone}/{account_or_zone_id}/access/apps/{uuid}/ca",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CaGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class CasWithRawResponse:
    def __init__(self, cas: Cas) -> None:
        self._cas = cas

        self.create = to_raw_response_wrapper(
            cas.create,
        )
        self.list = to_raw_response_wrapper(
            cas.list,
        )
        self.delete = to_raw_response_wrapper(
            cas.delete,
        )
        self.get = to_raw_response_wrapper(
            cas.get,
        )


class AsyncCasWithRawResponse:
    def __init__(self, cas: AsyncCas) -> None:
        self._cas = cas

        self.create = async_to_raw_response_wrapper(
            cas.create,
        )
        self.list = async_to_raw_response_wrapper(
            cas.list,
        )
        self.delete = async_to_raw_response_wrapper(
            cas.delete,
        )
        self.get = async_to_raw_response_wrapper(
            cas.get,
        )


class CasWithStreamingResponse:
    def __init__(self, cas: Cas) -> None:
        self._cas = cas

        self.create = to_streamed_response_wrapper(
            cas.create,
        )
        self.list = to_streamed_response_wrapper(
            cas.list,
        )
        self.delete = to_streamed_response_wrapper(
            cas.delete,
        )
        self.get = to_streamed_response_wrapper(
            cas.get,
        )


class AsyncCasWithStreamingResponse:
    def __init__(self, cas: AsyncCas) -> None:
        self._cas = cas

        self.create = async_to_streamed_response_wrapper(
            cas.create,
        )
        self.list = async_to_streamed_response_wrapper(
            cas.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            cas.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            cas.get,
        )
