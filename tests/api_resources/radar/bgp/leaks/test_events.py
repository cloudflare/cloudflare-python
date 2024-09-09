# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePagination, AsyncV4PagePagination
from cloudflare.types.radar.bgp.leaks import EventListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        event = client.radar.bgp.leaks.events.list()
        assert_matches_type(SyncV4PagePagination[EventListResponse], event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        event = client.radar.bgp.leaks.events.list(
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_range="7d",
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            event_id=0,
            format="JSON",
            involved_asn=0,
            involved_country="involvedCountry",
            leak_asn=0,
            page=0,
            per_page=0,
            sort_by="ID",
            sort_order="ASC",
        )
        assert_matches_type(SyncV4PagePagination[EventListResponse], event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.bgp.leaks.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncV4PagePagination[EventListResponse], event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.bgp.leaks.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncV4PagePagination[EventListResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.radar.bgp.leaks.events.list()
        assert_matches_type(AsyncV4PagePagination[EventListResponse], event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.radar.bgp.leaks.events.list(
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_range="7d",
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            event_id=0,
            format="JSON",
            involved_asn=0,
            involved_country="involvedCountry",
            leak_asn=0,
            page=0,
            per_page=0,
            sort_by="ID",
            sort_order="ASC",
        )
        assert_matches_type(AsyncV4PagePagination[EventListResponse], event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.leaks.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(AsyncV4PagePagination[EventListResponse], event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.leaks.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncV4PagePagination[EventListResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True
