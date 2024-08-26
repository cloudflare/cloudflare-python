# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.dex.fleet_status import DeviceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDevices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        device = client.zero_trust.dex.fleet_status.devices.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            page=1,
            per_page=10,
            to="2023-10-11T00:00:00Z",
        )
        assert_matches_type(SyncV4PagePaginationArray[DeviceListResponse], device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        device = client.zero_trust.dex.fleet_status.devices.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            page=1,
            per_page=10,
            to="2023-10-11T00:00:00Z",
            colo="SJC",
            device_id="cb49c27f-7f97-49c5-b6f3-f7c01ead0fd7",
            mode="proxy",
            platform="windows",
            sort_by="colo",
            source="last_seen",
            status="connected",
            version="1.0.0",
        )
        assert_matches_type(SyncV4PagePaginationArray[DeviceListResponse], device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.fleet_status.devices.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            page=1,
            per_page=10,
            to="2023-10-11T00:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[DeviceListResponse], device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.fleet_status.devices.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            page=1,
            per_page=10,
            to="2023-10-11T00:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[DeviceListResponse], device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.fleet_status.devices.with_raw_response.list(
                account_id="",
                from_="2023-10-11T00:00:00Z",
                page=1,
                per_page=10,
                to="2023-10-11T00:00:00Z",
            )


class TestAsyncDevices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        device = await async_client.zero_trust.dex.fleet_status.devices.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            page=1,
            per_page=10,
            to="2023-10-11T00:00:00Z",
        )
        assert_matches_type(AsyncV4PagePaginationArray[DeviceListResponse], device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        device = await async_client.zero_trust.dex.fleet_status.devices.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            page=1,
            per_page=10,
            to="2023-10-11T00:00:00Z",
            colo="SJC",
            device_id="cb49c27f-7f97-49c5-b6f3-f7c01ead0fd7",
            mode="proxy",
            platform="windows",
            sort_by="colo",
            source="last_seen",
            status="connected",
            version="1.0.0",
        )
        assert_matches_type(AsyncV4PagePaginationArray[DeviceListResponse], device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.fleet_status.devices.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            page=1,
            per_page=10,
            to="2023-10-11T00:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[DeviceListResponse], device, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.fleet_status.devices.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-10-11T00:00:00Z",
            page=1,
            per_page=10,
            to="2023-10-11T00:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[DeviceListResponse], device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.fleet_status.devices.with_raw_response.list(
                account_id="",
                from_="2023-10-11T00:00:00Z",
                page=1,
                per_page=10,
                to="2023-10-11T00:00:00Z",
            )
