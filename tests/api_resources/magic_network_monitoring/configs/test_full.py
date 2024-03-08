# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magic_network_monitoring import MagicVisibilityMNMConfig

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFull:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        full = client.magic_network_monitoring.configs.full.get(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(MagicVisibilityMNMConfig, full, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_network_monitoring.configs.full.with_raw_response.get(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        full = response.parse()
        assert_matches_type(MagicVisibilityMNMConfig, full, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_network_monitoring.configs.full.with_streaming_response.get(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            full = response.parse()
            assert_matches_type(MagicVisibilityMNMConfig, full, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFull:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        full = await async_client.magic_network_monitoring.configs.full.get(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(MagicVisibilityMNMConfig, full, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_network_monitoring.configs.full.with_raw_response.get(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        full = await response.parse()
        assert_matches_type(MagicVisibilityMNMConfig, full, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_network_monitoring.configs.full.with_streaming_response.get(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            full = await response.parse()
            assert_matches_type(MagicVisibilityMNMConfig, full, path=["response"])

        assert cast(Any, response.is_closed) is True
