# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.logpush import (
    TransformerGetResponse,
    TransformerListResponse,
    TransformerCreateResponse,
    TransformerDeleteResponse,
    TransformerUpdateResponse,
    TransformerPreviewResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransformers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        transformer = client.logpush.transformers.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            code="SELECT ClientIP, RayID FROM http_requests",
            name="redact-pii",
        )
        assert_matches_type(Optional[TransformerCreateResponse], transformer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        transformer = client.logpush.transformers.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            code="SELECT ClientIP, RayID FROM http_requests",
            name="redact-pii",
            description="Redacts PII fields from HTTP request logs.",
        )
        assert_matches_type(Optional[TransformerCreateResponse], transformer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.logpush.transformers.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            code="SELECT ClientIP, RayID FROM http_requests",
            name="redact-pii",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transformer = response.parse()
        assert_matches_type(Optional[TransformerCreateResponse], transformer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.logpush.transformers.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            code="SELECT ClientIP, RayID FROM http_requests",
            name="redact-pii",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transformer = response.parse()
            assert_matches_type(Optional[TransformerCreateResponse], transformer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.transformers.with_raw_response.create(
                account_id="",
                code="SELECT ClientIP, RayID FROM http_requests",
                name="redact-pii",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        transformer = client.logpush.transformers.update(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="redact-pii",
        )
        assert_matches_type(Optional[TransformerUpdateResponse], transformer, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        transformer = client.logpush.transformers.update(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="redact-pii",
            code="SELECT ClientIP, RayID FROM http_requests",
            description="Redacts PII fields from HTTP request logs.",
        )
        assert_matches_type(Optional[TransformerUpdateResponse], transformer, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.logpush.transformers.with_raw_response.update(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="redact-pii",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transformer = response.parse()
        assert_matches_type(Optional[TransformerUpdateResponse], transformer, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.logpush.transformers.with_streaming_response.update(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="redact-pii",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transformer = response.parse()
            assert_matches_type(Optional[TransformerUpdateResponse], transformer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.transformers.with_raw_response.update(
                transformer_id=42,
                account_id="",
                name="redact-pii",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        transformer = client.logpush.transformers.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[TransformerListResponse], transformer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.logpush.transformers.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transformer = response.parse()
        assert_matches_type(SyncSinglePage[TransformerListResponse], transformer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.logpush.transformers.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transformer = response.parse()
            assert_matches_type(SyncSinglePage[TransformerListResponse], transformer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.transformers.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        transformer = client.logpush.transformers.delete(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TransformerDeleteResponse], transformer, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.logpush.transformers.with_raw_response.delete(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transformer = response.parse()
        assert_matches_type(Optional[TransformerDeleteResponse], transformer, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.logpush.transformers.with_streaming_response.delete(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transformer = response.parse()
            assert_matches_type(Optional[TransformerDeleteResponse], transformer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.transformers.with_raw_response.delete(
                transformer_id=42,
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        transformer = client.logpush.transformers.get(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TransformerGetResponse], transformer, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.logpush.transformers.with_raw_response.get(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transformer = response.parse()
        assert_matches_type(Optional[TransformerGetResponse], transformer, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.logpush.transformers.with_streaming_response.get(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transformer = response.parse()
            assert_matches_type(Optional[TransformerGetResponse], transformer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.transformers.with_raw_response.get(
                transformer_id=42,
                account_id="",
            )

    @parametrize
    def test_method_preview(self, client: Cloudflare) -> None:
        transformer = client.logpush.transformers.preview(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input={
                "ClientIP": "bar",
                "ClientRequestHost": "bar",
                "EdgeStartTimestamp": "bar",
                "RayID": "bar",
            },
            sql="SELECT ClientIP, RayID FROM http_requests",
        )
        assert_matches_type(SyncSinglePage[TransformerPreviewResponse], transformer, path=["response"])

    @parametrize
    def test_raw_response_preview(self, client: Cloudflare) -> None:
        response = client.logpush.transformers.with_raw_response.preview(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input={
                "ClientIP": "bar",
                "ClientRequestHost": "bar",
                "EdgeStartTimestamp": "bar",
                "RayID": "bar",
            },
            sql="SELECT ClientIP, RayID FROM http_requests",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transformer = response.parse()
        assert_matches_type(SyncSinglePage[TransformerPreviewResponse], transformer, path=["response"])

    @parametrize
    def test_streaming_response_preview(self, client: Cloudflare) -> None:
        with client.logpush.transformers.with_streaming_response.preview(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input={
                "ClientIP": "bar",
                "ClientRequestHost": "bar",
                "EdgeStartTimestamp": "bar",
                "RayID": "bar",
            },
            sql="SELECT ClientIP, RayID FROM http_requests",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transformer = response.parse()
            assert_matches_type(SyncSinglePage[TransformerPreviewResponse], transformer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_preview(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.transformers.with_raw_response.preview(
                account_id="",
                input={
                    "ClientIP": "bar",
                    "ClientRequestHost": "bar",
                    "EdgeStartTimestamp": "bar",
                    "RayID": "bar",
                },
                sql="SELECT ClientIP, RayID FROM http_requests",
            )


class TestAsyncTransformers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        transformer = await async_client.logpush.transformers.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            code="SELECT ClientIP, RayID FROM http_requests",
            name="redact-pii",
        )
        assert_matches_type(Optional[TransformerCreateResponse], transformer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        transformer = await async_client.logpush.transformers.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            code="SELECT ClientIP, RayID FROM http_requests",
            name="redact-pii",
            description="Redacts PII fields from HTTP request logs.",
        )
        assert_matches_type(Optional[TransformerCreateResponse], transformer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.transformers.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            code="SELECT ClientIP, RayID FROM http_requests",
            name="redact-pii",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transformer = await response.parse()
        assert_matches_type(Optional[TransformerCreateResponse], transformer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.transformers.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            code="SELECT ClientIP, RayID FROM http_requests",
            name="redact-pii",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transformer = await response.parse()
            assert_matches_type(Optional[TransformerCreateResponse], transformer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.transformers.with_raw_response.create(
                account_id="",
                code="SELECT ClientIP, RayID FROM http_requests",
                name="redact-pii",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        transformer = await async_client.logpush.transformers.update(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="redact-pii",
        )
        assert_matches_type(Optional[TransformerUpdateResponse], transformer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        transformer = await async_client.logpush.transformers.update(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="redact-pii",
            code="SELECT ClientIP, RayID FROM http_requests",
            description="Redacts PII fields from HTTP request logs.",
        )
        assert_matches_type(Optional[TransformerUpdateResponse], transformer, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.transformers.with_raw_response.update(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="redact-pii",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transformer = await response.parse()
        assert_matches_type(Optional[TransformerUpdateResponse], transformer, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.transformers.with_streaming_response.update(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="redact-pii",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transformer = await response.parse()
            assert_matches_type(Optional[TransformerUpdateResponse], transformer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.transformers.with_raw_response.update(
                transformer_id=42,
                account_id="",
                name="redact-pii",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        transformer = await async_client.logpush.transformers.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[TransformerListResponse], transformer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.transformers.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transformer = await response.parse()
        assert_matches_type(AsyncSinglePage[TransformerListResponse], transformer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.transformers.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transformer = await response.parse()
            assert_matches_type(AsyncSinglePage[TransformerListResponse], transformer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.transformers.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        transformer = await async_client.logpush.transformers.delete(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TransformerDeleteResponse], transformer, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.transformers.with_raw_response.delete(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transformer = await response.parse()
        assert_matches_type(Optional[TransformerDeleteResponse], transformer, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.transformers.with_streaming_response.delete(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transformer = await response.parse()
            assert_matches_type(Optional[TransformerDeleteResponse], transformer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.transformers.with_raw_response.delete(
                transformer_id=42,
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        transformer = await async_client.logpush.transformers.get(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TransformerGetResponse], transformer, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.transformers.with_raw_response.get(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transformer = await response.parse()
        assert_matches_type(Optional[TransformerGetResponse], transformer, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.transformers.with_streaming_response.get(
            transformer_id=42,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transformer = await response.parse()
            assert_matches_type(Optional[TransformerGetResponse], transformer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.transformers.with_raw_response.get(
                transformer_id=42,
                account_id="",
            )

    @parametrize
    async def test_method_preview(self, async_client: AsyncCloudflare) -> None:
        transformer = await async_client.logpush.transformers.preview(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input={
                "ClientIP": "bar",
                "ClientRequestHost": "bar",
                "EdgeStartTimestamp": "bar",
                "RayID": "bar",
            },
            sql="SELECT ClientIP, RayID FROM http_requests",
        )
        assert_matches_type(AsyncSinglePage[TransformerPreviewResponse], transformer, path=["response"])

    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.transformers.with_raw_response.preview(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input={
                "ClientIP": "bar",
                "ClientRequestHost": "bar",
                "EdgeStartTimestamp": "bar",
                "RayID": "bar",
            },
            sql="SELECT ClientIP, RayID FROM http_requests",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transformer = await response.parse()
        assert_matches_type(AsyncSinglePage[TransformerPreviewResponse], transformer, path=["response"])

    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.transformers.with_streaming_response.preview(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input={
                "ClientIP": "bar",
                "ClientRequestHost": "bar",
                "EdgeStartTimestamp": "bar",
                "RayID": "bar",
            },
            sql="SELECT ClientIP, RayID FROM http_requests",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transformer = await response.parse()
            assert_matches_type(AsyncSinglePage[TransformerPreviewResponse], transformer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_preview(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.transformers.with_raw_response.preview(
                account_id="",
                input={
                    "ClientIP": "bar",
                    "ClientRequestHost": "bar",
                    "EdgeStartTimestamp": "bar",
                    "RayID": "bar",
                },
                sql="SELECT ClientIP, RayID FROM http_requests",
            )
