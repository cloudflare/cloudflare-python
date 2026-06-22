# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.logs.log_explorer.datasets import AvailableDataset

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvailable:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        available = client.logs.log_explorer.datasets.available.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[AvailableDataset], available, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        available = client.logs.log_explorer.datasets.available.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[AvailableDataset], available, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.logs.log_explorer.datasets.available.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        available = response.parse()
        assert_matches_type(SyncSinglePage[AvailableDataset], available, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.logs.log_explorer.datasets.available.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            available = response.parse()
            assert_matches_type(SyncSinglePage[AvailableDataset], available, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.logs.log_explorer.datasets.available.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.logs.log_explorer.datasets.available.with_raw_response.list(
                account_id="account_id",
            )


class TestAsyncAvailable:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        available = await async_client.logs.log_explorer.datasets.available.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[AvailableDataset], available, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        available = await async_client.logs.log_explorer.datasets.available.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[AvailableDataset], available, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logs.log_explorer.datasets.available.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        available = await response.parse()
        assert_matches_type(AsyncSinglePage[AvailableDataset], available, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logs.log_explorer.datasets.available.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            available = await response.parse()
            assert_matches_type(AsyncSinglePage[AvailableDataset], available, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.logs.log_explorer.datasets.available.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.logs.log_explorer.datasets.available.with_raw_response.list(
                account_id="account_id",
            )
