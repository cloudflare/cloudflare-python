# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.radar.bgp import HijackEventsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.bgp import hijack_events_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHijacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_events(self, client: Cloudflare) -> None:
        hijack = client.radar.bgp.hijacks.events()
        assert_matches_type(HijackEventsResponse, hijack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_events_with_all_params(self, client: Cloudflare) -> None:
        hijack = client.radar.bgp.hijacks.events(
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_range="7d",
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            event_id=0,
            format="JSON",
            hijacker_asn=0,
            involved_asn=0,
            involved_country="string",
            max_confidence=0,
            min_confidence=0,
            page=0,
            per_page=0,
            prefix="string",
            sort_by="TIME",
            sort_order="DESC",
            victim_asn=0,
        )
        assert_matches_type(HijackEventsResponse, hijack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_events(self, client: Cloudflare) -> None:
        response = client.radar.bgp.hijacks.with_raw_response.events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hijack = response.parse()
        assert_matches_type(HijackEventsResponse, hijack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_events(self, client: Cloudflare) -> None:
        with client.radar.bgp.hijacks.with_streaming_response.events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hijack = response.parse()
            assert_matches_type(HijackEventsResponse, hijack, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHijacks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_events(self, async_client: AsyncCloudflare) -> None:
        hijack = await async_client.radar.bgp.hijacks.events()
        assert_matches_type(HijackEventsResponse, hijack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_events_with_all_params(self, async_client: AsyncCloudflare) -> None:
        hijack = await async_client.radar.bgp.hijacks.events(
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_range="7d",
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            event_id=0,
            format="JSON",
            hijacker_asn=0,
            involved_asn=0,
            involved_country="string",
            max_confidence=0,
            min_confidence=0,
            page=0,
            per_page=0,
            prefix="string",
            sort_by="TIME",
            sort_order="DESC",
            victim_asn=0,
        )
        assert_matches_type(HijackEventsResponse, hijack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_events(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.hijacks.with_raw_response.events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hijack = await response.parse()
        assert_matches_type(HijackEventsResponse, hijack, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_events(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.hijacks.with_streaming_response.events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hijack = await response.parse()
            assert_matches_type(HijackEventsResponse, hijack, path=["response"])

        assert cast(Any, response.is_closed) is True
