# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRequest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        request = client.ai_gateway.logs.request.get(
            "string",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            id="my-gateway",
        )
        assert_matches_type(object, request, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.ai_gateway.logs.request.with_raw_response.get(
            "string",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            id="my-gateway",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(object, request, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.ai_gateway.logs.request.with_streaming_response.get(
            "string",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            id="my-gateway",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(object, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.logs.request.with_raw_response.get(
                "string",
                account_id="",
                id="my-gateway",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.logs.request.with_raw_response.get(
                "string",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `log_id` but received ''"):
            client.ai_gateway.logs.request.with_raw_response.get(
                "",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                id="my-gateway",
            )


class TestAsyncRequest:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        request = await async_client.ai_gateway.logs.request.get(
            "string",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            id="my-gateway",
        )
        assert_matches_type(object, request, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.logs.request.with_raw_response.get(
            "string",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            id="my-gateway",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(object, request, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.logs.request.with_streaming_response.get(
            "string",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            id="my-gateway",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(object, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.logs.request.with_raw_response.get(
                "string",
                account_id="",
                id="my-gateway",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.logs.request.with_raw_response.get(
                "string",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `log_id` but received ''"):
            await async_client.ai_gateway.logs.request.with_raw_response.get(
                "",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                id="my-gateway",
            )
