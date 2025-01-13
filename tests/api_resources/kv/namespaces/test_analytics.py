# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.kv.namespaces import Schema, Components

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalytics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        analytics = client.kv.namespaces.analytics.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Schema], analytics, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        analytics = client.kv.namespaces.analytics.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            query={
                "dimensions": ["accountId"],
                "filters": "requestType==read AND responseCode!=200",
                "limit": 0,
                "metrics": ["requests"],
                "since": parse_datetime("2019-01-02T02:20:00Z"),
                "sort": ["+requests", "-responseCode"],
                "until": parse_datetime("2019-01-02T03:20:00Z"),
            },
        )
        assert_matches_type(Optional[Schema], analytics, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.analytics.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(Optional[Schema], analytics, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.kv.namespaces.analytics.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(Optional[Schema], analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.analytics.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_stored(self, client: Cloudflare) -> None:
        analytics = client.kv.namespaces.analytics.stored(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Components], analytics, path=["response"])

    @parametrize
    def test_method_stored_with_all_params(self, client: Cloudflare) -> None:
        analytics = client.kv.namespaces.analytics.stored(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            query={
                "dimensions": ["namespaceId"],
                "filters": "namespaceId==a4e8cbb7-1b58-4990-925e-e026d40c4c64",
                "limit": 0,
                "metrics": ["storedBytes"],
                "since": parse_datetime("2019-01-02T02:20:00Z"),
                "sort": ["+storedBytes", "-namespaceId"],
                "until": parse_datetime("2019-01-02T03:20:00Z"),
            },
        )
        assert_matches_type(Optional[Components], analytics, path=["response"])

    @parametrize
    def test_raw_response_stored(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.analytics.with_raw_response.stored(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(Optional[Components], analytics, path=["response"])

    @parametrize
    def test_streaming_response_stored(self, client: Cloudflare) -> None:
        with client.kv.namespaces.analytics.with_streaming_response.stored(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(Optional[Components], analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stored(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.analytics.with_raw_response.stored(
                account_id="",
            )


class TestAsyncAnalytics:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        analytics = await async_client.kv.namespaces.analytics.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Schema], analytics, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        analytics = await async_client.kv.namespaces.analytics.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            query={
                "dimensions": ["accountId"],
                "filters": "requestType==read AND responseCode!=200",
                "limit": 0,
                "metrics": ["requests"],
                "since": parse_datetime("2019-01-02T02:20:00Z"),
                "sort": ["+requests", "-responseCode"],
                "until": parse_datetime("2019-01-02T03:20:00Z"),
            },
        )
        assert_matches_type(Optional[Schema], analytics, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.analytics.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(Optional[Schema], analytics, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.analytics.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(Optional[Schema], analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.analytics.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_stored(self, async_client: AsyncCloudflare) -> None:
        analytics = await async_client.kv.namespaces.analytics.stored(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Components], analytics, path=["response"])

    @parametrize
    async def test_method_stored_with_all_params(self, async_client: AsyncCloudflare) -> None:
        analytics = await async_client.kv.namespaces.analytics.stored(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            query={
                "dimensions": ["namespaceId"],
                "filters": "namespaceId==a4e8cbb7-1b58-4990-925e-e026d40c4c64",
                "limit": 0,
                "metrics": ["storedBytes"],
                "since": parse_datetime("2019-01-02T02:20:00Z"),
                "sort": ["+storedBytes", "-namespaceId"],
                "until": parse_datetime("2019-01-02T03:20:00Z"),
            },
        )
        assert_matches_type(Optional[Components], analytics, path=["response"])

    @parametrize
    async def test_raw_response_stored(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.analytics.with_raw_response.stored(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(Optional[Components], analytics, path=["response"])

    @parametrize
    async def test_streaming_response_stored(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.analytics.with_streaming_response.stored(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(Optional[Components], analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stored(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.analytics.with_raw_response.stored(
                account_id="",
            )
