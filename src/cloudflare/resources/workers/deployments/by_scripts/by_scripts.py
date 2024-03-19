# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from .details import (
    Details,
    AsyncDetails,
    DetailsWithRawResponse,
    AsyncDetailsWithRawResponse,
    DetailsWithStreamingResponse,
    AsyncDetailsWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.workers.deployments import ByScriptGetResponse

__all__ = ["ByScripts", "AsyncByScripts"]


class ByScripts(SyncAPIResource):
    @cached_property
    def details(self) -> Details:
        return Details(self._client)

    @cached_property
    def with_raw_response(self) -> ByScriptsWithRawResponse:
        return ByScriptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ByScriptsWithStreamingResponse:
        return ByScriptsWithStreamingResponse(self)

    def get(
        self,
        script_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByScriptGetResponse:
        """
        List Deployments

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_id:
            raise ValueError(f"Expected a non-empty value for `script_id` but received {script_id!r}")
        return self._get(
            f"/accounts/{account_id}/workers/deployments/by-script/{script_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ByScriptGetResponse], ResultWrapper[ByScriptGetResponse]),
        )


class AsyncByScripts(AsyncAPIResource):
    @cached_property
    def details(self) -> AsyncDetails:
        return AsyncDetails(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncByScriptsWithRawResponse:
        return AsyncByScriptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncByScriptsWithStreamingResponse:
        return AsyncByScriptsWithStreamingResponse(self)

    async def get(
        self,
        script_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByScriptGetResponse:
        """
        List Deployments

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_id:
            raise ValueError(f"Expected a non-empty value for `script_id` but received {script_id!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/deployments/by-script/{script_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ByScriptGetResponse], ResultWrapper[ByScriptGetResponse]),
        )


class ByScriptsWithRawResponse:
    def __init__(self, by_scripts: ByScripts) -> None:
        self._by_scripts = by_scripts

        self.get = to_raw_response_wrapper(
            by_scripts.get,
        )

    @cached_property
    def details(self) -> DetailsWithRawResponse:
        return DetailsWithRawResponse(self._by_scripts.details)


class AsyncByScriptsWithRawResponse:
    def __init__(self, by_scripts: AsyncByScripts) -> None:
        self._by_scripts = by_scripts

        self.get = async_to_raw_response_wrapper(
            by_scripts.get,
        )

    @cached_property
    def details(self) -> AsyncDetailsWithRawResponse:
        return AsyncDetailsWithRawResponse(self._by_scripts.details)


class ByScriptsWithStreamingResponse:
    def __init__(self, by_scripts: ByScripts) -> None:
        self._by_scripts = by_scripts

        self.get = to_streamed_response_wrapper(
            by_scripts.get,
        )

    @cached_property
    def details(self) -> DetailsWithStreamingResponse:
        return DetailsWithStreamingResponse(self._by_scripts.details)


class AsyncByScriptsWithStreamingResponse:
    def __init__(self, by_scripts: AsyncByScripts) -> None:
        self._by_scripts = by_scripts

        self.get = async_to_streamed_response_wrapper(
            by_scripts.get,
        )

    @cached_property
    def details(self) -> AsyncDetailsWithStreamingResponse:
        return AsyncDetailsWithStreamingResponse(self._by_scripts.details)
