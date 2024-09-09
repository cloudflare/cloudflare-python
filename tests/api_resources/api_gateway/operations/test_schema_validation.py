# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.api_gateway.operations import (
    SettingsMultipleRequest,
    SchemaValidationGetResponse,
    SchemaValidationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchemaValidation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        schema_validation = client.api_gateway.operations.schema_validation.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SchemaValidationUpdateResponse, schema_validation, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        schema_validation = client.api_gateway.operations.schema_validation.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            mitigation_action="log",
        )
        assert_matches_type(SchemaValidationUpdateResponse, schema_validation, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.api_gateway.operations.schema_validation.with_raw_response.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema_validation = response.parse()
        assert_matches_type(SchemaValidationUpdateResponse, schema_validation, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.api_gateway.operations.schema_validation.with_streaming_response.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema_validation = response.parse()
            assert_matches_type(SchemaValidationUpdateResponse, schema_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.operations.schema_validation.with_raw_response.update(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.api_gateway.operations.schema_validation.with_raw_response.update(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        schema_validation = client.api_gateway.operations.schema_validation.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            settings_multiple_request={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        )
        assert_matches_type(SettingsMultipleRequest, schema_validation, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.api_gateway.operations.schema_validation.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            settings_multiple_request={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema_validation = response.parse()
        assert_matches_type(SettingsMultipleRequest, schema_validation, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.api_gateway.operations.schema_validation.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            settings_multiple_request={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema_validation = response.parse()
            assert_matches_type(SettingsMultipleRequest, schema_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.operations.schema_validation.with_raw_response.edit(
                zone_id="",
                settings_multiple_request={
                    "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                    "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
                },
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        schema_validation = client.api_gateway.operations.schema_validation.get(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SchemaValidationGetResponse, schema_validation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.api_gateway.operations.schema_validation.with_raw_response.get(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema_validation = response.parse()
        assert_matches_type(SchemaValidationGetResponse, schema_validation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.api_gateway.operations.schema_validation.with_streaming_response.get(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema_validation = response.parse()
            assert_matches_type(SchemaValidationGetResponse, schema_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.operations.schema_validation.with_raw_response.get(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.api_gateway.operations.schema_validation.with_raw_response.get(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSchemaValidation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        schema_validation = await async_client.api_gateway.operations.schema_validation.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SchemaValidationUpdateResponse, schema_validation, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        schema_validation = await async_client.api_gateway.operations.schema_validation.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            mitigation_action="log",
        )
        assert_matches_type(SchemaValidationUpdateResponse, schema_validation, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.operations.schema_validation.with_raw_response.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema_validation = await response.parse()
        assert_matches_type(SchemaValidationUpdateResponse, schema_validation, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.operations.schema_validation.with_streaming_response.update(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema_validation = await response.parse()
            assert_matches_type(SchemaValidationUpdateResponse, schema_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.operations.schema_validation.with_raw_response.update(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.api_gateway.operations.schema_validation.with_raw_response.update(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        schema_validation = await async_client.api_gateway.operations.schema_validation.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            settings_multiple_request={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        )
        assert_matches_type(SettingsMultipleRequest, schema_validation, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.operations.schema_validation.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            settings_multiple_request={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema_validation = await response.parse()
        assert_matches_type(SettingsMultipleRequest, schema_validation, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.operations.schema_validation.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            settings_multiple_request={
                "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema_validation = await response.parse()
            assert_matches_type(SettingsMultipleRequest, schema_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.operations.schema_validation.with_raw_response.edit(
                zone_id="",
                settings_multiple_request={
                    "3818d821-5901-4147-a474-f5f5aec1d54e": {},
                    "b17c8043-99a0-4202-b7d9-8f7cdbee02cd": {},
                },
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        schema_validation = await async_client.api_gateway.operations.schema_validation.get(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SchemaValidationGetResponse, schema_validation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.operations.schema_validation.with_raw_response.get(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema_validation = await response.parse()
        assert_matches_type(SchemaValidationGetResponse, schema_validation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.operations.schema_validation.with_streaming_response.get(
            operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema_validation = await response.parse()
            assert_matches_type(SchemaValidationGetResponse, schema_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.operations.schema_validation.with_raw_response.get(
                operation_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.api_gateway.operations.schema_validation.with_raw_response.get(
                operation_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
