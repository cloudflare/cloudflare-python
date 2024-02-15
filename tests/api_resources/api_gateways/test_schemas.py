# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.api_gateways import (
    SchemaGetResponse,
    SchemaUpdateResponse,
    SchemaUpdateMultipleResponse,
    SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse,
)
from cloudflare.types.api_gateways.settings import APIShieldZoneSchemaValidationSettings

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchemas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        schema = client.api_gateways.schemas.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        schema = client.api_gateways.schemas.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            mitigation_action="block",
        )
        assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.api_gateways.schemas.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.api_gateways.schemas.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.schemas.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.api_gateways.schemas.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
        self, client: Cloudflare
    ) -> None:
        schema = (
            client.api_gateways.schemas.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )
        assert_matches_type(
            SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse, schema, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas_with_all_params(
        self, client: Cloudflare
    ) -> None:
        schema = (
            client.api_gateways.schemas.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
                "023e105f4ecef8ad9ca31a8372d0c353",
                feature=["thresholds"],
                host=["www.example.com"],
            )
        )
        assert_matches_type(
            SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse, schema, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
        self, client: Cloudflare
    ) -> None:
        response = client.api_gateways.schemas.with_raw_response.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(
            SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse, schema, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
        self, client: Cloudflare
    ) -> None:
        with client.api_gateways.schemas.with_streaming_response.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(
                SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse,
                schema,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.schemas.with_raw_response.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        schema = client.api_gateways.schemas.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SchemaGetResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.api_gateways.schemas.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaGetResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.api_gateways.schemas.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaGetResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.schemas.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.api_gateways.schemas.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_incremental(self, client: Cloudflare) -> None:
        schema = client.api_gateways.schemas.get_incremental(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(APIShieldZoneSchemaValidationSettings, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_incremental(self, client: Cloudflare) -> None:
        response = client.api_gateways.schemas.with_raw_response.get_incremental(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(APIShieldZoneSchemaValidationSettings, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_incremental(self, client: Cloudflare) -> None:
        with client.api_gateways.schemas.with_streaming_response.get_incremental(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(APIShieldZoneSchemaValidationSettings, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_incremental(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.schemas.with_raw_response.get_incremental(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_multiple(self, client: Cloudflare) -> None:
        schema = client.api_gateways.schemas.update_multiple(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        )
        assert_matches_type(SchemaUpdateMultipleResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_multiple(self, client: Cloudflare) -> None:
        response = client.api_gateways.schemas.with_raw_response.update_multiple(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(SchemaUpdateMultipleResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_multiple(self, client: Cloudflare) -> None:
        with client.api_gateways.schemas.with_streaming_response.update_multiple(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(SchemaUpdateMultipleResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_multiple(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.schemas.with_raw_response.update_multiple(
                "",
                body={
                    "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                    "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
                },
            )


class TestAsyncSchemas:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        schema = await async_client.api_gateways.schemas.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        schema = await async_client.api_gateways.schemas.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            mitigation_action="block",
        )
        assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.schemas.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.schemas.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaUpdateResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.schemas.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.api_gateways.schemas.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
        self, async_client: AsyncCloudflare
    ) -> None:
        schema = await async_client.api_gateways.schemas.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse, schema, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        schema = await async_client.api_gateways.schemas.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
            "023e105f4ecef8ad9ca31a8372d0c353",
            feature=["thresholds"],
            host=["www.example.com"],
        )
        assert_matches_type(
            SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse, schema, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.api_gateways.schemas.with_raw_response.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(
            SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse, schema, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.api_gateways.schemas.with_streaming_response.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(
                SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse,
                schema,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.schemas.with_raw_response.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        schema = await async_client.api_gateways.schemas.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SchemaGetResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.schemas.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaGetResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.schemas.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaGetResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.schemas.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.api_gateways.schemas.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_incremental(self, async_client: AsyncCloudflare) -> None:
        schema = await async_client.api_gateways.schemas.get_incremental(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(APIShieldZoneSchemaValidationSettings, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_incremental(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.schemas.with_raw_response.get_incremental(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(APIShieldZoneSchemaValidationSettings, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_incremental(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.schemas.with_streaming_response.get_incremental(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(APIShieldZoneSchemaValidationSettings, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_incremental(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.schemas.with_raw_response.get_incremental(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_multiple(self, async_client: AsyncCloudflare) -> None:
        schema = await async_client.api_gateways.schemas.update_multiple(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        )
        assert_matches_type(SchemaUpdateMultipleResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_multiple(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.schemas.with_raw_response.update_multiple(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(SchemaUpdateMultipleResponse, schema, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_multiple(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.schemas.with_streaming_response.update_multiple(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(SchemaUpdateMultipleResponse, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_multiple(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.schemas.with_raw_response.update_multiple(
                "",
                body={
                    "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                    "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
                },
            )
