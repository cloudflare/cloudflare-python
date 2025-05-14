# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.browser_rendering import LinkCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        link = client.browser_rendering.links.create(
            account_id="account_id",
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        link = client.browser_rendering.links.create(
            account_id="account_id",
            cache_ttl=86400,
            action_timeout=300000,
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
            visible_links_only=True,
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.browser_rendering.links.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = response.parse()
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.browser_rendering.links.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = response.parse()
            assert_matches_type(LinkCreateResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.links.with_raw_response.create(
                account_id="",
            )


class TestAsyncLinks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        link = await async_client.browser_rendering.links.create(
            account_id="account_id",
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        link = await async_client.browser_rendering.links.create(
            account_id="account_id",
            cache_ttl=86400,
            action_timeout=300000,
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
            visible_links_only=True,
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.links.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        link = await response.parse()
        assert_matches_type(LinkCreateResponse, link, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.links.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            link = await response.parse()
            assert_matches_type(LinkCreateResponse, link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.links.with_raw_response.create(
                account_id="",
            )
