# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.r2.buckets.domains import (
    CustomGetResponse,
    CustomListResponse,
    CustomCreateResponse,
    CustomDeleteResponse,
    CustomUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        custom = client.r2.buckets.domains.custom.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            enabled=True,
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
        )
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        custom = client.r2.buckets.domains.custom.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            enabled=True,
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
            min_tls="1.0",
            jurisdiction="default",
        )
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.r2.buckets.domains.custom.with_raw_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            enabled=True,
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.r2.buckets.domains.custom.with_streaming_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            enabled=True,
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomCreateResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.domains.custom.with_raw_response.create(
                bucket_name="example-bucket",
                account_id="",
                domain="prefix.example-domain.com",
                enabled=True,
                zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.domains.custom.with_raw_response.create(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="prefix.example-domain.com",
                enabled=True,
                zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        custom = client.r2.buckets.domains.custom.update(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        custom = client.r2.buckets.domains.custom.update(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            enabled=True,
            min_tls="1.0",
            jurisdiction="default",
        )
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.r2.buckets.domains.custom.with_raw_response.update(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.r2.buckets.domains.custom.with_streaming_response.update(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomUpdateResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.domains.custom.with_raw_response.update(
                domain="example-domain/custom-domain.com",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.domains.custom.with_raw_response.update(
                domain="example-domain/custom-domain.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            client.r2.buckets.domains.custom.with_raw_response.update(
                domain="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        custom = client.r2.buckets.domains.custom.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        custom = client.r2.buckets.domains.custom.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            jurisdiction="default",
        )
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.r2.buckets.domains.custom.with_raw_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.r2.buckets.domains.custom.with_streaming_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomListResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.domains.custom.with_raw_response.list(
                bucket_name="example-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.domains.custom.with_raw_response.list(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom = client.r2.buckets.domains.custom.delete(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        custom = client.r2.buckets.domains.custom.delete(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            jurisdiction="default",
        )
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.r2.buckets.domains.custom.with_raw_response.delete(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.r2.buckets.domains.custom.with_streaming_response.delete(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomDeleteResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.domains.custom.with_raw_response.delete(
                domain="example-domain/custom-domain.com",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.domains.custom.with_raw_response.delete(
                domain="example-domain/custom-domain.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            client.r2.buckets.domains.custom.with_raw_response.delete(
                domain="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        custom = client.r2.buckets.domains.custom.get(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(CustomGetResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        custom = client.r2.buckets.domains.custom.get(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            jurisdiction="default",
        )
        assert_matches_type(CustomGetResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.r2.buckets.domains.custom.with_raw_response.get(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomGetResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.r2.buckets.domains.custom.with_streaming_response.get(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomGetResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.domains.custom.with_raw_response.get(
                domain="example-domain/custom-domain.com",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.domains.custom.with_raw_response.get(
                domain="example-domain/custom-domain.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            client.r2.buckets.domains.custom.with_raw_response.get(
                domain="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )


class TestAsyncCustom:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.buckets.domains.custom.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            enabled=True,
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
        )
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.buckets.domains.custom.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            enabled=True,
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
            min_tls="1.0",
            jurisdiction="default",
        )
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.domains.custom.with_raw_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            enabled=True,
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomCreateResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.domains.custom.with_streaming_response.create(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="prefix.example-domain.com",
            enabled=True,
            zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomCreateResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.domains.custom.with_raw_response.create(
                bucket_name="example-bucket",
                account_id="",
                domain="prefix.example-domain.com",
                enabled=True,
                zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.domains.custom.with_raw_response.create(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="prefix.example-domain.com",
                enabled=True,
                zone_id="36ca64a6d92827b8a6b90be344bb1bfd",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.buckets.domains.custom.update(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.buckets.domains.custom.update(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            enabled=True,
            min_tls="1.0",
            jurisdiction="default",
        )
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.domains.custom.with_raw_response.update(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomUpdateResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.domains.custom.with_streaming_response.update(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomUpdateResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.domains.custom.with_raw_response.update(
                domain="example-domain/custom-domain.com",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.domains.custom.with_raw_response.update(
                domain="example-domain/custom-domain.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            await async_client.r2.buckets.domains.custom.with_raw_response.update(
                domain="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.buckets.domains.custom.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.buckets.domains.custom.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            jurisdiction="default",
        )
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.domains.custom.with_raw_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomListResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.domains.custom.with_streaming_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomListResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.domains.custom.with_raw_response.list(
                bucket_name="example-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.domains.custom.with_raw_response.list(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.buckets.domains.custom.delete(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.buckets.domains.custom.delete(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            jurisdiction="default",
        )
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.domains.custom.with_raw_response.delete(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomDeleteResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.domains.custom.with_streaming_response.delete(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomDeleteResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.domains.custom.with_raw_response.delete(
                domain="example-domain/custom-domain.com",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.domains.custom.with_raw_response.delete(
                domain="example-domain/custom-domain.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            await async_client.r2.buckets.domains.custom.with_raw_response.delete(
                domain="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.buckets.domains.custom.get(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(CustomGetResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom = await async_client.r2.buckets.domains.custom.get(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            jurisdiction="default",
        )
        assert_matches_type(CustomGetResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.domains.custom.with_raw_response.get(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomGetResponse, custom, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.domains.custom.with_streaming_response.get(
            domain="example-domain/custom-domain.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomGetResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.domains.custom.with_raw_response.get(
                domain="example-domain/custom-domain.com",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.domains.custom.with_raw_response.get(
                domain="example-domain/custom-domain.com",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            await async_client.r2.buckets.domains.custom.with_raw_response.get(
                domain="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )
