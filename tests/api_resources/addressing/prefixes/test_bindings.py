# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.addressing.prefixes import (
    BindingCreateResponse,
    BindingListResponse,
    BindingDeleteResponse,
    BindingGetResponse,
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
from cloudflare.types.addressing.prefixes import binding_create_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBindings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        binding = client.addressing.prefixes.bindings.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BindingCreateResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        binding = client.addressing.prefixes.bindings.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="192.0.2.0/24",
            service_id="2db684ee7ca04e159946fd05b99e1bcd",
        )
        assert_matches_type(BindingCreateResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bindings.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = response.parse()
        assert_matches_type(BindingCreateResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bindings.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = response.parse()
            assert_matches_type(BindingCreateResponse, binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addressing.prefixes.bindings.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            client.addressing.prefixes.bindings.with_raw_response.create(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        binding = client.addressing.prefixes.bindings.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BindingListResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bindings.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = response.parse()
        assert_matches_type(BindingListResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bindings.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = response.parse()
            assert_matches_type(BindingListResponse, binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addressing.prefixes.bindings.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            client.addressing.prefixes.bindings.with_raw_response.list(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        binding = client.addressing.prefixes.bindings.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BindingDeleteResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bindings.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = response.parse()
        assert_matches_type(BindingDeleteResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bindings.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = response.parse()
            assert_matches_type(BindingDeleteResponse, binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addressing.prefixes.bindings.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            client.addressing.prefixes.bindings.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_identifier` but received ''"):
            client.addressing.prefixes.bindings.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        binding = client.addressing.prefixes.bindings.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BindingGetResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bindings.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = response.parse()
        assert_matches_type(BindingGetResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bindings.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = response.parse()
            assert_matches_type(BindingGetResponse, binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addressing.prefixes.bindings.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            client.addressing.prefixes.bindings.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_identifier` but received ''"):
            client.addressing.prefixes.bindings.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncBindings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        binding = await async_client.addressing.prefixes.bindings.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BindingCreateResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        binding = await async_client.addressing.prefixes.bindings.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="192.0.2.0/24",
            service_id="2db684ee7ca04e159946fd05b99e1bcd",
        )
        assert_matches_type(BindingCreateResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bindings.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = await response.parse()
        assert_matches_type(BindingCreateResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bindings.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = await response.parse()
            assert_matches_type(BindingCreateResponse, binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addressing.prefixes.bindings.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            await async_client.addressing.prefixes.bindings.with_raw_response.create(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        binding = await async_client.addressing.prefixes.bindings.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BindingListResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bindings.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = await response.parse()
        assert_matches_type(BindingListResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bindings.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = await response.parse()
            assert_matches_type(BindingListResponse, binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addressing.prefixes.bindings.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            await async_client.addressing.prefixes.bindings.with_raw_response.list(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        binding = await async_client.addressing.prefixes.bindings.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BindingDeleteResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bindings.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = await response.parse()
        assert_matches_type(BindingDeleteResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bindings.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = await response.parse()
            assert_matches_type(BindingDeleteResponse, binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addressing.prefixes.bindings.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            await async_client.addressing.prefixes.bindings.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_identifier` but received ''"):
            await async_client.addressing.prefixes.bindings.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        binding = await async_client.addressing.prefixes.bindings.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BindingGetResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bindings.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binding = await response.parse()
        assert_matches_type(BindingGetResponse, binding, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bindings.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binding = await response.parse()
            assert_matches_type(BindingGetResponse, binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addressing.prefixes.bindings.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            await async_client.addressing.prefixes.bindings.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_identifier` but received ''"):
            await async_client.addressing.prefixes.bindings.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
