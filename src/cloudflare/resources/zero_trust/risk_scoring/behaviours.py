# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.zero_trust.risk_scoring.behaviour_update_response import BehaviourUpdateResponse

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from typing import Dict

from ....types.zero_trust.risk_scoring.behaviour_get_response import BehaviourGetResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from ....types.zero_trust.risk_scoring import behaviour_update_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.zero_trust.risk_scoring import behaviour_update_params

__all__ = ["BehavioursResource", "AsyncBehavioursResource"]

class BehavioursResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BehavioursResourceWithRawResponse:
        return BehavioursResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BehavioursResourceWithStreamingResponse:
        return BehavioursResourceWithStreamingResponse(self)

    def update(self,
    *,
    account_id: str,
    behaviors: Dict[str, behaviour_update_params.Behaviors],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> BehaviourUpdateResponse:
        """
        Update configuration for risk behaviors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/zt_risk_scoring/behaviors",
            body=maybe_transform({
                "behaviors": behaviors
            }, behaviour_update_params.BehaviourUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BehaviourUpdateResponse,
        )

    def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> BehaviourGetResponse:
        """
        Get all behaviors and associated configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/zt_risk_scoring/behaviors",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BehaviourGetResponse,
        )

class AsyncBehavioursResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBehavioursResourceWithRawResponse:
        return AsyncBehavioursResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBehavioursResourceWithStreamingResponse:
        return AsyncBehavioursResourceWithStreamingResponse(self)

    async def update(self,
    *,
    account_id: str,
    behaviors: Dict[str, behaviour_update_params.Behaviors],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> BehaviourUpdateResponse:
        """
        Update configuration for risk behaviors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/zt_risk_scoring/behaviors",
            body=await async_maybe_transform({
                "behaviors": behaviors
            }, behaviour_update_params.BehaviourUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BehaviourUpdateResponse,
        )

    async def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> BehaviourGetResponse:
        """
        Get all behaviors and associated configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/zt_risk_scoring/behaviors",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BehaviourGetResponse,
        )

class BehavioursResourceWithRawResponse:
    def __init__(self, behaviours: BehavioursResource) -> None:
        self._behaviours = behaviours

        self.update = to_raw_response_wrapper(
            behaviours.update,
        )
        self.get = to_raw_response_wrapper(
            behaviours.get,
        )

class AsyncBehavioursResourceWithRawResponse:
    def __init__(self, behaviours: AsyncBehavioursResource) -> None:
        self._behaviours = behaviours

        self.update = async_to_raw_response_wrapper(
            behaviours.update,
        )
        self.get = async_to_raw_response_wrapper(
            behaviours.get,
        )

class BehavioursResourceWithStreamingResponse:
    def __init__(self, behaviours: BehavioursResource) -> None:
        self._behaviours = behaviours

        self.update = to_streamed_response_wrapper(
            behaviours.update,
        )
        self.get = to_streamed_response_wrapper(
            behaviours.get,
        )

class AsyncBehavioursResourceWithStreamingResponse:
    def __init__(self, behaviours: AsyncBehavioursResource) -> None:
        self._behaviours = behaviours

        self.update = async_to_streamed_response_wrapper(
            behaviours.update,
        )
        self.get = async_to_streamed_response_wrapper(
            behaviours.get,
        )