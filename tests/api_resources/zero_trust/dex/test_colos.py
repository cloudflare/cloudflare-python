# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestColos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        colo = client.zero_trust.dex.colos.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-08-20T20:45:00Z",
            to="2023-08-24T20:45:00Z",
        )
        assert_matches_type(SyncSinglePage[object], colo, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        colo = client.zero_trust.dex.colos.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-08-20T20:45:00Z",
            to="2023-08-24T20:45:00Z",
            sort_by="fleet-status-usage",
        )
        assert_matches_type(SyncSinglePage[object], colo, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.colos.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-08-20T20:45:00Z",
            to="2023-08-24T20:45:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        colo = response.parse()
        assert_matches_type(SyncSinglePage[object], colo, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.colos.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-08-20T20:45:00Z",
            to="2023-08-24T20:45:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            colo = response.parse()
            assert_matches_type(SyncSinglePage[object], colo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.colos.with_raw_response.list(
                account_id="",
                from_="2023-08-20T20:45:00Z",
                to="2023-08-24T20:45:00Z",
            )


class TestAsyncColos:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        colo = await async_client.zero_trust.dex.colos.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-08-20T20:45:00Z",
            to="2023-08-24T20:45:00Z",
        )
        assert_matches_type(AsyncSinglePage[object], colo, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        colo = await async_client.zero_trust.dex.colos.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-08-20T20:45:00Z",
            to="2023-08-24T20:45:00Z",
            sort_by="fleet-status-usage",
        )
        assert_matches_type(AsyncSinglePage[object], colo, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.colos.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-08-20T20:45:00Z",
            to="2023-08-24T20:45:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        colo = await response.parse()
        assert_matches_type(AsyncSinglePage[object], colo, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.colos.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-08-20T20:45:00Z",
            to="2023-08-24T20:45:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            colo = await response.parse()
            assert_matches_type(AsyncSinglePage[object], colo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.colos.with_raw_response.list(
                account_id="",
                from_="2023-08-20T20:45:00Z",
                to="2023-08-24T20:45:00Z",
            )
