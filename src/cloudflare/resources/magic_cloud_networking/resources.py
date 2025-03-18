# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
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
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.magic_cloud_networking import (
    resource_get_params,
    resource_list_params,
    resource_export_params,
    resource_policy_preview_params,
)
from ...types.magic_cloud_networking.resource_get_response import ResourceGetResponse
from ...types.magic_cloud_networking.resource_list_response import ResourceListResponse
from ...types.magic_cloud_networking.resource_policy_preview_response import ResourcePolicyPreviewResponse

__all__ = ["ResourcesResource", "AsyncResourcesResource"]


class ResourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ResourcesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cloudflare: bool | NotGiven = NOT_GIVEN,
        desc: bool | NotGiven = NOT_GIVEN,
        managed: bool | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        resource_group: str | NotGiven = NOT_GIVEN,
        resource_id: List[str] | NotGiven = NOT_GIVEN,
        resource_type: List[
            Literal[
                "aws_customer_gateway",
                "aws_egress_only_internet_gateway",
                "aws_internet_gateway",
                "aws_instance",
                "aws_network_interface",
                "aws_route",
                "aws_route_table",
                "aws_route_table_association",
                "aws_subnet",
                "aws_vpc",
                "aws_vpc_ipv4_cidr_block_association",
                "aws_vpn_connection",
                "aws_vpn_connection_route",
                "aws_vpn_gateway",
                "aws_security_group",
                "aws_vpc_security_group_ingress_rule",
                "aws_vpc_security_group_egress_rule",
                "aws_ec2_managed_prefix_list",
                "aws_ec2_transit_gateway",
                "aws_ec2_transit_gateway_prefix_list_reference",
                "aws_ec2_transit_gateway_vpc_attachment",
                "azurerm_application_security_group",
                "azurerm_lb",
                "azurerm_lb_backend_address_pool",
                "azurerm_lb_nat_pool",
                "azurerm_lb_nat_rule",
                "azurerm_lb_rule",
                "azurerm_local_network_gateway",
                "azurerm_network_interface",
                "azurerm_network_interface_application_security_group_association",
                "azurerm_network_interface_backend_address_pool_association",
                "azurerm_network_interface_security_group_association",
                "azurerm_network_security_group",
                "azurerm_public_ip",
                "azurerm_route",
                "azurerm_route_table",
                "azurerm_subnet",
                "azurerm_subnet_route_table_association",
                "azurerm_virtual_machine",
                "azurerm_virtual_network_gateway_connection",
                "azurerm_virtual_network",
                "azurerm_virtual_network_gateway",
                "google_compute_network",
                "google_compute_subnetwork",
                "google_compute_vpn_gateway",
                "google_compute_vpn_tunnel",
                "google_compute_route",
                "google_compute_address",
                "google_compute_global_address",
                "google_compute_router",
                "google_compute_interconnect_attachment",
                "google_compute_ha_vpn_gateway",
                "google_compute_forwarding_rule",
                "google_compute_network_firewall_policy",
                "google_compute_network_firewall_policy_rule",
                "cloudflare_static_route",
                "cloudflare_ipsec_tunnel",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        search: List[str] | NotGiven = NOT_GIVEN,
        v2: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[ResourceListResponse]:
        """
        List resources in the Resource Catalog (Closed Beta)

        Args:
          order_by: one of ["id", "resource_type", "region"]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/cloud/resources",
            page=SyncV4PagePaginationArray[ResourceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cloudflare": cloudflare,
                        "desc": desc,
                        "managed": managed,
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                        "provider_id": provider_id,
                        "region": region,
                        "resource_group": resource_group,
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                        "search": search,
                        "v2": v2,
                    },
                    resource_list_params.ResourceListParams,
                ),
            ),
            model=ResourceListResponse,
        )

    def export(
        self,
        *,
        account_id: str,
        desc: bool | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        resource_group: str | NotGiven = NOT_GIVEN,
        resource_id: List[str] | NotGiven = NOT_GIVEN,
        resource_type: List[
            Literal[
                "aws_customer_gateway",
                "aws_egress_only_internet_gateway",
                "aws_internet_gateway",
                "aws_instance",
                "aws_network_interface",
                "aws_route",
                "aws_route_table",
                "aws_route_table_association",
                "aws_subnet",
                "aws_vpc",
                "aws_vpc_ipv4_cidr_block_association",
                "aws_vpn_connection",
                "aws_vpn_connection_route",
                "aws_vpn_gateway",
                "aws_security_group",
                "aws_vpc_security_group_ingress_rule",
                "aws_vpc_security_group_egress_rule",
                "aws_ec2_managed_prefix_list",
                "aws_ec2_transit_gateway",
                "aws_ec2_transit_gateway_prefix_list_reference",
                "aws_ec2_transit_gateway_vpc_attachment",
                "azurerm_application_security_group",
                "azurerm_lb",
                "azurerm_lb_backend_address_pool",
                "azurerm_lb_nat_pool",
                "azurerm_lb_nat_rule",
                "azurerm_lb_rule",
                "azurerm_local_network_gateway",
                "azurerm_network_interface",
                "azurerm_network_interface_application_security_group_association",
                "azurerm_network_interface_backend_address_pool_association",
                "azurerm_network_interface_security_group_association",
                "azurerm_network_security_group",
                "azurerm_public_ip",
                "azurerm_route",
                "azurerm_route_table",
                "azurerm_subnet",
                "azurerm_subnet_route_table_association",
                "azurerm_virtual_machine",
                "azurerm_virtual_network_gateway_connection",
                "azurerm_virtual_network",
                "azurerm_virtual_network_gateway",
                "google_compute_network",
                "google_compute_subnetwork",
                "google_compute_vpn_gateway",
                "google_compute_vpn_tunnel",
                "google_compute_route",
                "google_compute_address",
                "google_compute_global_address",
                "google_compute_router",
                "google_compute_interconnect_attachment",
                "google_compute_ha_vpn_gateway",
                "google_compute_forwarding_rule",
                "google_compute_network_firewall_policy",
                "google_compute_network_firewall_policy_rule",
                "cloudflare_static_route",
                "cloudflare_ipsec_tunnel",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        search: List[str] | NotGiven = NOT_GIVEN,
        v2: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Export resources in the Resource Catalog as a JSON file (Closed Beta)

        Args:
          order_by: one of ["id", "resource_type", "region"]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/magic/cloud/resources/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "desc": desc,
                        "order_by": order_by,
                        "provider_id": provider_id,
                        "region": region,
                        "resource_group": resource_group,
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                        "search": search,
                        "v2": v2,
                    },
                    resource_export_params.ResourceExportParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get(
        self,
        resource_id: str,
        *,
        account_id: str,
        v2: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGetResponse:
        """
        Read an resource from the Resource Catalog (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/cloud/resources/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"v2": v2}, resource_get_params.ResourceGetParams),
                post_parser=ResultWrapper[ResourceGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ResourceGetResponse], ResultWrapper[ResourceGetResponse]),
        )

    def policy_preview(
        self,
        *,
        account_id: str,
        policy: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Preview Rego query result against the latest resource catalog (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/cloud/resources/policy-preview",
            body=maybe_transform({"policy": policy}, resource_policy_preview_params.ResourcePolicyPreviewParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ResourcePolicyPreviewResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncResourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncResourcesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cloudflare: bool | NotGiven = NOT_GIVEN,
        desc: bool | NotGiven = NOT_GIVEN,
        managed: bool | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        resource_group: str | NotGiven = NOT_GIVEN,
        resource_id: List[str] | NotGiven = NOT_GIVEN,
        resource_type: List[
            Literal[
                "aws_customer_gateway",
                "aws_egress_only_internet_gateway",
                "aws_internet_gateway",
                "aws_instance",
                "aws_network_interface",
                "aws_route",
                "aws_route_table",
                "aws_route_table_association",
                "aws_subnet",
                "aws_vpc",
                "aws_vpc_ipv4_cidr_block_association",
                "aws_vpn_connection",
                "aws_vpn_connection_route",
                "aws_vpn_gateway",
                "aws_security_group",
                "aws_vpc_security_group_ingress_rule",
                "aws_vpc_security_group_egress_rule",
                "aws_ec2_managed_prefix_list",
                "aws_ec2_transit_gateway",
                "aws_ec2_transit_gateway_prefix_list_reference",
                "aws_ec2_transit_gateway_vpc_attachment",
                "azurerm_application_security_group",
                "azurerm_lb",
                "azurerm_lb_backend_address_pool",
                "azurerm_lb_nat_pool",
                "azurerm_lb_nat_rule",
                "azurerm_lb_rule",
                "azurerm_local_network_gateway",
                "azurerm_network_interface",
                "azurerm_network_interface_application_security_group_association",
                "azurerm_network_interface_backend_address_pool_association",
                "azurerm_network_interface_security_group_association",
                "azurerm_network_security_group",
                "azurerm_public_ip",
                "azurerm_route",
                "azurerm_route_table",
                "azurerm_subnet",
                "azurerm_subnet_route_table_association",
                "azurerm_virtual_machine",
                "azurerm_virtual_network_gateway_connection",
                "azurerm_virtual_network",
                "azurerm_virtual_network_gateway",
                "google_compute_network",
                "google_compute_subnetwork",
                "google_compute_vpn_gateway",
                "google_compute_vpn_tunnel",
                "google_compute_route",
                "google_compute_address",
                "google_compute_global_address",
                "google_compute_router",
                "google_compute_interconnect_attachment",
                "google_compute_ha_vpn_gateway",
                "google_compute_forwarding_rule",
                "google_compute_network_firewall_policy",
                "google_compute_network_firewall_policy_rule",
                "cloudflare_static_route",
                "cloudflare_ipsec_tunnel",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        search: List[str] | NotGiven = NOT_GIVEN,
        v2: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ResourceListResponse, AsyncV4PagePaginationArray[ResourceListResponse]]:
        """
        List resources in the Resource Catalog (Closed Beta)

        Args:
          order_by: one of ["id", "resource_type", "region"]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/cloud/resources",
            page=AsyncV4PagePaginationArray[ResourceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cloudflare": cloudflare,
                        "desc": desc,
                        "managed": managed,
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                        "provider_id": provider_id,
                        "region": region,
                        "resource_group": resource_group,
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                        "search": search,
                        "v2": v2,
                    },
                    resource_list_params.ResourceListParams,
                ),
            ),
            model=ResourceListResponse,
        )

    async def export(
        self,
        *,
        account_id: str,
        desc: bool | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        resource_group: str | NotGiven = NOT_GIVEN,
        resource_id: List[str] | NotGiven = NOT_GIVEN,
        resource_type: List[
            Literal[
                "aws_customer_gateway",
                "aws_egress_only_internet_gateway",
                "aws_internet_gateway",
                "aws_instance",
                "aws_network_interface",
                "aws_route",
                "aws_route_table",
                "aws_route_table_association",
                "aws_subnet",
                "aws_vpc",
                "aws_vpc_ipv4_cidr_block_association",
                "aws_vpn_connection",
                "aws_vpn_connection_route",
                "aws_vpn_gateway",
                "aws_security_group",
                "aws_vpc_security_group_ingress_rule",
                "aws_vpc_security_group_egress_rule",
                "aws_ec2_managed_prefix_list",
                "aws_ec2_transit_gateway",
                "aws_ec2_transit_gateway_prefix_list_reference",
                "aws_ec2_transit_gateway_vpc_attachment",
                "azurerm_application_security_group",
                "azurerm_lb",
                "azurerm_lb_backend_address_pool",
                "azurerm_lb_nat_pool",
                "azurerm_lb_nat_rule",
                "azurerm_lb_rule",
                "azurerm_local_network_gateway",
                "azurerm_network_interface",
                "azurerm_network_interface_application_security_group_association",
                "azurerm_network_interface_backend_address_pool_association",
                "azurerm_network_interface_security_group_association",
                "azurerm_network_security_group",
                "azurerm_public_ip",
                "azurerm_route",
                "azurerm_route_table",
                "azurerm_subnet",
                "azurerm_subnet_route_table_association",
                "azurerm_virtual_machine",
                "azurerm_virtual_network_gateway_connection",
                "azurerm_virtual_network",
                "azurerm_virtual_network_gateway",
                "google_compute_network",
                "google_compute_subnetwork",
                "google_compute_vpn_gateway",
                "google_compute_vpn_tunnel",
                "google_compute_route",
                "google_compute_address",
                "google_compute_global_address",
                "google_compute_router",
                "google_compute_interconnect_attachment",
                "google_compute_ha_vpn_gateway",
                "google_compute_forwarding_rule",
                "google_compute_network_firewall_policy",
                "google_compute_network_firewall_policy_rule",
                "cloudflare_static_route",
                "cloudflare_ipsec_tunnel",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        search: List[str] | NotGiven = NOT_GIVEN,
        v2: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Export resources in the Resource Catalog as a JSON file (Closed Beta)

        Args:
          order_by: one of ["id", "resource_type", "region"]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/magic/cloud/resources/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "desc": desc,
                        "order_by": order_by,
                        "provider_id": provider_id,
                        "region": region,
                        "resource_group": resource_group,
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                        "search": search,
                        "v2": v2,
                    },
                    resource_export_params.ResourceExportParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get(
        self,
        resource_id: str,
        *,
        account_id: str,
        v2: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceGetResponse:
        """
        Read an resource from the Resource Catalog (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not resource_id:
            raise ValueError(f"Expected a non-empty value for `resource_id` but received {resource_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/cloud/resources/{resource_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"v2": v2}, resource_get_params.ResourceGetParams),
                post_parser=ResultWrapper[ResourceGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ResourceGetResponse], ResultWrapper[ResourceGetResponse]),
        )

    async def policy_preview(
        self,
        *,
        account_id: str,
        policy: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Preview Rego query result against the latest resource catalog (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/cloud/resources/policy-preview",
            body=await async_maybe_transform(
                {"policy": policy}, resource_policy_preview_params.ResourcePolicyPreviewParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ResourcePolicyPreviewResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class ResourcesResourceWithRawResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

        self.list = to_raw_response_wrapper(
            resources.list,
        )
        self.export = to_custom_raw_response_wrapper(
            resources.export,
            BinaryAPIResponse,
        )
        self.get = to_raw_response_wrapper(
            resources.get,
        )
        self.policy_preview = to_raw_response_wrapper(
            resources.policy_preview,
        )


class AsyncResourcesResourceWithRawResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

        self.list = async_to_raw_response_wrapper(
            resources.list,
        )
        self.export = async_to_custom_raw_response_wrapper(
            resources.export,
            AsyncBinaryAPIResponse,
        )
        self.get = async_to_raw_response_wrapper(
            resources.get,
        )
        self.policy_preview = async_to_raw_response_wrapper(
            resources.policy_preview,
        )


class ResourcesResourceWithStreamingResponse:
    def __init__(self, resources: ResourcesResource) -> None:
        self._resources = resources

        self.list = to_streamed_response_wrapper(
            resources.list,
        )
        self.export = to_custom_streamed_response_wrapper(
            resources.export,
            StreamedBinaryAPIResponse,
        )
        self.get = to_streamed_response_wrapper(
            resources.get,
        )
        self.policy_preview = to_streamed_response_wrapper(
            resources.policy_preview,
        )


class AsyncResourcesResourceWithStreamingResponse:
    def __init__(self, resources: AsyncResourcesResource) -> None:
        self._resources = resources

        self.list = async_to_streamed_response_wrapper(
            resources.list,
        )
        self.export = async_to_custom_streamed_response_wrapper(
            resources.export,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get = async_to_streamed_response_wrapper(
            resources.get,
        )
        self.policy_preview = async_to_streamed_response_wrapper(
            resources.policy_preview,
        )
