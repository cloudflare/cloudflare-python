# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.user.load_balancers import Analytics

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        event = client.user.load_balancers.analytics.events.list()
        assert_matches_type(SyncSinglePage[Analytics], event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        event = client.user.load_balancers.analytics.events.list(
            origin_healthy=True,
            origin_name="primary-dc-1",
            pool_healthy=True,
            pool_id="17b5962d775c646f3f9725cbc7a53df4",
            pool_name="primary-dc",
            since=parse_datetime("2016-11-11T12:00:00Z"),
            until=parse_datetime("2016-11-11T13:00:00Z"),
        )
        assert_matches_type(SyncSinglePage[Analytics], event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.analytics.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncSinglePage[Analytics], event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.user.load_balancers.analytics.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncSinglePage[Analytics], event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.user.load_balancers.analytics.events.list()
        assert_matches_type(AsyncSinglePage[Analytics], event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.user.load_balancers.analytics.events.list(
            origin_healthy=True,
            origin_name="primary-dc-1",
            pool_healthy=True,
            pool_id="17b5962d775c646f3f9725cbc7a53df4",
            pool_name="primary-dc",
            since=parse_datetime("2016-11-11T12:00:00Z"),
            until=parse_datetime("2016-11-11T13:00:00Z"),
        )
        assert_matches_type(AsyncSinglePage[Analytics], event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.analytics.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(AsyncSinglePage[Analytics], event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.analytics.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncSinglePage[Analytics], event, path=["response"])

        assert cast(Any, response.is_closed) is True
