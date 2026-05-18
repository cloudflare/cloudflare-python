# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination
from cloudflare.types.r2.buckets import (
    ObjectListResponse,
    ObjectDeleteResponse,
    ObjectUploadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        object_ = client.r2.buckets.objects.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncCursorPagination[ObjectListResponse], object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        object_ = client.r2.buckets.objects.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="cursor",
            delimiter="delimiter",
            per_page=1,
            prefix="prefix",
            start_after="start_after",
            jurisdiction="default",
        )
        assert_matches_type(SyncCursorPagination[ObjectListResponse], object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.r2.buckets.objects.with_raw_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(SyncCursorPagination[ObjectListResponse], object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.r2.buckets.objects.with_streaming_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(SyncCursorPagination[ObjectListResponse], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.objects.with_raw_response.list(
                bucket_name="example-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.objects.with_raw_response.list(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        object_ = client.r2.buckets.objects.delete(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        object_ = client.r2.buckets.objects.delete(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            jurisdiction="default",
        )
        assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.r2.buckets.objects.with_raw_response.delete(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.r2.buckets.objects.with_streaming_response.delete(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.objects.with_raw_response.delete(
                object_key="path/to/my-object.txt",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.objects.with_raw_response.delete(
                object_key="path/to/my-object.txt",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_key` but received ''"):
            client.r2.buckets.objects.with_raw_response.delete(
                object_key="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/r2/buckets/example-bucket/objects/path/to/my-object.txt"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        object_ = client.r2.buckets.objects.get(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert object_.is_closed
        assert object_.json() == {"foo": "bar"}
        assert cast(Any, object_.is_closed) is True
        assert isinstance(object_, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_with_all_params(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/r2/buckets/example-bucket/objects/path/to/my-object.txt"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        object_ = client.r2.buckets.objects.get(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            jurisdiction="default",
            if_modified_since="If-Modified-Since",
            if_none_match="If-None-Match",
        )
        assert object_.is_closed
        assert object_.json() == {"foo": "bar"}
        assert cast(Any, object_.is_closed) is True
        assert isinstance(object_, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/r2/buckets/example-bucket/objects/path/to/my-object.txt"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        object_ = client.r2.buckets.objects.with_raw_response.get(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert object_.is_closed is True
        assert object_.http_request.headers.get("X-Stainless-Lang") == "python"
        assert object_.json() == {"foo": "bar"}
        assert isinstance(object_, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/r2/buckets/example-bucket/objects/path/to/my-object.txt"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.r2.buckets.objects.with_streaming_response.get(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as object_:
            assert not object_.is_closed
            assert object_.http_request.headers.get("X-Stainless-Lang") == "python"

            assert object_.json() == {"foo": "bar"}
            assert cast(Any, object_.is_closed) is True
            assert isinstance(object_, StreamedBinaryAPIResponse)

        assert cast(Any, object_.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.objects.with_raw_response.get(
                object_key="path/to/my-object.txt",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.objects.with_raw_response.get(
                object_key="path/to/my-object.txt",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_key` but received ''"):
            client.r2.buckets.objects.with_raw_response.get(
                object_key="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_upload(self, client: Cloudflare) -> None:
        object_ = client.r2.buckets.objects.upload(
            object_key="path/to/my-object.txt",
            body=b"Example data",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(ObjectUploadResponse, object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_upload_with_all_params(self, client: Cloudflare) -> None:
        object_ = client.r2.buckets.objects.upload(
            object_key="path/to/my-object.txt",
            body=b"Example data",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            jurisdiction="default",
            cf_r2_storage_class="Standard",
        )
        assert_matches_type(ObjectUploadResponse, object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_upload(self, client: Cloudflare) -> None:
        response = client.r2.buckets.objects.with_raw_response.upload(
            object_key="path/to/my-object.txt",
            body=b"Example data",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectUploadResponse, object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_upload(self, client: Cloudflare) -> None:
        with client.r2.buckets.objects.with_streaming_response.upload(
            object_key="path/to/my-object.txt",
            body=b"Example data",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectUploadResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_upload(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.objects.with_raw_response.upload(
                object_key="path/to/my-object.txt",
                body=b"Example data",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.objects.with_raw_response.upload(
                object_key="path/to/my-object.txt",
                body=b"Example data",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_key` but received ''"):
            client.r2.buckets.objects.with_raw_response.upload(
                object_key="",
                body=b"Example data",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )


class TestAsyncObjects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        object_ = await async_client.r2.buckets.objects.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncCursorPagination[ObjectListResponse], object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        object_ = await async_client.r2.buckets.objects.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="cursor",
            delimiter="delimiter",
            per_page=1,
            prefix="prefix",
            start_after="start_after",
            jurisdiction="default",
        )
        assert_matches_type(AsyncCursorPagination[ObjectListResponse], object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.objects.with_raw_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(AsyncCursorPagination[ObjectListResponse], object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.objects.with_streaming_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(AsyncCursorPagination[ObjectListResponse], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.objects.with_raw_response.list(
                bucket_name="example-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.objects.with_raw_response.list(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        object_ = await async_client.r2.buckets.objects.delete(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        object_ = await async_client.r2.buckets.objects.delete(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            jurisdiction="default",
        )
        assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.objects.with_raw_response.delete(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.objects.with_streaming_response.delete(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectDeleteResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.objects.with_raw_response.delete(
                object_key="path/to/my-object.txt",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.objects.with_raw_response.delete(
                object_key="path/to/my-object.txt",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_key` but received ''"):
            await async_client.r2.buckets.objects.with_raw_response.delete(
                object_key="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/r2/buckets/example-bucket/objects/path/to/my-object.txt"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        object_ = await async_client.r2.buckets.objects.get(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert object_.is_closed
        assert await object_.json() == {"foo": "bar"}
        assert cast(Any, object_.is_closed) is True
        assert isinstance(object_, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/r2/buckets/example-bucket/objects/path/to/my-object.txt"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        object_ = await async_client.r2.buckets.objects.get(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            jurisdiction="default",
            if_modified_since="If-Modified-Since",
            if_none_match="If-None-Match",
        )
        assert object_.is_closed
        assert await object_.json() == {"foo": "bar"}
        assert cast(Any, object_.is_closed) is True
        assert isinstance(object_, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/r2/buckets/example-bucket/objects/path/to/my-object.txt"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        object_ = await async_client.r2.buckets.objects.with_raw_response.get(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert object_.is_closed is True
        assert object_.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await object_.json() == {"foo": "bar"}
        assert isinstance(object_, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/r2/buckets/example-bucket/objects/path/to/my-object.txt"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.r2.buckets.objects.with_streaming_response.get(
            object_key="path/to/my-object.txt",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as object_:
            assert not object_.is_closed
            assert object_.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await object_.json() == {"foo": "bar"}
            assert cast(Any, object_.is_closed) is True
            assert isinstance(object_, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, object_.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.objects.with_raw_response.get(
                object_key="path/to/my-object.txt",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.objects.with_raw_response.get(
                object_key="path/to/my-object.txt",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_key` but received ''"):
            await async_client.r2.buckets.objects.with_raw_response.get(
                object_key="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_upload(self, async_client: AsyncCloudflare) -> None:
        object_ = await async_client.r2.buckets.objects.upload(
            object_key="path/to/my-object.txt",
            body=b"Example data",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(ObjectUploadResponse, object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncCloudflare) -> None:
        object_ = await async_client.r2.buckets.objects.upload(
            object_key="path/to/my-object.txt",
            body=b"Example data",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            jurisdiction="default",
            cf_r2_storage_class="Standard",
        )
        assert_matches_type(ObjectUploadResponse, object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.objects.with_raw_response.upload(
            object_key="path/to/my-object.txt",
            body=b"Example data",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectUploadResponse, object_, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.objects.with_streaming_response.upload(
            object_key="path/to/my-object.txt",
            body=b"Example data",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectUploadResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.objects.with_raw_response.upload(
                object_key="path/to/my-object.txt",
                body=b"Example data",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.objects.with_raw_response.upload(
                object_key="path/to/my-object.txt",
                body=b"Example data",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_key` but received ''"):
            await async_client.r2.buckets.objects.with_raw_response.upload(
                object_key="",
                body=b"Example data",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )
