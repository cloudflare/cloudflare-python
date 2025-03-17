# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events import CountryListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCountries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        country = client.cloudforce_one.threat_events.countries.list(
            account_id=0,
        )
        assert_matches_type(CountryListResponse, country, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.countries.with_raw_response.list(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryListResponse, country, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.countries.with_streaming_response.list(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryListResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCountries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        country = await async_client.cloudforce_one.threat_events.countries.list(
            account_id=0,
        )
        assert_matches_type(CountryListResponse, country, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.countries.with_raw_response.list(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryListResponse, country, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.countries.with_streaming_response.list(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryListResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True
