# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events import IndicatorTypeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndicatorTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        indicator_type = client.cloudforce_one.threat_events.indicator_types.list(
            account_id=0,
        )
        assert_matches_type(IndicatorTypeListResponse, indicator_type, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.indicator_types.with_raw_response.list(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_type = response.parse()
        assert_matches_type(IndicatorTypeListResponse, indicator_type, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.indicator_types.with_streaming_response.list(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_type = response.parse()
            assert_matches_type(IndicatorTypeListResponse, indicator_type, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIndicatorTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        indicator_type = await async_client.cloudforce_one.threat_events.indicator_types.list(
            account_id=0,
        )
        assert_matches_type(IndicatorTypeListResponse, indicator_type, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.indicator_types.with_raw_response.list(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_type = await response.parse()
        assert_matches_type(IndicatorTypeListResponse, indicator_type, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.indicator_types.with_streaming_response.list(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_type = await response.parse()
            assert_matches_type(IndicatorTypeListResponse, indicator_type, path=["response"])

        assert cast(Any, response.is_closed) is True
