# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from .address_spaces import (
    AddressSpacesResource,
    AsyncAddressSpacesResource,
    AddressSpacesResourceWithRawResponse,
    AsyncAddressSpacesResourceWithRawResponse,
    AddressSpacesResourceWithStreamingResponse,
    AsyncAddressSpacesResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.magic_cloud_networking import (
    on_ramp_get_params,
    on_ramp_edit_params,
    on_ramp_list_params,
    on_ramp_create_params,
    on_ramp_delete_params,
    on_ramp_update_params,
)
from ....types.magic_cloud_networking.on_ramp_get_response import OnRampGetResponse
from ....types.magic_cloud_networking.on_ramp_edit_response import OnRampEditResponse
from ....types.magic_cloud_networking.on_ramp_list_response import OnRampListResponse
from ....types.magic_cloud_networking.on_ramp_plan_response import OnRampPlanResponse
from ....types.magic_cloud_networking.on_ramp_apply_response import OnRampApplyResponse
from ....types.magic_cloud_networking.on_ramp_create_response import OnRampCreateResponse
from ....types.magic_cloud_networking.on_ramp_delete_response import OnRampDeleteResponse
from ....types.magic_cloud_networking.on_ramp_update_response import OnRampUpdateResponse

__all__ = ["OnRampsResource", "AsyncOnRampsResource"]


class OnRampsResource(SyncAPIResource):
    @cached_property
    def address_spaces(self) -> AddressSpacesResource:
        return AddressSpacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> OnRampsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OnRampsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnRampsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OnRampsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        cloud_type: Literal["AWS", "AZURE", "GOOGLE"],
        install_routes_in_cloud: bool,
        install_routes_in_magic_wan: bool,
        name: str,
        type: Literal["OnrampTypeSingle", "OnrampTypeHub"],
        adopted_hub_id: str | NotGiven = NOT_GIVEN,
        attached_hubs: List[str] | NotGiven = NOT_GIVEN,
        attached_vpcs: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        hub_provider_id: str | NotGiven = NOT_GIVEN,
        manage_hub_to_hub_attachments: bool | NotGiven = NOT_GIVEN,
        manage_vpc_to_hub_attachments: bool | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        vpc: str | NotGiven = NOT_GIVEN,
        forwarded: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampCreateResponse:
        """
        Create a new On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"forwarded": forwarded}), **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/magic/cloud/onramps",
            body=maybe_transform(
                {
                    "cloud_type": cloud_type,
                    "install_routes_in_cloud": install_routes_in_cloud,
                    "install_routes_in_magic_wan": install_routes_in_magic_wan,
                    "name": name,
                    "type": type,
                    "adopted_hub_id": adopted_hub_id,
                    "attached_hubs": attached_hubs,
                    "attached_vpcs": attached_vpcs,
                    "description": description,
                    "hub_provider_id": hub_provider_id,
                    "manage_hub_to_hub_attachments": manage_hub_to_hub_attachments,
                    "manage_vpc_to_hub_attachments": manage_vpc_to_hub_attachments,
                    "region": region,
                    "vpc": vpc,
                },
                on_ramp_create_params.OnRampCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OnRampCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OnRampCreateResponse], ResultWrapper[OnRampCreateResponse]),
        )

    def update(
        self,
        onramp_id: str,
        *,
        account_id: str,
        attached_hubs: List[str] | NotGiven = NOT_GIVEN,
        attached_vpcs: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        install_routes_in_cloud: bool | NotGiven = NOT_GIVEN,
        install_routes_in_magic_wan: bool | NotGiven = NOT_GIVEN,
        manage_hub_to_hub_attachments: bool | NotGiven = NOT_GIVEN,
        manage_vpc_to_hub_attachments: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        vpc: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampUpdateResponse:
        """
        Update an On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}",
            body=maybe_transform(
                {
                    "attached_hubs": attached_hubs,
                    "attached_vpcs": attached_vpcs,
                    "description": description,
                    "install_routes_in_cloud": install_routes_in_cloud,
                    "install_routes_in_magic_wan": install_routes_in_magic_wan,
                    "manage_hub_to_hub_attachments": manage_hub_to_hub_attachments,
                    "manage_vpc_to_hub_attachments": manage_vpc_to_hub_attachments,
                    "name": name,
                    "vpc": vpc,
                },
                on_ramp_update_params.OnRampUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OnRampUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OnRampUpdateResponse], ResultWrapper[OnRampUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        desc: bool | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        status: bool | NotGiven = NOT_GIVEN,
        vpcs: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[OnRampListResponse]:
        """
        List On-ramps (Closed Beta)

        Args:
          order_by: one of ["updated_at", "id", "cloud_type", "name"]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/cloud/onramps",
            page=SyncSinglePage[OnRampListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "desc": desc,
                        "order_by": order_by,
                        "status": status,
                        "vpcs": vpcs,
                    },
                    on_ramp_list_params.OnRampListParams,
                ),
            ),
            model=OnRampListResponse,
        )

    def delete(
        self,
        onramp_id: str,
        *,
        account_id: str,
        destroy: bool | NotGiven = NOT_GIVEN,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampDeleteResponse:
        """
        Delete an On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        return self._delete(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "destroy": destroy,
                        "force": force,
                    },
                    on_ramp_delete_params.OnRampDeleteParams,
                ),
                post_parser=ResultWrapper[OnRampDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[OnRampDeleteResponse], ResultWrapper[OnRampDeleteResponse]),
        )

    def apply(
        self,
        onramp_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampApplyResponse:
        """
        Apply an On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}/apply",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnRampApplyResponse,
        )

    def edit(
        self,
        onramp_id: str,
        *,
        account_id: str,
        attached_hubs: List[str] | NotGiven = NOT_GIVEN,
        attached_vpcs: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        install_routes_in_cloud: bool | NotGiven = NOT_GIVEN,
        install_routes_in_magic_wan: bool | NotGiven = NOT_GIVEN,
        manage_hub_to_hub_attachments: bool | NotGiven = NOT_GIVEN,
        manage_vpc_to_hub_attachments: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        vpc: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampEditResponse:
        """
        Update an On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        return self._patch(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}",
            body=maybe_transform(
                {
                    "attached_hubs": attached_hubs,
                    "attached_vpcs": attached_vpcs,
                    "description": description,
                    "install_routes_in_cloud": install_routes_in_cloud,
                    "install_routes_in_magic_wan": install_routes_in_magic_wan,
                    "manage_hub_to_hub_attachments": manage_hub_to_hub_attachments,
                    "manage_vpc_to_hub_attachments": manage_vpc_to_hub_attachments,
                    "name": name,
                    "vpc": vpc,
                },
                on_ramp_edit_params.OnRampEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OnRampEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[OnRampEditResponse], ResultWrapper[OnRampEditResponse]),
        )

    def export(
        self,
        onramp_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Export an On-ramp to terraform ready file(s) (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        extra_headers = {"Accept": "application/zip", **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def get(
        self,
        onramp_id: str,
        *,
        account_id: str,
        planned_resources: bool | NotGiven = NOT_GIVEN,
        post_apply_resources: bool | NotGiven = NOT_GIVEN,
        status: bool | NotGiven = NOT_GIVEN,
        vpcs: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampGetResponse:
        """
        Read an On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "planned_resources": planned_resources,
                        "post_apply_resources": post_apply_resources,
                        "status": status,
                        "vpcs": vpcs,
                    },
                    on_ramp_get_params.OnRampGetParams,
                ),
                post_parser=ResultWrapper[OnRampGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OnRampGetResponse], ResultWrapper[OnRampGetResponse]),
        )

    def plan(
        self,
        onramp_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampPlanResponse:
        """
        Plan an On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}/plan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnRampPlanResponse,
        )


class AsyncOnRampsResource(AsyncAPIResource):
    @cached_property
    def address_spaces(self) -> AsyncAddressSpacesResource:
        return AsyncAddressSpacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOnRampsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOnRampsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnRampsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOnRampsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        cloud_type: Literal["AWS", "AZURE", "GOOGLE"],
        install_routes_in_cloud: bool,
        install_routes_in_magic_wan: bool,
        name: str,
        type: Literal["OnrampTypeSingle", "OnrampTypeHub"],
        adopted_hub_id: str | NotGiven = NOT_GIVEN,
        attached_hubs: List[str] | NotGiven = NOT_GIVEN,
        attached_vpcs: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        hub_provider_id: str | NotGiven = NOT_GIVEN,
        manage_hub_to_hub_attachments: bool | NotGiven = NOT_GIVEN,
        manage_vpc_to_hub_attachments: bool | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        vpc: str | NotGiven = NOT_GIVEN,
        forwarded: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampCreateResponse:
        """
        Create a new On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"forwarded": forwarded}), **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/magic/cloud/onramps",
            body=await async_maybe_transform(
                {
                    "cloud_type": cloud_type,
                    "install_routes_in_cloud": install_routes_in_cloud,
                    "install_routes_in_magic_wan": install_routes_in_magic_wan,
                    "name": name,
                    "type": type,
                    "adopted_hub_id": adopted_hub_id,
                    "attached_hubs": attached_hubs,
                    "attached_vpcs": attached_vpcs,
                    "description": description,
                    "hub_provider_id": hub_provider_id,
                    "manage_hub_to_hub_attachments": manage_hub_to_hub_attachments,
                    "manage_vpc_to_hub_attachments": manage_vpc_to_hub_attachments,
                    "region": region,
                    "vpc": vpc,
                },
                on_ramp_create_params.OnRampCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OnRampCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OnRampCreateResponse], ResultWrapper[OnRampCreateResponse]),
        )

    async def update(
        self,
        onramp_id: str,
        *,
        account_id: str,
        attached_hubs: List[str] | NotGiven = NOT_GIVEN,
        attached_vpcs: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        install_routes_in_cloud: bool | NotGiven = NOT_GIVEN,
        install_routes_in_magic_wan: bool | NotGiven = NOT_GIVEN,
        manage_hub_to_hub_attachments: bool | NotGiven = NOT_GIVEN,
        manage_vpc_to_hub_attachments: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        vpc: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampUpdateResponse:
        """
        Update an On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}",
            body=await async_maybe_transform(
                {
                    "attached_hubs": attached_hubs,
                    "attached_vpcs": attached_vpcs,
                    "description": description,
                    "install_routes_in_cloud": install_routes_in_cloud,
                    "install_routes_in_magic_wan": install_routes_in_magic_wan,
                    "manage_hub_to_hub_attachments": manage_hub_to_hub_attachments,
                    "manage_vpc_to_hub_attachments": manage_vpc_to_hub_attachments,
                    "name": name,
                    "vpc": vpc,
                },
                on_ramp_update_params.OnRampUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OnRampUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OnRampUpdateResponse], ResultWrapper[OnRampUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        desc: bool | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        status: bool | NotGiven = NOT_GIVEN,
        vpcs: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OnRampListResponse, AsyncSinglePage[OnRampListResponse]]:
        """
        List On-ramps (Closed Beta)

        Args:
          order_by: one of ["updated_at", "id", "cloud_type", "name"]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/cloud/onramps",
            page=AsyncSinglePage[OnRampListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "desc": desc,
                        "order_by": order_by,
                        "status": status,
                        "vpcs": vpcs,
                    },
                    on_ramp_list_params.OnRampListParams,
                ),
            ),
            model=OnRampListResponse,
        )

    async def delete(
        self,
        onramp_id: str,
        *,
        account_id: str,
        destroy: bool | NotGiven = NOT_GIVEN,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampDeleteResponse:
        """
        Delete an On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "destroy": destroy,
                        "force": force,
                    },
                    on_ramp_delete_params.OnRampDeleteParams,
                ),
                post_parser=ResultWrapper[OnRampDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[OnRampDeleteResponse], ResultWrapper[OnRampDeleteResponse]),
        )

    async def apply(
        self,
        onramp_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampApplyResponse:
        """
        Apply an On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}/apply",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnRampApplyResponse,
        )

    async def edit(
        self,
        onramp_id: str,
        *,
        account_id: str,
        attached_hubs: List[str] | NotGiven = NOT_GIVEN,
        attached_vpcs: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        install_routes_in_cloud: bool | NotGiven = NOT_GIVEN,
        install_routes_in_magic_wan: bool | NotGiven = NOT_GIVEN,
        manage_hub_to_hub_attachments: bool | NotGiven = NOT_GIVEN,
        manage_vpc_to_hub_attachments: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        vpc: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampEditResponse:
        """
        Update an On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}",
            body=await async_maybe_transform(
                {
                    "attached_hubs": attached_hubs,
                    "attached_vpcs": attached_vpcs,
                    "description": description,
                    "install_routes_in_cloud": install_routes_in_cloud,
                    "install_routes_in_magic_wan": install_routes_in_magic_wan,
                    "manage_hub_to_hub_attachments": manage_hub_to_hub_attachments,
                    "manage_vpc_to_hub_attachments": manage_vpc_to_hub_attachments,
                    "name": name,
                    "vpc": vpc,
                },
                on_ramp_edit_params.OnRampEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OnRampEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[OnRampEditResponse], ResultWrapper[OnRampEditResponse]),
        )

    async def export(
        self,
        onramp_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Export an On-ramp to terraform ready file(s) (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        extra_headers = {"Accept": "application/zip", **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get(
        self,
        onramp_id: str,
        *,
        account_id: str,
        planned_resources: bool | NotGiven = NOT_GIVEN,
        post_apply_resources: bool | NotGiven = NOT_GIVEN,
        status: bool | NotGiven = NOT_GIVEN,
        vpcs: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampGetResponse:
        """
        Read an On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "planned_resources": planned_resources,
                        "post_apply_resources": post_apply_resources,
                        "status": status,
                        "vpcs": vpcs,
                    },
                    on_ramp_get_params.OnRampGetParams,
                ),
                post_parser=ResultWrapper[OnRampGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OnRampGetResponse], ResultWrapper[OnRampGetResponse]),
        )

    async def plan(
        self,
        onramp_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnRampPlanResponse:
        """
        Plan an On-ramp (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not onramp_id:
            raise ValueError(f"Expected a non-empty value for `onramp_id` but received {onramp_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/cloud/onramps/{onramp_id}/plan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnRampPlanResponse,
        )


class OnRampsResourceWithRawResponse:
    def __init__(self, on_ramps: OnRampsResource) -> None:
        self._on_ramps = on_ramps

        self.create = to_raw_response_wrapper(
            on_ramps.create,
        )
        self.update = to_raw_response_wrapper(
            on_ramps.update,
        )
        self.list = to_raw_response_wrapper(
            on_ramps.list,
        )
        self.delete = to_raw_response_wrapper(
            on_ramps.delete,
        )
        self.apply = to_raw_response_wrapper(
            on_ramps.apply,
        )
        self.edit = to_raw_response_wrapper(
            on_ramps.edit,
        )
        self.export = to_custom_raw_response_wrapper(
            on_ramps.export,
            BinaryAPIResponse,
        )
        self.get = to_raw_response_wrapper(
            on_ramps.get,
        )
        self.plan = to_raw_response_wrapper(
            on_ramps.plan,
        )

    @cached_property
    def address_spaces(self) -> AddressSpacesResourceWithRawResponse:
        return AddressSpacesResourceWithRawResponse(self._on_ramps.address_spaces)


class AsyncOnRampsResourceWithRawResponse:
    def __init__(self, on_ramps: AsyncOnRampsResource) -> None:
        self._on_ramps = on_ramps

        self.create = async_to_raw_response_wrapper(
            on_ramps.create,
        )
        self.update = async_to_raw_response_wrapper(
            on_ramps.update,
        )
        self.list = async_to_raw_response_wrapper(
            on_ramps.list,
        )
        self.delete = async_to_raw_response_wrapper(
            on_ramps.delete,
        )
        self.apply = async_to_raw_response_wrapper(
            on_ramps.apply,
        )
        self.edit = async_to_raw_response_wrapper(
            on_ramps.edit,
        )
        self.export = async_to_custom_raw_response_wrapper(
            on_ramps.export,
            AsyncBinaryAPIResponse,
        )
        self.get = async_to_raw_response_wrapper(
            on_ramps.get,
        )
        self.plan = async_to_raw_response_wrapper(
            on_ramps.plan,
        )

    @cached_property
    def address_spaces(self) -> AsyncAddressSpacesResourceWithRawResponse:
        return AsyncAddressSpacesResourceWithRawResponse(self._on_ramps.address_spaces)


class OnRampsResourceWithStreamingResponse:
    def __init__(self, on_ramps: OnRampsResource) -> None:
        self._on_ramps = on_ramps

        self.create = to_streamed_response_wrapper(
            on_ramps.create,
        )
        self.update = to_streamed_response_wrapper(
            on_ramps.update,
        )
        self.list = to_streamed_response_wrapper(
            on_ramps.list,
        )
        self.delete = to_streamed_response_wrapper(
            on_ramps.delete,
        )
        self.apply = to_streamed_response_wrapper(
            on_ramps.apply,
        )
        self.edit = to_streamed_response_wrapper(
            on_ramps.edit,
        )
        self.export = to_custom_streamed_response_wrapper(
            on_ramps.export,
            StreamedBinaryAPIResponse,
        )
        self.get = to_streamed_response_wrapper(
            on_ramps.get,
        )
        self.plan = to_streamed_response_wrapper(
            on_ramps.plan,
        )

    @cached_property
    def address_spaces(self) -> AddressSpacesResourceWithStreamingResponse:
        return AddressSpacesResourceWithStreamingResponse(self._on_ramps.address_spaces)


class AsyncOnRampsResourceWithStreamingResponse:
    def __init__(self, on_ramps: AsyncOnRampsResource) -> None:
        self._on_ramps = on_ramps

        self.create = async_to_streamed_response_wrapper(
            on_ramps.create,
        )
        self.update = async_to_streamed_response_wrapper(
            on_ramps.update,
        )
        self.list = async_to_streamed_response_wrapper(
            on_ramps.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            on_ramps.delete,
        )
        self.apply = async_to_streamed_response_wrapper(
            on_ramps.apply,
        )
        self.edit = async_to_streamed_response_wrapper(
            on_ramps.edit,
        )
        self.export = async_to_custom_streamed_response_wrapper(
            on_ramps.export,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get = async_to_streamed_response_wrapper(
            on_ramps.get,
        )
        self.plan = async_to_streamed_response_wrapper(
            on_ramps.plan,
        )

    @cached_property
    def address_spaces(self) -> AsyncAddressSpacesResourceWithStreamingResponse:
        return AsyncAddressSpacesResourceWithStreamingResponse(self._on_ramps.address_spaces)
