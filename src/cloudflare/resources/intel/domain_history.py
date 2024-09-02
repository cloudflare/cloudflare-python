# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.intel.domain_history_get_response import DomainHistoryGetResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options

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
from ...types import shared_params
from ...types.intel import domain_history_get_params
from typing import cast
from typing import cast

__all__ = ["DomainHistoryResource", "AsyncDomainHistoryResource"]


class DomainHistoryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainHistoryResourceWithRawResponse:
        return DomainHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainHistoryResourceWithStreamingResponse:
        return DomainHistoryResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainHistoryGetResponse]:
        """
        Get Domain History

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/domain-history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"domain": domain}, domain_history_get_params.DomainHistoryGetParams),
                post_parser=ResultWrapper[Optional[DomainHistoryGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainHistoryGetResponse]], ResultWrapper[DomainHistoryGetResponse]),
        )


class AsyncDomainHistoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainHistoryResourceWithRawResponse:
        return AsyncDomainHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainHistoryResourceWithStreamingResponse:
        return AsyncDomainHistoryResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainHistoryGetResponse]:
        """
        Get Domain History

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/domain-history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"domain": domain}, domain_history_get_params.DomainHistoryGetParams),
                post_parser=ResultWrapper[Optional[DomainHistoryGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainHistoryGetResponse]], ResultWrapper[DomainHistoryGetResponse]),
        )


class DomainHistoryResourceWithRawResponse:
    def __init__(self, domain_history: DomainHistoryResource) -> None:
        self._domain_history = domain_history

        self.get = to_raw_response_wrapper(
            domain_history.get,
        )


class AsyncDomainHistoryResourceWithRawResponse:
    def __init__(self, domain_history: AsyncDomainHistoryResource) -> None:
        self._domain_history = domain_history

        self.get = async_to_raw_response_wrapper(
            domain_history.get,
        )


class DomainHistoryResourceWithStreamingResponse:
    def __init__(self, domain_history: DomainHistoryResource) -> None:
        self._domain_history = domain_history

        self.get = to_streamed_response_wrapper(
            domain_history.get,
        )


class AsyncDomainHistoryResourceWithStreamingResponse:
    def __init__(self, domain_history: AsyncDomainHistoryResource) -> None:
        self._domain_history = domain_history

        self.get = async_to_streamed_response_wrapper(
            domain_history.get,
        )
