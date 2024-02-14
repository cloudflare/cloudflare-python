# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.zerotrust import ConnectivitySettingUpdateResponse, ConnectivitySettingGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zerotrust import connectivity_setting_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectivitySettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        connectivity_setting = client.zerotrust.connectivity_settings.update(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ConnectivitySettingUpdateResponse, connectivity_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        connectivity_setting = client.zerotrust.connectivity_settings.update(
            "699d98642c564d2e855e9661899b7252",
            icmp_proxy_enabled=True,
            offramp_warp_enabled=True,
        )
        assert_matches_type(ConnectivitySettingUpdateResponse, connectivity_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zerotrust.connectivity_settings.with_raw_response.update(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_setting = response.parse()
        assert_matches_type(ConnectivitySettingUpdateResponse, connectivity_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zerotrust.connectivity_settings.with_streaming_response.update(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_setting = response.parse()
            assert_matches_type(ConnectivitySettingUpdateResponse, connectivity_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zerotrust.connectivity_settings.with_raw_response.update(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        connectivity_setting = client.zerotrust.connectivity_settings.get(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ConnectivitySettingGetResponse, connectivity_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zerotrust.connectivity_settings.with_raw_response.get(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_setting = response.parse()
        assert_matches_type(ConnectivitySettingGetResponse, connectivity_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zerotrust.connectivity_settings.with_streaming_response.get(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_setting = response.parse()
            assert_matches_type(ConnectivitySettingGetResponse, connectivity_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zerotrust.connectivity_settings.with_raw_response.get(
                "",
            )


class TestAsyncConnectivitySettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        connectivity_setting = await async_client.zerotrust.connectivity_settings.update(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ConnectivitySettingUpdateResponse, connectivity_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        connectivity_setting = await async_client.zerotrust.connectivity_settings.update(
            "699d98642c564d2e855e9661899b7252",
            icmp_proxy_enabled=True,
            offramp_warp_enabled=True,
        )
        assert_matches_type(ConnectivitySettingUpdateResponse, connectivity_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zerotrust.connectivity_settings.with_raw_response.update(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_setting = await response.parse()
        assert_matches_type(ConnectivitySettingUpdateResponse, connectivity_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zerotrust.connectivity_settings.with_streaming_response.update(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_setting = await response.parse()
            assert_matches_type(ConnectivitySettingUpdateResponse, connectivity_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zerotrust.connectivity_settings.with_raw_response.update(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        connectivity_setting = await async_client.zerotrust.connectivity_settings.get(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ConnectivitySettingGetResponse, connectivity_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zerotrust.connectivity_settings.with_raw_response.get(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_setting = await response.parse()
        assert_matches_type(ConnectivitySettingGetResponse, connectivity_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zerotrust.connectivity_settings.with_streaming_response.get(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_setting = await response.parse()
            assert_matches_type(ConnectivitySettingGetResponse, connectivity_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zerotrust.connectivity_settings.with_raw_response.get(
                "",
            )
