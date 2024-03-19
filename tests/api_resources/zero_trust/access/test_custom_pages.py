# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.access import (
    AccessCustomPage,
    CustomPageListResponse,
    CustomPageDeleteResponse,
    AccessCustomPageWithoutHTML,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
        )
        assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
            app_count=0,
        )
        assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.custom_pages.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = response.parse()
        assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.custom_pages.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = response.parse()
            assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.create(
                "",
                custom_html="<html><body><h1>Access Denied</h1></body></html>",
                name="string",
                type="identity_denied",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
        )
        assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
            app_count=0,
        )
        assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.custom_pages.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = response.parse()
        assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.custom_pages.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = response.parse()
            assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                identifier="",
                custom_html="<html><body><h1>Access Denied</h1></body></html>",
                name="string",
                type="identity_denied",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.update(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                custom_html="<html><body><h1>Access Denied</h1></body></html>",
                name="string",
                type="identity_denied",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CustomPageListResponse], custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.custom_pages.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = response.parse()
        assert_matches_type(Optional[CustomPageListResponse], custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.custom_pages.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = response.parse()
            assert_matches_type(Optional[CustomPageListResponse], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomPageDeleteResponse, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.custom_pages.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = response.parse()
        assert_matches_type(CustomPageDeleteResponse, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.custom_pages.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = response.parse()
            assert_matches_type(CustomPageDeleteResponse, custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.delete(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AccessCustomPage, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.custom_pages.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = response.parse()
        assert_matches_type(AccessCustomPage, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.custom_pages.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = response.parse()
            assert_matches_type(AccessCustomPage, custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.get(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCustomPages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
        )
        assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
            app_count=0,
        )
        assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.custom_pages.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = await response.parse()
        assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.custom_pages.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = await response.parse()
            assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.create(
                "",
                custom_html="<html><body><h1>Access Denied</h1></body></html>",
                name="string",
                type="identity_denied",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
        )
        assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
            app_count=0,
        )
        assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.custom_pages.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = await response.parse()
        assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.custom_pages.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="string",
            type="identity_denied",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = await response.parse()
            assert_matches_type(AccessCustomPageWithoutHTML, custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                identifier="",
                custom_html="<html><body><h1>Access Denied</h1></body></html>",
                name="string",
                type="identity_denied",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.update(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                custom_html="<html><body><h1>Access Denied</h1></body></html>",
                name="string",
                type="identity_denied",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CustomPageListResponse], custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.custom_pages.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = await response.parse()
        assert_matches_type(Optional[CustomPageListResponse], custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.custom_pages.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = await response.parse()
            assert_matches_type(Optional[CustomPageListResponse], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomPageDeleteResponse, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.custom_pages.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = await response.parse()
        assert_matches_type(CustomPageDeleteResponse, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.custom_pages.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = await response.parse()
            assert_matches_type(CustomPageDeleteResponse, custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.delete(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AccessCustomPage, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.custom_pages.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = await response.parse()
        assert_matches_type(AccessCustomPage, custom_page, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.custom_pages.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = await response.parse()
            assert_matches_type(AccessCustomPage, custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.get(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
