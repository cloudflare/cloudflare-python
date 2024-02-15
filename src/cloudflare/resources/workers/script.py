# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["Script", "AsyncScript"]


class Script(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScriptWithRawResponse:
        return ScriptWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScriptWithStreamingResponse:
        return ScriptWithStreamingResponse(self)

    def delete(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete your Worker.

        This call has no response body on a successful delete.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/zones/{zone_id}/workers/script",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncScript(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScriptWithRawResponse:
        return AsyncScriptWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScriptWithStreamingResponse:
        return AsyncScriptWithStreamingResponse(self)

    async def delete(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete your Worker.

        This call has no response body on a successful delete.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/zones/{zone_id}/workers/script",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ScriptWithRawResponse:
    def __init__(self, script: Script) -> None:
        self._script = script

        self.delete = to_raw_response_wrapper(
            script.delete,
        )


class AsyncScriptWithRawResponse:
    def __init__(self, script: AsyncScript) -> None:
        self._script = script

        self.delete = async_to_raw_response_wrapper(
            script.delete,
        )


class ScriptWithStreamingResponse:
    def __init__(self, script: Script) -> None:
        self._script = script

        self.delete = to_streamed_response_wrapper(
            script.delete,
        )


class AsyncScriptWithStreamingResponse:
    def __init__(self, script: AsyncScript) -> None:
        self._script = script

        self.delete = async_to_streamed_response_wrapper(
            script.delete,
        )
