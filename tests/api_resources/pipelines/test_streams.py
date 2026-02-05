# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.pipelines import (
    StreamGetResponse,
    StreamListResponse,
    StreamCreateResponse,
    StreamUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStreams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        stream = client.pipelines.streams.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_stream",
        )
        assert_matches_type(StreamCreateResponse, stream, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        stream = client.pipelines.streams.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_stream",
            format={
                "type": "json",
                "decimal_encoding": "number",
                "timestamp_format": "rfc3339",
                "unstructured": True,
            },
            http={
                "authentication": False,
                "enabled": True,
                "cors": {"origins": ["string"]},
            },
            schema={
                "fields": [
                    {
                        "type": "int32",
                        "metadata_key": "metadata_key",
                        "name": "name",
                        "required": True,
                        "sql_name": "sql_name",
                    }
                ],
                "format": {
                    "type": "json",
                    "decimal_encoding": "number",
                    "timestamp_format": "rfc3339",
                    "unstructured": True,
                },
                "inferred": True,
            },
            worker_binding={"enabled": True},
        )
        assert_matches_type(StreamCreateResponse, stream, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.pipelines.streams.with_raw_response.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_stream",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(StreamCreateResponse, stream, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.pipelines.streams.with_streaming_response.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_stream",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(StreamCreateResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.streams.with_raw_response.create(
                account_id="",
                name="my_stream",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        stream = client.pipelines.streams.update(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StreamUpdateResponse, stream, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        stream = client.pipelines.streams.update(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            http={
                "authentication": False,
                "enabled": True,
                "cors": {"origins": ["string"]},
            },
            worker_binding={"enabled": True},
        )
        assert_matches_type(StreamUpdateResponse, stream, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.pipelines.streams.with_raw_response.update(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(StreamUpdateResponse, stream, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.pipelines.streams.with_streaming_response.update(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(StreamUpdateResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.streams.with_raw_response.update(
                stream_id="033e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stream_id` but received ''"):
            client.pipelines.streams.with_raw_response.update(
                stream_id="",
                account_id="0123105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        stream = client.pipelines.streams.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[StreamListResponse], stream, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        stream = client.pipelines.streams.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=0,
            pipeline_id="043e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[StreamListResponse], stream, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.pipelines.streams.with_raw_response.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[StreamListResponse], stream, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.pipelines.streams.with_streaming_response.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[StreamListResponse], stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.streams.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        stream = client.pipelines.streams.delete(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert stream is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        stream = client.pipelines.streams.delete(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            force="force",
        )
        assert stream is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.pipelines.streams.with_raw_response.delete(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert stream is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.pipelines.streams.with_streaming_response.delete(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert stream is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.streams.with_raw_response.delete(
                stream_id="033e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stream_id` but received ''"):
            client.pipelines.streams.with_raw_response.delete(
                stream_id="",
                account_id="0123105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        stream = client.pipelines.streams.get(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StreamGetResponse, stream, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.pipelines.streams.with_raw_response.get(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(StreamGetResponse, stream, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.pipelines.streams.with_streaming_response.get(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(StreamGetResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.streams.with_raw_response.get(
                stream_id="033e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stream_id` but received ''"):
            client.pipelines.streams.with_raw_response.get(
                stream_id="",
                account_id="0123105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncStreams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.pipelines.streams.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_stream",
        )
        assert_matches_type(StreamCreateResponse, stream, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.pipelines.streams.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_stream",
            format={
                "type": "json",
                "decimal_encoding": "number",
                "timestamp_format": "rfc3339",
                "unstructured": True,
            },
            http={
                "authentication": False,
                "enabled": True,
                "cors": {"origins": ["string"]},
            },
            schema={
                "fields": [
                    {
                        "type": "int32",
                        "metadata_key": "metadata_key",
                        "name": "name",
                        "required": True,
                        "sql_name": "sql_name",
                    }
                ],
                "format": {
                    "type": "json",
                    "decimal_encoding": "number",
                    "timestamp_format": "rfc3339",
                    "unstructured": True,
                },
                "inferred": True,
            },
            worker_binding={"enabled": True},
        )
        assert_matches_type(StreamCreateResponse, stream, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.streams.with_raw_response.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_stream",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(StreamCreateResponse, stream, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.streams.with_streaming_response.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_stream",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(StreamCreateResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.streams.with_raw_response.create(
                account_id="",
                name="my_stream",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.pipelines.streams.update(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StreamUpdateResponse, stream, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.pipelines.streams.update(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            http={
                "authentication": False,
                "enabled": True,
                "cors": {"origins": ["string"]},
            },
            worker_binding={"enabled": True},
        )
        assert_matches_type(StreamUpdateResponse, stream, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.streams.with_raw_response.update(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(StreamUpdateResponse, stream, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.streams.with_streaming_response.update(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(StreamUpdateResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.streams.with_raw_response.update(
                stream_id="033e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stream_id` but received ''"):
            await async_client.pipelines.streams.with_raw_response.update(
                stream_id="",
                account_id="0123105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.pipelines.streams.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[StreamListResponse], stream, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.pipelines.streams.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=0,
            pipeline_id="043e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[StreamListResponse], stream, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.streams.with_raw_response.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[StreamListResponse], stream, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.streams.with_streaming_response.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[StreamListResponse], stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.streams.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.pipelines.streams.delete(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert stream is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.pipelines.streams.delete(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            force="force",
        )
        assert stream is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.streams.with_raw_response.delete(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert stream is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.streams.with_streaming_response.delete(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert stream is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.streams.with_raw_response.delete(
                stream_id="033e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stream_id` but received ''"):
            await async_client.pipelines.streams.with_raw_response.delete(
                stream_id="",
                account_id="0123105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.pipelines.streams.get(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StreamGetResponse, stream, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.streams.with_raw_response.get(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(StreamGetResponse, stream, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.streams.with_streaming_response.get(
            stream_id="033e105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(StreamGetResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.streams.with_raw_response.get(
                stream_id="033e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stream_id` but received ''"):
            await async_client.pipelines.streams.with_raw_response.get(
                stream_id="",
                account_id="0123105f4ecef8ad9ca31a8372d0c353",
            )
