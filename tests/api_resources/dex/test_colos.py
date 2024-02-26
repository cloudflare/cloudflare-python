# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dex import ColoListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestColos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        colo = client.dex.colos.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-08-24T20:45:00Z",
            time_start="2023-08-20T20:45:00Z",
        )
        assert_matches_type(Optional[ColoListResponse], colo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        colo = client.dex.colos.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-08-24T20:45:00Z",
            time_start="2023-08-20T20:45:00Z",
            sort_by="fleet-status-usage",
        )
        assert_matches_type(Optional[ColoListResponse], colo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dex.colos.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-08-24T20:45:00Z",
            time_start="2023-08-20T20:45:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        colo = response.parse()
        assert_matches_type(Optional[ColoListResponse], colo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dex.colos.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-08-24T20:45:00Z",
            time_start="2023-08-20T20:45:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            colo = response.parse()
            assert_matches_type(Optional[ColoListResponse], colo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dex.colos.with_raw_response.list(
                account_id="",
                time_end="2023-08-24T20:45:00Z",
                time_start="2023-08-20T20:45:00Z",
            )


class TestAsyncColos:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        colo = await async_client.dex.colos.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-08-24T20:45:00Z",
            time_start="2023-08-20T20:45:00Z",
        )
        assert_matches_type(Optional[ColoListResponse], colo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        colo = await async_client.dex.colos.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-08-24T20:45:00Z",
            time_start="2023-08-20T20:45:00Z",
            sort_by="fleet-status-usage",
        )
        assert_matches_type(Optional[ColoListResponse], colo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dex.colos.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-08-24T20:45:00Z",
            time_start="2023-08-20T20:45:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        colo = await response.parse()
        assert_matches_type(Optional[ColoListResponse], colo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dex.colos.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-08-24T20:45:00Z",
            time_start="2023-08-20T20:45:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            colo = await response.parse()
            assert_matches_type(Optional[ColoListResponse], colo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dex.colos.with_raw_response.list(
                account_id="",
                time_end="2023-08-24T20:45:00Z",
                time_start="2023-08-20T20:45:00Z",
            )
