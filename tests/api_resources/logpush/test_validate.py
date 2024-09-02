# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.logpush import ValidateDestinationResponse, ValidateOriginResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.logpush import validate_destination_params
from cloudflare.types.logpush import validate_origin_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_destination(self, client: Cloudflare) -> None:
        validate = client.logpush.validate.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_destination_with_all_params(self, client: Cloudflare) -> None:
        validate = client.logpush.validate.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_destination(self, client: Cloudflare) -> None:
        response = client.logpush.validate.with_raw_response.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = response.parse()
        assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_destination(self, client: Cloudflare) -> None:
        with client.logpush.validate.with_streaming_response.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = response.parse()
            assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_destination(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.validate.with_raw_response.destination(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.logpush.validate.with_raw_response.destination(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_origin(self, client: Cloudflare) -> None:
        validate = client.logpush.validate.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_origin_with_all_params(self, client: Cloudflare) -> None:
        validate = client.logpush.validate.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_origin(self, client: Cloudflare) -> None:
        response = client.logpush.validate.with_raw_response.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = response.parse()
        assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_origin(self, client: Cloudflare) -> None:
        with client.logpush.validate.with_streaming_response.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = response.parse()
            assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_origin(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.validate.with_raw_response.origin(
                logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.logpush.validate.with_raw_response.origin(
                logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
                account_id="account_id",
            )


class TestAsyncValidate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_destination(self, async_client: AsyncCloudflare) -> None:
        validate = await async_client.logpush.validate.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_destination_with_all_params(self, async_client: AsyncCloudflare) -> None:
        validate = await async_client.logpush.validate.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_destination(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.validate.with_raw_response.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = await response.parse()
        assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_destination(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.validate.with_streaming_response.destination(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = await response.parse()
            assert_matches_type(Optional[ValidateDestinationResponse], validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_destination(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.validate.with_raw_response.destination(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.logpush.validate.with_raw_response.destination(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_origin(self, async_client: AsyncCloudflare) -> None:
        validate = await async_client.logpush.validate.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_origin_with_all_params(self, async_client: AsyncCloudflare) -> None:
        validate = await async_client.logpush.validate.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        )
        assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_origin(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.validate.with_raw_response.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = await response.parse()
        assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_origin(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.validate.with_streaming_response.origin(
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = await response.parse()
            assert_matches_type(Optional[ValidateOriginResponse], validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_origin(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.validate.with_raw_response.origin(
                logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.logpush.validate.with_raw_response.origin(
                logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
                account_id="account_id",
            )
