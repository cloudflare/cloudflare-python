# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.kv.namespaces import bulk_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        bulk = client.kv.namespaces.bulk.update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )
        assert_matches_type(object, bulk, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.bulk.with_raw_response.update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(object, bulk, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.kv.namespaces.bulk.with_streaming_response.update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(object, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.bulk.with_raw_response.update(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
                body=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.bulk.with_raw_response.update(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}, {}, {}],
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        bulk = client.kv.namespaces.bulk.delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, bulk, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.bulk.with_raw_response.delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(object, bulk, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.kv.namespaces.bulk.with_streaming_response.delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(object, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.bulk.with_raw_response.delete(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.bulk.with_raw_response.delete(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        bulk = await async_client.kv.namespaces.bulk.update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )
        assert_matches_type(object, bulk, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.bulk.with_raw_response.update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(object, bulk, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.bulk.with_streaming_response.update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(object, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.bulk.with_raw_response.update(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
                body=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.bulk.with_raw_response.update(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}, {}, {}],
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        bulk = await async_client.kv.namespaces.bulk.delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, bulk, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.bulk.with_raw_response.delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(object, bulk, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.bulk.with_streaming_response.delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(object, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.bulk.with_raw_response.delete(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.bulk.with_raw_response.delete(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
