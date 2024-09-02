# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.botnet_feed.configs.asn_delete_response import ASNDeleteResponse

from ...._wrappers import ResultWrapper

from typing import Optional, Type

from ...._base_client import make_request_options

from ....types.botnet_feed.configs.asn_get_response import ASNGetResponse

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ASNResource", "AsyncASNResource"]


class ASNResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ASNResourceWithRawResponse:
        return ASNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ASNResourceWithStreamingResponse:
        return ASNResourceWithStreamingResponse(self)

    def delete(
        self,
        asn_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASNDeleteResponse]:
        """
        Delete an ASN from botnet threat feed for a given user.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            f"/accounts/{account_id}/botnet_feed/configs/asn/{asn_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ASNDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASNDeleteResponse]], ResultWrapper[ASNDeleteResponse]),
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASNGetResponse]:
        """
        Gets a list of all ASNs registered for a user for the DDoS Botnet Feed API.

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
            f"/accounts/{account_id}/botnet_feed/configs/asn",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ASNGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASNGetResponse]], ResultWrapper[ASNGetResponse]),
        )


class AsyncASNResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncASNResourceWithRawResponse:
        return AsyncASNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncASNResourceWithStreamingResponse:
        return AsyncASNResourceWithStreamingResponse(self)

    async def delete(
        self,
        asn_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASNDeleteResponse]:
        """
        Delete an ASN from botnet threat feed for a given user.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/botnet_feed/configs/asn/{asn_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ASNDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASNDeleteResponse]], ResultWrapper[ASNDeleteResponse]),
        )

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASNGetResponse]:
        """
        Gets a list of all ASNs registered for a user for the DDoS Botnet Feed API.

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
            f"/accounts/{account_id}/botnet_feed/configs/asn",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ASNGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASNGetResponse]], ResultWrapper[ASNGetResponse]),
        )


class ASNResourceWithRawResponse:
    def __init__(self, asn: ASNResource) -> None:
        self._asn = asn

        self.delete = to_raw_response_wrapper(
            asn.delete,
        )
        self.get = to_raw_response_wrapper(
            asn.get,
        )


class AsyncASNResourceWithRawResponse:
    def __init__(self, asn: AsyncASNResource) -> None:
        self._asn = asn

        self.delete = async_to_raw_response_wrapper(
            asn.delete,
        )
        self.get = async_to_raw_response_wrapper(
            asn.get,
        )


class ASNResourceWithStreamingResponse:
    def __init__(self, asn: ASNResource) -> None:
        self._asn = asn

        self.delete = to_streamed_response_wrapper(
            asn.delete,
        )
        self.get = to_streamed_response_wrapper(
            asn.get,
        )


class AsyncASNResourceWithStreamingResponse:
    def __init__(self, asn: AsyncASNResource) -> None:
        self._asn = asn

        self.delete = async_to_streamed_response_wrapper(
            asn.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            asn.get,
        )
