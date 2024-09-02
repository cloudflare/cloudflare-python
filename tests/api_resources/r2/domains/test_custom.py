# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.r2.domains import (
    CustomCreateResponse,
    CustomUpdateResponse,
    CustomListResponse,
    CustomDeleteResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.r2.domains import custom_create_params
from cloudflare.types.r2.domains import custom_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        custom = client.r2.domains.custom.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
        )
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        custom = client.r2.domains.custom.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
            enabled=True,
        )
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.r2.domains.custom.with_raw_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.r2.domains.custom.with_streaming_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomCreateResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.domains.custom.with_raw_response.create(
                bucket_name="example-bucket",
                account_id="",
                domain="prefix.example-domain.com",
                zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.domains.custom.with_raw_response.create(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="prefix.example-domain.com",
                zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        custom = client.r2.domains.custom.update(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        custom = client.r2.domains.custom.update(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            enabled=True,
        )
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.r2.domains.custom.with_raw_response.update(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.r2.domains.custom.with_streaming_response.update(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomUpdateResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.domains.custom.with_raw_response.update(
                domain_name="example-domain/custom-domain.com",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.domains.custom.with_raw_response.update(
                domain_name="example-domain/custom-domain.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            client.r2.domains.custom.with_raw_response.update(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        custom = client.r2.domains.custom.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.r2.domains.custom.with_raw_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.r2.domains.custom.with_streaming_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomListResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.domains.custom.with_raw_response.list(
                bucket_name="example-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.domains.custom.with_raw_response.list(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom = client.r2.domains.custom.delete(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.r2.domains.custom.with_raw_response.delete(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.r2.domains.custom.with_streaming_response.delete(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomDeleteResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.domains.custom.with_raw_response.delete(
                domain_name="example-domain/custom-domain.com",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.domains.custom.with_raw_response.delete(
                domain_name="example-domain/custom-domain.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            client.r2.domains.custom.with_raw_response.delete(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )


class TestAsyncCustom:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.domains.custom.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
        )
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.domains.custom.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
            enabled=True,
        )
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.domains.custom.with_raw_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.domains.custom.with_streaming_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomCreateResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.domains.custom.with_raw_response.create(
                bucket_name="example-bucket",
                account_id="",
                domain="prefix.example-domain.com",
                zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.domains.custom.with_raw_response.create(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="prefix.example-domain.com",
                zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.domains.custom.update(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.domains.custom.update(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            enabled=True,
        )
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.domains.custom.with_raw_response.update(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.domains.custom.with_streaming_response.update(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomUpdateResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.domains.custom.with_raw_response.update(
                domain_name="example-domain/custom-domain.com",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.domains.custom.with_raw_response.update(
                domain_name="example-domain/custom-domain.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            await async_client.r2.domains.custom.with_raw_response.update(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.domains.custom.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.domains.custom.with_raw_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.domains.custom.with_streaming_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomListResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.domains.custom.with_raw_response.list(
                bucket_name="example-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.domains.custom.with_raw_response.list(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.domains.custom.delete(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.domains.custom.with_raw_response.delete(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.domains.custom.with_streaming_response.delete(
            domain_name="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomDeleteResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.domains.custom.with_raw_response.delete(
                domain_name="example-domain/custom-domain.com",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.domains.custom.with_raw_response.delete(
                domain_name="example-domain/custom-domain.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            await async_client.r2.domains.custom.with_raw_response.delete(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )
