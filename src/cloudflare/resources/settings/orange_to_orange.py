# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import OrangeToOrangeUpdateResponse, OrangeToOrangeGetResponse, orange_to_orange_update_params

from typing import Type, Optional

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.settings import orange_to_orange_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["OrangeToOrange", "AsyncOrangeToOrange"]


class OrangeToOrange(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrangeToOrangeWithRawResponse:
        return OrangeToOrangeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrangeToOrangeWithStreamingResponse:
        return OrangeToOrangeWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: orange_to_orange_update_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrangeToOrangeUpdateResponse]:
        """
        Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
        on Cloudflare.

        Args:
          zone_id: Identifier

          value: Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
              on Cloudflare.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/orange_to_orange",
            body=maybe_transform({"value": value}, orange_to_orange_update_params.OrangeToOrangeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrangeToOrangeUpdateResponse]], ResultWrapper[OrangeToOrangeUpdateResponse]),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrangeToOrangeGetResponse]:
        """
        Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
        on Cloudflare.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/orange_to_orange",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrangeToOrangeGetResponse]], ResultWrapper[OrangeToOrangeGetResponse]),
        )


class AsyncOrangeToOrange(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrangeToOrangeWithRawResponse:
        return AsyncOrangeToOrangeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrangeToOrangeWithStreamingResponse:
        return AsyncOrangeToOrangeWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: orange_to_orange_update_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrangeToOrangeUpdateResponse]:
        """
        Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
        on Cloudflare.

        Args:
          zone_id: Identifier

          value: Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
              on Cloudflare.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/orange_to_orange",
            body=maybe_transform({"value": value}, orange_to_orange_update_params.OrangeToOrangeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrangeToOrangeUpdateResponse]], ResultWrapper[OrangeToOrangeUpdateResponse]),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrangeToOrangeGetResponse]:
        """
        Orange to Orange (O2O) allows zones on Cloudflare to CNAME to other zones also
        on Cloudflare.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/orange_to_orange",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrangeToOrangeGetResponse]], ResultWrapper[OrangeToOrangeGetResponse]),
        )


class OrangeToOrangeWithRawResponse:
    def __init__(self, orange_to_orange: OrangeToOrange) -> None:
        self._orange_to_orange = orange_to_orange

        self.update = to_raw_response_wrapper(
            orange_to_orange.update,
        )
        self.get = to_raw_response_wrapper(
            orange_to_orange.get,
        )


class AsyncOrangeToOrangeWithRawResponse:
    def __init__(self, orange_to_orange: AsyncOrangeToOrange) -> None:
        self._orange_to_orange = orange_to_orange

        self.update = async_to_raw_response_wrapper(
            orange_to_orange.update,
        )
        self.get = async_to_raw_response_wrapper(
            orange_to_orange.get,
        )


class OrangeToOrangeWithStreamingResponse:
    def __init__(self, orange_to_orange: OrangeToOrange) -> None:
        self._orange_to_orange = orange_to_orange

        self.update = to_streamed_response_wrapper(
            orange_to_orange.update,
        )
        self.get = to_streamed_response_wrapper(
            orange_to_orange.get,
        )


class AsyncOrangeToOrangeWithStreamingResponse:
    def __init__(self, orange_to_orange: AsyncOrangeToOrange) -> None:
        self._orange_to_orange = orange_to_orange

        self.update = async_to_streamed_response_wrapper(
            orange_to_orange.update,
        )
        self.get = async_to_streamed_response_wrapper(
            orange_to_orange.get,
        )
