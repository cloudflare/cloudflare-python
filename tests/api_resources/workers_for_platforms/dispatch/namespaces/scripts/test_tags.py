# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import (
    TagListResponse,
    TagUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        tag = client.workers_for_platforms.dispatch.namespaces.scripts.tags.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            body=["my-tag"],
        )
        assert_matches_type(SyncSinglePage[TagUpdateResponse], tag, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            body=["my-tag"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(SyncSinglePage[TagUpdateResponse], tag, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_streaming_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            body=["my-tag"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(SyncSinglePage[TagUpdateResponse], tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.update(
                script_name="this-is_my_script-01",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
                body=["my-tag"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.update(
                script_name="this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
                body=["my-tag"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.update(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
                body=["my-tag"],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        tag = client.workers_for_platforms.dispatch.namespaces.scripts.tags.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert_matches_type(SyncSinglePage[TagListResponse], tag, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(SyncSinglePage[TagListResponse], tag, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_streaming_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(SyncSinglePage[TagListResponse], tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.list(
                script_name="this-is_my_script-01",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.list(
                script_name="this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.list(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        tag = client.workers_for_platforms.dispatch.namespaces.scripts.tags.delete(
            tag="my-tag",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.delete(
            tag="my-tag",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_streaming_response.delete(
            tag="my-tag",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(object, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.delete(
                tag="my-tag",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.delete(
                tag="my-tag",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.delete(
                tag="my-tag",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.delete(
                tag="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
                script_name="this-is_my_script-01",
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            body=["my-tag"],
        )
        assert_matches_type(AsyncSinglePage[TagUpdateResponse], tag, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            body=["my-tag"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(AsyncSinglePage[TagUpdateResponse], tag, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_streaming_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            body=["my-tag"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(AsyncSinglePage[TagUpdateResponse], tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.update(
                script_name="this-is_my_script-01",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
                body=["my-tag"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.update(
                script_name="this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
                body=["my-tag"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.update(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
                body=["my-tag"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert_matches_type(AsyncSinglePage[TagListResponse], tag, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(AsyncSinglePage[TagListResponse], tag, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_streaming_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(AsyncSinglePage[TagListResponse], tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.list(
                script_name="this-is_my_script-01",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.list(
                script_name="this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.list(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        tag = await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.delete(
            tag="my-tag",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.delete(
            tag="my-tag",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(object, tag, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_streaming_response.delete(
            tag="my-tag",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(object, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.delete(
                tag="my-tag",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.delete(
                tag="my-tag",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.delete(
                tag="my-tag",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.tags.with_raw_response.delete(
                tag="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
                script_name="this-is_my_script-01",
            )
