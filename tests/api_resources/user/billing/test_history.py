# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.user.billing import BillingHistory

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        history = client.user.billing.history.list()
        assert_matches_type(SyncV4PagePaginationArray[BillingHistory], history, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        history = client.user.billing.history.list(
            action="subscription",
            occurred_at=parse_datetime("2014-03-01T12:21:59.3456Z"),
            order="type",
            page=1,
            per_page=5,
            type="charge",
        )
        assert_matches_type(SyncV4PagePaginationArray[BillingHistory], history, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.user.billing.history.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[BillingHistory], history, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.user.billing.history.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[BillingHistory], history, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHistory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        history = await async_client.user.billing.history.list()
        assert_matches_type(AsyncV4PagePaginationArray[BillingHistory], history, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        history = await async_client.user.billing.history.list(
            action="subscription",
            occurred_at=parse_datetime("2014-03-01T12:21:59.3456Z"),
            order="type",
            page=1,
            per_page=5,
            type="charge",
        )
        assert_matches_type(AsyncV4PagePaginationArray[BillingHistory], history, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.billing.history.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[BillingHistory], history, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.billing.history.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[BillingHistory], history, path=["response"])

        assert cast(Any, response.is_closed) is True
