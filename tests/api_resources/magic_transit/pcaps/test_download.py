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


class TestDownload:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/pcaps/023e105f4ecef8ad9ca31a8372d0c353/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        download = client.magic_transit.pcaps.download.get(
            pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert download.is_closed
        assert download.json() == {"foo": "bar"}
        assert cast(Any, download.is_closed) is True
        assert isinstance(download, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/pcaps/023e105f4ecef8ad9ca31a8372d0c353/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        download = client.magic_transit.pcaps.download.with_raw_response.get(
            pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert download.is_closed is True
        assert download.http_request.headers.get("X-Stainless-Lang") == "python"
        assert download.json() == {"foo": "bar"}
        assert isinstance(download, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/pcaps/023e105f4ecef8ad9ca31a8372d0c353/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.magic_transit.pcaps.download.with_streaming_response.get(
            pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as download:
            assert not download.is_closed
            assert download.http_request.headers.get("X-Stainless-Lang") == "python"

            assert download.json() == {"foo": "bar"}
            assert cast(Any, download.is_closed) is True
            assert isinstance(download, StreamedBinaryAPIResponse)

        assert cast(Any, download.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.pcaps.download.with_raw_response.get(
                pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pcap_id` but received ''"):
            client.magic_transit.pcaps.download.with_raw_response.get(
                pcap_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncDownload:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/pcaps/023e105f4ecef8ad9ca31a8372d0c353/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        download = await async_client.magic_transit.pcaps.download.get(
            pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert download.is_closed
        assert await download.json() == {"foo": "bar"}
        assert cast(Any, download.is_closed) is True
        assert isinstance(download, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/pcaps/023e105f4ecef8ad9ca31a8372d0c353/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        download = await async_client.magic_transit.pcaps.download.with_raw_response.get(
            pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert download.is_closed is True
        assert download.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await download.json() == {"foo": "bar"}
        assert isinstance(download, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/pcaps/023e105f4ecef8ad9ca31a8372d0c353/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.magic_transit.pcaps.download.with_streaming_response.get(
            pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as download:
            assert not download.is_closed
            assert download.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await download.json() == {"foo": "bar"}
            assert cast(Any, download.is_closed) is True
            assert isinstance(download, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, download.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.pcaps.download.with_raw_response.get(
                pcap_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pcap_id` but received ''"):
            await async_client.magic_transit.pcaps.download.with_raw_response.get(
                pcap_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
