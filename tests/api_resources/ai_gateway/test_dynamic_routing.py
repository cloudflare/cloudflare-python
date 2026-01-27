# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ai_gateway import (
    DynamicRoutingGetResponse,
    DynamicRoutingListResponse,
    DynamicRoutingCreateResponse,
    DynamicRoutingDeleteResponse,
    DynamicRoutingUpdateResponse,
    DynamicRoutingGetVersionResponse,
    DynamicRoutingListVersionsResponse,
    DynamicRoutingCreateVersionResponse,
    DynamicRoutingListDeploymentsResponse,
    DynamicRoutingCreateDeploymentResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDynamicRouting:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        dynamic_routing = client.ai_gateway.dynamic_routing.create(
            gateway_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            elements=[
                {
                    "id": "id",
                    "outputs": {"next": {"element_id": "elementId"}},
                    "type": "start",
                }
            ],
            name="name",
        )
        assert_matches_type(DynamicRoutingCreateResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.ai_gateway.dynamic_routing.with_raw_response.create(
            gateway_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            elements=[
                {
                    "id": "id",
                    "outputs": {"next": {"element_id": "elementId"}},
                    "type": "start",
                }
            ],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = response.parse()
        assert_matches_type(DynamicRoutingCreateResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.ai_gateway.dynamic_routing.with_streaming_response.create(
            gateway_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            elements=[
                {
                    "id": "id",
                    "outputs": {"next": {"element_id": "elementId"}},
                    "type": "start",
                }
            ],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = response.parse()
            assert_matches_type(DynamicRoutingCreateResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.create(
                gateway_id="54442216",
                account_id="",
                elements=[
                    {
                        "id": "id",
                        "outputs": {"next": {"element_id": "elementId"}},
                        "type": "start",
                    }
                ],
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.create(
                gateway_id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                elements=[
                    {
                        "id": "id",
                        "outputs": {"next": {"element_id": "elementId"}},
                        "type": "start",
                    }
                ],
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        dynamic_routing = client.ai_gateway.dynamic_routing.update(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            name="Route Name",
        )
        assert_matches_type(DynamicRoutingUpdateResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.ai_gateway.dynamic_routing.with_raw_response.update(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            name="Route Name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = response.parse()
        assert_matches_type(DynamicRoutingUpdateResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.ai_gateway.dynamic_routing.with_streaming_response.update(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            name="Route Name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = response.parse()
            assert_matches_type(DynamicRoutingUpdateResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.update(
                id="54442216",
                account_id="",
                gateway_id="54442216",
                name="Route Name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.update(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
                name="Route Name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.update(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
                name="Route Name",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        dynamic_routing = client.ai_gateway.dynamic_routing.list(
            gateway_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(DynamicRoutingListResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.ai_gateway.dynamic_routing.with_raw_response.list(
            gateway_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = response.parse()
        assert_matches_type(DynamicRoutingListResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.ai_gateway.dynamic_routing.with_streaming_response.list(
            gateway_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = response.parse()
            assert_matches_type(DynamicRoutingListResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.list(
                gateway_id="54442216",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.list(
                gateway_id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        dynamic_routing = client.ai_gateway.dynamic_routing.delete(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )
        assert_matches_type(DynamicRoutingDeleteResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.ai_gateway.dynamic_routing.with_raw_response.delete(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = response.parse()
        assert_matches_type(DynamicRoutingDeleteResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.ai_gateway.dynamic_routing.with_streaming_response.delete(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = response.parse()
            assert_matches_type(DynamicRoutingDeleteResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.delete(
                id="54442216",
                account_id="",
                gateway_id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.delete(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.delete(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
            )

    @parametrize
    def test_method_create_deployment(self, client: Cloudflare) -> None:
        dynamic_routing = client.ai_gateway.dynamic_routing.create_deployment(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            comment="Route Deployment Comment",
            version_id="54442216",
        )
        assert_matches_type(DynamicRoutingCreateDeploymentResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_raw_response_create_deployment(self, client: Cloudflare) -> None:
        response = client.ai_gateway.dynamic_routing.with_raw_response.create_deployment(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            comment="Route Deployment Comment",
            version_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = response.parse()
        assert_matches_type(DynamicRoutingCreateDeploymentResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_streaming_response_create_deployment(self, client: Cloudflare) -> None:
        with client.ai_gateway.dynamic_routing.with_streaming_response.create_deployment(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            comment="Route Deployment Comment",
            version_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = response.parse()
            assert_matches_type(DynamicRoutingCreateDeploymentResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_deployment(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.create_deployment(
                id="54442216",
                account_id="",
                gateway_id="54442216",
                comment="Route Deployment Comment",
                version_id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.create_deployment(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
                comment="Route Deployment Comment",
                version_id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.create_deployment(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
                comment="Route Deployment Comment",
                version_id="54442216",
            )

    @parametrize
    def test_method_create_version(self, client: Cloudflare) -> None:
        dynamic_routing = client.ai_gateway.dynamic_routing.create_version(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            comment="Route Version Comment",
            elements=[
                {
                    "id": "id",
                    "outputs": {"next": {"element_id": "elementId"}},
                    "type": "start",
                }
            ],
        )
        assert_matches_type(DynamicRoutingCreateVersionResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_raw_response_create_version(self, client: Cloudflare) -> None:
        response = client.ai_gateway.dynamic_routing.with_raw_response.create_version(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            comment="Route Version Comment",
            elements=[
                {
                    "id": "id",
                    "outputs": {"next": {"element_id": "elementId"}},
                    "type": "start",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = response.parse()
        assert_matches_type(DynamicRoutingCreateVersionResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_streaming_response_create_version(self, client: Cloudflare) -> None:
        with client.ai_gateway.dynamic_routing.with_streaming_response.create_version(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            comment="Route Version Comment",
            elements=[
                {
                    "id": "id",
                    "outputs": {"next": {"element_id": "elementId"}},
                    "type": "start",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = response.parse()
            assert_matches_type(DynamicRoutingCreateVersionResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_version(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.create_version(
                id="54442216",
                account_id="",
                gateway_id="54442216",
                comment="Route Version Comment",
                elements=[
                    {
                        "id": "id",
                        "outputs": {"next": {"element_id": "elementId"}},
                        "type": "start",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.create_version(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
                comment="Route Version Comment",
                elements=[
                    {
                        "id": "id",
                        "outputs": {"next": {"element_id": "elementId"}},
                        "type": "start",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.create_version(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
                comment="Route Version Comment",
                elements=[
                    {
                        "id": "id",
                        "outputs": {"next": {"element_id": "elementId"}},
                        "type": "start",
                    }
                ],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        dynamic_routing = client.ai_gateway.dynamic_routing.get(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )
        assert_matches_type(DynamicRoutingGetResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.ai_gateway.dynamic_routing.with_raw_response.get(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = response.parse()
        assert_matches_type(DynamicRoutingGetResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.ai_gateway.dynamic_routing.with_streaming_response.get(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = response.parse()
            assert_matches_type(DynamicRoutingGetResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.get(
                id="54442216",
                account_id="",
                gateway_id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.get(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.get(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
            )

    @parametrize
    def test_method_get_version(self, client: Cloudflare) -> None:
        dynamic_routing = client.ai_gateway.dynamic_routing.get_version(
            version_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            id="54442216",
        )
        assert_matches_type(DynamicRoutingGetVersionResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_raw_response_get_version(self, client: Cloudflare) -> None:
        response = client.ai_gateway.dynamic_routing.with_raw_response.get_version(
            version_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = response.parse()
        assert_matches_type(DynamicRoutingGetVersionResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_streaming_response_get_version(self, client: Cloudflare) -> None:
        with client.ai_gateway.dynamic_routing.with_streaming_response.get_version(
            version_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = response.parse()
            assert_matches_type(DynamicRoutingGetVersionResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_version(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.get_version(
                version_id="54442216",
                account_id="",
                gateway_id="54442216",
                id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.get_version(
                version_id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
                id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.get_version(
                version_id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.get_version(
                version_id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
                id="54442216",
            )

    @parametrize
    def test_method_list_deployments(self, client: Cloudflare) -> None:
        dynamic_routing = client.ai_gateway.dynamic_routing.list_deployments(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )
        assert_matches_type(DynamicRoutingListDeploymentsResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_raw_response_list_deployments(self, client: Cloudflare) -> None:
        response = client.ai_gateway.dynamic_routing.with_raw_response.list_deployments(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = response.parse()
        assert_matches_type(DynamicRoutingListDeploymentsResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_streaming_response_list_deployments(self, client: Cloudflare) -> None:
        with client.ai_gateway.dynamic_routing.with_streaming_response.list_deployments(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = response.parse()
            assert_matches_type(DynamicRoutingListDeploymentsResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_deployments(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.list_deployments(
                id="54442216",
                account_id="",
                gateway_id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.list_deployments(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.list_deployments(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
            )

    @parametrize
    def test_method_list_versions(self, client: Cloudflare) -> None:
        dynamic_routing = client.ai_gateway.dynamic_routing.list_versions(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )
        assert_matches_type(DynamicRoutingListVersionsResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_raw_response_list_versions(self, client: Cloudflare) -> None:
        response = client.ai_gateway.dynamic_routing.with_raw_response.list_versions(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = response.parse()
        assert_matches_type(DynamicRoutingListVersionsResponse, dynamic_routing, path=["response"])

    @parametrize
    def test_streaming_response_list_versions(self, client: Cloudflare) -> None:
        with client.ai_gateway.dynamic_routing.with_streaming_response.list_versions(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = response.parse()
            assert_matches_type(DynamicRoutingListVersionsResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_versions(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.list_versions(
                id="54442216",
                account_id="",
                gateway_id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.list_versions(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ai_gateway.dynamic_routing.with_raw_response.list_versions(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
            )


class TestAsyncDynamicRouting:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        dynamic_routing = await async_client.ai_gateway.dynamic_routing.create(
            gateway_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            elements=[
                {
                    "id": "id",
                    "outputs": {"next": {"element_id": "elementId"}},
                    "type": "start",
                }
            ],
            name="name",
        )
        assert_matches_type(DynamicRoutingCreateResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.dynamic_routing.with_raw_response.create(
            gateway_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            elements=[
                {
                    "id": "id",
                    "outputs": {"next": {"element_id": "elementId"}},
                    "type": "start",
                }
            ],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = await response.parse()
        assert_matches_type(DynamicRoutingCreateResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.dynamic_routing.with_streaming_response.create(
            gateway_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            elements=[
                {
                    "id": "id",
                    "outputs": {"next": {"element_id": "elementId"}},
                    "type": "start",
                }
            ],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = await response.parse()
            assert_matches_type(DynamicRoutingCreateResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.create(
                gateway_id="54442216",
                account_id="",
                elements=[
                    {
                        "id": "id",
                        "outputs": {"next": {"element_id": "elementId"}},
                        "type": "start",
                    }
                ],
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.create(
                gateway_id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                elements=[
                    {
                        "id": "id",
                        "outputs": {"next": {"element_id": "elementId"}},
                        "type": "start",
                    }
                ],
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        dynamic_routing = await async_client.ai_gateway.dynamic_routing.update(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            name="Route Name",
        )
        assert_matches_type(DynamicRoutingUpdateResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.dynamic_routing.with_raw_response.update(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            name="Route Name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = await response.parse()
        assert_matches_type(DynamicRoutingUpdateResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.dynamic_routing.with_streaming_response.update(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            name="Route Name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = await response.parse()
            assert_matches_type(DynamicRoutingUpdateResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.update(
                id="54442216",
                account_id="",
                gateway_id="54442216",
                name="Route Name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.update(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
                name="Route Name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.update(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
                name="Route Name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        dynamic_routing = await async_client.ai_gateway.dynamic_routing.list(
            gateway_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )
        assert_matches_type(DynamicRoutingListResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.dynamic_routing.with_raw_response.list(
            gateway_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = await response.parse()
        assert_matches_type(DynamicRoutingListResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.dynamic_routing.with_streaming_response.list(
            gateway_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = await response.parse()
            assert_matches_type(DynamicRoutingListResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.list(
                gateway_id="54442216",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.list(
                gateway_id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        dynamic_routing = await async_client.ai_gateway.dynamic_routing.delete(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )
        assert_matches_type(DynamicRoutingDeleteResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.dynamic_routing.with_raw_response.delete(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = await response.parse()
        assert_matches_type(DynamicRoutingDeleteResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.dynamic_routing.with_streaming_response.delete(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = await response.parse()
            assert_matches_type(DynamicRoutingDeleteResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.delete(
                id="54442216",
                account_id="",
                gateway_id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.delete(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.delete(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
            )

    @parametrize
    async def test_method_create_deployment(self, async_client: AsyncCloudflare) -> None:
        dynamic_routing = await async_client.ai_gateway.dynamic_routing.create_deployment(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            comment="Route Deployment Comment",
            version_id="54442216",
        )
        assert_matches_type(DynamicRoutingCreateDeploymentResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_raw_response_create_deployment(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.dynamic_routing.with_raw_response.create_deployment(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            comment="Route Deployment Comment",
            version_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = await response.parse()
        assert_matches_type(DynamicRoutingCreateDeploymentResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_streaming_response_create_deployment(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.dynamic_routing.with_streaming_response.create_deployment(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            comment="Route Deployment Comment",
            version_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = await response.parse()
            assert_matches_type(DynamicRoutingCreateDeploymentResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_deployment(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.create_deployment(
                id="54442216",
                account_id="",
                gateway_id="54442216",
                comment="Route Deployment Comment",
                version_id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.create_deployment(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
                comment="Route Deployment Comment",
                version_id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.create_deployment(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
                comment="Route Deployment Comment",
                version_id="54442216",
            )

    @parametrize
    async def test_method_create_version(self, async_client: AsyncCloudflare) -> None:
        dynamic_routing = await async_client.ai_gateway.dynamic_routing.create_version(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            comment="Route Version Comment",
            elements=[
                {
                    "id": "id",
                    "outputs": {"next": {"element_id": "elementId"}},
                    "type": "start",
                }
            ],
        )
        assert_matches_type(DynamicRoutingCreateVersionResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_raw_response_create_version(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.dynamic_routing.with_raw_response.create_version(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            comment="Route Version Comment",
            elements=[
                {
                    "id": "id",
                    "outputs": {"next": {"element_id": "elementId"}},
                    "type": "start",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = await response.parse()
        assert_matches_type(DynamicRoutingCreateVersionResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_streaming_response_create_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.dynamic_routing.with_streaming_response.create_version(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            comment="Route Version Comment",
            elements=[
                {
                    "id": "id",
                    "outputs": {"next": {"element_id": "elementId"}},
                    "type": "start",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = await response.parse()
            assert_matches_type(DynamicRoutingCreateVersionResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_version(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.create_version(
                id="54442216",
                account_id="",
                gateway_id="54442216",
                comment="Route Version Comment",
                elements=[
                    {
                        "id": "id",
                        "outputs": {"next": {"element_id": "elementId"}},
                        "type": "start",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.create_version(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
                comment="Route Version Comment",
                elements=[
                    {
                        "id": "id",
                        "outputs": {"next": {"element_id": "elementId"}},
                        "type": "start",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.create_version(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
                comment="Route Version Comment",
                elements=[
                    {
                        "id": "id",
                        "outputs": {"next": {"element_id": "elementId"}},
                        "type": "start",
                    }
                ],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        dynamic_routing = await async_client.ai_gateway.dynamic_routing.get(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )
        assert_matches_type(DynamicRoutingGetResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.dynamic_routing.with_raw_response.get(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = await response.parse()
        assert_matches_type(DynamicRoutingGetResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.dynamic_routing.with_streaming_response.get(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = await response.parse()
            assert_matches_type(DynamicRoutingGetResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.get(
                id="54442216",
                account_id="",
                gateway_id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.get(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.get(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
            )

    @parametrize
    async def test_method_get_version(self, async_client: AsyncCloudflare) -> None:
        dynamic_routing = await async_client.ai_gateway.dynamic_routing.get_version(
            version_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            id="54442216",
        )
        assert_matches_type(DynamicRoutingGetVersionResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_raw_response_get_version(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.dynamic_routing.with_raw_response.get_version(
            version_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = await response.parse()
        assert_matches_type(DynamicRoutingGetVersionResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_streaming_response_get_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.dynamic_routing.with_streaming_response.get_version(
            version_id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
            id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = await response.parse()
            assert_matches_type(DynamicRoutingGetVersionResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_version(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.get_version(
                version_id="54442216",
                account_id="",
                gateway_id="54442216",
                id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.get_version(
                version_id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
                id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.get_version(
                version_id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.get_version(
                version_id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
                id="54442216",
            )

    @parametrize
    async def test_method_list_deployments(self, async_client: AsyncCloudflare) -> None:
        dynamic_routing = await async_client.ai_gateway.dynamic_routing.list_deployments(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )
        assert_matches_type(DynamicRoutingListDeploymentsResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_raw_response_list_deployments(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.dynamic_routing.with_raw_response.list_deployments(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = await response.parse()
        assert_matches_type(DynamicRoutingListDeploymentsResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_streaming_response_list_deployments(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.dynamic_routing.with_streaming_response.list_deployments(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = await response.parse()
            assert_matches_type(DynamicRoutingListDeploymentsResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_deployments(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.list_deployments(
                id="54442216",
                account_id="",
                gateway_id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.list_deployments(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.list_deployments(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
            )

    @parametrize
    async def test_method_list_versions(self, async_client: AsyncCloudflare) -> None:
        dynamic_routing = await async_client.ai_gateway.dynamic_routing.list_versions(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )
        assert_matches_type(DynamicRoutingListVersionsResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_raw_response_list_versions(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.dynamic_routing.with_raw_response.list_versions(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_routing = await response.parse()
        assert_matches_type(DynamicRoutingListVersionsResponse, dynamic_routing, path=["response"])

    @parametrize
    async def test_streaming_response_list_versions(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.dynamic_routing.with_streaming_response.list_versions(
            id="54442216",
            account_id="0d37909e38d3e99c29fa2cd343ac421a",
            gateway_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_routing = await response.parse()
            assert_matches_type(DynamicRoutingListVersionsResponse, dynamic_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_versions(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.list_versions(
                id="54442216",
                account_id="",
                gateway_id="54442216",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.list_versions(
                id="54442216",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ai_gateway.dynamic_routing.with_raw_response.list_versions(
                id="",
                account_id="0d37909e38d3e99c29fa2cd343ac421a",
                gateway_id="54442216",
            )
