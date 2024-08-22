# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.email_routing.rules.catch_all_update_response import CatchAllUpdateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, Iterable

from ...._base_client import make_request_options

from ....types.email_routing.rules.catch_all_action_param import CatchAllActionParam

from ....types.email_routing.rules.catch_all_matcher_param import CatchAllMatcherParam

from typing_extensions import Literal

from ....types.email_routing.rules.catch_all_get_response import CatchAllGetResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.email_routing.rules import catch_all_update_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["CatchAllsResource", "AsyncCatchAllsResource"]

class CatchAllsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CatchAllsResourceWithRawResponse:
        return CatchAllsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CatchAllsResourceWithStreamingResponse:
        return CatchAllsResourceWithStreamingResponse(self)

    def update(self,
    zone_identifier: str,
    *,
    actions: Iterable[CatchAllActionParam],
    matchers: Iterable[CatchAllMatcherParam],
    enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
    name: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CatchAllUpdateResponse]:
        """
        Enable or disable catch-all routing rule, or change action to forward to
        specific destination address.

        Args:
          zone_identifier: Identifier

          actions: List actions for the catch-all routing rule.

          matchers: List of matchers for the catch-all routing rule.

          enabled: Routing rule status.

          name: Routing rule name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return self._put(
            f"/zones/{zone_identifier}/email/routing/rules/catch_all",
            body=maybe_transform({
                "actions": actions,
                "matchers": matchers,
                "enabled": enabled,
                "name": name,
            }, catch_all_update_params.CatchAllUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CatchAllUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[CatchAllUpdateResponse]], ResultWrapper[CatchAllUpdateResponse]),
        )

    def get(self,
    zone_identifier: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CatchAllGetResponse]:
        """
        Get information on the default catch-all routing rule.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return self._get(
            f"/zones/{zone_identifier}/email/routing/rules/catch_all",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CatchAllGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[CatchAllGetResponse]], ResultWrapper[CatchAllGetResponse]),
        )

class AsyncCatchAllsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCatchAllsResourceWithRawResponse:
        return AsyncCatchAllsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCatchAllsResourceWithStreamingResponse:
        return AsyncCatchAllsResourceWithStreamingResponse(self)

    async def update(self,
    zone_identifier: str,
    *,
    actions: Iterable[CatchAllActionParam],
    matchers: Iterable[CatchAllMatcherParam],
    enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
    name: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CatchAllUpdateResponse]:
        """
        Enable or disable catch-all routing rule, or change action to forward to
        specific destination address.

        Args:
          zone_identifier: Identifier

          actions: List actions for the catch-all routing rule.

          matchers: List of matchers for the catch-all routing rule.

          enabled: Routing rule status.

          name: Routing rule name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return await self._put(
            f"/zones/{zone_identifier}/email/routing/rules/catch_all",
            body=await async_maybe_transform({
                "actions": actions,
                "matchers": matchers,
                "enabled": enabled,
                "name": name,
            }, catch_all_update_params.CatchAllUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CatchAllUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[CatchAllUpdateResponse]], ResultWrapper[CatchAllUpdateResponse]),
        )

    async def get(self,
    zone_identifier: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CatchAllGetResponse]:
        """
        Get information on the default catch-all routing rule.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return await self._get(
            f"/zones/{zone_identifier}/email/routing/rules/catch_all",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CatchAllGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[CatchAllGetResponse]], ResultWrapper[CatchAllGetResponse]),
        )

class CatchAllsResourceWithRawResponse:
    def __init__(self, catch_alls: CatchAllsResource) -> None:
        self._catch_alls = catch_alls

        self.update = to_raw_response_wrapper(
            catch_alls.update,
        )
        self.get = to_raw_response_wrapper(
            catch_alls.get,
        )

class AsyncCatchAllsResourceWithRawResponse:
    def __init__(self, catch_alls: AsyncCatchAllsResource) -> None:
        self._catch_alls = catch_alls

        self.update = async_to_raw_response_wrapper(
            catch_alls.update,
        )
        self.get = async_to_raw_response_wrapper(
            catch_alls.get,
        )

class CatchAllsResourceWithStreamingResponse:
    def __init__(self, catch_alls: CatchAllsResource) -> None:
        self._catch_alls = catch_alls

        self.update = to_streamed_response_wrapper(
            catch_alls.update,
        )
        self.get = to_streamed_response_wrapper(
            catch_alls.get,
        )

class AsyncCatchAllsResourceWithStreamingResponse:
    def __init__(self, catch_alls: AsyncCatchAllsResource) -> None:
        self._catch_alls = catch_alls

        self.update = async_to_streamed_response_wrapper(
            catch_alls.update,
        )
        self.get = async_to_streamed_response_wrapper(
            catch_alls.get,
        )