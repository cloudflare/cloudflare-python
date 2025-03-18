# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ResourceListResponse",
    "MonthlyCostEstimate",
    "Observations",
    "Section",
    "SectionHiddenItem",
    "SectionHiddenItemValue",
    "SectionHiddenItemValueMcnStringItem",
    "SectionHiddenItemValueMcnYamlItem",
    "SectionHiddenItemValueMcnYamlDiffItem",
    "SectionHiddenItemValueMcnYamlDiffItemYamlDiff",
    "SectionHiddenItemValueMcnResourcePreviewItem",
    "SectionHiddenItemValueMcnResourcePreviewItemResourcePreview",
    "SectionHiddenItemValueMcnListItem",
    "SectionHiddenItemValueMcnListItemList",
    "SectionHiddenItemValueMcnListItemListMcnStringItem",
    "SectionHiddenItemValueMcnListItemListMcnResourcePreviewItem",
    "SectionHiddenItemValueMcnListItemListMcnResourcePreviewItemResourcePreview",
    "SectionVisibleItem",
    "SectionVisibleItemValue",
    "SectionVisibleItemValueMcnStringItem",
    "SectionVisibleItemValueMcnYamlItem",
    "SectionVisibleItemValueMcnYamlDiffItem",
    "SectionVisibleItemValueMcnYamlDiffItemYamlDiff",
    "SectionVisibleItemValueMcnResourcePreviewItem",
    "SectionVisibleItemValueMcnResourcePreviewItemResourcePreview",
    "SectionVisibleItemValueMcnListItem",
    "SectionVisibleItemValueMcnListItemList",
    "SectionVisibleItemValueMcnListItemListMcnStringItem",
    "SectionVisibleItemValueMcnListItemListMcnResourcePreviewItem",
    "SectionVisibleItemValueMcnListItemListMcnResourcePreviewItemResourcePreview",
    "ManagedBy",
]


class MonthlyCostEstimate(BaseModel):
    currency: str

    monthly_cost: float


class Observations(BaseModel):
    first_observed_at: str

    last_observed_at: str

    provider_id: str

    resource_id: str


class SectionHiddenItemValueMcnStringItem(BaseModel):
    item_type: str

    string: str


class SectionHiddenItemValueMcnYamlItem(BaseModel):
    item_type: str

    yaml: str


class SectionHiddenItemValueMcnYamlDiffItemYamlDiff(BaseModel):
    diff: str

    left_description: str

    left_yaml: str

    right_description: str

    right_yaml: str


class SectionHiddenItemValueMcnYamlDiffItem(BaseModel):
    item_type: str

    yaml_diff: SectionHiddenItemValueMcnYamlDiffItemYamlDiff


class SectionHiddenItemValueMcnResourcePreviewItemResourcePreview(BaseModel):
    id: str

    cloud_type: Literal["AWS", "AZURE", "GOOGLE", "CLOUDFLARE"]

    detail: str

    name: str

    resource_type: Literal[
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

    title: str


class SectionHiddenItemValueMcnResourcePreviewItem(BaseModel):
    item_type: str

    resource_preview: SectionHiddenItemValueMcnResourcePreviewItemResourcePreview


class SectionHiddenItemValueMcnListItemListMcnStringItem(BaseModel):
    item_type: str

    string: str


class SectionHiddenItemValueMcnListItemListMcnResourcePreviewItemResourcePreview(BaseModel):
    id: str

    cloud_type: Literal["AWS", "AZURE", "GOOGLE", "CLOUDFLARE"]

    detail: str

    name: str

    resource_type: Literal[
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

    title: str


class SectionHiddenItemValueMcnListItemListMcnResourcePreviewItem(BaseModel):
    item_type: str

    resource_preview: SectionHiddenItemValueMcnListItemListMcnResourcePreviewItemResourcePreview


SectionHiddenItemValueMcnListItemList: TypeAlias = Annotated[
    Union[
        SectionHiddenItemValueMcnListItemListMcnStringItem, SectionHiddenItemValueMcnListItemListMcnResourcePreviewItem
    ],
    PropertyInfo(discriminator="item_type"),
]


class SectionHiddenItemValueMcnListItem(BaseModel):
    item_type: str

    rule_list: List[SectionHiddenItemValueMcnListItemList] = FieldInfo(alias="list")


SectionHiddenItemValue: TypeAlias = Annotated[
    Union[
        SectionHiddenItemValueMcnStringItem,
        SectionHiddenItemValueMcnYamlItem,
        SectionHiddenItemValueMcnYamlDiffItem,
        SectionHiddenItemValueMcnResourcePreviewItem,
        SectionHiddenItemValueMcnListItem,
    ],
    PropertyInfo(discriminator="item_type"),
]


class SectionHiddenItem(BaseModel):
    help_text: Optional[str] = FieldInfo(alias="helpText", default=None)

    name: Optional[str] = None

    value: Optional[SectionHiddenItemValue] = None


class SectionVisibleItemValueMcnStringItem(BaseModel):
    item_type: str

    string: str


class SectionVisibleItemValueMcnYamlItem(BaseModel):
    item_type: str

    yaml: str


class SectionVisibleItemValueMcnYamlDiffItemYamlDiff(BaseModel):
    diff: str

    left_description: str

    left_yaml: str

    right_description: str

    right_yaml: str


class SectionVisibleItemValueMcnYamlDiffItem(BaseModel):
    item_type: str

    yaml_diff: SectionVisibleItemValueMcnYamlDiffItemYamlDiff


class SectionVisibleItemValueMcnResourcePreviewItemResourcePreview(BaseModel):
    id: str

    cloud_type: Literal["AWS", "AZURE", "GOOGLE", "CLOUDFLARE"]

    detail: str

    name: str

    resource_type: Literal[
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

    title: str


class SectionVisibleItemValueMcnResourcePreviewItem(BaseModel):
    item_type: str

    resource_preview: SectionVisibleItemValueMcnResourcePreviewItemResourcePreview


class SectionVisibleItemValueMcnListItemListMcnStringItem(BaseModel):
    item_type: str

    string: str


class SectionVisibleItemValueMcnListItemListMcnResourcePreviewItemResourcePreview(BaseModel):
    id: str

    cloud_type: Literal["AWS", "AZURE", "GOOGLE", "CLOUDFLARE"]

    detail: str

    name: str

    resource_type: Literal[
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

    title: str


class SectionVisibleItemValueMcnListItemListMcnResourcePreviewItem(BaseModel):
    item_type: str

    resource_preview: SectionVisibleItemValueMcnListItemListMcnResourcePreviewItemResourcePreview


SectionVisibleItemValueMcnListItemList: TypeAlias = Annotated[
    Union[
        SectionVisibleItemValueMcnListItemListMcnStringItem,
        SectionVisibleItemValueMcnListItemListMcnResourcePreviewItem,
    ],
    PropertyInfo(discriminator="item_type"),
]


class SectionVisibleItemValueMcnListItem(BaseModel):
    item_type: str

    rule_list: List[SectionVisibleItemValueMcnListItemList] = FieldInfo(alias="list")


SectionVisibleItemValue: TypeAlias = Annotated[
    Union[
        SectionVisibleItemValueMcnStringItem,
        SectionVisibleItemValueMcnYamlItem,
        SectionVisibleItemValueMcnYamlDiffItem,
        SectionVisibleItemValueMcnResourcePreviewItem,
        SectionVisibleItemValueMcnListItem,
    ],
    PropertyInfo(discriminator="item_type"),
]


class SectionVisibleItem(BaseModel):
    help_text: Optional[str] = FieldInfo(alias="helpText", default=None)

    name: Optional[str] = None

    value: Optional[SectionVisibleItemValue] = None


class Section(BaseModel):
    hidden_items: List[SectionHiddenItem]

    name: str

    visible_items: List[SectionVisibleItem]

    help_text: Optional[str] = None


class ManagedBy(BaseModel):
    id: str

    client_type: Literal["MAGIC_WAN_CLOUD_ONRAMP"]

    name: str


class ResourceListResponse(BaseModel):
    id: str

    account_id: str

    cloud_type: Literal["AWS", "AZURE", "GOOGLE", "CLOUDFLARE"]

    config: Dict[str, object]

    deployment_provider: str

    managed: bool

    monthly_cost_estimate: MonthlyCostEstimate

    name: str

    native_id: str

    observations: Dict[str, Observations]

    provider_ids: List[str]

    provider_names_by_id: Dict[str, str]

    region: str

    resource_group: str

    resource_type: Literal[
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

    sections: List[Section]

    state: Dict[str, object]

    tags: Dict[str, str]

    updated_at: str

    url: str

    managed_by: Optional[List[ManagedBy]] = None
