# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.gateways import (
    LocationUpdateResponse,
    LocationDeleteResponse,
    LocationGetResponse,
    LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse,
    LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.gateways import location_update_params
from cloudflare.types.gateways import location_zero_trust_gateway_locations_create_zero_trust_gateway_location_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        location = client.gateways.locations.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )
        assert_matches_type(LocationUpdateResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        location = client.gateways.locations.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
            client_default=False,
            ecs_support=False,
            networks=[{"network": "192.0.2.1/32"}, {"network": "192.0.2.1/32"}, {"network": "192.0.2.1/32"}],
        )
        assert_matches_type(LocationUpdateResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.gateways.locations.with_raw_response.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(LocationUpdateResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.gateways.locations.with_streaming_response.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(LocationUpdateResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        location = client.gateways.locations.delete(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LocationDeleteResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.gateways.locations.with_raw_response.delete(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(LocationDeleteResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.gateways.locations.with_streaming_response.delete(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(LocationDeleteResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        location = client.gateways.locations.get(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.gateways.locations.with_raw_response.get(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.gateways.locations.with_streaming_response.get(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(LocationGetResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_gateway_locations_create_zero_trust_gateway_location(self, client: Cloudflare) -> None:
        location = client.gateways.locations.zero_trust_gateway_locations_create_zero_trust_gateway_location(
            "699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )
        assert_matches_type(
            LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse, location, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_gateway_locations_create_zero_trust_gateway_location_with_all_params(
        self, client: Cloudflare
    ) -> None:
        location = client.gateways.locations.zero_trust_gateway_locations_create_zero_trust_gateway_location(
            "699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
            client_default=False,
            ecs_support=False,
            networks=[{"network": "192.0.2.1/32"}, {"network": "192.0.2.1/32"}, {"network": "192.0.2.1/32"}],
        )
        assert_matches_type(
            LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse, location, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_gateway_locations_create_zero_trust_gateway_location(
        self, client: Cloudflare
    ) -> None:
        response = (
            client.gateways.locations.with_raw_response.zero_trust_gateway_locations_create_zero_trust_gateway_location(
                "699d98642c564d2e855e9661899b7252",
                name="Austin Office Location",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(
            LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse, location, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_gateway_locations_create_zero_trust_gateway_location(
        self, client: Cloudflare
    ) -> None:
        with client.gateways.locations.with_streaming_response.zero_trust_gateway_locations_create_zero_trust_gateway_location(
            "699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(
                LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse, location, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_gateway_locations_list_zero_trust_gateway_locations(self, client: Cloudflare) -> None:
        location = client.gateways.locations.zero_trust_gateway_locations_list_zero_trust_gateway_locations(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse],
            location,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_gateway_locations_list_zero_trust_gateway_locations(
        self, client: Cloudflare
    ) -> None:
        response = (
            client.gateways.locations.with_raw_response.zero_trust_gateway_locations_list_zero_trust_gateway_locations(
                "699d98642c564d2e855e9661899b7252",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(
            Optional[LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse],
            location,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_gateway_locations_list_zero_trust_gateway_locations(
        self, client: Cloudflare
    ) -> None:
        with client.gateways.locations.with_streaming_response.zero_trust_gateway_locations_list_zero_trust_gateway_locations(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(
                Optional[LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse],
                location,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncLocations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.gateways.locations.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )
        assert_matches_type(LocationUpdateResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.gateways.locations.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
            client_default=False,
            ecs_support=False,
            networks=[{"network": "192.0.2.1/32"}, {"network": "192.0.2.1/32"}, {"network": "192.0.2.1/32"}],
        )
        assert_matches_type(LocationUpdateResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.locations.with_raw_response.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(LocationUpdateResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.locations.with_streaming_response.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(LocationUpdateResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.gateways.locations.delete(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LocationDeleteResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.locations.with_raw_response.delete(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(LocationDeleteResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.locations.with_streaming_response.delete(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(LocationDeleteResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.gateways.locations.get(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.locations.with_raw_response.get(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.locations.with_streaming_response.get(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(LocationGetResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_gateway_locations_create_zero_trust_gateway_location(
        self, async_client: AsyncCloudflare
    ) -> None:
        location = (
            await async_client.gateways.locations.zero_trust_gateway_locations_create_zero_trust_gateway_location(
                "699d98642c564d2e855e9661899b7252",
                name="Austin Office Location",
            )
        )
        assert_matches_type(
            LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse, location, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_gateway_locations_create_zero_trust_gateway_location_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        location = (
            await async_client.gateways.locations.zero_trust_gateway_locations_create_zero_trust_gateway_location(
                "699d98642c564d2e855e9661899b7252",
                name="Austin Office Location",
                client_default=False,
                ecs_support=False,
                networks=[{"network": "192.0.2.1/32"}, {"network": "192.0.2.1/32"}, {"network": "192.0.2.1/32"}],
            )
        )
        assert_matches_type(
            LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse, location, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_gateway_locations_create_zero_trust_gateway_location(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.gateways.locations.with_raw_response.zero_trust_gateway_locations_create_zero_trust_gateway_location(
            "699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(
            LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse, location, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_gateway_locations_create_zero_trust_gateway_location(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.locations.with_streaming_response.zero_trust_gateway_locations_create_zero_trust_gateway_location(
            "699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(
                LocationZeroTrustGatewayLocationsCreateZeroTrustGatewayLocationResponse, location, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_gateway_locations_list_zero_trust_gateway_locations(
        self, async_client: AsyncCloudflare
    ) -> None:
        location = await async_client.gateways.locations.zero_trust_gateway_locations_list_zero_trust_gateway_locations(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse],
            location,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_gateway_locations_list_zero_trust_gateway_locations(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.gateways.locations.with_raw_response.zero_trust_gateway_locations_list_zero_trust_gateway_locations(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(
            Optional[LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse],
            location,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_gateway_locations_list_zero_trust_gateway_locations(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.locations.with_streaming_response.zero_trust_gateway_locations_list_zero_trust_gateway_locations(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(
                Optional[LocationZeroTrustGatewayLocationsListZeroTrustGatewayLocationsResponse],
                location,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
