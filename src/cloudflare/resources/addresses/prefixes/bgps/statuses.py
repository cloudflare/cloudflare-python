# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.addresses.prefixes.bgps import (
    StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse,
    StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse,
)

from typing import Type

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .....types.addresses.prefixes.bgps import (
    status_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status_params,
)
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Statuses", "AsyncStatuses"]


class Statuses(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusesWithRawResponse:
        return StatusesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusesWithStreamingResponse:
        return StatusesWithStreamingResponse(self)

    def ip_address_management_dynamic_advertisement_get_advertisement_status(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse:
        """
        List the current advertisement state for a prefix.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse],
                ResultWrapper[StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse],
            ),
        )

    def ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        advertised: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse:
        """
        Advertise or withdraw BGP route for a prefix.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          advertised: Enablement of prefix advertisement to the Internet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return self._patch(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/status",
            body=maybe_transform(
                {"advertised": advertised},
                status_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status_params.StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse],
                ResultWrapper[
                    StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse
                ],
            ),
        )


class AsyncStatuses(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusesWithRawResponse:
        return AsyncStatusesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusesWithStreamingResponse:
        return AsyncStatusesWithStreamingResponse(self)

    async def ip_address_management_dynamic_advertisement_get_advertisement_status(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse:
        """
        List the current advertisement state for a prefix.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse],
                ResultWrapper[StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse],
            ),
        )

    async def ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        advertised: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse:
        """
        Advertise or withdraw BGP route for a prefix.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          advertised: Enablement of prefix advertisement to the Internet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return await self._patch(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/status",
            body=maybe_transform(
                {"advertised": advertised},
                status_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status_params.StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse],
                ResultWrapper[
                    StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse
                ],
            ),
        )


class StatusesWithRawResponse:
    def __init__(self, statuses: Statuses) -> None:
        self._statuses = statuses

        self.ip_address_management_dynamic_advertisement_get_advertisement_status = to_raw_response_wrapper(
            statuses.ip_address_management_dynamic_advertisement_get_advertisement_status,
        )
        self.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status = (
            to_raw_response_wrapper(
                statuses.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status,
            )
        )


class AsyncStatusesWithRawResponse:
    def __init__(self, statuses: AsyncStatuses) -> None:
        self._statuses = statuses

        self.ip_address_management_dynamic_advertisement_get_advertisement_status = async_to_raw_response_wrapper(
            statuses.ip_address_management_dynamic_advertisement_get_advertisement_status,
        )
        self.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status = (
            async_to_raw_response_wrapper(
                statuses.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status,
            )
        )


class StatusesWithStreamingResponse:
    def __init__(self, statuses: Statuses) -> None:
        self._statuses = statuses

        self.ip_address_management_dynamic_advertisement_get_advertisement_status = to_streamed_response_wrapper(
            statuses.ip_address_management_dynamic_advertisement_get_advertisement_status,
        )
        self.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status = (
            to_streamed_response_wrapper(
                statuses.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status,
            )
        )


class AsyncStatusesWithStreamingResponse:
    def __init__(self, statuses: AsyncStatuses) -> None:
        self._statuses = statuses

        self.ip_address_management_dynamic_advertisement_get_advertisement_status = async_to_streamed_response_wrapper(
            statuses.ip_address_management_dynamic_advertisement_get_advertisement_status,
        )
        self.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status = (
            async_to_streamed_response_wrapper(
                statuses.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status,
            )
        )
