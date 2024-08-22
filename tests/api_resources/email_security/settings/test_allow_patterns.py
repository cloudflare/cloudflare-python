# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.email_security.settings import AllowPatternCreateResponse, AllowPatternListResponse, AllowPatternDeleteResponse, AllowPatternEditResponse, AllowPatternGetResponse

from typing import Any, cast

from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.email_security.settings import allow_pattern_create_params
from cloudflare.types.email_security.settings import allow_pattern_list_params
from cloudflare.types.email_security.settings import allow_pattern_edit_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestAllowPatterns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        allow_pattern = client.email_security.settings.allow_patterns.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recipient=False,
            is_regex=False,
            is_sender=True,
            is_spoof=False,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
        )
        assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        allow_pattern = client.email_security.settings.allow_patterns.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recipient=False,
            is_regex=False,
            is_sender=True,
            is_spoof=False,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
            comments="Trust all messages send from test@example.com",
        )
        assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:

        response = client.email_security.settings.allow_patterns.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recipient=False,
            is_regex=False,
            is_sender=True,
            is_spoof=False,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        allow_pattern = response.parse()
        assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.email_security.settings.allow_patterns.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recipient=False,
            is_regex=False,
            is_sender=True,
            is_spoof=False,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            allow_pattern = response.parse()
            assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.email_security.settings.allow_patterns.with_raw_response.create(
              account_id="",
              is_recipient=False,
              is_regex=False,
              is_sender=True,
              is_spoof=False,
              pattern="test@example.com",
              pattern_type="EMAIL",
              verify_sender=True,
          )

    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        allow_pattern = client.email_security.settings.allow_patterns.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }, {
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }, {
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }],
        )
        assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:

        response = client.email_security.settings.allow_patterns.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }, {
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }, {
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        allow_pattern = response.parse()
        assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.email_security.settings.allow_patterns.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }, {
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }, {
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            allow_pattern = response.parse()
            assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.email_security.settings.allow_patterns.with_raw_response.create(
              account_id="",
              body=[{
                  "is_recipient": False,
                  "is_regex": False,
                  "is_sender": True,
                  "is_spoof": False,
                  "pattern": "test@example.com",
                  "pattern_type": "EMAIL",
                  "verify_sender": True,
              }, {
                  "is_recipient": False,
                  "is_regex": False,
                  "is_sender": True,
                  "is_spoof": False,
                  "pattern": "test@example.com",
                  "pattern_type": "EMAIL",
                  "verify_sender": True,
              }, {
                  "is_recipient": False,
                  "is_regex": False,
                  "is_sender": True,
                  "is_spoof": False,
                  "pattern": "test@example.com",
                  "pattern_type": "EMAIL",
                  "verify_sender": True,
              }],
          )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        allow_pattern = client.email_security.settings.allow_patterns.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[AllowPatternListResponse], allow_pattern, path=['response'])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        allow_pattern = client.email_security.settings.allow_patterns.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            is_recipient=True,
            is_sender=True,
            is_spoof=True,
            order="pattern",
            page=1,
            pattern_type="EMAIL",
            per_page=1,
            search="search",
            verify_sender=True,
        )
        assert_matches_type(SyncV4PagePaginationArray[AllowPatternListResponse], allow_pattern, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:

        response = client.email_security.settings.allow_patterns.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        allow_pattern = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[AllowPatternListResponse], allow_pattern, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.email_security.settings.allow_patterns.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            allow_pattern = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[AllowPatternListResponse], allow_pattern, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.email_security.settings.allow_patterns.with_raw_response.list(
              account_id="",
          )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        allow_pattern = client.email_security.settings.allow_patterns.delete(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AllowPatternDeleteResponse, allow_pattern, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:

        response = client.email_security.settings.allow_patterns.with_raw_response.delete(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        allow_pattern = response.parse()
        assert_matches_type(AllowPatternDeleteResponse, allow_pattern, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.email_security.settings.allow_patterns.with_streaming_response.delete(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            allow_pattern = response.parse()
            assert_matches_type(AllowPatternDeleteResponse, allow_pattern, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.email_security.settings.allow_patterns.with_raw_response.delete(
              pattern_id=2401,
              account_id="",
          )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        allow_pattern = client.email_security.settings.allow_patterns.edit(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AllowPatternEditResponse, allow_pattern, path=['response'])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        allow_pattern = client.email_security.settings.allow_patterns.edit(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            comments="comments",
            is_recipient=True,
            is_regex=True,
            is_sender=True,
            is_spoof=True,
            pattern="x",
            pattern_type="EMAIL",
            verify_sender=True,
        )
        assert_matches_type(AllowPatternEditResponse, allow_pattern, path=['response'])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:

        response = client.email_security.settings.allow_patterns.with_raw_response.edit(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        allow_pattern = response.parse()
        assert_matches_type(AllowPatternEditResponse, allow_pattern, path=['response'])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.email_security.settings.allow_patterns.with_streaming_response.edit(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            allow_pattern = response.parse()
            assert_matches_type(AllowPatternEditResponse, allow_pattern, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.email_security.settings.allow_patterns.with_raw_response.edit(
              pattern_id=2401,
              account_id="",
          )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        allow_pattern = client.email_security.settings.allow_patterns.get(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AllowPatternGetResponse, allow_pattern, path=['response'])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.email_security.settings.allow_patterns.with_raw_response.get(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        allow_pattern = response.parse()
        assert_matches_type(AllowPatternGetResponse, allow_pattern, path=['response'])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_security.settings.allow_patterns.with_streaming_response.get(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            allow_pattern = response.parse()
            assert_matches_type(AllowPatternGetResponse, allow_pattern, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.email_security.settings.allow_patterns.with_raw_response.get(
              pattern_id=2401,
              account_id="",
          )
class TestAsyncAllowPatterns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        allow_pattern = await async_client.email_security.settings.allow_patterns.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recipient=False,
            is_regex=False,
            is_sender=True,
            is_spoof=False,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
        )
        assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        allow_pattern = await async_client.email_security.settings.allow_patterns.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recipient=False,
            is_regex=False,
            is_sender=True,
            is_spoof=False,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
            comments="Trust all messages send from test@example.com",
        )
        assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.email_security.settings.allow_patterns.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recipient=False,
            is_regex=False,
            is_sender=True,
            is_spoof=False,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        allow_pattern = await response.parse()
        assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.allow_patterns.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_recipient=False,
            is_regex=False,
            is_sender=True,
            is_spoof=False,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            allow_pattern = await response.parse()
            assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.email_security.settings.allow_patterns.with_raw_response.create(
              account_id="",
              is_recipient=False,
              is_regex=False,
              is_sender=True,
              is_spoof=False,
              pattern="test@example.com",
              pattern_type="EMAIL",
              verify_sender=True,
          )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        allow_pattern = await async_client.email_security.settings.allow_patterns.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }, {
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }, {
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }],
        )
        assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.email_security.settings.allow_patterns.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }, {
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }, {
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        allow_pattern = await response.parse()
        assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.allow_patterns.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }, {
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }, {
                "is_recipient": False,
                "is_regex": False,
                "is_sender": True,
                "is_spoof": False,
                "pattern": "test@example.com",
                "pattern_type": "EMAIL",
                "verify_sender": True,
            }],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            allow_pattern = await response.parse()
            assert_matches_type(AllowPatternCreateResponse, allow_pattern, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.email_security.settings.allow_patterns.with_raw_response.create(
              account_id="",
              body=[{
                  "is_recipient": False,
                  "is_regex": False,
                  "is_sender": True,
                  "is_spoof": False,
                  "pattern": "test@example.com",
                  "pattern_type": "EMAIL",
                  "verify_sender": True,
              }, {
                  "is_recipient": False,
                  "is_regex": False,
                  "is_sender": True,
                  "is_spoof": False,
                  "pattern": "test@example.com",
                  "pattern_type": "EMAIL",
                  "verify_sender": True,
              }, {
                  "is_recipient": False,
                  "is_regex": False,
                  "is_sender": True,
                  "is_spoof": False,
                  "pattern": "test@example.com",
                  "pattern_type": "EMAIL",
                  "verify_sender": True,
              }],
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        allow_pattern = await async_client.email_security.settings.allow_patterns.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[AllowPatternListResponse], allow_pattern, path=['response'])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        allow_pattern = await async_client.email_security.settings.allow_patterns.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            is_recipient=True,
            is_sender=True,
            is_spoof=True,
            order="pattern",
            page=1,
            pattern_type="EMAIL",
            per_page=1,
            search="search",
            verify_sender=True,
        )
        assert_matches_type(AsyncV4PagePaginationArray[AllowPatternListResponse], allow_pattern, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.email_security.settings.allow_patterns.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        allow_pattern = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[AllowPatternListResponse], allow_pattern, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.allow_patterns.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            allow_pattern = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[AllowPatternListResponse], allow_pattern, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.email_security.settings.allow_patterns.with_raw_response.list(
              account_id="",
          )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        allow_pattern = await async_client.email_security.settings.allow_patterns.delete(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AllowPatternDeleteResponse, allow_pattern, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.email_security.settings.allow_patterns.with_raw_response.delete(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        allow_pattern = await response.parse()
        assert_matches_type(AllowPatternDeleteResponse, allow_pattern, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.allow_patterns.with_streaming_response.delete(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            allow_pattern = await response.parse()
            assert_matches_type(AllowPatternDeleteResponse, allow_pattern, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.email_security.settings.allow_patterns.with_raw_response.delete(
              pattern_id=2401,
              account_id="",
          )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        allow_pattern = await async_client.email_security.settings.allow_patterns.edit(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AllowPatternEditResponse, allow_pattern, path=['response'])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        allow_pattern = await async_client.email_security.settings.allow_patterns.edit(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            comments="comments",
            is_recipient=True,
            is_regex=True,
            is_sender=True,
            is_spoof=True,
            pattern="x",
            pattern_type="EMAIL",
            verify_sender=True,
        )
        assert_matches_type(AllowPatternEditResponse, allow_pattern, path=['response'])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.email_security.settings.allow_patterns.with_raw_response.edit(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        allow_pattern = await response.parse()
        assert_matches_type(AllowPatternEditResponse, allow_pattern, path=['response'])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.allow_patterns.with_streaming_response.edit(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            allow_pattern = await response.parse()
            assert_matches_type(AllowPatternEditResponse, allow_pattern, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.email_security.settings.allow_patterns.with_raw_response.edit(
              pattern_id=2401,
              account_id="",
          )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        allow_pattern = await async_client.email_security.settings.allow_patterns.get(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AllowPatternGetResponse, allow_pattern, path=['response'])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.email_security.settings.allow_patterns.with_raw_response.get(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        allow_pattern = await response.parse()
        assert_matches_type(AllowPatternGetResponse, allow_pattern, path=['response'])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.allow_patterns.with_streaming_response.get(
            pattern_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            allow_pattern = await response.parse()
            assert_matches_type(AllowPatternGetResponse, allow_pattern, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.email_security.settings.allow_patterns.with_raw_response.get(
              pattern_id=2401,
              account_id="",
          )