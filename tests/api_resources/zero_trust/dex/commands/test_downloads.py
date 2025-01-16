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


class TestDownloads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/01a7362d577a6c3019a474fd6f485823/dex/commands/5758fefe-ae7e-4538-a39b-1fef6abcb909/downloads/filename"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        download = client.zero_trust.dex.commands.downloads.get(
            filename="filename",
            account_id="01a7362d577a6c3019a474fd6f485823",
            command_id="5758fefe-ae7e-4538-a39b-1fef6abcb909",
        )
        assert download.is_closed
        assert download.json() == {"foo": "bar"}
        assert cast(Any, download.is_closed) is True
        assert isinstance(download, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/01a7362d577a6c3019a474fd6f485823/dex/commands/5758fefe-ae7e-4538-a39b-1fef6abcb909/downloads/filename"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        download = client.zero_trust.dex.commands.downloads.with_raw_response.get(
            filename="filename",
            account_id="01a7362d577a6c3019a474fd6f485823",
            command_id="5758fefe-ae7e-4538-a39b-1fef6abcb909",
        )

        assert download.is_closed is True
        assert download.http_request.headers.get("X-Stainless-Lang") == "python"
        assert download.json() == {"foo": "bar"}
        assert isinstance(download, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/01a7362d577a6c3019a474fd6f485823/dex/commands/5758fefe-ae7e-4538-a39b-1fef6abcb909/downloads/filename"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.zero_trust.dex.commands.downloads.with_streaming_response.get(
            filename="filename",
            account_id="01a7362d577a6c3019a474fd6f485823",
            command_id="5758fefe-ae7e-4538-a39b-1fef6abcb909",
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
            client.zero_trust.dex.commands.downloads.with_raw_response.get(
                filename="filename",
                account_id="",
                command_id="5758fefe-ae7e-4538-a39b-1fef6abcb909",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `command_id` but received ''"):
            client.zero_trust.dex.commands.downloads.with_raw_response.get(
                filename="filename",
                account_id="01a7362d577a6c3019a474fd6f485823",
                command_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            client.zero_trust.dex.commands.downloads.with_raw_response.get(
                filename="",
                account_id="01a7362d577a6c3019a474fd6f485823",
                command_id="5758fefe-ae7e-4538-a39b-1fef6abcb909",
            )


class TestAsyncDownloads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/01a7362d577a6c3019a474fd6f485823/dex/commands/5758fefe-ae7e-4538-a39b-1fef6abcb909/downloads/filename"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        download = await async_client.zero_trust.dex.commands.downloads.get(
            filename="filename",
            account_id="01a7362d577a6c3019a474fd6f485823",
            command_id="5758fefe-ae7e-4538-a39b-1fef6abcb909",
        )
        assert download.is_closed
        assert await download.json() == {"foo": "bar"}
        assert cast(Any, download.is_closed) is True
        assert isinstance(download, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/01a7362d577a6c3019a474fd6f485823/dex/commands/5758fefe-ae7e-4538-a39b-1fef6abcb909/downloads/filename"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        download = await async_client.zero_trust.dex.commands.downloads.with_raw_response.get(
            filename="filename",
            account_id="01a7362d577a6c3019a474fd6f485823",
            command_id="5758fefe-ae7e-4538-a39b-1fef6abcb909",
        )

        assert download.is_closed is True
        assert download.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await download.json() == {"foo": "bar"}
        assert isinstance(download, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/01a7362d577a6c3019a474fd6f485823/dex/commands/5758fefe-ae7e-4538-a39b-1fef6abcb909/downloads/filename"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.zero_trust.dex.commands.downloads.with_streaming_response.get(
            filename="filename",
            account_id="01a7362d577a6c3019a474fd6f485823",
            command_id="5758fefe-ae7e-4538-a39b-1fef6abcb909",
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
            await async_client.zero_trust.dex.commands.downloads.with_raw_response.get(
                filename="filename",
                account_id="",
                command_id="5758fefe-ae7e-4538-a39b-1fef6abcb909",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `command_id` but received ''"):
            await async_client.zero_trust.dex.commands.downloads.with_raw_response.get(
                filename="filename",
                account_id="01a7362d577a6c3019a474fd6f485823",
                command_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            await async_client.zero_trust.dex.commands.downloads.with_raw_response.get(
                filename="",
                account_id="01a7362d577a6c3019a474fd6f485823",
                command_id="5758fefe-ae7e-4538-a39b-1fef6abcb909",
            )
