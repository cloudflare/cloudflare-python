# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.load_balancers.pools import ReferenceGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        reference = client.load_balancers.pools.references.get(
            pool_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ReferenceGetResponse, reference, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.references.with_raw_response.get(
            pool_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = response.parse()
        assert_matches_type(ReferenceGetResponse, reference, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.references.with_streaming_response.get(
            pool_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = response.parse()
            assert_matches_type(ReferenceGetResponse, reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.pools.references.with_raw_response.get(
                pool_id="17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.load_balancers.pools.references.with_raw_response.get(
                pool_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncReferences:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        reference = await async_client.load_balancers.pools.references.get(
            pool_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ReferenceGetResponse, reference, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.pools.references.with_raw_response.get(
            pool_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = await response.parse()
        assert_matches_type(ReferenceGetResponse, reference, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.pools.references.with_streaming_response.get(
            pool_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = await response.parse()
            assert_matches_type(ReferenceGetResponse, reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.pools.references.with_raw_response.get(
                pool_id="17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.load_balancers.pools.references.with_raw_response.get(
                pool_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
