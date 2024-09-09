# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.access import (
    CustomPage,
    CustomPageWithoutHTML,
    CustomPageDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
        )
        assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
            app_count=0,
        )
        assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.custom_pages.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = response.parse()
        assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.custom_pages.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = response.parse()
            assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.create(
                account_id="",
                custom_html="<html><body><h1>Access Denied</h1></body></html>",
                name="name",
                type="identity_denied",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.update(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
        )
        assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.update(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
            app_count=0,
        )
        assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.custom_pages.with_raw_response.update(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = response.parse()
        assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.custom_pages.with_streaming_response.update(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = response.parse()
            assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.update(
                custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                custom_html="<html><body><h1>Access Denied</h1></body></html>",
                name="name",
                type="identity_denied",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_page_id` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.update(
                custom_page_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_html="<html><body><h1>Access Denied</h1></body></html>",
                name="name",
                type="identity_denied",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.custom_pages.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = response.parse()
        assert_matches_type(SyncSinglePage[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.custom_pages.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = response.parse()
            assert_matches_type(SyncSinglePage[CustomPageWithoutHTML], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.delete(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CustomPageDeleteResponse], custom_page, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.custom_pages.with_raw_response.delete(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = response.parse()
        assert_matches_type(Optional[CustomPageDeleteResponse], custom_page, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.custom_pages.with_streaming_response.delete(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = response.parse()
            assert_matches_type(Optional[CustomPageDeleteResponse], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.delete(
                custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_page_id` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.delete(
                custom_page_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        custom_page = client.zero_trust.access.custom_pages.get(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CustomPage], custom_page, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.custom_pages.with_raw_response.get(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = response.parse()
        assert_matches_type(Optional[CustomPage], custom_page, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.custom_pages.with_streaming_response.get(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = response.parse()
            assert_matches_type(Optional[CustomPage], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.get(
                custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_page_id` but received ''"):
            client.zero_trust.access.custom_pages.with_raw_response.get(
                custom_page_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCustomPages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
        )
        assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
            app_count=0,
        )
        assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.custom_pages.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = await response.parse()
        assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.custom_pages.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = await response.parse()
            assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.create(
                account_id="",
                custom_html="<html><body><h1>Access Denied</h1></body></html>",
                name="name",
                type="identity_denied",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.update(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
        )
        assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.update(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
            app_count=0,
        )
        assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.custom_pages.with_raw_response.update(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = await response.parse()
        assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.custom_pages.with_streaming_response.update(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_html="<html><body><h1>Access Denied</h1></body></html>",
            name="name",
            type="identity_denied",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = await response.parse()
            assert_matches_type(Optional[CustomPageWithoutHTML], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.update(
                custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                custom_html="<html><body><h1>Access Denied</h1></body></html>",
                name="name",
                type="identity_denied",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_page_id` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.update(
                custom_page_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_html="<html><body><h1>Access Denied</h1></body></html>",
                name="name",
                type="identity_denied",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.custom_pages.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = await response.parse()
        assert_matches_type(AsyncSinglePage[CustomPageWithoutHTML], custom_page, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.custom_pages.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = await response.parse()
            assert_matches_type(AsyncSinglePage[CustomPageWithoutHTML], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.delete(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CustomPageDeleteResponse], custom_page, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.custom_pages.with_raw_response.delete(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = await response.parse()
        assert_matches_type(Optional[CustomPageDeleteResponse], custom_page, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.custom_pages.with_streaming_response.delete(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = await response.parse()
            assert_matches_type(Optional[CustomPageDeleteResponse], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.delete(
                custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_page_id` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.delete(
                custom_page_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        custom_page = await async_client.zero_trust.access.custom_pages.get(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CustomPage], custom_page, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.custom_pages.with_raw_response.get(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_page = await response.parse()
        assert_matches_type(Optional[CustomPage], custom_page, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.custom_pages.with_streaming_response.get(
            custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_page = await response.parse()
            assert_matches_type(Optional[CustomPage], custom_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.get(
                custom_page_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_page_id` but received ''"):
            await async_client.zero_trust.access.custom_pages.with_raw_response.get(
                custom_page_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
