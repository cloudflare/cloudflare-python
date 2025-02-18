# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.tunnels import (
    WARPConnectorGetResponse,
    WARPConnectorEditResponse,
    WARPConnectorListResponse,
    WARPConnectorCreateResponse,
    WARPConnectorDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWARPConnector:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        warp_connector = client.zero_trust.tunnels.warp_connector.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="blog",
        )
        assert_matches_type(WARPConnectorCreateResponse, warp_connector, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.tunnels.warp_connector.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="blog",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp_connector = response.parse()
        assert_matches_type(WARPConnectorCreateResponse, warp_connector, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.tunnels.warp_connector.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="blog",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp_connector = response.parse()
            assert_matches_type(WARPConnectorCreateResponse, warp_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.tunnels.warp_connector.with_raw_response.create(
                account_id="",
                name="blog",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        warp_connector = client.zero_trust.tunnels.warp_connector.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncV4PagePaginationArray[WARPConnectorListResponse], warp_connector, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        warp_connector = client.zero_trust.tunnels.warp_connector.list(
            account_id="699d98642c564d2e855e9661899b7252",
            exclude_prefix="vpc1-",
            existed_at="2019-10-12T07%3A20%3A50.52Z",
            include_prefix="vpc1-",
            is_deleted=True,
            name="blog",
            page=1,
            per_page=1,
            status="inactive",
            uuid="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            was_active_at=parse_datetime("2009-11-10T23:00:00Z"),
            was_inactive_at=parse_datetime("2009-11-10T23:00:00Z"),
        )
        assert_matches_type(SyncV4PagePaginationArray[WARPConnectorListResponse], warp_connector, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.tunnels.warp_connector.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp_connector = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[WARPConnectorListResponse], warp_connector, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.tunnels.warp_connector.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp_connector = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[WARPConnectorListResponse], warp_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.tunnels.warp_connector.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        warp_connector = client.zero_trust.tunnels.warp_connector.delete(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(WARPConnectorDeleteResponse, warp_connector, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.tunnels.warp_connector.with_raw_response.delete(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp_connector = response.parse()
        assert_matches_type(WARPConnectorDeleteResponse, warp_connector, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.tunnels.warp_connector.with_streaming_response.delete(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp_connector = response.parse()
            assert_matches_type(WARPConnectorDeleteResponse, warp_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.tunnels.warp_connector.with_raw_response.delete(
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.zero_trust.tunnels.warp_connector.with_raw_response.delete(
                tunnel_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        warp_connector = client.zero_trust.tunnels.warp_connector.edit(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(WARPConnectorEditResponse, warp_connector, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        warp_connector = client.zero_trust.tunnels.warp_connector.edit(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="blog",
            tunnel_secret="AQIDBAUGBwgBAgMEBQYHCAECAwQFBgcIAQIDBAUGBwg=",
        )
        assert_matches_type(WARPConnectorEditResponse, warp_connector, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.tunnels.warp_connector.with_raw_response.edit(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp_connector = response.parse()
        assert_matches_type(WARPConnectorEditResponse, warp_connector, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.tunnels.warp_connector.with_streaming_response.edit(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp_connector = response.parse()
            assert_matches_type(WARPConnectorEditResponse, warp_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.tunnels.warp_connector.with_raw_response.edit(
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.zero_trust.tunnels.warp_connector.with_raw_response.edit(
                tunnel_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        warp_connector = client.zero_trust.tunnels.warp_connector.get(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(WARPConnectorGetResponse, warp_connector, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.tunnels.warp_connector.with_raw_response.get(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp_connector = response.parse()
        assert_matches_type(WARPConnectorGetResponse, warp_connector, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.tunnels.warp_connector.with_streaming_response.get(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp_connector = response.parse()
            assert_matches_type(WARPConnectorGetResponse, warp_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.tunnels.warp_connector.with_raw_response.get(
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.zero_trust.tunnels.warp_connector.with_raw_response.get(
                tunnel_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncWARPConnector:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        warp_connector = await async_client.zero_trust.tunnels.warp_connector.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="blog",
        )
        assert_matches_type(WARPConnectorCreateResponse, warp_connector, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.tunnels.warp_connector.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="blog",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp_connector = await response.parse()
        assert_matches_type(WARPConnectorCreateResponse, warp_connector, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.tunnels.warp_connector.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="blog",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp_connector = await response.parse()
            assert_matches_type(WARPConnectorCreateResponse, warp_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.tunnels.warp_connector.with_raw_response.create(
                account_id="",
                name="blog",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        warp_connector = await async_client.zero_trust.tunnels.warp_connector.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncV4PagePaginationArray[WARPConnectorListResponse], warp_connector, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        warp_connector = await async_client.zero_trust.tunnels.warp_connector.list(
            account_id="699d98642c564d2e855e9661899b7252",
            exclude_prefix="vpc1-",
            existed_at="2019-10-12T07%3A20%3A50.52Z",
            include_prefix="vpc1-",
            is_deleted=True,
            name="blog",
            page=1,
            per_page=1,
            status="inactive",
            uuid="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            was_active_at=parse_datetime("2009-11-10T23:00:00Z"),
            was_inactive_at=parse_datetime("2009-11-10T23:00:00Z"),
        )
        assert_matches_type(AsyncV4PagePaginationArray[WARPConnectorListResponse], warp_connector, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.tunnels.warp_connector.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp_connector = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[WARPConnectorListResponse], warp_connector, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.tunnels.warp_connector.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp_connector = await response.parse()
            assert_matches_type(
                AsyncV4PagePaginationArray[WARPConnectorListResponse], warp_connector, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.tunnels.warp_connector.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        warp_connector = await async_client.zero_trust.tunnels.warp_connector.delete(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(WARPConnectorDeleteResponse, warp_connector, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.tunnels.warp_connector.with_raw_response.delete(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp_connector = await response.parse()
        assert_matches_type(WARPConnectorDeleteResponse, warp_connector, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.tunnels.warp_connector.with_streaming_response.delete(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp_connector = await response.parse()
            assert_matches_type(WARPConnectorDeleteResponse, warp_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.tunnels.warp_connector.with_raw_response.delete(
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.zero_trust.tunnels.warp_connector.with_raw_response.delete(
                tunnel_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        warp_connector = await async_client.zero_trust.tunnels.warp_connector.edit(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(WARPConnectorEditResponse, warp_connector, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        warp_connector = await async_client.zero_trust.tunnels.warp_connector.edit(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="blog",
            tunnel_secret="AQIDBAUGBwgBAgMEBQYHCAECAwQFBgcIAQIDBAUGBwg=",
        )
        assert_matches_type(WARPConnectorEditResponse, warp_connector, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.tunnels.warp_connector.with_raw_response.edit(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp_connector = await response.parse()
        assert_matches_type(WARPConnectorEditResponse, warp_connector, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.tunnels.warp_connector.with_streaming_response.edit(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp_connector = await response.parse()
            assert_matches_type(WARPConnectorEditResponse, warp_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.tunnels.warp_connector.with_raw_response.edit(
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.zero_trust.tunnels.warp_connector.with_raw_response.edit(
                tunnel_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        warp_connector = await async_client.zero_trust.tunnels.warp_connector.get(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(WARPConnectorGetResponse, warp_connector, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.tunnels.warp_connector.with_raw_response.get(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp_connector = await response.parse()
        assert_matches_type(WARPConnectorGetResponse, warp_connector, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.tunnels.warp_connector.with_streaming_response.get(
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp_connector = await response.parse()
            assert_matches_type(WARPConnectorGetResponse, warp_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.tunnels.warp_connector.with_raw_response.get(
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.zero_trust.tunnels.warp_connector.with_raw_response.get(
                tunnel_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )
