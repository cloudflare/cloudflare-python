# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dex import (
    FleetStatusLiveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFleetStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_live(self, client: Cloudflare) -> None:
        fleet_status = client.zero_trust.dex.fleet_status.live(
            account_id="01a7362d577a6c3019a474fd6f485823",
            since_minutes=10,
        )
        assert_matches_type(Optional[FleetStatusLiveResponse], fleet_status, path=["response"])

    @parametrize
    def test_raw_response_live(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.fleet_status.with_raw_response.live(
            account_id="01a7362d577a6c3019a474fd6f485823",
            since_minutes=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet_status = response.parse()
        assert_matches_type(Optional[FleetStatusLiveResponse], fleet_status, path=["response"])

    @parametrize
    def test_streaming_response_live(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.fleet_status.with_streaming_response.live(
            account_id="01a7362d577a6c3019a474fd6f485823",
            since_minutes=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet_status = response.parse()
            assert_matches_type(Optional[FleetStatusLiveResponse], fleet_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_live(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.fleet_status.with_raw_response.live(
                account_id="",
                since_minutes=10,
            )

    @parametrize
    def test_method_over_time(self, client: Cloudflare) -> None:
        fleet_status = client.zero_trust.dex.fleet_status.over_time(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            to="2023-10-11T00:00:00Z",
        )
        assert fleet_status is None

    @parametrize
    def test_method_over_time_with_all_params(self, client: Cloudflare) -> None:
        fleet_status = client.zero_trust.dex.fleet_status.over_time(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            to="2023-10-11T00:00:00Z",
            colo="SJC",
            device_id="cb49c27f-7f97-49c5-b6f3-f7c01ead0fd7",
        )
        assert fleet_status is None

    @parametrize
    def test_raw_response_over_time(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.fleet_status.with_raw_response.over_time(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            to="2023-10-11T00:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet_status = response.parse()
        assert fleet_status is None

    @parametrize
    def test_streaming_response_over_time(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.fleet_status.with_streaming_response.over_time(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            to="2023-10-11T00:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet_status = response.parse()
            assert fleet_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_over_time(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.fleet_status.with_raw_response.over_time(
                account_id="",
                from_="2023-10-11T00:00:00Z",
                to="2023-10-11T00:00:00Z",
            )


class TestAsyncFleetStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_live(self, async_client: AsyncCloudflare) -> None:
        fleet_status = await async_client.zero_trust.dex.fleet_status.live(
            account_id="01a7362d577a6c3019a474fd6f485823",
            since_minutes=10,
        )
        assert_matches_type(Optional[FleetStatusLiveResponse], fleet_status, path=["response"])

    @parametrize
    async def test_raw_response_live(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.fleet_status.with_raw_response.live(
            account_id="01a7362d577a6c3019a474fd6f485823",
            since_minutes=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet_status = await response.parse()
        assert_matches_type(Optional[FleetStatusLiveResponse], fleet_status, path=["response"])

    @parametrize
    async def test_streaming_response_live(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.fleet_status.with_streaming_response.live(
            account_id="01a7362d577a6c3019a474fd6f485823",
            since_minutes=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet_status = await response.parse()
            assert_matches_type(Optional[FleetStatusLiveResponse], fleet_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_live(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.fleet_status.with_raw_response.live(
                account_id="",
                since_minutes=10,
            )

    @parametrize
    async def test_method_over_time(self, async_client: AsyncCloudflare) -> None:
        fleet_status = await async_client.zero_trust.dex.fleet_status.over_time(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            to="2023-10-11T00:00:00Z",
        )
        assert fleet_status is None

    @parametrize
    async def test_method_over_time_with_all_params(self, async_client: AsyncCloudflare) -> None:
        fleet_status = await async_client.zero_trust.dex.fleet_status.over_time(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            to="2023-10-11T00:00:00Z",
            colo="SJC",
            device_id="cb49c27f-7f97-49c5-b6f3-f7c01ead0fd7",
        )
        assert fleet_status is None

    @parametrize
    async def test_raw_response_over_time(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.fleet_status.with_raw_response.over_time(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            to="2023-10-11T00:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet_status = await response.parse()
        assert fleet_status is None

    @parametrize
    async def test_streaming_response_over_time(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.fleet_status.with_streaming_response.over_time(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            to="2023-10-11T00:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet_status = await response.parse()
            assert fleet_status is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_over_time(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.fleet_status.with_raw_response.over_time(
                account_id="",
                from_="2023-10-11T00:00:00Z",
                to="2023-10-11T00:00:00Z",
            )
