# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResourceListParams"]


class ResourceListParams(TypedDict, total=False):
    account_id: Required[str]

    cloudflare: bool

    desc: bool

    managed: bool

    order_by: str
    """One of ["id", "resource_type", "region"]."""

    page: int

    per_page: int

    provider_id: str

    region: str

    resource_group: str

    resource_id: List[str]

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

    search: List[str]

    v2: bool
