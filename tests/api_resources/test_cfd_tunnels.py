# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import (
    CfdTunnelGetResponse,
    CfdTunnelDeleteResponse,
    CfdTunnelUpdateResponse,
    CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse,
    CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse,
)
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCfdTunnels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        cfd_tunnel = client.cfd_tunnels.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(CfdTunnelUpdateResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        cfd_tunnel = client.cfd_tunnels.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="blog",
            tunnel_secret="AQIDBAUGBwgBAgMEBQYHCAECAwQFBgcIAQIDBAUGBwg=",
        )
        assert_matches_type(CfdTunnelUpdateResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.cfd_tunnels.with_raw_response.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cfd_tunnel = response.parse()
        assert_matches_type(CfdTunnelUpdateResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.cfd_tunnels.with_streaming_response.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cfd_tunnel = response.parse()
            assert_matches_type(CfdTunnelUpdateResponse, cfd_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cfd_tunnels.with_raw_response.update(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.cfd_tunnels.with_raw_response.update(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        cfd_tunnel = client.cfd_tunnels.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(CfdTunnelDeleteResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cfd_tunnels.with_raw_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cfd_tunnel = response.parse()
        assert_matches_type(CfdTunnelDeleteResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cfd_tunnels.with_streaming_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cfd_tunnel = response.parse()
            assert_matches_type(CfdTunnelDeleteResponse, cfd_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cfd_tunnels.with_raw_response.delete(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.cfd_tunnels.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_tunnel_create_a_cloudflare_tunnel(self, client: Cloudflare) -> None:
        cfd_tunnel = client.cfd_tunnels.cloudflare_tunnel_create_a_cloudflare_tunnel(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
        )
        assert_matches_type(CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_tunnel_create_a_cloudflare_tunnel_with_all_params(self, client: Cloudflare) -> None:
        cfd_tunnel = client.cfd_tunnels.cloudflare_tunnel_create_a_cloudflare_tunnel(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
            config_src="cloudflare",
            tunnel_secret="AQIDBAUGBwgBAgMEBQYHCAECAwQFBgcIAQIDBAUGBwg=",
        )
        assert_matches_type(CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cloudflare_tunnel_create_a_cloudflare_tunnel(self, client: Cloudflare) -> None:
        response = client.cfd_tunnels.with_raw_response.cloudflare_tunnel_create_a_cloudflare_tunnel(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cfd_tunnel = response.parse()
        assert_matches_type(CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cloudflare_tunnel_create_a_cloudflare_tunnel(self, client: Cloudflare) -> None:
        with client.cfd_tunnels.with_streaming_response.cloudflare_tunnel_create_a_cloudflare_tunnel(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cfd_tunnel = response.parse()
            assert_matches_type(CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse, cfd_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cloudflare_tunnel_create_a_cloudflare_tunnel(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cfd_tunnels.with_raw_response.cloudflare_tunnel_create_a_cloudflare_tunnel(
                "",
                name="blog",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_tunnel_list_cloudflare_tunnels(self, client: Cloudflare) -> None:
        cfd_tunnel = client.cfd_tunnels.cloudflare_tunnel_list_cloudflare_tunnels(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse], cfd_tunnel, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_tunnel_list_cloudflare_tunnels_with_all_params(self, client: Cloudflare) -> None:
        cfd_tunnel = client.cfd_tunnels.cloudflare_tunnel_list_cloudflare_tunnels(
            "699d98642c564d2e855e9661899b7252",
            exclude_prefix="vpc1-",
            existed_at=parse_datetime("2019-10-12T07:20:50.52Z"),
            include_prefix="vpc1-",
            is_deleted=True,
            name="blog",
            page=1,
            per_page=1,
            was_active_at=parse_datetime("2009-11-10T23:00:00Z"),
            was_inactive_at=parse_datetime("2009-11-10T23:00:00Z"),
        )
        assert_matches_type(
            Optional[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse], cfd_tunnel, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cloudflare_tunnel_list_cloudflare_tunnels(self, client: Cloudflare) -> None:
        response = client.cfd_tunnels.with_raw_response.cloudflare_tunnel_list_cloudflare_tunnels(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cfd_tunnel = response.parse()
        assert_matches_type(
            Optional[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse], cfd_tunnel, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cloudflare_tunnel_list_cloudflare_tunnels(self, client: Cloudflare) -> None:
        with client.cfd_tunnels.with_streaming_response.cloudflare_tunnel_list_cloudflare_tunnels(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cfd_tunnel = response.parse()
            assert_matches_type(
                Optional[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse], cfd_tunnel, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cloudflare_tunnel_list_cloudflare_tunnels(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cfd_tunnels.with_raw_response.cloudflare_tunnel_list_cloudflare_tunnels(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        cfd_tunnel = client.cfd_tunnels.get(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(CfdTunnelGetResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cfd_tunnels.with_raw_response.get(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cfd_tunnel = response.parse()
        assert_matches_type(CfdTunnelGetResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cfd_tunnels.with_streaming_response.get(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cfd_tunnel = response.parse()
            assert_matches_type(CfdTunnelGetResponse, cfd_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cfd_tunnels.with_raw_response.get(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.cfd_tunnels.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncCfdTunnels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        cfd_tunnel = await async_client.cfd_tunnels.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(CfdTunnelUpdateResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cfd_tunnel = await async_client.cfd_tunnels.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="blog",
            tunnel_secret="AQIDBAUGBwgBAgMEBQYHCAECAwQFBgcIAQIDBAUGBwg=",
        )
        assert_matches_type(CfdTunnelUpdateResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cfd_tunnels.with_raw_response.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cfd_tunnel = await response.parse()
        assert_matches_type(CfdTunnelUpdateResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cfd_tunnels.with_streaming_response.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cfd_tunnel = await response.parse()
            assert_matches_type(CfdTunnelUpdateResponse, cfd_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cfd_tunnels.with_raw_response.update(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.cfd_tunnels.with_raw_response.update(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        cfd_tunnel = await async_client.cfd_tunnels.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(CfdTunnelDeleteResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cfd_tunnels.with_raw_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cfd_tunnel = await response.parse()
        assert_matches_type(CfdTunnelDeleteResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cfd_tunnels.with_streaming_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cfd_tunnel = await response.parse()
            assert_matches_type(CfdTunnelDeleteResponse, cfd_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cfd_tunnels.with_raw_response.delete(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.cfd_tunnels.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_tunnel_create_a_cloudflare_tunnel(self, async_client: AsyncCloudflare) -> None:
        cfd_tunnel = await async_client.cfd_tunnels.cloudflare_tunnel_create_a_cloudflare_tunnel(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
        )
        assert_matches_type(CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_tunnel_create_a_cloudflare_tunnel_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        cfd_tunnel = await async_client.cfd_tunnels.cloudflare_tunnel_create_a_cloudflare_tunnel(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
            config_src="cloudflare",
            tunnel_secret="AQIDBAUGBwgBAgMEBQYHCAECAwQFBgcIAQIDBAUGBwg=",
        )
        assert_matches_type(CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cloudflare_tunnel_create_a_cloudflare_tunnel(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.cfd_tunnels.with_raw_response.cloudflare_tunnel_create_a_cloudflare_tunnel(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cfd_tunnel = await response.parse()
        assert_matches_type(CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cloudflare_tunnel_create_a_cloudflare_tunnel(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.cfd_tunnels.with_streaming_response.cloudflare_tunnel_create_a_cloudflare_tunnel(
            "699d98642c564d2e855e9661899b7252",
            name="blog",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cfd_tunnel = await response.parse()
            assert_matches_type(CfdTunnelCloudflareTunnelCreateACloudflareTunnelResponse, cfd_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cloudflare_tunnel_create_a_cloudflare_tunnel(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cfd_tunnels.with_raw_response.cloudflare_tunnel_create_a_cloudflare_tunnel(
                "",
                name="blog",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_tunnel_list_cloudflare_tunnels(self, async_client: AsyncCloudflare) -> None:
        cfd_tunnel = await async_client.cfd_tunnels.cloudflare_tunnel_list_cloudflare_tunnels(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse], cfd_tunnel, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_tunnel_list_cloudflare_tunnels_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        cfd_tunnel = await async_client.cfd_tunnels.cloudflare_tunnel_list_cloudflare_tunnels(
            "699d98642c564d2e855e9661899b7252",
            exclude_prefix="vpc1-",
            existed_at=parse_datetime("2019-10-12T07:20:50.52Z"),
            include_prefix="vpc1-",
            is_deleted=True,
            name="blog",
            page=1,
            per_page=1,
            was_active_at=parse_datetime("2009-11-10T23:00:00Z"),
            was_inactive_at=parse_datetime("2009-11-10T23:00:00Z"),
        )
        assert_matches_type(
            Optional[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse], cfd_tunnel, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cloudflare_tunnel_list_cloudflare_tunnels(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cfd_tunnels.with_raw_response.cloudflare_tunnel_list_cloudflare_tunnels(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cfd_tunnel = await response.parse()
        assert_matches_type(
            Optional[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse], cfd_tunnel, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cloudflare_tunnel_list_cloudflare_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.cfd_tunnels.with_streaming_response.cloudflare_tunnel_list_cloudflare_tunnels(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cfd_tunnel = await response.parse()
            assert_matches_type(
                Optional[CfdTunnelCloudflareTunnelListCloudflareTunnelsResponse], cfd_tunnel, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cloudflare_tunnel_list_cloudflare_tunnels(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cfd_tunnels.with_raw_response.cloudflare_tunnel_list_cloudflare_tunnels(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        cfd_tunnel = await async_client.cfd_tunnels.get(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(CfdTunnelGetResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cfd_tunnels.with_raw_response.get(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cfd_tunnel = await response.parse()
        assert_matches_type(CfdTunnelGetResponse, cfd_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cfd_tunnels.with_streaming_response.get(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cfd_tunnel = await response.parse()
            assert_matches_type(CfdTunnelGetResponse, cfd_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cfd_tunnels.with_raw_response.get(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.cfd_tunnels.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )
