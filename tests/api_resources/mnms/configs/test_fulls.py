# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.mnms.configs import FullListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFulls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        full = client.mnms.configs.fulls.list(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(FullListResponse, full, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.mnms.configs.fulls.with_raw_response.list(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        full = response.parse()
        assert_matches_type(FullListResponse, full, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.mnms.configs.fulls.with_streaming_response.list(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            full = response.parse()
            assert_matches_type(FullListResponse, full, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFulls:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        full = await async_client.mnms.configs.fulls.list(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(FullListResponse, full, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.mnms.configs.fulls.with_raw_response.list(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        full = await response.parse()
        assert_matches_type(FullListResponse, full, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.mnms.configs.fulls.with_streaming_response.list(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            full = await response.parse()
            assert_matches_type(FullListResponse, full, path=["response"])

        assert cast(Any, response.is_closed) is True
