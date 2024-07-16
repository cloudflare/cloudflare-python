# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from cloudflare import Cloudflare, AsyncCloudflare
from cloudflare._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/zones/023e105f4ecef8ad9ca31a8372d0c353/snippets/snippet_name_01/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        content = client.snippets.content.get(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert content.is_closed
        assert content.json() == {"foo": "bar"}
        assert cast(Any, content.is_closed) is True
        assert isinstance(content, BinaryAPIResponse)

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/zones/023e105f4ecef8ad9ca31a8372d0c353/snippets/snippet_name_01/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        content = client.snippets.content.with_raw_response.get(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert content.is_closed is True
        assert content.http_request.headers.get("X-Stainless-Lang") == "python"
        assert content.json() == {"foo": "bar"}
        assert isinstance(content, BinaryAPIResponse)

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/zones/023e105f4ecef8ad9ca31a8372d0c353/snippets/snippet_name_01/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.snippets.content.with_streaming_response.get(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as content:
            assert not content.is_closed
            assert content.http_request.headers.get("X-Stainless-Lang") == "python"

            assert content.json() == {"foo": "bar"}
            assert cast(Any, content.is_closed) is True
            assert isinstance(content, StreamedBinaryAPIResponse)

        assert cast(Any, content.is_closed) is True

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.snippets.content.with_raw_response.get(
                snippet_name="snippet_name_01",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            client.snippets.content.with_raw_response.get(
                snippet_name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncContent:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/zones/023e105f4ecef8ad9ca31a8372d0c353/snippets/snippet_name_01/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        content = await async_client.snippets.content.get(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert content.is_closed
        assert await content.json() == {"foo": "bar"}
        assert cast(Any, content.is_closed) is True
        assert isinstance(content, AsyncBinaryAPIResponse)

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/zones/023e105f4ecef8ad9ca31a8372d0c353/snippets/snippet_name_01/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        content = await async_client.snippets.content.with_raw_response.get(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert content.is_closed is True
        assert content.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await content.json() == {"foo": "bar"}
        assert isinstance(content, AsyncBinaryAPIResponse)

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/zones/023e105f4ecef8ad9ca31a8372d0c353/snippets/snippet_name_01/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.snippets.content.with_streaming_response.get(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as content:
            assert not content.is_closed
            assert content.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await content.json() == {"foo": "bar"}
            assert cast(Any, content.is_closed) is True
            assert isinstance(content, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, content.is_closed) is True

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.snippets.content.with_raw_response.get(
                snippet_name="snippet_name_01",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            await async_client.snippets.content.with_raw_response.get(
                snippet_name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
