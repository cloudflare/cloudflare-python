# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust import (
    ConnectivitySettingGetResponse,
    ConnectivitySettingEditResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectivitySettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        connectivity_setting = client.zero_trust.connectivity_settings.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ConnectivitySettingEditResponse, connectivity_setting, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        connectivity_setting = client.zero_trust.connectivity_settings.edit(
            account_id="699d98642c564d2e855e9661899b7252",
            icmp_proxy_enabled=True,
            offramp_warp_enabled=True,
        )
        assert_matches_type(ConnectivitySettingEditResponse, connectivity_setting, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.connectivity_settings.with_raw_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_setting = response.parse()
        assert_matches_type(ConnectivitySettingEditResponse, connectivity_setting, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.connectivity_settings.with_streaming_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_setting = response.parse()
            assert_matches_type(ConnectivitySettingEditResponse, connectivity_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.connectivity_settings.with_raw_response.edit(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        connectivity_setting = client.zero_trust.connectivity_settings.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ConnectivitySettingGetResponse, connectivity_setting, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.connectivity_settings.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_setting = response.parse()
        assert_matches_type(ConnectivitySettingGetResponse, connectivity_setting, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.connectivity_settings.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_setting = response.parse()
            assert_matches_type(ConnectivitySettingGetResponse, connectivity_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.connectivity_settings.with_raw_response.get(
                account_id="",
            )


class TestAsyncConnectivitySettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        connectivity_setting = await async_client.zero_trust.connectivity_settings.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ConnectivitySettingEditResponse, connectivity_setting, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        connectivity_setting = await async_client.zero_trust.connectivity_settings.edit(
            account_id="699d98642c564d2e855e9661899b7252",
            icmp_proxy_enabled=True,
            offramp_warp_enabled=True,
        )
        assert_matches_type(ConnectivitySettingEditResponse, connectivity_setting, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.connectivity_settings.with_raw_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_setting = await response.parse()
        assert_matches_type(ConnectivitySettingEditResponse, connectivity_setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.connectivity_settings.with_streaming_response.edit(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_setting = await response.parse()
            assert_matches_type(ConnectivitySettingEditResponse, connectivity_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.connectivity_settings.with_raw_response.edit(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        connectivity_setting = await async_client.zero_trust.connectivity_settings.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ConnectivitySettingGetResponse, connectivity_setting, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.connectivity_settings.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connectivity_setting = await response.parse()
        assert_matches_type(ConnectivitySettingGetResponse, connectivity_setting, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.connectivity_settings.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connectivity_setting = await response.parse()
            assert_matches_type(ConnectivitySettingGetResponse, connectivity_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.connectivity_settings.with_raw_response.get(
                account_id="",
            )
