# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .availabilities import Availabilities, AsyncAvailabilities

from ..._compat import cached_property

from .verifies import Verifies, AsyncVerifies

from ...types import CustomNCreateResponse, CustomNListResponse, CustomNDeleteResponse

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
from ...types import custom_n_create_params
from .availabilities import (
    Availabilities,
    AsyncAvailabilities,
    AvailabilitiesWithRawResponse,
    AsyncAvailabilitiesWithRawResponse,
    AvailabilitiesWithStreamingResponse,
    AsyncAvailabilitiesWithStreamingResponse,
)
from .verifies import (
    Verifies,
    AsyncVerifies,
    VerifiesWithRawResponse,
    AsyncVerifiesWithRawResponse,
    VerifiesWithStreamingResponse,
    AsyncVerifiesWithStreamingResponse,
)
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["CustomNs", "AsyncCustomNs"]


class CustomNs(SyncAPIResource):
    @cached_property
    def availabilities(self) -> Availabilities:
        return Availabilities(self._client)

    @cached_property
    def verifies(self) -> Verifies:
        return Verifies(self._client)

    @cached_property
    def with_raw_response(self) -> CustomNsWithRawResponse:
        return CustomNsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomNsWithStreamingResponse:
        return CustomNsWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        ns_name: str,
        ns_set: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomNCreateResponse:
        """
        Add Account Custom Nameserver

        Args:
          account_id: Account identifier tag.

          ns_name: The FQDN of the name server.

          ns_set: The number of the set that this name server belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/custom_ns",
            body=maybe_transform(
                {
                    "ns_name": ns_name,
                    "ns_set": ns_set,
                },
                custom_n_create_params.CustomNCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomNCreateResponse], ResultWrapper[CustomNCreateResponse]),
        )

    def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomNListResponse]:
        """
        List an account's custom nameservers.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/custom_ns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomNListResponse]], ResultWrapper[CustomNListResponse]),
        )

    def delete(
        self,
        custom_ns_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomNDeleteResponse]:
        """
        Delete Account Custom Nameserver

        Args:
          account_id: Account identifier tag.

          custom_ns_id: The FQDN of the name server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not custom_ns_id:
            raise ValueError(f"Expected a non-empty value for `custom_ns_id` but received {custom_ns_id!r}")
        return cast(
            Optional[CustomNDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/custom_ns/{custom_ns_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomNDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncCustomNs(AsyncAPIResource):
    @cached_property
    def availabilities(self) -> AsyncAvailabilities:
        return AsyncAvailabilities(self._client)

    @cached_property
    def verifies(self) -> AsyncVerifies:
        return AsyncVerifies(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomNsWithRawResponse:
        return AsyncCustomNsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomNsWithStreamingResponse:
        return AsyncCustomNsWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        ns_name: str,
        ns_set: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomNCreateResponse:
        """
        Add Account Custom Nameserver

        Args:
          account_id: Account identifier tag.

          ns_name: The FQDN of the name server.

          ns_set: The number of the set that this name server belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/custom_ns",
            body=maybe_transform(
                {
                    "ns_name": ns_name,
                    "ns_set": ns_set,
                },
                custom_n_create_params.CustomNCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomNCreateResponse], ResultWrapper[CustomNCreateResponse]),
        )

    async def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomNListResponse]:
        """
        List an account's custom nameservers.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/custom_ns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomNListResponse]], ResultWrapper[CustomNListResponse]),
        )

    async def delete(
        self,
        custom_ns_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomNDeleteResponse]:
        """
        Delete Account Custom Nameserver

        Args:
          account_id: Account identifier tag.

          custom_ns_id: The FQDN of the name server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not custom_ns_id:
            raise ValueError(f"Expected a non-empty value for `custom_ns_id` but received {custom_ns_id!r}")
        return cast(
            Optional[CustomNDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/custom_ns/{custom_ns_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomNDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class CustomNsWithRawResponse:
    def __init__(self, custom_ns: CustomNs) -> None:
        self._custom_ns = custom_ns

        self.create = to_raw_response_wrapper(
            custom_ns.create,
        )
        self.list = to_raw_response_wrapper(
            custom_ns.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_ns.delete,
        )

    @cached_property
    def availabilities(self) -> AvailabilitiesWithRawResponse:
        return AvailabilitiesWithRawResponse(self._custom_ns.availabilities)

    @cached_property
    def verifies(self) -> VerifiesWithRawResponse:
        return VerifiesWithRawResponse(self._custom_ns.verifies)


class AsyncCustomNsWithRawResponse:
    def __init__(self, custom_ns: AsyncCustomNs) -> None:
        self._custom_ns = custom_ns

        self.create = async_to_raw_response_wrapper(
            custom_ns.create,
        )
        self.list = async_to_raw_response_wrapper(
            custom_ns.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_ns.delete,
        )

    @cached_property
    def availabilities(self) -> AsyncAvailabilitiesWithRawResponse:
        return AsyncAvailabilitiesWithRawResponse(self._custom_ns.availabilities)

    @cached_property
    def verifies(self) -> AsyncVerifiesWithRawResponse:
        return AsyncVerifiesWithRawResponse(self._custom_ns.verifies)


class CustomNsWithStreamingResponse:
    def __init__(self, custom_ns: CustomNs) -> None:
        self._custom_ns = custom_ns

        self.create = to_streamed_response_wrapper(
            custom_ns.create,
        )
        self.list = to_streamed_response_wrapper(
            custom_ns.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_ns.delete,
        )

    @cached_property
    def availabilities(self) -> AvailabilitiesWithStreamingResponse:
        return AvailabilitiesWithStreamingResponse(self._custom_ns.availabilities)

    @cached_property
    def verifies(self) -> VerifiesWithStreamingResponse:
        return VerifiesWithStreamingResponse(self._custom_ns.verifies)


class AsyncCustomNsWithStreamingResponse:
    def __init__(self, custom_ns: AsyncCustomNs) -> None:
        self._custom_ns = custom_ns

        self.create = async_to_streamed_response_wrapper(
            custom_ns.create,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_ns.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_ns.delete,
        )

    @cached_property
    def availabilities(self) -> AsyncAvailabilitiesWithStreamingResponse:
        return AsyncAvailabilitiesWithStreamingResponse(self._custom_ns.availabilities)

    @cached_property
    def verifies(self) -> AsyncVerifiesWithStreamingResponse:
        return AsyncVerifiesWithStreamingResponse(self._custom_ns.verifies)
