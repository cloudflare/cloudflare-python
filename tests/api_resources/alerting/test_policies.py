# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.alerting import (
    Policy,
    PolicyCreateResponse,
    PolicyDeleteResponse,
    PolicyUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        policy = client.alerting.policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            alert_type="access_custom_certificate_expiration_type",
            enabled=True,
            mechanisms={},
            name="SSL Notification Event Policy",
        )
        assert_matches_type(Optional[PolicyCreateResponse], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        policy = client.alerting.policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            alert_type="access_custom_certificate_expiration_type",
            enabled=True,
            mechanisms={
                "email": [{"id": "test@example.com"}],
                "pagerduty": [{}],
                "webhooks": [{}],
            },
            name="SSL Notification Event Policy",
            alert_interval="30m",
            description="Something describing the policy.",
            filters={
                "actions": ["string"],
                "affected_asns": ["string"],
                "affected_components": ["string"],
                "affected_locations": ["string"],
                "airport_code": ["string"],
                "alert_trigger_preferences": ["string"],
                "alert_trigger_preferences_value": ["string"],
                "enabled": ["string"],
                "environment": ["string"],
                "event": ["string"],
                "event_source": ["string"],
                "event_type": ["string"],
                "group_by": ["string"],
                "health_check_id": ["string"],
                "incident_impact": ["INCIDENT_IMPACT_NONE"],
                "input_id": ["string"],
                "insight_class": ["string"],
                "limit": ["string"],
                "logo_tag": ["string"],
                "megabits_per_second": ["string"],
                "new_health": ["string"],
                "new_status": ["string"],
                "packets_per_second": ["string"],
                "pool_id": ["string"],
                "pop_names": ["string"],
                "product": ["string"],
                "project_id": ["string"],
                "protocol": ["string"],
                "query_tag": ["string"],
                "requests_per_second": ["string"],
                "selectors": ["string"],
                "services": ["string"],
                "slo": ["99.9"],
                "status": ["string"],
                "target_hostname": ["string"],
                "target_ip": ["string"],
                "target_zone_name": ["string"],
                "traffic_exclusions": ["security_events"],
                "tunnel_id": ["string"],
                "tunnel_name": ["string"],
                "where": ["string"],
                "zones": ["string"],
            },
        )
        assert_matches_type(Optional[PolicyCreateResponse], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.alerting.policies.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            alert_type="access_custom_certificate_expiration_type",
            enabled=True,
            mechanisms={},
            name="SSL Notification Event Policy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Optional[PolicyCreateResponse], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.alerting.policies.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            alert_type="access_custom_certificate_expiration_type",
            enabled=True,
            mechanisms={},
            name="SSL Notification Event Policy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Optional[PolicyCreateResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.policies.with_raw_response.create(
                account_id="",
                alert_type="access_custom_certificate_expiration_type",
                enabled=True,
                mechanisms={},
                name="SSL Notification Event Policy",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        policy = client.alerting.policies.update(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        policy = client.alerting.policies.update(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            alert_interval="30m",
            alert_type="access_custom_certificate_expiration_type",
            description="Something describing the policy.",
            enabled=True,
            filters={
                "actions": ["string"],
                "affected_asns": ["string"],
                "affected_components": ["string"],
                "affected_locations": ["string"],
                "airport_code": ["string"],
                "alert_trigger_preferences": ["string"],
                "alert_trigger_preferences_value": ["string"],
                "enabled": ["string"],
                "environment": ["string"],
                "event": ["string"],
                "event_source": ["string"],
                "event_type": ["string"],
                "group_by": ["string"],
                "health_check_id": ["string"],
                "incident_impact": ["INCIDENT_IMPACT_NONE"],
                "input_id": ["string"],
                "insight_class": ["string"],
                "limit": ["string"],
                "logo_tag": ["string"],
                "megabits_per_second": ["string"],
                "new_health": ["string"],
                "new_status": ["string"],
                "packets_per_second": ["string"],
                "pool_id": ["string"],
                "pop_names": ["string"],
                "product": ["string"],
                "project_id": ["string"],
                "protocol": ["string"],
                "query_tag": ["string"],
                "requests_per_second": ["string"],
                "selectors": ["string"],
                "services": ["string"],
                "slo": ["99.9"],
                "status": ["string"],
                "target_hostname": ["string"],
                "target_ip": ["string"],
                "target_zone_name": ["string"],
                "traffic_exclusions": ["security_events"],
                "tunnel_id": ["string"],
                "tunnel_name": ["string"],
                "where": ["string"],
                "zones": ["string"],
            },
            mechanisms={
                "email": [{"id": "test@example.com"}],
                "pagerduty": [{}],
                "webhooks": [{}],
            },
            name="SSL Notification Event Policy",
        )
        assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.alerting.policies.with_raw_response.update(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.alerting.policies.with_streaming_response.update(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.policies.with_raw_response.update(
                policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.alerting.policies.with_raw_response.update(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        policy = client.alerting.policies.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Policy], policy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.alerting.policies.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(SyncSinglePage[Policy], policy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.alerting.policies.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(SyncSinglePage[Policy], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.policies.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        policy = client.alerting.policies.delete(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.alerting.policies.with_raw_response.delete(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.alerting.policies.with_streaming_response.delete(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.policies.with_raw_response.delete(
                policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.alerting.policies.with_raw_response.delete(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        policy = client.alerting.policies.get(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Policy], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.alerting.policies.with_raw_response.get(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Optional[Policy], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.alerting.policies.with_streaming_response.get(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Optional[Policy], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.policies.with_raw_response.get(
                policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.alerting.policies.with_raw_response.get(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.alerting.policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            alert_type="access_custom_certificate_expiration_type",
            enabled=True,
            mechanisms={},
            name="SSL Notification Event Policy",
        )
        assert_matches_type(Optional[PolicyCreateResponse], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.alerting.policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            alert_type="access_custom_certificate_expiration_type",
            enabled=True,
            mechanisms={
                "email": [{"id": "test@example.com"}],
                "pagerduty": [{}],
                "webhooks": [{}],
            },
            name="SSL Notification Event Policy",
            alert_interval="30m",
            description="Something describing the policy.",
            filters={
                "actions": ["string"],
                "affected_asns": ["string"],
                "affected_components": ["string"],
                "affected_locations": ["string"],
                "airport_code": ["string"],
                "alert_trigger_preferences": ["string"],
                "alert_trigger_preferences_value": ["string"],
                "enabled": ["string"],
                "environment": ["string"],
                "event": ["string"],
                "event_source": ["string"],
                "event_type": ["string"],
                "group_by": ["string"],
                "health_check_id": ["string"],
                "incident_impact": ["INCIDENT_IMPACT_NONE"],
                "input_id": ["string"],
                "insight_class": ["string"],
                "limit": ["string"],
                "logo_tag": ["string"],
                "megabits_per_second": ["string"],
                "new_health": ["string"],
                "new_status": ["string"],
                "packets_per_second": ["string"],
                "pool_id": ["string"],
                "pop_names": ["string"],
                "product": ["string"],
                "project_id": ["string"],
                "protocol": ["string"],
                "query_tag": ["string"],
                "requests_per_second": ["string"],
                "selectors": ["string"],
                "services": ["string"],
                "slo": ["99.9"],
                "status": ["string"],
                "target_hostname": ["string"],
                "target_ip": ["string"],
                "target_zone_name": ["string"],
                "traffic_exclusions": ["security_events"],
                "tunnel_id": ["string"],
                "tunnel_name": ["string"],
                "where": ["string"],
                "zones": ["string"],
            },
        )
        assert_matches_type(Optional[PolicyCreateResponse], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.policies.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            alert_type="access_custom_certificate_expiration_type",
            enabled=True,
            mechanisms={},
            name="SSL Notification Event Policy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Optional[PolicyCreateResponse], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.policies.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            alert_type="access_custom_certificate_expiration_type",
            enabled=True,
            mechanisms={},
            name="SSL Notification Event Policy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Optional[PolicyCreateResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.policies.with_raw_response.create(
                account_id="",
                alert_type="access_custom_certificate_expiration_type",
                enabled=True,
                mechanisms={},
                name="SSL Notification Event Policy",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.alerting.policies.update(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.alerting.policies.update(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            alert_interval="30m",
            alert_type="access_custom_certificate_expiration_type",
            description="Something describing the policy.",
            enabled=True,
            filters={
                "actions": ["string"],
                "affected_asns": ["string"],
                "affected_components": ["string"],
                "affected_locations": ["string"],
                "airport_code": ["string"],
                "alert_trigger_preferences": ["string"],
                "alert_trigger_preferences_value": ["string"],
                "enabled": ["string"],
                "environment": ["string"],
                "event": ["string"],
                "event_source": ["string"],
                "event_type": ["string"],
                "group_by": ["string"],
                "health_check_id": ["string"],
                "incident_impact": ["INCIDENT_IMPACT_NONE"],
                "input_id": ["string"],
                "insight_class": ["string"],
                "limit": ["string"],
                "logo_tag": ["string"],
                "megabits_per_second": ["string"],
                "new_health": ["string"],
                "new_status": ["string"],
                "packets_per_second": ["string"],
                "pool_id": ["string"],
                "pop_names": ["string"],
                "product": ["string"],
                "project_id": ["string"],
                "protocol": ["string"],
                "query_tag": ["string"],
                "requests_per_second": ["string"],
                "selectors": ["string"],
                "services": ["string"],
                "slo": ["99.9"],
                "status": ["string"],
                "target_hostname": ["string"],
                "target_ip": ["string"],
                "target_zone_name": ["string"],
                "traffic_exclusions": ["security_events"],
                "tunnel_id": ["string"],
                "tunnel_name": ["string"],
                "where": ["string"],
                "zones": ["string"],
            },
            mechanisms={
                "email": [{"id": "test@example.com"}],
                "pagerduty": [{}],
                "webhooks": [{}],
            },
            name="SSL Notification Event Policy",
        )
        assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.policies.with_raw_response.update(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.policies.with_streaming_response.update(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Optional[PolicyUpdateResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.policies.with_raw_response.update(
                policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.alerting.policies.with_raw_response.update(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.alerting.policies.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Policy], policy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.policies.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(AsyncSinglePage[Policy], policy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.policies.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(AsyncSinglePage[Policy], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.policies.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.alerting.policies.delete(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.policies.with_raw_response.delete(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.policies.with_streaming_response.delete(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.policies.with_raw_response.delete(
                policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.alerting.policies.with_raw_response.delete(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.alerting.policies.get(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Policy], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.policies.with_raw_response.get(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Optional[Policy], policy, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.policies.with_streaming_response.get(
            policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Optional[Policy], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4274"
    )
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.policies.with_raw_response.get(
                policy_id="0da2b59e-f118-439d-8097-bdfb215203c9",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.alerting.policies.with_raw_response.get(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
