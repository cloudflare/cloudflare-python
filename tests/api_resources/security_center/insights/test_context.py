# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.security_center.insights import ContextGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContext:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        context = client.security_center.insights.context.get(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ContextGetResponse], context, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.security_center.insights.context.with_raw_response.get(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(Optional[ContextGetResponse], context, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.security_center.insights.context.with_streaming_response.get(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(Optional[ContextGetResponse], context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.security_center.insights.context.with_raw_response.get(
                issue_id="issue_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `issue_id` but received ''"):
            client.security_center.insights.context.with_raw_response.get(
                issue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncContext:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        context = await async_client.security_center.insights.context.get(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ContextGetResponse], context, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.security_center.insights.context.with_raw_response.get(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(Optional[ContextGetResponse], context, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.security_center.insights.context.with_streaming_response.get(
            issue_id="issue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(Optional[ContextGetResponse], context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.security_center.insights.context.with_raw_response.get(
                issue_id="issue_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `issue_id` but received ''"):
            await async_client.security_center.insights.context.with_raw_response.get(
                issue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
