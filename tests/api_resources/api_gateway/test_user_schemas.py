# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.api_gateway import (
    PublicSchema,
    SchemaUpload,
    UserSchemaDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserSchemas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        user_schema = client.api_gateway.user_schemas.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
        )
        assert_matches_type(SchemaUpload, user_schema, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        user_schema = client.api_gateway.user_schemas.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
            name="petstore schema",
            validation_enabled="true",
        )
        assert_matches_type(SchemaUpload, user_schema, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.api_gateway.user_schemas.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = response.parse()
        assert_matches_type(SchemaUpload, user_schema, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.api_gateway.user_schemas.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = response.parse()
            assert_matches_type(SchemaUpload, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.user_schemas.with_raw_response.create(
                zone_id="",
                file=b"raw file contents",
                kind="openapi_v3",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        user_schema = client.api_gateway.user_schemas.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[PublicSchema], user_schema, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        user_schema = client.api_gateway.user_schemas.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            omit_source=True,
            page=1,
            per_page=5,
            validation_enabled=True,
        )
        assert_matches_type(SyncV4PagePaginationArray[PublicSchema], user_schema, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.api_gateway.user_schemas.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[PublicSchema], user_schema, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.api_gateway.user_schemas.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[PublicSchema], user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.user_schemas.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        user_schema = client.api_gateway.user_schemas.delete(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UserSchemaDeleteResponse, user_schema, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.api_gateway.user_schemas.with_raw_response.delete(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = response.parse()
        assert_matches_type(UserSchemaDeleteResponse, user_schema, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.api_gateway.user_schemas.with_streaming_response.delete(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = response.parse()
            assert_matches_type(UserSchemaDeleteResponse, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.user_schemas.with_raw_response.delete(
                schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.api_gateway.user_schemas.with_raw_response.delete(
                schema_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        user_schema = client.api_gateway.user_schemas.edit(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PublicSchema, user_schema, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        user_schema = client.api_gateway.user_schemas.edit(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_enabled=True,
        )
        assert_matches_type(PublicSchema, user_schema, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.api_gateway.user_schemas.with_raw_response.edit(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = response.parse()
        assert_matches_type(PublicSchema, user_schema, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.api_gateway.user_schemas.with_streaming_response.edit(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = response.parse()
            assert_matches_type(PublicSchema, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.user_schemas.with_raw_response.edit(
                schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.api_gateway.user_schemas.with_raw_response.edit(
                schema_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        user_schema = client.api_gateway.user_schemas.get(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PublicSchema, user_schema, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        user_schema = client.api_gateway.user_schemas.get(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            omit_source=True,
        )
        assert_matches_type(PublicSchema, user_schema, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.api_gateway.user_schemas.with_raw_response.get(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = response.parse()
        assert_matches_type(PublicSchema, user_schema, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.api_gateway.user_schemas.with_streaming_response.get(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = response.parse()
            assert_matches_type(PublicSchema, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.user_schemas.with_raw_response.get(
                schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            client.api_gateway.user_schemas.with_raw_response.get(
                schema_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncUserSchemas:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateway.user_schemas.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
        )
        assert_matches_type(SchemaUpload, user_schema, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateway.user_schemas.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
            name="petstore schema",
            validation_enabled="true",
        )
        assert_matches_type(SchemaUpload, user_schema, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.user_schemas.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = await response.parse()
        assert_matches_type(SchemaUpload, user_schema, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.user_schemas.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file=b"raw file contents",
            kind="openapi_v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = await response.parse()
            assert_matches_type(SchemaUpload, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.user_schemas.with_raw_response.create(
                zone_id="",
                file=b"raw file contents",
                kind="openapi_v3",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateway.user_schemas.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[PublicSchema], user_schema, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateway.user_schemas.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            omit_source=True,
            page=1,
            per_page=5,
            validation_enabled=True,
        )
        assert_matches_type(AsyncV4PagePaginationArray[PublicSchema], user_schema, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.user_schemas.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[PublicSchema], user_schema, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.user_schemas.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[PublicSchema], user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.user_schemas.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateway.user_schemas.delete(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UserSchemaDeleteResponse, user_schema, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.user_schemas.with_raw_response.delete(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = await response.parse()
        assert_matches_type(UserSchemaDeleteResponse, user_schema, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.user_schemas.with_streaming_response.delete(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = await response.parse()
            assert_matches_type(UserSchemaDeleteResponse, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.user_schemas.with_raw_response.delete(
                schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.api_gateway.user_schemas.with_raw_response.delete(
                schema_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateway.user_schemas.edit(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PublicSchema, user_schema, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateway.user_schemas.edit(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_enabled=True,
        )
        assert_matches_type(PublicSchema, user_schema, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.user_schemas.with_raw_response.edit(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = await response.parse()
        assert_matches_type(PublicSchema, user_schema, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.user_schemas.with_streaming_response.edit(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = await response.parse()
            assert_matches_type(PublicSchema, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.user_schemas.with_raw_response.edit(
                schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.api_gateway.user_schemas.with_raw_response.edit(
                schema_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateway.user_schemas.get(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PublicSchema, user_schema, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user_schema = await async_client.api_gateway.user_schemas.get(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            omit_source=True,
        )
        assert_matches_type(PublicSchema, user_schema, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.user_schemas.with_raw_response.get(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_schema = await response.parse()
        assert_matches_type(PublicSchema, user_schema, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.user_schemas.with_streaming_response.get(
            schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_schema = await response.parse()
            assert_matches_type(PublicSchema, user_schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.user_schemas.with_raw_response.get(
                schema_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schema_id` but received ''"):
            await async_client.api_gateway.user_schemas.with_raw_response.get(
                schema_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
