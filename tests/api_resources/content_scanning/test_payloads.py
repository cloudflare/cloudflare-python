# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.content_scanning import (
    PayloadListResponse,
    PayloadCreateResponse,
    PayloadDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayloads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        payload = client.content_scanning.payloads.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"payload": 'lookup_json_string(http.request.body.raw, "file")'}],
        )
        assert_matches_type(Optional[PayloadCreateResponse], payload, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.content_scanning.payloads.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"payload": 'lookup_json_string(http.request.body.raw, "file")'}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload = response.parse()
        assert_matches_type(Optional[PayloadCreateResponse], payload, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.content_scanning.payloads.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"payload": 'lookup_json_string(http.request.body.raw, "file")'}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload = response.parse()
            assert_matches_type(Optional[PayloadCreateResponse], payload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.content_scanning.payloads.with_raw_response.create(
                zone_id="",
                body=[{"payload": 'lookup_json_string(http.request.body.raw, "file")'}],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        payload = client.content_scanning.payloads.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[PayloadListResponse], payload, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.content_scanning.payloads.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload = response.parse()
        assert_matches_type(SyncSinglePage[PayloadListResponse], payload, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.content_scanning.payloads.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload = response.parse()
            assert_matches_type(SyncSinglePage[PayloadListResponse], payload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.content_scanning.payloads.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        payload = client.content_scanning.payloads.delete(
            expression_id="a350a054caa840c9becd89c3b4f0195b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PayloadDeleteResponse], payload, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.content_scanning.payloads.with_raw_response.delete(
            expression_id="a350a054caa840c9becd89c3b4f0195b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload = response.parse()
        assert_matches_type(Optional[PayloadDeleteResponse], payload, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.content_scanning.payloads.with_streaming_response.delete(
            expression_id="a350a054caa840c9becd89c3b4f0195b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload = response.parse()
            assert_matches_type(Optional[PayloadDeleteResponse], payload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.content_scanning.payloads.with_raw_response.delete(
                expression_id="a350a054caa840c9becd89c3b4f0195b",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expression_id` but received ''"):
            client.content_scanning.payloads.with_raw_response.delete(
                expression_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPayloads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        payload = await async_client.content_scanning.payloads.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"payload": 'lookup_json_string(http.request.body.raw, "file")'}],
        )
        assert_matches_type(Optional[PayloadCreateResponse], payload, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.content_scanning.payloads.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"payload": 'lookup_json_string(http.request.body.raw, "file")'}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload = await response.parse()
        assert_matches_type(Optional[PayloadCreateResponse], payload, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.content_scanning.payloads.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"payload": 'lookup_json_string(http.request.body.raw, "file")'}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload = await response.parse()
            assert_matches_type(Optional[PayloadCreateResponse], payload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.content_scanning.payloads.with_raw_response.create(
                zone_id="",
                body=[{"payload": 'lookup_json_string(http.request.body.raw, "file")'}],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        payload = await async_client.content_scanning.payloads.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[PayloadListResponse], payload, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.content_scanning.payloads.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload = await response.parse()
        assert_matches_type(AsyncSinglePage[PayloadListResponse], payload, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.content_scanning.payloads.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload = await response.parse()
            assert_matches_type(AsyncSinglePage[PayloadListResponse], payload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.content_scanning.payloads.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        payload = await async_client.content_scanning.payloads.delete(
            expression_id="a350a054caa840c9becd89c3b4f0195b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PayloadDeleteResponse], payload, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.content_scanning.payloads.with_raw_response.delete(
            expression_id="a350a054caa840c9becd89c3b4f0195b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payload = await response.parse()
        assert_matches_type(Optional[PayloadDeleteResponse], payload, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.content_scanning.payloads.with_streaming_response.delete(
            expression_id="a350a054caa840c9becd89c3b4f0195b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payload = await response.parse()
            assert_matches_type(Optional[PayloadDeleteResponse], payload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.content_scanning.payloads.with_raw_response.delete(
                expression_id="a350a054caa840c9becd89c3b4f0195b",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expression_id` but received ''"):
            await async_client.content_scanning.payloads.with_raw_response.delete(
                expression_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
