# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .status import StatusResource, AsyncStatusResource

from ...._compat import cached_property

from ....types.secondary_dns.outgoing_create_response import OutgoingCreateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, List

from ...._base_client import make_request_options

from ....types.secondary_dns.outgoing_update_response import OutgoingUpdateResponse

from ....types.secondary_dns.outgoing_delete_response import OutgoingDeleteResponse

from ....types.secondary_dns.disable_transfer import DisableTransfer

from ....types.secondary_dns.enable_transfer import EnableTransfer

from ....types.secondary_dns.outgoing_force_notify_response import OutgoingForceNotifyResponse

from ....types.secondary_dns.outgoing_get_response import OutgoingGetResponse

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
from ....types.secondary_dns import outgoing_create_params
from ....types.secondary_dns import outgoing_update_params
from ....types.secondary_dns import outgoing_disable_params
from ....types.secondary_dns import outgoing_enable_params
from ....types.secondary_dns import outgoing_force_notify_params
from .status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
)
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["OutgoingResource", "AsyncOutgoingResource"]


class OutgoingResource(SyncAPIResource):
    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> OutgoingResourceWithRawResponse:
        return OutgoingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutgoingResourceWithStreamingResponse:
        return OutgoingResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        name: str,
        peers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OutgoingCreateResponse]:
        """
        Create primary zone configuration for outgoing zone transfers.

        Args:
          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            body=maybe_transform(
                {
                    "name": name,
                    "peers": peers,
                },
                outgoing_create_params.OutgoingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OutgoingCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingCreateResponse]], ResultWrapper[OutgoingCreateResponse]),
        )

    def update(
        self,
        *,
        zone_id: str,
        name: str,
        peers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OutgoingUpdateResponse]:
        """
        Update primary zone configuration for outgoing zone transfers.

        Args:
          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            body=maybe_transform(
                {
                    "name": name,
                    "peers": peers,
                },
                outgoing_update_params.OutgoingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OutgoingUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingUpdateResponse]], ResultWrapper[OutgoingUpdateResponse]),
        )

    def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OutgoingDeleteResponse]:
        """
        Delete primary zone configuration for outgoing zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._delete(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OutgoingDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingDeleteResponse]], ResultWrapper[OutgoingDeleteResponse]),
        )

    def disable(
        self,
        *,
        zone_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Disable outgoing zone transfers for primary zone and clears IXFR backlog of
        primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing/disable",
            body=maybe_transform(body, outgoing_disable_params.OutgoingDisableParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DisableTransfer]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def enable(
        self,
        *,
        zone_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Enable outgoing zone transfers for primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing/enable",
            body=maybe_transform(body, outgoing_enable_params.OutgoingEnableParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EnableTransfer]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def force_notify(
        self,
        *,
        zone_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Notifies the secondary nameserver(s) and clears IXFR backlog of primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing/force_notify",
            body=maybe_transform(body, outgoing_force_notify_params.OutgoingForceNotifyParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OutgoingForceNotifyResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OutgoingGetResponse]:
        """
        Get primary zone configuration for outgoing zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OutgoingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingGetResponse]], ResultWrapper[OutgoingGetResponse]),
        )


class AsyncOutgoingResource(AsyncAPIResource):
    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOutgoingResourceWithRawResponse:
        return AsyncOutgoingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutgoingResourceWithStreamingResponse:
        return AsyncOutgoingResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        name: str,
        peers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OutgoingCreateResponse]:
        """
        Create primary zone configuration for outgoing zone transfers.

        Args:
          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "peers": peers,
                },
                outgoing_create_params.OutgoingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OutgoingCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingCreateResponse]], ResultWrapper[OutgoingCreateResponse]),
        )

    async def update(
        self,
        *,
        zone_id: str,
        name: str,
        peers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OutgoingUpdateResponse]:
        """
        Update primary zone configuration for outgoing zone transfers.

        Args:
          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "peers": peers,
                },
                outgoing_update_params.OutgoingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OutgoingUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingUpdateResponse]], ResultWrapper[OutgoingUpdateResponse]),
        )

    async def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OutgoingDeleteResponse]:
        """
        Delete primary zone configuration for outgoing zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OutgoingDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingDeleteResponse]], ResultWrapper[OutgoingDeleteResponse]),
        )

    async def disable(
        self,
        *,
        zone_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Disable outgoing zone transfers for primary zone and clears IXFR backlog of
        primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing/disable",
            body=await async_maybe_transform(body, outgoing_disable_params.OutgoingDisableParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DisableTransfer]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def enable(
        self,
        *,
        zone_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Enable outgoing zone transfers for primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing/enable",
            body=await async_maybe_transform(body, outgoing_enable_params.OutgoingEnableParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EnableTransfer]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def force_notify(
        self,
        *,
        zone_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Notifies the secondary nameserver(s) and clears IXFR backlog of primary zone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/secondary_dns/outgoing/force_notify",
            body=await async_maybe_transform(body, outgoing_force_notify_params.OutgoingForceNotifyParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OutgoingForceNotifyResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OutgoingGetResponse]:
        """
        Get primary zone configuration for outgoing zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/secondary_dns/outgoing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OutgoingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OutgoingGetResponse]], ResultWrapper[OutgoingGetResponse]),
        )


class OutgoingResourceWithRawResponse:
    def __init__(self, outgoing: OutgoingResource) -> None:
        self._outgoing = outgoing

        self.create = to_raw_response_wrapper(
            outgoing.create,
        )
        self.update = to_raw_response_wrapper(
            outgoing.update,
        )
        self.delete = to_raw_response_wrapper(
            outgoing.delete,
        )
        self.disable = to_raw_response_wrapper(
            outgoing.disable,
        )
        self.enable = to_raw_response_wrapper(
            outgoing.enable,
        )
        self.force_notify = to_raw_response_wrapper(
            outgoing.force_notify,
        )
        self.get = to_raw_response_wrapper(
            outgoing.get,
        )

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._outgoing.status)


class AsyncOutgoingResourceWithRawResponse:
    def __init__(self, outgoing: AsyncOutgoingResource) -> None:
        self._outgoing = outgoing

        self.create = async_to_raw_response_wrapper(
            outgoing.create,
        )
        self.update = async_to_raw_response_wrapper(
            outgoing.update,
        )
        self.delete = async_to_raw_response_wrapper(
            outgoing.delete,
        )
        self.disable = async_to_raw_response_wrapper(
            outgoing.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            outgoing.enable,
        )
        self.force_notify = async_to_raw_response_wrapper(
            outgoing.force_notify,
        )
        self.get = async_to_raw_response_wrapper(
            outgoing.get,
        )

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._outgoing.status)


class OutgoingResourceWithStreamingResponse:
    def __init__(self, outgoing: OutgoingResource) -> None:
        self._outgoing = outgoing

        self.create = to_streamed_response_wrapper(
            outgoing.create,
        )
        self.update = to_streamed_response_wrapper(
            outgoing.update,
        )
        self.delete = to_streamed_response_wrapper(
            outgoing.delete,
        )
        self.disable = to_streamed_response_wrapper(
            outgoing.disable,
        )
        self.enable = to_streamed_response_wrapper(
            outgoing.enable,
        )
        self.force_notify = to_streamed_response_wrapper(
            outgoing.force_notify,
        )
        self.get = to_streamed_response_wrapper(
            outgoing.get,
        )

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._outgoing.status)


class AsyncOutgoingResourceWithStreamingResponse:
    def __init__(self, outgoing: AsyncOutgoingResource) -> None:
        self._outgoing = outgoing

        self.create = async_to_streamed_response_wrapper(
            outgoing.create,
        )
        self.update = async_to_streamed_response_wrapper(
            outgoing.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            outgoing.delete,
        )
        self.disable = async_to_streamed_response_wrapper(
            outgoing.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            outgoing.enable,
        )
        self.force_notify = async_to_streamed_response_wrapper(
            outgoing.force_notify,
        )
        self.get = async_to_streamed_response_wrapper(
            outgoing.get,
        )

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._outgoing.status)
