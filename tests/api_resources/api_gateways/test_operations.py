# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.api_gateways import (
    OperationUpdateResponse,
    OperationListResponse,
    OperationDeleteResponse,
    OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse,
    OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse,
    OperationGetResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.api_gateways import operation_update_params
from cloudflare.types.api_gateways import operation_list_params
from cloudflare.types.api_gateways import operation_api_shield_endpoint_management_add_operations_to_a_zone_params
from cloudflare.types.api_gateways import (
    operation_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone_params,
)
from cloudflare.types.api_gateways import operation_get_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOperations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        operation = client.api_gateways.operations.update(
            "0d9bf70c-92e1-4bb3-9411-34a3bcc59003",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OperationUpdateResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        operation = client.api_gateways.operations.update(
            "0d9bf70c-92e1-4bb3-9411-34a3bcc59003",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            state="review",
        )
        assert_matches_type(OperationUpdateResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.api_gateways.operations.with_raw_response.update(
            "0d9bf70c-92e1-4bb3-9411-34a3bcc59003",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(OperationUpdateResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.api_gateways.operations.with_streaming_response.update(
            "0d9bf70c-92e1-4bb3-9411-34a3bcc59003",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(OperationUpdateResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.operations.with_raw_response.update(
                "0d9bf70c-92e1-4bb3-9411-34a3bcc59003",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.api_gateways.operations.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        operation = client.api_gateways.operations.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OperationListResponse], operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        operation = client.api_gateways.operations.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            diff=True,
            direction="desc",
            endpoint="/api/v1",
            host=["api.cloudflare.com"],
            method=["GET"],
            order="method",
            origin="ML",
            page={},
            per_page={},
            state="review",
        )
        assert_matches_type(Optional[OperationListResponse], operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.api_gateways.operations.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(Optional[OperationListResponse], operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.api_gateways.operations.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(Optional[OperationListResponse], operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.operations.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        operation = client.api_gateways.operations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OperationDeleteResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.api_gateways.operations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(OperationDeleteResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.api_gateways.operations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(OperationDeleteResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.operations.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.api_gateways.operations.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_api_shield_endpoint_management_add_operations_to_a_zone(self, client: Cloudflare) -> None:
        operation = client.api_gateways.operations.api_shield_endpoint_management_add_operations_to_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
            ],
        )
        assert_matches_type(
            Optional[OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse], operation, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_api_shield_endpoint_management_add_operations_to_a_zone(self, client: Cloudflare) -> None:
        response = (
            client.api_gateways.operations.with_raw_response.api_shield_endpoint_management_add_operations_to_a_zone(
                "023e105f4ecef8ad9ca31a8372d0c353",
                body=[
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                ],
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(
            Optional[OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse], operation, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_api_shield_endpoint_management_add_operations_to_a_zone(
        self, client: Cloudflare
    ) -> None:
        with client.api_gateways.operations.with_streaming_response.api_shield_endpoint_management_add_operations_to_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(
                Optional[OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse], operation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_api_shield_endpoint_management_add_operations_to_a_zone(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.operations.with_raw_response.api_shield_endpoint_management_add_operations_to_a_zone(
                "",
                body=[
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                ],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
        self, client: Cloudflare
    ) -> None:
        operation = client.api_gateways.operations.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse],
            operation,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone_with_all_params(
        self, client: Cloudflare
    ) -> None:
        operation = client.api_gateways.operations.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            endpoint="/api/v1",
            feature=["thresholds"],
            host=["api.cloudflare.com"],
            method=["GET"],
            order="method",
            page={},
            per_page=5,
        )
        assert_matches_type(
            Optional[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse],
            operation,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
        self, client: Cloudflare
    ) -> None:
        response = client.api_gateways.operations.with_raw_response.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(
            Optional[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse],
            operation,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
        self, client: Cloudflare
    ) -> None:
        with client.api_gateways.operations.with_streaming_response.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(
                Optional[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse],
                operation,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.operations.with_raw_response.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        operation = client.api_gateways.operations.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OperationGetResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        operation = client.api_gateways.operations.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            feature=["thresholds"],
        )
        assert_matches_type(OperationGetResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.api_gateways.operations.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(OperationGetResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.api_gateways.operations.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(OperationGetResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.operations.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.api_gateways.operations.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncOperations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.api_gateways.operations.update(
            "0d9bf70c-92e1-4bb3-9411-34a3bcc59003",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OperationUpdateResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.api_gateways.operations.update(
            "0d9bf70c-92e1-4bb3-9411-34a3bcc59003",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            state="review",
        )
        assert_matches_type(OperationUpdateResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.operations.with_raw_response.update(
            "0d9bf70c-92e1-4bb3-9411-34a3bcc59003",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(OperationUpdateResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.operations.with_streaming_response.update(
            "0d9bf70c-92e1-4bb3-9411-34a3bcc59003",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(OperationUpdateResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.operations.with_raw_response.update(
                "0d9bf70c-92e1-4bb3-9411-34a3bcc59003",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.api_gateways.operations.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.api_gateways.operations.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OperationListResponse], operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.api_gateways.operations.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            diff=True,
            direction="desc",
            endpoint="/api/v1",
            host=["api.cloudflare.com"],
            method=["GET"],
            order="method",
            origin="ML",
            page={},
            per_page={},
            state="review",
        )
        assert_matches_type(Optional[OperationListResponse], operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.operations.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(Optional[OperationListResponse], operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.operations.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(Optional[OperationListResponse], operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.operations.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.api_gateways.operations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OperationDeleteResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.operations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(OperationDeleteResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.operations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(OperationDeleteResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.operations.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.api_gateways.operations.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_api_shield_endpoint_management_add_operations_to_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        operation = await async_client.api_gateways.operations.api_shield_endpoint_management_add_operations_to_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
            ],
        )
        assert_matches_type(
            Optional[OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse], operation, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_api_shield_endpoint_management_add_operations_to_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.api_gateways.operations.with_raw_response.api_shield_endpoint_management_add_operations_to_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(
            Optional[OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse], operation, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_api_shield_endpoint_management_add_operations_to_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.api_gateways.operations.with_streaming_response.api_shield_endpoint_management_add_operations_to_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
                {
                    "endpoint": "/api/v1/users/{var1}",
                    "host": "www.example.com",
                    "method": "GET",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(
                Optional[OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse], operation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_api_shield_endpoint_management_add_operations_to_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.operations.with_raw_response.api_shield_endpoint_management_add_operations_to_a_zone(
                "",
                body=[
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                    {
                        "endpoint": "/api/v1/users/{var1}",
                        "host": "www.example.com",
                        "method": "GET",
                    },
                ],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        operation = await async_client.api_gateways.operations.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse],
            operation,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        operation = await async_client.api_gateways.operations.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            endpoint="/api/v1",
            feature=["thresholds"],
            host=["api.cloudflare.com"],
            method=["GET"],
            order="method",
            page={},
            per_page=5,
        )
        assert_matches_type(
            Optional[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse],
            operation,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.api_gateways.operations.with_raw_response.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(
            Optional[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse],
            operation,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.api_gateways.operations.with_streaming_response.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(
                Optional[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse],
                operation,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.operations.with_raw_response.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.api_gateways.operations.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OperationGetResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        operation = await async_client.api_gateways.operations.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            feature=["thresholds"],
        )
        assert_matches_type(OperationGetResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.operations.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(OperationGetResponse, operation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.operations.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(OperationGetResponse, operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.operations.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.api_gateways.operations.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
