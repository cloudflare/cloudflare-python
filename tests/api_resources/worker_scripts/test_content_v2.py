# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast

from cloudflare._response import (
    BinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContentV2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/scripts/this-is_my_script-01/content/v2"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        content_v2 = client.worker_scripts.content_v2.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert content_v2.is_closed
        assert content_v2.json() == {"foo": "bar"}
        assert cast(Any, content_v2.is_closed) is True
        assert isinstance(content_v2, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/scripts/this-is_my_script-01/content/v2"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        content_v2 = client.worker_scripts.content_v2.with_raw_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert content_v2.is_closed is True
        assert content_v2.http_request.headers.get("X-Stainless-Lang") == "python"
        assert content_v2.json() == {"foo": "bar"}
        assert isinstance(content_v2, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/scripts/this-is_my_script-01/content/v2"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.worker_scripts.content_v2.with_streaming_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as content_v2:
            assert not content_v2.is_closed
            assert content_v2.http_request.headers.get("X-Stainless-Lang") == "python"

            assert content_v2.json() == {"foo": "bar"}
            assert cast(Any, content_v2.is_closed) is True
            assert isinstance(content_v2, StreamedBinaryAPIResponse)

        assert cast(Any, content_v2.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.worker_scripts.content_v2.with_raw_response.get(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.worker_scripts.content_v2.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncContentV2:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/scripts/this-is_my_script-01/content/v2"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        content_v2 = await async_client.worker_scripts.content_v2.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert content_v2.is_closed
        assert await content_v2.json() == {"foo": "bar"}
        assert cast(Any, content_v2.is_closed) is True
        assert isinstance(content_v2, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/scripts/this-is_my_script-01/content/v2"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        content_v2 = await async_client.worker_scripts.content_v2.with_raw_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert content_v2.is_closed is True
        assert content_v2.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await content_v2.json() == {"foo": "bar"}
        assert isinstance(content_v2, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/scripts/this-is_my_script-01/content/v2"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.worker_scripts.content_v2.with_streaming_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as content_v2:
            assert not content_v2.is_closed
            assert content_v2.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await content_v2.json() == {"foo": "bar"}
            assert cast(Any, content_v2.is_closed) is True
            assert isinstance(content_v2, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, content_v2.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.worker_scripts.content_v2.with_raw_response.get(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.worker_scripts.content_v2.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
