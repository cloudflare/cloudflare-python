# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.alerting.destinations import (
    Pagerduty,
    PagerdutyLinkResponse,
    PagerdutyCreateResponse,
    PagerdutyDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPagerduty:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        pagerduty = client.alerting.destinations.pagerduty.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PagerdutyCreateResponse], pagerduty, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.alerting.destinations.pagerduty.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = response.parse()
        assert_matches_type(Optional[PagerdutyCreateResponse], pagerduty, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.alerting.destinations.pagerduty.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = response.parse()
            assert_matches_type(Optional[PagerdutyCreateResponse], pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.destinations.pagerduty.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        pagerduty = client.alerting.destinations.pagerduty.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PagerdutyDeleteResponse, pagerduty, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.alerting.destinations.pagerduty.with_raw_response.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = response.parse()
        assert_matches_type(PagerdutyDeleteResponse, pagerduty, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.alerting.destinations.pagerduty.with_streaming_response.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = response.parse()
            assert_matches_type(PagerdutyDeleteResponse, pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.destinations.pagerduty.with_raw_response.delete(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        pagerduty = client.alerting.destinations.pagerduty.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Pagerduty], pagerduty, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.alerting.destinations.pagerduty.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = response.parse()
        assert_matches_type(SyncSinglePage[Pagerduty], pagerduty, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.alerting.destinations.pagerduty.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = response.parse()
            assert_matches_type(SyncSinglePage[Pagerduty], pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.destinations.pagerduty.with_raw_response.get(
                account_id="",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    def test_method_link(self, client: Cloudflare) -> None:
        pagerduty = client.alerting.destinations.pagerduty.link(
            token_id="8c71e667571b4f61b94d9e4b12158038",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PagerdutyLinkResponse], pagerduty, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    def test_raw_response_link(self, client: Cloudflare) -> None:
        response = client.alerting.destinations.pagerduty.with_raw_response.link(
            token_id="8c71e667571b4f61b94d9e4b12158038",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = response.parse()
        assert_matches_type(Optional[PagerdutyLinkResponse], pagerduty, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    def test_streaming_response_link(self, client: Cloudflare) -> None:
        with client.alerting.destinations.pagerduty.with_streaming_response.link(
            token_id="8c71e667571b4f61b94d9e4b12158038",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = response.parse()
            assert_matches_type(Optional[PagerdutyLinkResponse], pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    def test_path_params_link(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.destinations.pagerduty.with_raw_response.link(
                token_id="8c71e667571b4f61b94d9e4b12158038",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            client.alerting.destinations.pagerduty.with_raw_response.link(
                token_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPagerduty:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        pagerduty = await async_client.alerting.destinations.pagerduty.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PagerdutyCreateResponse], pagerduty, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.destinations.pagerduty.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = await response.parse()
        assert_matches_type(Optional[PagerdutyCreateResponse], pagerduty, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.destinations.pagerduty.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = await response.parse()
            assert_matches_type(Optional[PagerdutyCreateResponse], pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.destinations.pagerduty.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        pagerduty = await async_client.alerting.destinations.pagerduty.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PagerdutyDeleteResponse, pagerduty, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.destinations.pagerduty.with_raw_response.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = await response.parse()
        assert_matches_type(PagerdutyDeleteResponse, pagerduty, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.destinations.pagerduty.with_streaming_response.delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = await response.parse()
            assert_matches_type(PagerdutyDeleteResponse, pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.destinations.pagerduty.with_raw_response.delete(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        pagerduty = await async_client.alerting.destinations.pagerduty.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Pagerduty], pagerduty, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.destinations.pagerduty.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = await response.parse()
        assert_matches_type(AsyncSinglePage[Pagerduty], pagerduty, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.destinations.pagerduty.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = await response.parse()
            assert_matches_type(AsyncSinglePage[Pagerduty], pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.destinations.pagerduty.with_raw_response.get(
                account_id="",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    async def test_method_link(self, async_client: AsyncCloudflare) -> None:
        pagerduty = await async_client.alerting.destinations.pagerduty.link(
            token_id="8c71e667571b4f61b94d9e4b12158038",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PagerdutyLinkResponse], pagerduty, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    async def test_raw_response_link(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.destinations.pagerduty.with_raw_response.link(
            token_id="8c71e667571b4f61b94d9e4b12158038",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = await response.parse()
        assert_matches_type(Optional[PagerdutyLinkResponse], pagerduty, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    async def test_streaming_response_link(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.destinations.pagerduty.with_streaming_response.link(
            token_id="8c71e667571b4f61b94d9e4b12158038",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = await response.parse()
            assert_matches_type(Optional[PagerdutyLinkResponse], pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4285"
    )
    @parametrize
    async def test_path_params_link(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.destinations.pagerduty.with_raw_response.link(
                token_id="8c71e667571b4f61b94d9e4b12158038",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            await async_client.alerting.destinations.pagerduty.with_raw_response.link(
                token_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
