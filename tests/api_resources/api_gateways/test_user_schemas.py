# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.api_gateways import (
    APIShieldPublicSchema,
    UserSchemaListResponse,
    UserSchemaDeleteResponse,
    APIShieldSchemaUploadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserSchemas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        user_schema = client.api_gateways.user_schemas.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
        )
        assert_matches_type(APIShieldSchemaUploadResponse, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        user_schema = client.api_gateways.user_schemas.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
            name="petstore schema",
            validation_enabled="true",
        )
        assert_matches_type(APIShieldSchemaUploadResponse, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.api_gateways.user_schemas.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = response.parse()
        assert_matches_type(APIShieldSchemaUploadResponse, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.api_gateways.user_schemas.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = response.parse()
            assert_matches_type(APIShieldSchemaUploadResponse, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.user_schemas.with_raw_response.create(
                "",
                file=b"raw file contents",
                kind="openapi_v3",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        user_schema = client.api_gateways.user_schemas.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        user_schema = client.api_gateways.user_schemas.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_enabled=True,
        )
        assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.api_gateways.user_schemas.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = response.parse()
        assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.api_gateways.user_schemas.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = response.parse()
            assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.user_schemas.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.api_gateways.user_schemas.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        user_schema = client.api_gateways.user_schemas.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserSchemaListResponse], user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        user_schema = client.api_gateways.user_schemas.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            omit_source=True,
            page={},
            per_page={},
            validation_enabled=True,
        )
        assert_matches_type(Optional[UserSchemaListResponse], user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.api_gateways.user_schemas.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = response.parse()
        assert_matches_type(Optional[UserSchemaListResponse], user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.api_gateways.user_schemas.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = response.parse()
            assert_matches_type(Optional[UserSchemaListResponse], user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.user_schemas.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        user_schema = client.api_gateways.user_schemas.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UserSchemaDeleteResponse, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.api_gateways.user_schemas.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = response.parse()
        assert_matches_type(UserSchemaDeleteResponse, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.api_gateways.user_schemas.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = response.parse()
            assert_matches_type(UserSchemaDeleteResponse, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.user_schemas.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.api_gateways.user_schemas.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        user_schema = client.api_gateways.user_schemas.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        user_schema = client.api_gateways.user_schemas.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            omit_source=True,
        )
        assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.api_gateways.user_schemas.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = response.parse()
        assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.api_gateways.user_schemas.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = response.parse()
            assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.user_schemas.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.api_gateways.user_schemas.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncUserSchemas:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateways.user_schemas.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
        )
        assert_matches_type(APIShieldSchemaUploadResponse, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateways.user_schemas.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
            name="petstore schema",
            validation_enabled="true",
        )
        assert_matches_type(APIShieldSchemaUploadResponse, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.user_schemas.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = await response.parse()
        assert_matches_type(APIShieldSchemaUploadResponse, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.user_schemas.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = await response.parse()
            assert_matches_type(APIShieldSchemaUploadResponse, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.user_schemas.with_raw_response.create(
                "",
                file=b"raw file contents",
                kind="openapi_v3",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateways.user_schemas.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateways.user_schemas.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_enabled=True,
        )
        assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.user_schemas.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = await response.parse()
        assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.user_schemas.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = await response.parse()
            assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.user_schemas.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.api_gateways.user_schemas.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateways.user_schemas.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserSchemaListResponse], user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateways.user_schemas.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            omit_source=True,
            page={},
            per_page={},
            validation_enabled=True,
        )
        assert_matches_type(Optional[UserSchemaListResponse], user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.user_schemas.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = await response.parse()
        assert_matches_type(Optional[UserSchemaListResponse], user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.user_schemas.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = await response.parse()
            assert_matches_type(Optional[UserSchemaListResponse], user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.user_schemas.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateways.user_schemas.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UserSchemaDeleteResponse, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.user_schemas.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = await response.parse()
        assert_matches_type(UserSchemaDeleteResponse, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.user_schemas.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = await response.parse()
            assert_matches_type(UserSchemaDeleteResponse, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.user_schemas.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.api_gateways.user_schemas.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateways.user_schemas.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateways.user_schemas.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            omit_source=True,
        )
        assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.user_schemas.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = await response.parse()
        assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.user_schemas.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = await response.parse()
            assert_matches_type(APIShieldPublicSchema, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.user_schemas.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.api_gateways.user_schemas.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
