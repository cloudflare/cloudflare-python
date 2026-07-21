# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.analytics_query.data_security import ContentFindingTopNResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContentFindings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_top_n(self, client: Cloudflare) -> None:
        content_finding = client.analytics_query.data_security.content_findings.top_n(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            n=10,
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )
        assert_matches_type(SyncSinglePage[ContentFindingTopNResponse], content_finding, path=["response"])

    @parametrize
    def test_raw_response_top_n(self, client: Cloudflare) -> None:
        response = client.analytics_query.data_security.content_findings.with_raw_response.top_n(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            n=10,
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_finding = response.parse()
        assert_matches_type(SyncSinglePage[ContentFindingTopNResponse], content_finding, path=["response"])

    @parametrize
    def test_streaming_response_top_n(self, client: Cloudflare) -> None:
        with client.analytics_query.data_security.content_findings.with_streaming_response.top_n(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            n=10,
            to=parse_datetime("2024-11-08T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_finding = response.parse()
            assert_matches_type(SyncSinglePage[ContentFindingTopNResponse], content_finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_top_n(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.analytics_query.data_security.content_findings.with_raw_response.top_n(
                account_id="",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                n=10,
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )


class TestAsyncContentFindings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_top_n(self, async_client: AsyncCloudflare) -> None:
        content_finding = await async_client.analytics_query.data_security.content_findings.top_n(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            n=10,
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )
        assert_matches_type(AsyncSinglePage[ContentFindingTopNResponse], content_finding, path=["response"])

    @parametrize
    async def test_raw_response_top_n(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.analytics_query.data_security.content_findings.with_raw_response.top_n(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            n=10,
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_finding = await response.parse()
        assert_matches_type(AsyncSinglePage[ContentFindingTopNResponse], content_finding, path=["response"])

    @parametrize
    async def test_streaming_response_top_n(self, async_client: AsyncCloudflare) -> None:
        async with async_client.analytics_query.data_security.content_findings.with_streaming_response.top_n(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            n=10,
            to=parse_datetime("2024-11-08T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_finding = await response.parse()
            assert_matches_type(AsyncSinglePage[ContentFindingTopNResponse], content_finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_top_n(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.analytics_query.data_security.content_findings.with_raw_response.top_n(
                account_id="",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                n=10,
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )
