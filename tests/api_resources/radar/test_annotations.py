# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar import AnnotationListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnnotations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        annotation = client.radar.annotations.list()
        assert_matches_type(AnnotationListResponse, annotation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        annotation = client.radar.annotations.list(
            asn=174,
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_range="7d",
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            format="JSON",
            limit=5,
            location="US",
            offset=0,
        )
        assert_matches_type(AnnotationListResponse, annotation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.annotations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = response.parse()
        assert_matches_type(AnnotationListResponse, annotation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.annotations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = response.parse()
            assert_matches_type(AnnotationListResponse, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnnotations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        annotation = await async_client.radar.annotations.list()
        assert_matches_type(AnnotationListResponse, annotation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        annotation = await async_client.radar.annotations.list(
            asn=174,
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_range="7d",
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            format="JSON",
            limit=5,
            location="US",
            offset=0,
        )
        assert_matches_type(AnnotationListResponse, annotation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.annotations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = await response.parse()
        assert_matches_type(AnnotationListResponse, annotation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.annotations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = await response.parse()
            assert_matches_type(AnnotationListResponse, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True
