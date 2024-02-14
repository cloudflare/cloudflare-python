# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dex.fleet_status import LiveListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLive:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        live = client.dex.fleet_status.live.list(
            "01a7362d577a6c3019a474fd6f485823",
            since_minutes=10,
        )
        assert_matches_type(LiveListResponse, live, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dex.fleet_status.live.with_raw_response.list(
            "01a7362d577a6c3019a474fd6f485823",
            since_minutes=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live = response.parse()
        assert_matches_type(LiveListResponse, live, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dex.fleet_status.live.with_streaming_response.list(
            "01a7362d577a6c3019a474fd6f485823",
            since_minutes=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live = response.parse()
            assert_matches_type(LiveListResponse, live, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dex.fleet_status.live.with_raw_response.list(
                "",
                since_minutes=10,
            )


class TestAsyncLive:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        live = await async_client.dex.fleet_status.live.list(
            "01a7362d577a6c3019a474fd6f485823",
            since_minutes=10,
        )
        assert_matches_type(LiveListResponse, live, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dex.fleet_status.live.with_raw_response.list(
            "01a7362d577a6c3019a474fd6f485823",
            since_minutes=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live = await response.parse()
        assert_matches_type(LiveListResponse, live, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dex.fleet_status.live.with_streaming_response.list(
            "01a7362d577a6c3019a474fd6f485823",
            since_minutes=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live = await response.parse()
            assert_matches_type(LiveListResponse, live, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dex.fleet_status.live.with_raw_response.list(
                "",
                since_minutes=10,
            )
