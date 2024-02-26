# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import (
    TunnelGetResponse,
    TunnelEditResponse,
    TunnelListResponse,
    TunnelCreateResponse,
    TunnelDeleteResponse,
)
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTunnels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        tunnel = client.tunnels.create(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
            tunnel_secret={},
        )
        assert_matches_type(TunnelCreateResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.tunnels.with_raw_response.create(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
            tunnel_secret={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = response.parse()
        assert_matches_type(TunnelCreateResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.tunnels.with_streaming_response.create(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
            tunnel_secret={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = response.parse()
            assert_matches_type(TunnelCreateResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.tunnels.with_raw_response.create(
                "",
                name="blog",
                tunnel_secret={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        tunnel = client.tunnels.list(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncV4PagePaginationArray[TunnelListResponse], tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        tunnel = client.tunnels.list(
            "699d98642c564d2e855e9661899b7252",
            exclude_prefix="vpc1-",
            existed_at=parse_datetime("2019-10-12T07:20:50.52Z"),
            include_prefix="vpc1-",
            is_deleted=True,
            name="blog",
            page=1,
            per_page=1,
            tun_types="cfd_tunnel,warp_connector",
            was_active_at=parse_datetime("2009-11-10T23:00:00Z"),
            was_inactive_at=parse_datetime("2009-11-10T23:00:00Z"),
        )
        assert_matches_type(SyncV4PagePaginationArray[TunnelListResponse], tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.tunnels.with_raw_response.list(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[TunnelListResponse], tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.tunnels.with_streaming_response.list(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[TunnelListResponse], tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.tunnels.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        tunnel = client.tunnels.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(TunnelDeleteResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.tunnels.with_raw_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = response.parse()
        assert_matches_type(TunnelDeleteResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.tunnels.with_streaming_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = response.parse()
            assert_matches_type(TunnelDeleteResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.tunnels.with_raw_response.delete(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.tunnels.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        tunnel = client.tunnels.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(TunnelEditResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        tunnel = client.tunnels.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="blog",
            tunnel_secret="AQIDBAUGBwgBAgMEBQYHCAECAwQFBgcIAQIDBAUGBwg=",
        )
        assert_matches_type(TunnelEditResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.tunnels.with_raw_response.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = response.parse()
        assert_matches_type(TunnelEditResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.tunnels.with_streaming_response.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = response.parse()
            assert_matches_type(TunnelEditResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.tunnels.with_raw_response.edit(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.tunnels.with_raw_response.edit(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        tunnel = client.tunnels.get(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(TunnelGetResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.tunnels.with_raw_response.get(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = response.parse()
        assert_matches_type(TunnelGetResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.tunnels.with_streaming_response.get(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = response.parse()
            assert_matches_type(TunnelGetResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.tunnels.with_raw_response.get(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.tunnels.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncTunnels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        tunnel = await async_client.tunnels.create(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
            tunnel_secret={},
        )
        assert_matches_type(TunnelCreateResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.tunnels.with_raw_response.create(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
            tunnel_secret={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = await response.parse()
        assert_matches_type(TunnelCreateResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.tunnels.with_streaming_response.create(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
            tunnel_secret={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = await response.parse()
            assert_matches_type(TunnelCreateResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.tunnels.with_raw_response.create(
                "",
                name="blog",
                tunnel_secret={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        tunnel = await async_client.tunnels.list(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncV4PagePaginationArray[TunnelListResponse], tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        tunnel = await async_client.tunnels.list(
            "699d98642c564d2e855e9661899b7252",
            exclude_prefix="vpc1-",
            existed_at=parse_datetime("2019-10-12T07:20:50.52Z"),
            include_prefix="vpc1-",
            is_deleted=True,
            name="blog",
            page=1,
            per_page=1,
            tun_types="cfd_tunnel,warp_connector",
            was_active_at=parse_datetime("2009-11-10T23:00:00Z"),
            was_inactive_at=parse_datetime("2009-11-10T23:00:00Z"),
        )
        assert_matches_type(AsyncV4PagePaginationArray[TunnelListResponse], tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.tunnels.with_raw_response.list(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[TunnelListResponse], tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.tunnels.with_streaming_response.list(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[TunnelListResponse], tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.tunnels.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        tunnel = await async_client.tunnels.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(TunnelDeleteResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.tunnels.with_raw_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = await response.parse()
        assert_matches_type(TunnelDeleteResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.tunnels.with_streaming_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = await response.parse()
            assert_matches_type(TunnelDeleteResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.tunnels.with_raw_response.delete(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.tunnels.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        tunnel = await async_client.tunnels.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(TunnelEditResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        tunnel = await async_client.tunnels.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="blog",
            tunnel_secret="AQIDBAUGBwgBAgMEBQYHCAECAwQFBgcIAQIDBAUGBwg=",
        )
        assert_matches_type(TunnelEditResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.tunnels.with_raw_response.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = await response.parse()
        assert_matches_type(TunnelEditResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.tunnels.with_streaming_response.edit(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = await response.parse()
            assert_matches_type(TunnelEditResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.tunnels.with_raw_response.edit(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.tunnels.with_raw_response.edit(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        tunnel = await async_client.tunnels.get(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(TunnelGetResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.tunnels.with_raw_response.get(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = await response.parse()
        assert_matches_type(TunnelGetResponse, tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.tunnels.with_streaming_response.get(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = await response.parse()
            assert_matches_type(TunnelGetResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.tunnels.with_raw_response.get(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.tunnels.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )
