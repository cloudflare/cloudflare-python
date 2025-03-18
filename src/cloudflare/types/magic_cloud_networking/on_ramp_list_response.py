# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "OnRampListResponse",
    "PlannedMonthlyCostEstimate",
    "PlannedResource",
    "PlannedResourceDiff",
    "PlannedResourceMonthlyCostEstimateDiff",
    "PlannedResourceResource",
    "PostApplyMonthlyCostEstimate",
    "PostApplyResources",
    "PostApplyResourcesMonthlyCostEstimate",
    "PostApplyResourcesObservations",
    "PostApplyResourcesSection",
    "PostApplyResourcesSectionHiddenItem",
    "PostApplyResourcesSectionHiddenItemValue",
    "PostApplyResourcesSectionHiddenItemValueMcnStringItem",
    "PostApplyResourcesSectionHiddenItemValueMcnYamlItem",
    "PostApplyResourcesSectionHiddenItemValueMcnYamlDiffItem",
    "PostApplyResourcesSectionHiddenItemValueMcnYamlDiffItemYamlDiff",
    "PostApplyResourcesSectionHiddenItemValueMcnResourcePreviewItem",
    "PostApplyResourcesSectionHiddenItemValueMcnResourcePreviewItemResourcePreview",
    "PostApplyResourcesSectionHiddenItemValueMcnListItem",
    "PostApplyResourcesSectionHiddenItemValueMcnListItemList",
    "PostApplyResourcesSectionHiddenItemValueMcnListItemListMcnStringItem",
    "PostApplyResourcesSectionHiddenItemValueMcnListItemListMcnResourcePreviewItem",
    "PostApplyResourcesSectionHiddenItemValueMcnListItemListMcnResourcePreviewItemResourcePreview",
    "PostApplyResourcesSectionVisibleItem",
    "PostApplyResourcesSectionVisibleItemValue",
    "PostApplyResourcesSectionVisibleItemValueMcnStringItem",
    "PostApplyResourcesSectionVisibleItemValueMcnYamlItem",
    "PostApplyResourcesSectionVisibleItemValueMcnYamlDiffItem",
    "PostApplyResourcesSectionVisibleItemValueMcnYamlDiffItemYamlDiff",
    "PostApplyResourcesSectionVisibleItemValueMcnResourcePreviewItem",
    "PostApplyResourcesSectionVisibleItemValueMcnResourcePreviewItemResourcePreview",
    "PostApplyResourcesSectionVisibleItemValueMcnListItem",
    "PostApplyResourcesSectionVisibleItemValueMcnListItemList",
    "PostApplyResourcesSectionVisibleItemValueMcnListItemListMcnStringItem",
    "PostApplyResourcesSectionVisibleItemValueMcnListItemListMcnResourcePreviewItem",
    "PostApplyResourcesSectionVisibleItemValueMcnListItemListMcnResourcePreviewItemResourcePreview",
    "PostApplyResourcesManagedBy",
    "Status",
    "StatusApplyProgress",
    "StatusPlanProgress",
    "StatusLifecycleErrors",
    "StatusLifecycleErrorsMeta",
    "StatusLifecycleErrorsSource",
    "VPCsByID",
    "VPCsByIDMonthlyCostEstimate",
    "VPCsByIDObservations",
    "VPCsByIDSection",
    "VPCsByIDSectionHiddenItem",
    "VPCsByIDSectionHiddenItemValue",
    "VPCsByIDSectionHiddenItemValueMcnStringItem",
    "VPCsByIDSectionHiddenItemValueMcnYamlItem",
    "VPCsByIDSectionHiddenItemValueMcnYamlDiffItem",
    "VPCsByIDSectionHiddenItemValueMcnYamlDiffItemYamlDiff",
    "VPCsByIDSectionHiddenItemValueMcnResourcePreviewItem",
    "VPCsByIDSectionHiddenItemValueMcnResourcePreviewItemResourcePreview",
    "VPCsByIDSectionHiddenItemValueMcnListItem",
    "VPCsByIDSectionHiddenItemValueMcnListItemList",
    "VPCsByIDSectionHiddenItemValueMcnListItemListMcnStringItem",
    "VPCsByIDSectionHiddenItemValueMcnListItemListMcnResourcePreviewItem",
    "VPCsByIDSectionHiddenItemValueMcnListItemListMcnResourcePreviewItemResourcePreview",
    "VPCsByIDSectionVisibleItem",
    "VPCsByIDSectionVisibleItemValue",
    "VPCsByIDSectionVisibleItemValueMcnStringItem",
    "VPCsByIDSectionVisibleItemValueMcnYamlItem",
    "VPCsByIDSectionVisibleItemValueMcnYamlDiffItem",
    "VPCsByIDSectionVisibleItemValueMcnYamlDiffItemYamlDiff",
    "VPCsByIDSectionVisibleItemValueMcnResourcePreviewItem",
    "VPCsByIDSectionVisibleItemValueMcnResourcePreviewItemResourcePreview",
    "VPCsByIDSectionVisibleItemValueMcnListItem",
    "VPCsByIDSectionVisibleItemValueMcnListItemList",
    "VPCsByIDSectionVisibleItemValueMcnListItemListMcnStringItem",
    "VPCsByIDSectionVisibleItemValueMcnListItemListMcnResourcePreviewItem",
    "VPCsByIDSectionVisibleItemValueMcnListItemListMcnResourcePreviewItemResourcePreview",
    "VPCsByIDManagedBy",
]


class PlannedMonthlyCostEstimate(BaseModel):
    currency: str

    current_monthly_cost: float

    diff: float

    proposed_monthly_cost: float


class PlannedResourceDiff(BaseModel):
    diff: str

    left_description: str

    left_yaml: str

    right_description: str

    right_yaml: str


class PlannedResourceMonthlyCostEstimateDiff(BaseModel):
    currency: str

    current_monthly_cost: float

    diff: float

    proposed_monthly_cost: float


class PlannedResourceResource(BaseModel):
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


class PlannedResource(BaseModel):
    diff: PlannedResourceDiff

    keys_require_replace: List[str]

    monthly_cost_estimate_diff: PlannedResourceMonthlyCostEstimateDiff

    planned_action: Literal["no_op", "create", "update", "replace", "destroy"]

    resource: PlannedResourceResource


class PostApplyMonthlyCostEstimate(BaseModel):
    currency: str

    monthly_cost: float


class PostApplyResourcesMonthlyCostEstimate(BaseModel):
    currency: str

    monthly_cost: float


class PostApplyResourcesObservations(BaseModel):
    first_observed_at: str

    last_observed_at: str

    provider_id: str

    resource_id: str


class PostApplyResourcesSectionHiddenItemValueMcnStringItem(BaseModel):
    item_type: str

    string: str


class PostApplyResourcesSectionHiddenItemValueMcnYamlItem(BaseModel):
    item_type: str

    yaml: str


class PostApplyResourcesSectionHiddenItemValueMcnYamlDiffItemYamlDiff(BaseModel):
    diff: str

    left_description: str

    left_yaml: str

    right_description: str

    right_yaml: str


class PostApplyResourcesSectionHiddenItemValueMcnYamlDiffItem(BaseModel):
    item_type: str

    yaml_diff: PostApplyResourcesSectionHiddenItemValueMcnYamlDiffItemYamlDiff


class PostApplyResourcesSectionHiddenItemValueMcnResourcePreviewItemResourcePreview(BaseModel):
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


class PostApplyResourcesSectionHiddenItemValueMcnResourcePreviewItem(BaseModel):
    item_type: str

    resource_preview: PostApplyResourcesSectionHiddenItemValueMcnResourcePreviewItemResourcePreview


class PostApplyResourcesSectionHiddenItemValueMcnListItemListMcnStringItem(BaseModel):
    item_type: str

    string: str


class PostApplyResourcesSectionHiddenItemValueMcnListItemListMcnResourcePreviewItemResourcePreview(BaseModel):
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


class PostApplyResourcesSectionHiddenItemValueMcnListItemListMcnResourcePreviewItem(BaseModel):
    item_type: str

    resource_preview: PostApplyResourcesSectionHiddenItemValueMcnListItemListMcnResourcePreviewItemResourcePreview


PostApplyResourcesSectionHiddenItemValueMcnListItemList: TypeAlias = Annotated[
    Union[
        PostApplyResourcesSectionHiddenItemValueMcnListItemListMcnStringItem,
        PostApplyResourcesSectionHiddenItemValueMcnListItemListMcnResourcePreviewItem,
    ],
    PropertyInfo(discriminator="item_type"),
]


class PostApplyResourcesSectionHiddenItemValueMcnListItem(BaseModel):
    item_type: str

    rule_list: List[PostApplyResourcesSectionHiddenItemValueMcnListItemList] = FieldInfo(alias="list")


PostApplyResourcesSectionHiddenItemValue: TypeAlias = Annotated[
    Union[
        PostApplyResourcesSectionHiddenItemValueMcnStringItem,
        PostApplyResourcesSectionHiddenItemValueMcnYamlItem,
        PostApplyResourcesSectionHiddenItemValueMcnYamlDiffItem,
        PostApplyResourcesSectionHiddenItemValueMcnResourcePreviewItem,
        PostApplyResourcesSectionHiddenItemValueMcnListItem,
    ],
    PropertyInfo(discriminator="item_type"),
]


class PostApplyResourcesSectionHiddenItem(BaseModel):
    help_text: Optional[str] = FieldInfo(alias="helpText", default=None)

    name: Optional[str] = None

    value: Optional[PostApplyResourcesSectionHiddenItemValue] = None


class PostApplyResourcesSectionVisibleItemValueMcnStringItem(BaseModel):
    item_type: str

    string: str


class PostApplyResourcesSectionVisibleItemValueMcnYamlItem(BaseModel):
    item_type: str

    yaml: str


class PostApplyResourcesSectionVisibleItemValueMcnYamlDiffItemYamlDiff(BaseModel):
    diff: str

    left_description: str

    left_yaml: str

    right_description: str

    right_yaml: str


class PostApplyResourcesSectionVisibleItemValueMcnYamlDiffItem(BaseModel):
    item_type: str

    yaml_diff: PostApplyResourcesSectionVisibleItemValueMcnYamlDiffItemYamlDiff


class PostApplyResourcesSectionVisibleItemValueMcnResourcePreviewItemResourcePreview(BaseModel):
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


class PostApplyResourcesSectionVisibleItemValueMcnResourcePreviewItem(BaseModel):
    item_type: str

    resource_preview: PostApplyResourcesSectionVisibleItemValueMcnResourcePreviewItemResourcePreview


class PostApplyResourcesSectionVisibleItemValueMcnListItemListMcnStringItem(BaseModel):
    item_type: str

    string: str


class PostApplyResourcesSectionVisibleItemValueMcnListItemListMcnResourcePreviewItemResourcePreview(BaseModel):
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


class PostApplyResourcesSectionVisibleItemValueMcnListItemListMcnResourcePreviewItem(BaseModel):
    item_type: str

    resource_preview: PostApplyResourcesSectionVisibleItemValueMcnListItemListMcnResourcePreviewItemResourcePreview


PostApplyResourcesSectionVisibleItemValueMcnListItemList: TypeAlias = Annotated[
    Union[
        PostApplyResourcesSectionVisibleItemValueMcnListItemListMcnStringItem,
        PostApplyResourcesSectionVisibleItemValueMcnListItemListMcnResourcePreviewItem,
    ],
    PropertyInfo(discriminator="item_type"),
]


class PostApplyResourcesSectionVisibleItemValueMcnListItem(BaseModel):
    item_type: str

    rule_list: List[PostApplyResourcesSectionVisibleItemValueMcnListItemList] = FieldInfo(alias="list")


PostApplyResourcesSectionVisibleItemValue: TypeAlias = Annotated[
    Union[
        PostApplyResourcesSectionVisibleItemValueMcnStringItem,
        PostApplyResourcesSectionVisibleItemValueMcnYamlItem,
        PostApplyResourcesSectionVisibleItemValueMcnYamlDiffItem,
        PostApplyResourcesSectionVisibleItemValueMcnResourcePreviewItem,
        PostApplyResourcesSectionVisibleItemValueMcnListItem,
    ],
    PropertyInfo(discriminator="item_type"),
]


class PostApplyResourcesSectionVisibleItem(BaseModel):
    help_text: Optional[str] = FieldInfo(alias="helpText", default=None)

    name: Optional[str] = None

    value: Optional[PostApplyResourcesSectionVisibleItemValue] = None


class PostApplyResourcesSection(BaseModel):
    hidden_items: List[PostApplyResourcesSectionHiddenItem]

    name: str

    visible_items: List[PostApplyResourcesSectionVisibleItem]

    help_text: Optional[str] = None


class PostApplyResourcesManagedBy(BaseModel):
    id: str

    client_type: Literal["MAGIC_WAN_CLOUD_ONRAMP"]

    name: str


class PostApplyResources(BaseModel):
    id: str

    account_id: str

    cloud_type: Literal["AWS", "AZURE", "GOOGLE", "CLOUDFLARE"]

    config: Dict[str, object]

    deployment_provider: str

    managed: bool

    monthly_cost_estimate: PostApplyResourcesMonthlyCostEstimate

    name: str

    native_id: str

    observations: Dict[str, PostApplyResourcesObservations]

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

    sections: List[PostApplyResourcesSection]

    state: Dict[str, object]

    tags: Dict[str, str]

    updated_at: str

    url: str

    managed_by: Optional[List[PostApplyResourcesManagedBy]] = None


class StatusApplyProgress(BaseModel):
    done: int

    total: int


class StatusPlanProgress(BaseModel):
    done: int

    total: int


class StatusLifecycleErrorsMeta(BaseModel):
    l10n_key: Optional[str] = None

    loggable_error: Optional[str] = None

    template_data: Optional[object] = None

    trace_id: Optional[str] = None


class StatusLifecycleErrorsSource(BaseModel):
    parameter: Optional[str] = None

    parameter_value_index: Optional[int] = None

    pointer: Optional[str] = None


class StatusLifecycleErrors(BaseModel):
    code: Literal[
        1001,
        1002,
        1003,
        1004,
        1005,
        1006,
        1007,
        1008,
        1009,
        1010,
        1011,
        1012,
        1013,
        1014,
        1015,
        1016,
        1017,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        3001,
        3002,
        3003,
        3004,
        3005,
        3006,
        3007,
        4001,
        4002,
        4003,
        4004,
        4005,
        4006,
        4007,
        4008,
        4009,
        4010,
        4011,
        4012,
        4013,
        4014,
        4015,
        4016,
        4017,
        4018,
        4019,
        4020,
        4021,
        4022,
        4023,
        5001,
        5002,
        5003,
        5004,
        102000,
        102001,
        102002,
        102003,
        102004,
        102005,
        102006,
        102007,
        102008,
        102009,
        102010,
        102011,
        102012,
        102013,
        102014,
        102015,
        102016,
        102017,
        102018,
        102019,
        102020,
        102021,
        102022,
        102023,
        102024,
        102025,
        102026,
        102027,
        102028,
        102029,
        102030,
        102031,
        102032,
        102033,
        102034,
        102035,
        102036,
        102037,
        102038,
        102039,
        102040,
        102041,
        102042,
        102043,
        102044,
        102045,
        102046,
        102047,
        102048,
        102049,
        102050,
        102051,
        102052,
        102053,
        102054,
        102055,
        102056,
        102057,
        102058,
        102059,
        102060,
        102061,
        102062,
        102063,
        102064,
        102065,
        102066,
        103001,
        103002,
        103003,
        103004,
        103005,
        103006,
        103007,
        103008,
    ]

    message: str

    documentation_url: Optional[str] = None

    meta: Optional[StatusLifecycleErrorsMeta] = None

    source: Optional[StatusLifecycleErrorsSource] = None


class Status(BaseModel):
    apply_progress: StatusApplyProgress

    lifecycle_state: Literal[
        "OnrampNeedsApply",
        "OnrampPendingPlan",
        "OnrampPlanning",
        "OnrampPlanFailed",
        "OnrampPendingApproval",
        "OnrampPendingApply",
        "OnrampApplying",
        "OnrampApplyFailed",
        "OnrampActive",
        "OnrampPendingDestroy",
        "OnrampDestroying",
        "OnrampDestroyFailed",
    ]

    plan_progress: StatusPlanProgress

    routes: List[str]

    tunnels: List[str]

    lifecycle_errors: Optional[Dict[str, StatusLifecycleErrors]] = None


class VPCsByIDMonthlyCostEstimate(BaseModel):
    currency: str

    monthly_cost: float


class VPCsByIDObservations(BaseModel):
    first_observed_at: str

    last_observed_at: str

    provider_id: str

    resource_id: str


class VPCsByIDSectionHiddenItemValueMcnStringItem(BaseModel):
    item_type: str

    string: str


class VPCsByIDSectionHiddenItemValueMcnYamlItem(BaseModel):
    item_type: str

    yaml: str


class VPCsByIDSectionHiddenItemValueMcnYamlDiffItemYamlDiff(BaseModel):
    diff: str

    left_description: str

    left_yaml: str

    right_description: str

    right_yaml: str


class VPCsByIDSectionHiddenItemValueMcnYamlDiffItem(BaseModel):
    item_type: str

    yaml_diff: VPCsByIDSectionHiddenItemValueMcnYamlDiffItemYamlDiff


class VPCsByIDSectionHiddenItemValueMcnResourcePreviewItemResourcePreview(BaseModel):
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


class VPCsByIDSectionHiddenItemValueMcnResourcePreviewItem(BaseModel):
    item_type: str

    resource_preview: VPCsByIDSectionHiddenItemValueMcnResourcePreviewItemResourcePreview


class VPCsByIDSectionHiddenItemValueMcnListItemListMcnStringItem(BaseModel):
    item_type: str

    string: str


class VPCsByIDSectionHiddenItemValueMcnListItemListMcnResourcePreviewItemResourcePreview(BaseModel):
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


class VPCsByIDSectionHiddenItemValueMcnListItemListMcnResourcePreviewItem(BaseModel):
    item_type: str

    resource_preview: VPCsByIDSectionHiddenItemValueMcnListItemListMcnResourcePreviewItemResourcePreview


VPCsByIDSectionHiddenItemValueMcnListItemList: TypeAlias = Annotated[
    Union[
        VPCsByIDSectionHiddenItemValueMcnListItemListMcnStringItem,
        VPCsByIDSectionHiddenItemValueMcnListItemListMcnResourcePreviewItem,
    ],
    PropertyInfo(discriminator="item_type"),
]


class VPCsByIDSectionHiddenItemValueMcnListItem(BaseModel):
    item_type: str

    rule_list: List[VPCsByIDSectionHiddenItemValueMcnListItemList] = FieldInfo(alias="list")


VPCsByIDSectionHiddenItemValue: TypeAlias = Annotated[
    Union[
        VPCsByIDSectionHiddenItemValueMcnStringItem,
        VPCsByIDSectionHiddenItemValueMcnYamlItem,
        VPCsByIDSectionHiddenItemValueMcnYamlDiffItem,
        VPCsByIDSectionHiddenItemValueMcnResourcePreviewItem,
        VPCsByIDSectionHiddenItemValueMcnListItem,
    ],
    PropertyInfo(discriminator="item_type"),
]


class VPCsByIDSectionHiddenItem(BaseModel):
    help_text: Optional[str] = FieldInfo(alias="helpText", default=None)

    name: Optional[str] = None

    value: Optional[VPCsByIDSectionHiddenItemValue] = None


class VPCsByIDSectionVisibleItemValueMcnStringItem(BaseModel):
    item_type: str

    string: str


class VPCsByIDSectionVisibleItemValueMcnYamlItem(BaseModel):
    item_type: str

    yaml: str


class VPCsByIDSectionVisibleItemValueMcnYamlDiffItemYamlDiff(BaseModel):
    diff: str

    left_description: str

    left_yaml: str

    right_description: str

    right_yaml: str


class VPCsByIDSectionVisibleItemValueMcnYamlDiffItem(BaseModel):
    item_type: str

    yaml_diff: VPCsByIDSectionVisibleItemValueMcnYamlDiffItemYamlDiff


class VPCsByIDSectionVisibleItemValueMcnResourcePreviewItemResourcePreview(BaseModel):
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


class VPCsByIDSectionVisibleItemValueMcnResourcePreviewItem(BaseModel):
    item_type: str

    resource_preview: VPCsByIDSectionVisibleItemValueMcnResourcePreviewItemResourcePreview


class VPCsByIDSectionVisibleItemValueMcnListItemListMcnStringItem(BaseModel):
    item_type: str

    string: str


class VPCsByIDSectionVisibleItemValueMcnListItemListMcnResourcePreviewItemResourcePreview(BaseModel):
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


class VPCsByIDSectionVisibleItemValueMcnListItemListMcnResourcePreviewItem(BaseModel):
    item_type: str

    resource_preview: VPCsByIDSectionVisibleItemValueMcnListItemListMcnResourcePreviewItemResourcePreview


VPCsByIDSectionVisibleItemValueMcnListItemList: TypeAlias = Annotated[
    Union[
        VPCsByIDSectionVisibleItemValueMcnListItemListMcnStringItem,
        VPCsByIDSectionVisibleItemValueMcnListItemListMcnResourcePreviewItem,
    ],
    PropertyInfo(discriminator="item_type"),
]


class VPCsByIDSectionVisibleItemValueMcnListItem(BaseModel):
    item_type: str

    rule_list: List[VPCsByIDSectionVisibleItemValueMcnListItemList] = FieldInfo(alias="list")


VPCsByIDSectionVisibleItemValue: TypeAlias = Annotated[
    Union[
        VPCsByIDSectionVisibleItemValueMcnStringItem,
        VPCsByIDSectionVisibleItemValueMcnYamlItem,
        VPCsByIDSectionVisibleItemValueMcnYamlDiffItem,
        VPCsByIDSectionVisibleItemValueMcnResourcePreviewItem,
        VPCsByIDSectionVisibleItemValueMcnListItem,
    ],
    PropertyInfo(discriminator="item_type"),
]


class VPCsByIDSectionVisibleItem(BaseModel):
    help_text: Optional[str] = FieldInfo(alias="helpText", default=None)

    name: Optional[str] = None

    value: Optional[VPCsByIDSectionVisibleItemValue] = None


class VPCsByIDSection(BaseModel):
    hidden_items: List[VPCsByIDSectionHiddenItem]

    name: str

    visible_items: List[VPCsByIDSectionVisibleItem]

    help_text: Optional[str] = None


class VPCsByIDManagedBy(BaseModel):
    id: str

    client_type: Literal["MAGIC_WAN_CLOUD_ONRAMP"]

    name: str


class VPCsByID(BaseModel):
    id: str

    account_id: str

    cloud_type: Literal["AWS", "AZURE", "GOOGLE", "CLOUDFLARE"]

    config: Dict[str, object]

    deployment_provider: str

    managed: bool

    monthly_cost_estimate: VPCsByIDMonthlyCostEstimate

    name: str

    native_id: str

    observations: Dict[str, VPCsByIDObservations]

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

    sections: List[VPCsByIDSection]

    state: Dict[str, object]

    tags: Dict[str, str]

    updated_at: str

    url: str

    managed_by: Optional[List[VPCsByIDManagedBy]] = None


class OnRampListResponse(BaseModel):
    id: str

    cloud_type: Literal["AWS", "AZURE", "GOOGLE"]

    install_routes_in_cloud: bool

    install_routes_in_magic_wan: bool

    name: str

    type: Literal["OnrampTypeSingle", "OnrampTypeHub"]

    updated_at: str

    attached_hubs: Optional[List[str]] = None

    attached_vpcs: Optional[List[str]] = None

    description: Optional[str] = None

    hub: Optional[str] = None

    last_applied_at: Optional[str] = None

    last_exported_at: Optional[str] = None

    last_planned_at: Optional[str] = None

    manage_hub_to_hub_attachments: Optional[bool] = None

    manage_vpc_to_hub_attachments: Optional[bool] = None

    planned_monthly_cost_estimate: Optional[PlannedMonthlyCostEstimate] = None

    planned_resources: Optional[List[PlannedResource]] = None

    planned_resources_unavailable: Optional[bool] = None

    post_apply_monthly_cost_estimate: Optional[PostApplyMonthlyCostEstimate] = None

    post_apply_resources: Optional[Dict[str, PostApplyResources]] = None

    post_apply_resources_unavailable: Optional[bool] = None

    region: Optional[str] = None

    status: Optional[Status] = None

    vpc: Optional[str] = None

    vpcs_by_id: Optional[Dict[str, VPCsByID]] = None

    vpcs_by_id_unavailable: Optional[List[str]] = None
    """The list of vpc IDs for which resource details could not be generated."""
