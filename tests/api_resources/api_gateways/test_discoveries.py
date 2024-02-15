# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.api_gateways import DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDiscoveries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
        self, client: Cloudflare
    ) -> None:
        discovery = client.api_gateways.discoveries.api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse, discovery, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
        self, client: Cloudflare
    ) -> None:
        response = client.api_gateways.discoveries.with_raw_response.api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discovery = response.parse()
        assert_matches_type(
            DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse, discovery, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
        self, client: Cloudflare
    ) -> None:
        with client.api_gateways.discoveries.with_streaming_response.api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discovery = response.parse()
            assert_matches_type(
                DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse, discovery, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.discoveries.with_raw_response.api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
                "",
            )


class TestAsyncDiscoveries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        discovery = await async_client.api_gateways.discoveries.api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse, discovery, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.api_gateways.discoveries.with_raw_response.api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discovery = await response.parse()
        assert_matches_type(
            DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse, discovery, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.api_gateways.discoveries.with_streaming_response.api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discovery = await response.parse()
            assert_matches_type(
                DiscoveryAPIShieldEndpointManagementGetAPIDiscoveryResultsForAZoneResponse, discovery, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.discoveries.with_raw_response.api_shield_endpoint_management_get_api_discovery_results_for_a_zone(
                "",
            )
