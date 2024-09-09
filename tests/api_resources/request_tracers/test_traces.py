# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.request_tracers import TraceCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTraces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        trace = client.request_tracers.traces.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            method="PUT",
            url="https://some.zone/some_path",
        )
        assert_matches_type(Optional[TraceCreateResponse], trace, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        trace = client.request_tracers.traces.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            method="PUT",
            url="https://some.zone/some_path",
            body={
                "base64": "c29tZV9yZXF1ZXN0X2JvZHk=",
                "json": {},
                "plain_text": "plain_text",
            },
            context={
                "bot_score": 0,
                "geoloc": {
                    "city": "London",
                    "continent": "continent",
                    "is_eu_country": True,
                    "iso_code": "iso_code",
                    "latitude": 0,
                    "longitude": 0,
                    "postal_code": "postal_code",
                    "region_code": "region_code",
                    "subdivision_2_iso_code": "subdivision_2_iso_code",
                    "timezone": "timezone",
                },
                "skip_challenge": True,
                "threat_score": 0,
            },
            cookies={
                "cookie_name_1": "cookie_value_1",
                "cookie_name_2": "cookie_value_2",
            },
            headers={
                "header_name_1": "header_value_1",
                "header_name_2": "header_value_2",
            },
            protocol="HTTP/1.1",
            skip_response=True,
        )
        assert_matches_type(Optional[TraceCreateResponse], trace, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.request_tracers.traces.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            method="PUT",
            url="https://some.zone/some_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = response.parse()
        assert_matches_type(Optional[TraceCreateResponse], trace, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.request_tracers.traces.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            method="PUT",
            url="https://some.zone/some_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = response.parse()
            assert_matches_type(Optional[TraceCreateResponse], trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.request_tracers.traces.with_raw_response.create(
                account_id="",
                method="PUT",
                url="https://some.zone/some_path",
            )


class TestAsyncTraces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        trace = await async_client.request_tracers.traces.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            method="PUT",
            url="https://some.zone/some_path",
        )
        assert_matches_type(Optional[TraceCreateResponse], trace, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        trace = await async_client.request_tracers.traces.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            method="PUT",
            url="https://some.zone/some_path",
            body={
                "base64": "c29tZV9yZXF1ZXN0X2JvZHk=",
                "json": {},
                "plain_text": "plain_text",
            },
            context={
                "bot_score": 0,
                "geoloc": {
                    "city": "London",
                    "continent": "continent",
                    "is_eu_country": True,
                    "iso_code": "iso_code",
                    "latitude": 0,
                    "longitude": 0,
                    "postal_code": "postal_code",
                    "region_code": "region_code",
                    "subdivision_2_iso_code": "subdivision_2_iso_code",
                    "timezone": "timezone",
                },
                "skip_challenge": True,
                "threat_score": 0,
            },
            cookies={
                "cookie_name_1": "cookie_value_1",
                "cookie_name_2": "cookie_value_2",
            },
            headers={
                "header_name_1": "header_value_1",
                "header_name_2": "header_value_2",
            },
            protocol="HTTP/1.1",
            skip_response=True,
        )
        assert_matches_type(Optional[TraceCreateResponse], trace, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.request_tracers.traces.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            method="PUT",
            url="https://some.zone/some_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trace = await response.parse()
        assert_matches_type(Optional[TraceCreateResponse], trace, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.request_tracers.traces.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            method="PUT",
            url="https://some.zone/some_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trace = await response.parse()
            assert_matches_type(Optional[TraceCreateResponse], trace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.request_tracers.traces.with_raw_response.create(
                account_id="",
                method="PUT",
                url="https://some.zone/some_path",
            )
