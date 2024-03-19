# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.bgp import LeakEventsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLeaks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_events(self, client: Cloudflare) -> None:
        leak = client.radar.bgp.leaks.events()
        assert_matches_type(LeakEventsResponse, leak, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_events_with_all_params(self, client: Cloudflare) -> None:
        leak = client.radar.bgp.leaks.events(
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_range="7d",
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            event_id=0,
            format="JSON",
            involved_asn=0,
            involved_country="string",
            leak_asn=0,
            page=0,
            per_page=0,
            sort_by="TIME",
            sort_order="DESC",
        )
        assert_matches_type(LeakEventsResponse, leak, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_events(self, client: Cloudflare) -> None:
        response = client.radar.bgp.leaks.with_raw_response.events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        leak = response.parse()
        assert_matches_type(LeakEventsResponse, leak, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_events(self, client: Cloudflare) -> None:
        with client.radar.bgp.leaks.with_streaming_response.events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            leak = response.parse()
            assert_matches_type(LeakEventsResponse, leak, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLeaks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_events(self, async_client: AsyncCloudflare) -> None:
        leak = await async_client.radar.bgp.leaks.events()
        assert_matches_type(LeakEventsResponse, leak, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_events_with_all_params(self, async_client: AsyncCloudflare) -> None:
        leak = await async_client.radar.bgp.leaks.events(
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_range="7d",
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            event_id=0,
            format="JSON",
            involved_asn=0,
            involved_country="string",
            leak_asn=0,
            page=0,
            per_page=0,
            sort_by="TIME",
            sort_order="DESC",
        )
        assert_matches_type(LeakEventsResponse, leak, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_events(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.leaks.with_raw_response.events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        leak = await response.parse()
        assert_matches_type(LeakEventsResponse, leak, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_events(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.leaks.with_streaming_response.events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            leak = await response.parse()
            assert_matches_type(LeakEventsResponse, leak, path=["response"])

        assert cast(Any, response.is_closed) is True
