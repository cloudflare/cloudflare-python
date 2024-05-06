# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.ai_gateway import LogGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        log = client.ai_gateway.logs.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(LogGetResponse, log, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        log = client.ai_gateway.logs.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            cached=True,
            direction="asc",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            order_by="created_at",
            page=1,
            per_page=5,
            search="string",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            success=True,
        )
        assert_matches_type(LogGetResponse, log, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.ai_gateway.logs.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogGetResponse, log, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.ai_gateway.logs.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogGetResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.logs.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.logs.with_raw_response.get(
                "",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
            )


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        log = await async_client.ai_gateway.logs.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(LogGetResponse, log, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        log = await async_client.ai_gateway.logs.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            cached=True,
            direction="asc",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            order_by="created_at",
            page=1,
            per_page=5,
            search="string",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            success=True,
        )
        assert_matches_type(LogGetResponse, log, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.logs.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogGetResponse, log, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.logs.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogGetResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.logs.with_raw_response.get(
                "",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
            )
