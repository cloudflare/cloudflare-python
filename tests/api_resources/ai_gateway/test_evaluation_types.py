# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.ai_gateway import EvaluationTypeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluationTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        evaluation_type = client.ai_gateway.evaluation_types.list(
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(SyncV4PagePaginationArray[EvaluationTypeListResponse], evaluation_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        evaluation_type = client.ai_gateway.evaluation_types.list(
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            order_by="order_by",
            order_by_direction="asc",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[EvaluationTypeListResponse], evaluation_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.ai_gateway.evaluation_types.with_raw_response.list(
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_type = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[EvaluationTypeListResponse], evaluation_type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.ai_gateway.evaluation_types.with_streaming_response.list(
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_type = response.parse()
            assert_matches_type(
                SyncV4PagePaginationArray[EvaluationTypeListResponse], evaluation_type, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.evaluation_types.with_raw_response.list(
                account_id="",
            )


class TestAsyncEvaluationTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        evaluation_type = await async_client.ai_gateway.evaluation_types.list(
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(AsyncV4PagePaginationArray[EvaluationTypeListResponse], evaluation_type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        evaluation_type = await async_client.ai_gateway.evaluation_types.list(
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            order_by="order_by",
            order_by_direction="asc",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[EvaluationTypeListResponse], evaluation_type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.evaluation_types.with_raw_response.list(
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_type = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[EvaluationTypeListResponse], evaluation_type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.evaluation_types.with_streaming_response.list(
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_type = await response.parse()
            assert_matches_type(
                AsyncV4PagePaginationArray[EvaluationTypeListResponse], evaluation_type, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.evaluation_types.with_raw_response.list(
                account_id="",
            )
