# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.networks import (
    HostnameRoute,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHostnameRoutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        hostname_route = client.zero_trust.networks.hostname_routes.create(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        hostname_route = client.zero_trust.networks.hostname_routes.create(
            account_id="699d98642c564d2e855e9661899b7252",
            comment="example comment",
            hostname="office-1.local",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.hostname_routes.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_route = response.parse()
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.hostname_routes.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_route = response.parse()
            assert_matches_type(HostnameRoute, hostname_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.hostname_routes.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        hostname_route = client.zero_trust.networks.hostname_routes.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncV4PagePaginationArray[HostnameRoute], hostname_route, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        hostname_route = client.zero_trust.networks.hostname_routes.list(
            account_id="699d98642c564d2e855e9661899b7252",
            id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            comment="example%20comment",
            existed_at="2019-10-12T07%3A20%3A50.52Z",
            hostname="office-1.local",
            is_deleted=True,
            page=1,
            per_page=1,
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(SyncV4PagePaginationArray[HostnameRoute], hostname_route, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.hostname_routes.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_route = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[HostnameRoute], hostname_route, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.hostname_routes.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_route = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[HostnameRoute], hostname_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.hostname_routes.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        hostname_route = client.zero_trust.networks.hostname_routes.delete(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.hostname_routes.with_raw_response.delete(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_route = response.parse()
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.hostname_routes.with_streaming_response.delete(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_route = response.parse()
            assert_matches_type(HostnameRoute, hostname_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.hostname_routes.with_raw_response.delete(
                hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname_route_id` but received ''"):
            client.zero_trust.networks.hostname_routes.with_raw_response.delete(
                hostname_route_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        hostname_route = client.zero_trust.networks.hostname_routes.edit(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        hostname_route = client.zero_trust.networks.hostname_routes.edit(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            comment="example comment",
            hostname="office-1.local",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.hostname_routes.with_raw_response.edit(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_route = response.parse()
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.hostname_routes.with_streaming_response.edit(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_route = response.parse()
            assert_matches_type(HostnameRoute, hostname_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.hostname_routes.with_raw_response.edit(
                hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname_route_id` but received ''"):
            client.zero_trust.networks.hostname_routes.with_raw_response.edit(
                hostname_route_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        hostname_route = client.zero_trust.networks.hostname_routes.get(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.hostname_routes.with_raw_response.get(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_route = response.parse()
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.hostname_routes.with_streaming_response.get(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_route = response.parse()
            assert_matches_type(HostnameRoute, hostname_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.hostname_routes.with_raw_response.get(
                hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname_route_id` but received ''"):
            client.zero_trust.networks.hostname_routes.with_raw_response.get(
                hostname_route_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncHostnameRoutes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        hostname_route = await async_client.zero_trust.networks.hostname_routes.create(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        hostname_route = await async_client.zero_trust.networks.hostname_routes.create(
            account_id="699d98642c564d2e855e9661899b7252",
            comment="example comment",
            hostname="office-1.local",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.hostname_routes.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_route = await response.parse()
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.hostname_routes.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_route = await response.parse()
            assert_matches_type(HostnameRoute, hostname_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.hostname_routes.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        hostname_route = await async_client.zero_trust.networks.hostname_routes.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncV4PagePaginationArray[HostnameRoute], hostname_route, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        hostname_route = await async_client.zero_trust.networks.hostname_routes.list(
            account_id="699d98642c564d2e855e9661899b7252",
            id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            comment="example%20comment",
            existed_at="2019-10-12T07%3A20%3A50.52Z",
            hostname="office-1.local",
            is_deleted=True,
            page=1,
            per_page=1,
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(AsyncV4PagePaginationArray[HostnameRoute], hostname_route, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.hostname_routes.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_route = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[HostnameRoute], hostname_route, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.hostname_routes.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_route = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[HostnameRoute], hostname_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.hostname_routes.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        hostname_route = await async_client.zero_trust.networks.hostname_routes.delete(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.hostname_routes.with_raw_response.delete(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_route = await response.parse()
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.hostname_routes.with_streaming_response.delete(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_route = await response.parse()
            assert_matches_type(HostnameRoute, hostname_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.hostname_routes.with_raw_response.delete(
                hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname_route_id` but received ''"):
            await async_client.zero_trust.networks.hostname_routes.with_raw_response.delete(
                hostname_route_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        hostname_route = await async_client.zero_trust.networks.hostname_routes.edit(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        hostname_route = await async_client.zero_trust.networks.hostname_routes.edit(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            comment="example comment",
            hostname="office-1.local",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.hostname_routes.with_raw_response.edit(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_route = await response.parse()
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.hostname_routes.with_streaming_response.edit(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_route = await response.parse()
            assert_matches_type(HostnameRoute, hostname_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.hostname_routes.with_raw_response.edit(
                hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname_route_id` but received ''"):
            await async_client.zero_trust.networks.hostname_routes.with_raw_response.edit(
                hostname_route_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        hostname_route = await async_client.zero_trust.networks.hostname_routes.get(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.hostname_routes.with_raw_response.get(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname_route = await response.parse()
        assert_matches_type(HostnameRoute, hostname_route, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.hostname_routes.with_streaming_response.get(
            hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname_route = await response.parse()
            assert_matches_type(HostnameRoute, hostname_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.hostname_routes.with_raw_response.get(
                hostname_route_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname_route_id` but received ''"):
            await async_client.zero_trust.networks.hostname_routes.with_raw_response.get(
                hostname_route_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )
