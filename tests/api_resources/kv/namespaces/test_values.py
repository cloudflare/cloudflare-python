# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

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
from cloudflare.types.kv.namespaces import ValueDeleteResponse, ValueUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValues:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        value = client.kv.namespaces.values.update(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        )
        assert_matches_type(Optional[ValueUpdateResponse], value, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        value = client.kv.namespaces.values.update(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
            expiration=1578435000,
            expiration_ttl=300,
        )
        assert_matches_type(Optional[ValueUpdateResponse], value, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.values.with_raw_response.update(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(Optional[ValueUpdateResponse], value, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.kv.namespaces.values.with_streaming_response.update(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(Optional[ValueUpdateResponse], value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.values.with_raw_response.update(
                key_name="My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                metadata='{"someMetadataKey": "someMetadataValue"}',
                value="Some Value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.values.with_raw_response.update(
                key_name="My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
                metadata='{"someMetadataKey": "someMetadataValue"}',
                value="Some Value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            client.kv.namespaces.values.with_raw_response.update(
                key_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                metadata='{"someMetadataKey": "someMetadataValue"}',
                value="Some Value",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_update_uses_multipart_form_data(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        """Test that values.update sends data as multipart/form-data, not JSON.

        This is a regression test for https://github.com/cloudflare/cloudflare-python/issues/2519
        """
        respx_mock.put(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/storage/kv/namespaces/0f2ac74b498b48028cb68387c421e279/values/My-Key"
        ).mock(return_value=httpx.Response(200, json={"success": True, "result": {}}))

        client.kv.namespaces.values.update(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        )

        # Verify the request was made
        assert respx_mock.calls.call_count == 1
        request = respx_mock.calls[0].request

        # Verify Content-Type is multipart/form-data (with boundary)
        content_type = request.headers.get("content-type", "")
        assert content_type.startswith("multipart/form-data"), (
            f"Expected Content-Type to start with 'multipart/form-data', got '{content_type}'"
        )

        # Verify the body contains separate form fields for value and metadata
        body = request.content.decode("utf-8")
        assert "Some Value" in body, "Value should be in the multipart body"
        assert "someMetadataKey" in body, "Metadata should be in the multipart body"

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        value = client.kv.namespaces.values.delete(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )
        assert_matches_type(Optional[ValueDeleteResponse], value, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.values.with_raw_response.delete(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(Optional[ValueDeleteResponse], value, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.kv.namespaces.values.with_streaming_response.delete(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(Optional[ValueDeleteResponse], value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.values.with_raw_response.delete(
                key_name="My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.values.with_raw_response.delete(
                key_name="My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            client.kv.namespaces.values.with_raw_response.delete(
                key_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

    @pytest.mark.skip(reason="HTTP 406 from prism")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/storage/kv/namespaces/0f2ac74b498b48028cb68387c421e279/values/My-Key"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        value = client.kv.namespaces.values.get(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )
        assert value.is_closed
        assert value.json() == {"foo": "bar"}
        assert cast(Any, value.is_closed) is True
        assert isinstance(value, BinaryAPIResponse)

    @pytest.mark.skip(reason="HTTP 406 from prism")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/storage/kv/namespaces/0f2ac74b498b48028cb68387c421e279/values/My-Key"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        value = client.kv.namespaces.values.with_raw_response.get(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )

        assert value.is_closed is True
        assert value.http_request.headers.get("X-Stainless-Lang") == "python"
        assert value.json() == {"foo": "bar"}
        assert isinstance(value, BinaryAPIResponse)

    @pytest.mark.skip(reason="HTTP 406 from prism")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/storage/kv/namespaces/0f2ac74b498b48028cb68387c421e279/values/My-Key"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.kv.namespaces.values.with_streaming_response.get(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        ) as value:
            assert not value.is_closed
            assert value.http_request.headers.get("X-Stainless-Lang") == "python"

            assert value.json() == {"foo": "bar"}
            assert cast(Any, value.is_closed) is True
            assert isinstance(value, StreamedBinaryAPIResponse)

        assert cast(Any, value.is_closed) is True

    @pytest.mark.skip(reason="HTTP 406 from prism")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.values.with_raw_response.get(
                key_name="My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.values.with_raw_response.get(
                key_name="My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            client.kv.namespaces.values.with_raw_response.get(
                key_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )


class TestAsyncValues:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        value = await async_client.kv.namespaces.values.update(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        )
        assert_matches_type(Optional[ValueUpdateResponse], value, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        value = await async_client.kv.namespaces.values.update(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
            expiration=1578435000,
            expiration_ttl=300,
        )
        assert_matches_type(Optional[ValueUpdateResponse], value, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.values.with_raw_response.update(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(Optional[ValueUpdateResponse], value, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.values.with_streaming_response.update(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(Optional[ValueUpdateResponse], value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.update(
                key_name="My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                metadata='{"someMetadataKey": "someMetadataValue"}',
                value="Some Value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.update(
                key_name="My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
                metadata='{"someMetadataKey": "someMetadataValue"}',
                value="Some Value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.update(
                key_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                metadata='{"someMetadataKey": "someMetadataValue"}',
                value="Some Value",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_update_uses_multipart_form_data(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        """Test that values.update sends data as multipart/form-data, not JSON.

        This is a regression test for https://github.com/cloudflare/cloudflare-python/issues/2519
        """
        respx_mock.put(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/storage/kv/namespaces/0f2ac74b498b48028cb68387c421e279/values/My-Key"
        ).mock(return_value=httpx.Response(200, json={"success": True, "result": {}}))

        await async_client.kv.namespaces.values.update(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        )

        # Verify the request was made
        assert respx_mock.calls.call_count == 1
        request = respx_mock.calls[0].request

        # Verify Content-Type is multipart/form-data (with boundary)
        content_type = request.headers.get("content-type", "")
        assert content_type.startswith("multipart/form-data"), (
            f"Expected Content-Type to start with 'multipart/form-data', got '{content_type}'"
        )

        # Verify the body contains separate form fields for value and metadata
        body = request.content.decode("utf-8")
        assert "Some Value" in body, "Value should be in the multipart body"
        assert "someMetadataKey" in body, "Metadata should be in the multipart body"

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        value = await async_client.kv.namespaces.values.delete(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )
        assert_matches_type(Optional[ValueDeleteResponse], value, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.values.with_raw_response.delete(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(Optional[ValueDeleteResponse], value, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.values.with_streaming_response.delete(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(Optional[ValueDeleteResponse], value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.delete(
                key_name="My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.delete(
                key_name="My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.delete(
                key_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

    @pytest.mark.skip(reason="HTTP 406 from prism")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/storage/kv/namespaces/0f2ac74b498b48028cb68387c421e279/values/My-Key"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        value = await async_client.kv.namespaces.values.get(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )
        assert value.is_closed
        assert await value.json() == {"foo": "bar"}
        assert cast(Any, value.is_closed) is True
        assert isinstance(value, AsyncBinaryAPIResponse)

    @pytest.mark.skip(reason="HTTP 406 from prism")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/storage/kv/namespaces/0f2ac74b498b48028cb68387c421e279/values/My-Key"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        value = await async_client.kv.namespaces.values.with_raw_response.get(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )

        assert value.is_closed is True
        assert value.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await value.json() == {"foo": "bar"}
        assert isinstance(value, AsyncBinaryAPIResponse)

    @pytest.mark.skip(reason="HTTP 406 from prism")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/storage/kv/namespaces/0f2ac74b498b48028cb68387c421e279/values/My-Key"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.kv.namespaces.values.with_streaming_response.get(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        ) as value:
            assert not value.is_closed
            assert value.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await value.json() == {"foo": "bar"}
            assert cast(Any, value.is_closed) is True
            assert isinstance(value, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, value.is_closed) is True

    @pytest.mark.skip(reason="HTTP 406 from prism")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.get(
                key_name="My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.get(
                key_name="My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.get(
                key_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )
