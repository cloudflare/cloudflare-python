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


class TestPDF:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        pdf = client.browser_rendering.pdf.create(
            account_id="account_id",
        )
        assert pdf.is_closed
        assert pdf.json() == {"foo": "bar"}
        assert cast(Any, pdf.is_closed) is True
        assert isinstance(pdf, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        pdf = client.browser_rendering.pdf.create(
            account_id="account_id",
            cache_ttl=86400,
            add_script_tag=[
                {
                    "id": "id",
                    "content": "content",
                    "type": "type",
                    "url": "url",
                }
            ],
            add_style_tag=[
                {
                    "content": "content",
                    "url": "url",
                }
            ],
            allow_request_pattern=["string"],
            allow_resource_types=["document"],
            authenticate={
                "password": "x",
                "username": "x",
            },
            best_attempt=True,
            cookies=[
                {
                    "name": "name",
                    "value": "value",
                    "domain": "domain",
                    "expires": 0,
                    "http_only": True,
                    "partition_key": "partitionKey",
                    "path": "path",
                    "priority": "Low",
                    "same_party": True,
                    "same_site": "Strict",
                    "secure": True,
                    "source_port": 0,
                    "source_scheme": "Unset",
                    "url": "url",
                }
            ],
            emulate_media_type="emulateMediaType",
            goto_options={
                "referer": "referer",
                "referrer_policy": "referrerPolicy",
                "timeout": 60000,
                "wait_until": "load",
            },
            html="x",
            reject_request_pattern=["string"],
            reject_resource_types=["document"],
            set_extra_http_headers={"foo": "string"},
            set_java_script_enabled=True,
            url="https://example.com",
            user_agent="userAgent",
            viewport={
                "height": 0,
                "width": 0,
                "device_scale_factor": 0,
                "has_touch": True,
                "is_landscape": True,
                "is_mobile": True,
            },
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert pdf.is_closed
        assert pdf.json() == {"foo": "bar"}
        assert cast(Any, pdf.is_closed) is True
        assert isinstance(pdf, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        pdf = client.browser_rendering.pdf.with_raw_response.create(
            account_id="account_id",
        )

        assert pdf.is_closed is True
        assert pdf.http_request.headers.get("X-Stainless-Lang") == "python"
        assert pdf.json() == {"foo": "bar"}
        assert isinstance(pdf, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.browser_rendering.pdf.with_streaming_response.create(
            account_id="account_id",
        ) as pdf:
            assert not pdf.is_closed
            assert pdf.http_request.headers.get("X-Stainless-Lang") == "python"

            assert pdf.json() == {"foo": "bar"}
            assert cast(Any, pdf.is_closed) is True
            assert isinstance(pdf, StreamedBinaryAPIResponse)

        assert cast(Any, pdf.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.pdf.with_raw_response.create(
                account_id="",
            )


class TestAsyncPDF:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        pdf = await async_client.browser_rendering.pdf.create(
            account_id="account_id",
        )
        assert pdf.is_closed
        assert await pdf.json() == {"foo": "bar"}
        assert cast(Any, pdf.is_closed) is True
        assert isinstance(pdf, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        pdf = await async_client.browser_rendering.pdf.create(
            account_id="account_id",
            cache_ttl=86400,
            add_script_tag=[
                {
                    "id": "id",
                    "content": "content",
                    "type": "type",
                    "url": "url",
                }
            ],
            add_style_tag=[
                {
                    "content": "content",
                    "url": "url",
                }
            ],
            allow_request_pattern=["string"],
            allow_resource_types=["document"],
            authenticate={
                "password": "x",
                "username": "x",
            },
            best_attempt=True,
            cookies=[
                {
                    "name": "name",
                    "value": "value",
                    "domain": "domain",
                    "expires": 0,
                    "http_only": True,
                    "partition_key": "partitionKey",
                    "path": "path",
                    "priority": "Low",
                    "same_party": True,
                    "same_site": "Strict",
                    "secure": True,
                    "source_port": 0,
                    "source_scheme": "Unset",
                    "url": "url",
                }
            ],
            emulate_media_type="emulateMediaType",
            goto_options={
                "referer": "referer",
                "referrer_policy": "referrerPolicy",
                "timeout": 60000,
                "wait_until": "load",
            },
            html="x",
            reject_request_pattern=["string"],
            reject_resource_types=["document"],
            set_extra_http_headers={"foo": "string"},
            set_java_script_enabled=True,
            url="https://example.com",
            user_agent="userAgent",
            viewport={
                "height": 0,
                "width": 0,
                "device_scale_factor": 0,
                "has_touch": True,
                "is_landscape": True,
                "is_mobile": True,
            },
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert pdf.is_closed
        assert await pdf.json() == {"foo": "bar"}
        assert cast(Any, pdf.is_closed) is True
        assert isinstance(pdf, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        pdf = await async_client.browser_rendering.pdf.with_raw_response.create(
            account_id="account_id",
        )

        assert pdf.is_closed is True
        assert pdf.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await pdf.json() == {"foo": "bar"}
        assert isinstance(pdf, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/account_id/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.browser_rendering.pdf.with_streaming_response.create(
            account_id="account_id",
        ) as pdf:
            assert not pdf.is_closed
            assert pdf.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await pdf.json() == {"foo": "bar"}
            assert cast(Any, pdf.is_closed) is True
            assert isinstance(pdf, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, pdf.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.pdf.with_raw_response.create(
                account_id="",
            )
