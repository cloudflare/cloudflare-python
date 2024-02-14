# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.radar.searches import GlobalListResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.searches import global_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGlobals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        global_ = client.radar.searches.globals.list(
            query="United",
        )
        assert_matches_type(GlobalListResponse, global_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        global_ = client.radar.searches.globals.list(
            query="United",
            exclude=["SPECIAL_EVENTS", "NOTEBOOKS", "LOCATIONS"],
            format="JSON",
            include=["SPECIAL_EVENTS", "NOTEBOOKS", "LOCATIONS"],
            limit=5,
            limit_per_group=0,
        )
        assert_matches_type(GlobalListResponse, global_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.searches.globals.with_raw_response.list(
            query="United",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ = response.parse()
        assert_matches_type(GlobalListResponse, global_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.searches.globals.with_streaming_response.list(
            query="United",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ = response.parse()
            assert_matches_type(GlobalListResponse, global_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGlobals:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        global_ = await async_client.radar.searches.globals.list(
            query="United",
        )
        assert_matches_type(GlobalListResponse, global_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        global_ = await async_client.radar.searches.globals.list(
            query="United",
            exclude=["SPECIAL_EVENTS", "NOTEBOOKS", "LOCATIONS"],
            format="JSON",
            include=["SPECIAL_EVENTS", "NOTEBOOKS", "LOCATIONS"],
            limit=5,
            limit_per_group=0,
        )
        assert_matches_type(GlobalListResponse, global_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.searches.globals.with_raw_response.list(
            query="United",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ = await response.parse()
        assert_matches_type(GlobalListResponse, global_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.searches.globals.with_streaming_response.list(
            query="United",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ = await response.parse()
            assert_matches_type(GlobalListResponse, global_, path=["response"])

        assert cast(Any, response.is_closed) is True
