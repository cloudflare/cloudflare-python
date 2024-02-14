# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.alerting.v3s import (
    PolicyUpdateResponse,
    PolicyDeleteResponse,
    PolicyGetResponse,
    PolicyNotificationPoliciesCreateANotificationPolicyResponse,
    PolicyNotificationPoliciesListNotificationPoliciesResponse,
    policy_update_params,
    policy_notification_policies_create_a_notification_policy_params,
)

from typing import Type, Dict, Iterable, Optional

from typing_extensions import Literal

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
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.alerting.v3s import policy_update_params
from ....types.alerting.v3s import policy_notification_policies_create_a_notification_policy_params
from ...._wrappers import ResultWrapper
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

__all__ = ["Policies", "AsyncPolicies"]


class Policies(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoliciesWithRawResponse:
        return PoliciesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesWithStreamingResponse:
        return PoliciesWithStreamingResponse(self)

    def update(
        self,
        policy_id: str,
        *,
        account_id: str,
        alert_type: Literal[
            "access_custom_certificate_expiration_type",
            "advanced_ddos_attack_l4_alert",
            "advanced_ddos_attack_l7_alert",
            "advanced_http_alert_error",
            "bgp_hijack_notification",
            "billing_usage_alert",
            "block_notification_block_removed",
            "block_notification_new_block",
            "block_notification_review_rejected",
            "brand_protection_alert",
            "brand_protection_digest",
            "clickhouse_alert_fw_anomaly",
            "clickhouse_alert_fw_ent_anomaly",
            "custom_ssl_certificate_event_type",
            "dedicated_ssl_certificate_event_type",
            "dos_attack_l4",
            "dos_attack_l7",
            "expiring_service_token_alert",
            "failing_logpush_job_disabled_alert",
            "fbm_auto_advertisement",
            "fbm_dosd_attack",
            "fbm_volumetric_attack",
            "health_check_status_notification",
            "hostname_aop_custom_certificate_expiration_type",
            "http_alert_edge_error",
            "http_alert_origin_error",
            "incident_alert",
            "load_balancing_health_alert",
            "load_balancing_pool_enablement_alert",
            "logo_match_alert",
            "magic_tunnel_health_check_event",
            "maintenance_event_notification",
            "mtls_certificate_store_certificate_expiration_type",
            "pages_event_alert",
            "radar_notification",
            "real_origin_monitoring",
            "scriptmonitor_alert_new_code_change_detections",
            "scriptmonitor_alert_new_hosts",
            "scriptmonitor_alert_new_malicious_hosts",
            "scriptmonitor_alert_new_malicious_scripts",
            "scriptmonitor_alert_new_malicious_url",
            "scriptmonitor_alert_new_max_length_resource_url",
            "scriptmonitor_alert_new_resources",
            "secondary_dns_all_primaries_failing",
            "secondary_dns_primaries_failing",
            "secondary_dns_zone_successfully_updated",
            "secondary_dns_zone_validation_warning",
            "sentinel_alert",
            "stream_live_notifications",
            "tunnel_health_event",
            "tunnel_update_event",
            "universal_ssl_event_type",
            "web_analytics_metrics_update",
            "zone_aop_custom_certificate_expiration_type",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        filters: policy_update_params.Filters | NotGiven = NOT_GIVEN,
        mechanisms: Dict[str, Iterable[policy_update_params.Mechanisms]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyUpdateResponse:
        """
        Update a Notification policy.

        Args:
          account_id: The account id

          policy_id: The unique identifier of a notification policy

          alert_type: Refers to which event will trigger a Notification dispatch. You can use the
              endpoint to get available alert types which then will give you a list of
              possible values.

          description: Optional description for the Notification policy.

          enabled: Whether or not the Notification policy is enabled.

          filters: Optional filters that allow you to be alerted only on a subset of events for
              that alert type based on some criteria. This is only available for select alert
              types. See alert type documentation for more details.

          mechanisms: List of IDs that will be used when dispatching a notification. IDs for email
              type will be the email address.

          name: Name of the policy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._put(
            f"/accounts/{account_id}/alerting/v3/policies/{policy_id}",
            body=maybe_transform(
                {
                    "alert_type": alert_type,
                    "description": description,
                    "enabled": enabled,
                    "filters": filters,
                    "mechanisms": mechanisms,
                    "name": name,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PolicyUpdateResponse], ResultWrapper[PolicyUpdateResponse]),
        )

    def delete(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyDeleteResponse]:
        """
        Delete a Notification policy.

        Args:
          account_id: The account id

          policy_id: The unique identifier of a notification policy

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return cast(
            Optional[PolicyDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/alerting/v3/policies/{policy_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PolicyDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyGetResponse:
        """
        Get details for a single policy.

        Args:
          account_id: The account id

          policy_id: The unique identifier of a notification policy

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get(
            f"/accounts/{account_id}/alerting/v3/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PolicyGetResponse], ResultWrapper[PolicyGetResponse]),
        )

    def notification_policies_create_a_notification_policy(
        self,
        account_id: str,
        *,
        alert_type: Literal[
            "access_custom_certificate_expiration_type",
            "advanced_ddos_attack_l4_alert",
            "advanced_ddos_attack_l7_alert",
            "advanced_http_alert_error",
            "bgp_hijack_notification",
            "billing_usage_alert",
            "block_notification_block_removed",
            "block_notification_new_block",
            "block_notification_review_rejected",
            "brand_protection_alert",
            "brand_protection_digest",
            "clickhouse_alert_fw_anomaly",
            "clickhouse_alert_fw_ent_anomaly",
            "custom_ssl_certificate_event_type",
            "dedicated_ssl_certificate_event_type",
            "dos_attack_l4",
            "dos_attack_l7",
            "expiring_service_token_alert",
            "failing_logpush_job_disabled_alert",
            "fbm_auto_advertisement",
            "fbm_dosd_attack",
            "fbm_volumetric_attack",
            "health_check_status_notification",
            "hostname_aop_custom_certificate_expiration_type",
            "http_alert_edge_error",
            "http_alert_origin_error",
            "incident_alert",
            "load_balancing_health_alert",
            "load_balancing_pool_enablement_alert",
            "logo_match_alert",
            "magic_tunnel_health_check_event",
            "maintenance_event_notification",
            "mtls_certificate_store_certificate_expiration_type",
            "pages_event_alert",
            "radar_notification",
            "real_origin_monitoring",
            "scriptmonitor_alert_new_code_change_detections",
            "scriptmonitor_alert_new_hosts",
            "scriptmonitor_alert_new_malicious_hosts",
            "scriptmonitor_alert_new_malicious_scripts",
            "scriptmonitor_alert_new_malicious_url",
            "scriptmonitor_alert_new_max_length_resource_url",
            "scriptmonitor_alert_new_resources",
            "secondary_dns_all_primaries_failing",
            "secondary_dns_primaries_failing",
            "secondary_dns_zone_successfully_updated",
            "secondary_dns_zone_validation_warning",
            "sentinel_alert",
            "stream_live_notifications",
            "tunnel_health_event",
            "tunnel_update_event",
            "universal_ssl_event_type",
            "web_analytics_metrics_update",
            "zone_aop_custom_certificate_expiration_type",
        ],
        enabled: bool,
        mechanisms: Dict[str, Iterable[policy_notification_policies_create_a_notification_policy_params.Mechanisms]],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        filters: policy_notification_policies_create_a_notification_policy_params.Filters | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyNotificationPoliciesCreateANotificationPolicyResponse:
        """
        Creates a new Notification policy.

        Args:
          account_id: The account id

          alert_type: Refers to which event will trigger a Notification dispatch. You can use the
              endpoint to get available alert types which then will give you a list of
              possible values.

          enabled: Whether or not the Notification policy is enabled.

          mechanisms: List of IDs that will be used when dispatching a notification. IDs for email
              type will be the email address.

          name: Name of the policy.

          description: Optional description for the Notification policy.

          filters: Optional filters that allow you to be alerted only on a subset of events for
              that alert type based on some criteria. This is only available for select alert
              types. See alert type documentation for more details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/alerting/v3/policies",
            body=maybe_transform(
                {
                    "alert_type": alert_type,
                    "enabled": enabled,
                    "mechanisms": mechanisms,
                    "name": name,
                    "description": description,
                    "filters": filters,
                },
                policy_notification_policies_create_a_notification_policy_params.PolicyNotificationPoliciesCreateANotificationPolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PolicyNotificationPoliciesCreateANotificationPolicyResponse],
                ResultWrapper[PolicyNotificationPoliciesCreateANotificationPolicyResponse],
            ),
        )

    def notification_policies_list_notification_policies(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyNotificationPoliciesListNotificationPoliciesResponse]:
        """
        Get a list of all Notification policies.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/alerting/v3/policies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PolicyNotificationPoliciesListNotificationPoliciesResponse]],
                ResultWrapper[PolicyNotificationPoliciesListNotificationPoliciesResponse],
            ),
        )


class AsyncPolicies(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoliciesWithRawResponse:
        return AsyncPoliciesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesWithStreamingResponse:
        return AsyncPoliciesWithStreamingResponse(self)

    async def update(
        self,
        policy_id: str,
        *,
        account_id: str,
        alert_type: Literal[
            "access_custom_certificate_expiration_type",
            "advanced_ddos_attack_l4_alert",
            "advanced_ddos_attack_l7_alert",
            "advanced_http_alert_error",
            "bgp_hijack_notification",
            "billing_usage_alert",
            "block_notification_block_removed",
            "block_notification_new_block",
            "block_notification_review_rejected",
            "brand_protection_alert",
            "brand_protection_digest",
            "clickhouse_alert_fw_anomaly",
            "clickhouse_alert_fw_ent_anomaly",
            "custom_ssl_certificate_event_type",
            "dedicated_ssl_certificate_event_type",
            "dos_attack_l4",
            "dos_attack_l7",
            "expiring_service_token_alert",
            "failing_logpush_job_disabled_alert",
            "fbm_auto_advertisement",
            "fbm_dosd_attack",
            "fbm_volumetric_attack",
            "health_check_status_notification",
            "hostname_aop_custom_certificate_expiration_type",
            "http_alert_edge_error",
            "http_alert_origin_error",
            "incident_alert",
            "load_balancing_health_alert",
            "load_balancing_pool_enablement_alert",
            "logo_match_alert",
            "magic_tunnel_health_check_event",
            "maintenance_event_notification",
            "mtls_certificate_store_certificate_expiration_type",
            "pages_event_alert",
            "radar_notification",
            "real_origin_monitoring",
            "scriptmonitor_alert_new_code_change_detections",
            "scriptmonitor_alert_new_hosts",
            "scriptmonitor_alert_new_malicious_hosts",
            "scriptmonitor_alert_new_malicious_scripts",
            "scriptmonitor_alert_new_malicious_url",
            "scriptmonitor_alert_new_max_length_resource_url",
            "scriptmonitor_alert_new_resources",
            "secondary_dns_all_primaries_failing",
            "secondary_dns_primaries_failing",
            "secondary_dns_zone_successfully_updated",
            "secondary_dns_zone_validation_warning",
            "sentinel_alert",
            "stream_live_notifications",
            "tunnel_health_event",
            "tunnel_update_event",
            "universal_ssl_event_type",
            "web_analytics_metrics_update",
            "zone_aop_custom_certificate_expiration_type",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        filters: policy_update_params.Filters | NotGiven = NOT_GIVEN,
        mechanisms: Dict[str, Iterable[policy_update_params.Mechanisms]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyUpdateResponse:
        """
        Update a Notification policy.

        Args:
          account_id: The account id

          policy_id: The unique identifier of a notification policy

          alert_type: Refers to which event will trigger a Notification dispatch. You can use the
              endpoint to get available alert types which then will give you a list of
              possible values.

          description: Optional description for the Notification policy.

          enabled: Whether or not the Notification policy is enabled.

          filters: Optional filters that allow you to be alerted only on a subset of events for
              that alert type based on some criteria. This is only available for select alert
              types. See alert type documentation for more details.

          mechanisms: List of IDs that will be used when dispatching a notification. IDs for email
              type will be the email address.

          name: Name of the policy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._put(
            f"/accounts/{account_id}/alerting/v3/policies/{policy_id}",
            body=maybe_transform(
                {
                    "alert_type": alert_type,
                    "description": description,
                    "enabled": enabled,
                    "filters": filters,
                    "mechanisms": mechanisms,
                    "name": name,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PolicyUpdateResponse], ResultWrapper[PolicyUpdateResponse]),
        )

    async def delete(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyDeleteResponse]:
        """
        Delete a Notification policy.

        Args:
          account_id: The account id

          policy_id: The unique identifier of a notification policy

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return cast(
            Optional[PolicyDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/alerting/v3/policies/{policy_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PolicyDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyGetResponse:
        """
        Get details for a single policy.

        Args:
          account_id: The account id

          policy_id: The unique identifier of a notification policy

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._get(
            f"/accounts/{account_id}/alerting/v3/policies/{policy_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PolicyGetResponse], ResultWrapper[PolicyGetResponse]),
        )

    async def notification_policies_create_a_notification_policy(
        self,
        account_id: str,
        *,
        alert_type: Literal[
            "access_custom_certificate_expiration_type",
            "advanced_ddos_attack_l4_alert",
            "advanced_ddos_attack_l7_alert",
            "advanced_http_alert_error",
            "bgp_hijack_notification",
            "billing_usage_alert",
            "block_notification_block_removed",
            "block_notification_new_block",
            "block_notification_review_rejected",
            "brand_protection_alert",
            "brand_protection_digest",
            "clickhouse_alert_fw_anomaly",
            "clickhouse_alert_fw_ent_anomaly",
            "custom_ssl_certificate_event_type",
            "dedicated_ssl_certificate_event_type",
            "dos_attack_l4",
            "dos_attack_l7",
            "expiring_service_token_alert",
            "failing_logpush_job_disabled_alert",
            "fbm_auto_advertisement",
            "fbm_dosd_attack",
            "fbm_volumetric_attack",
            "health_check_status_notification",
            "hostname_aop_custom_certificate_expiration_type",
            "http_alert_edge_error",
            "http_alert_origin_error",
            "incident_alert",
            "load_balancing_health_alert",
            "load_balancing_pool_enablement_alert",
            "logo_match_alert",
            "magic_tunnel_health_check_event",
            "maintenance_event_notification",
            "mtls_certificate_store_certificate_expiration_type",
            "pages_event_alert",
            "radar_notification",
            "real_origin_monitoring",
            "scriptmonitor_alert_new_code_change_detections",
            "scriptmonitor_alert_new_hosts",
            "scriptmonitor_alert_new_malicious_hosts",
            "scriptmonitor_alert_new_malicious_scripts",
            "scriptmonitor_alert_new_malicious_url",
            "scriptmonitor_alert_new_max_length_resource_url",
            "scriptmonitor_alert_new_resources",
            "secondary_dns_all_primaries_failing",
            "secondary_dns_primaries_failing",
            "secondary_dns_zone_successfully_updated",
            "secondary_dns_zone_validation_warning",
            "sentinel_alert",
            "stream_live_notifications",
            "tunnel_health_event",
            "tunnel_update_event",
            "universal_ssl_event_type",
            "web_analytics_metrics_update",
            "zone_aop_custom_certificate_expiration_type",
        ],
        enabled: bool,
        mechanisms: Dict[str, Iterable[policy_notification_policies_create_a_notification_policy_params.Mechanisms]],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        filters: policy_notification_policies_create_a_notification_policy_params.Filters | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PolicyNotificationPoliciesCreateANotificationPolicyResponse:
        """
        Creates a new Notification policy.

        Args:
          account_id: The account id

          alert_type: Refers to which event will trigger a Notification dispatch. You can use the
              endpoint to get available alert types which then will give you a list of
              possible values.

          enabled: Whether or not the Notification policy is enabled.

          mechanisms: List of IDs that will be used when dispatching a notification. IDs for email
              type will be the email address.

          name: Name of the policy.

          description: Optional description for the Notification policy.

          filters: Optional filters that allow you to be alerted only on a subset of events for
              that alert type based on some criteria. This is only available for select alert
              types. See alert type documentation for more details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/alerting/v3/policies",
            body=maybe_transform(
                {
                    "alert_type": alert_type,
                    "enabled": enabled,
                    "mechanisms": mechanisms,
                    "name": name,
                    "description": description,
                    "filters": filters,
                },
                policy_notification_policies_create_a_notification_policy_params.PolicyNotificationPoliciesCreateANotificationPolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PolicyNotificationPoliciesCreateANotificationPolicyResponse],
                ResultWrapper[PolicyNotificationPoliciesCreateANotificationPolicyResponse],
            ),
        )

    async def notification_policies_list_notification_policies(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyNotificationPoliciesListNotificationPoliciesResponse]:
        """
        Get a list of all Notification policies.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/alerting/v3/policies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PolicyNotificationPoliciesListNotificationPoliciesResponse]],
                ResultWrapper[PolicyNotificationPoliciesListNotificationPoliciesResponse],
            ),
        )


class PoliciesWithRawResponse:
    def __init__(self, policies: Policies) -> None:
        self._policies = policies

        self.update = to_raw_response_wrapper(
            policies.update,
        )
        self.delete = to_raw_response_wrapper(
            policies.delete,
        )
        self.get = to_raw_response_wrapper(
            policies.get,
        )
        self.notification_policies_create_a_notification_policy = to_raw_response_wrapper(
            policies.notification_policies_create_a_notification_policy,
        )
        self.notification_policies_list_notification_policies = to_raw_response_wrapper(
            policies.notification_policies_list_notification_policies,
        )


class AsyncPoliciesWithRawResponse:
    def __init__(self, policies: AsyncPolicies) -> None:
        self._policies = policies

        self.update = async_to_raw_response_wrapper(
            policies.update,
        )
        self.delete = async_to_raw_response_wrapper(
            policies.delete,
        )
        self.get = async_to_raw_response_wrapper(
            policies.get,
        )
        self.notification_policies_create_a_notification_policy = async_to_raw_response_wrapper(
            policies.notification_policies_create_a_notification_policy,
        )
        self.notification_policies_list_notification_policies = async_to_raw_response_wrapper(
            policies.notification_policies_list_notification_policies,
        )


class PoliciesWithStreamingResponse:
    def __init__(self, policies: Policies) -> None:
        self._policies = policies

        self.update = to_streamed_response_wrapper(
            policies.update,
        )
        self.delete = to_streamed_response_wrapper(
            policies.delete,
        )
        self.get = to_streamed_response_wrapper(
            policies.get,
        )
        self.notification_policies_create_a_notification_policy = to_streamed_response_wrapper(
            policies.notification_policies_create_a_notification_policy,
        )
        self.notification_policies_list_notification_policies = to_streamed_response_wrapper(
            policies.notification_policies_list_notification_policies,
        )


class AsyncPoliciesWithStreamingResponse:
    def __init__(self, policies: AsyncPolicies) -> None:
        self._policies = policies

        self.update = async_to_streamed_response_wrapper(
            policies.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            policies.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            policies.get,
        )
        self.notification_policies_create_a_notification_policy = async_to_streamed_response_wrapper(
            policies.notification_policies_create_a_notification_policy,
        )
        self.notification_policies_list_notification_policies = async_to_streamed_response_wrapper(
            policies.notification_policies_list_notification_policies,
        )
