# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.workers.scripts import (
    ScheduleWorkerCronTriggerGetCronTriggersResponse,
    ScheduleWorkerCronTriggerUpdateCronTriggersResponse,
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
from cloudflare.types.workers.scripts import schedule_worker_cron_trigger_update_cron_triggers_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_cron_trigger_get_cron_triggers(self, client: Cloudflare) -> None:
        schedule = client.workers.scripts.schedules.worker_cron_trigger_get_cron_triggers(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ScheduleWorkerCronTriggerGetCronTriggersResponse, schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_cron_trigger_get_cron_triggers(self, client: Cloudflare) -> None:
        response = client.workers.scripts.schedules.with_raw_response.worker_cron_trigger_get_cron_triggers(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleWorkerCronTriggerGetCronTriggersResponse, schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_cron_trigger_get_cron_triggers(self, client: Cloudflare) -> None:
        with client.workers.scripts.schedules.with_streaming_response.worker_cron_trigger_get_cron_triggers(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleWorkerCronTriggerGetCronTriggersResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_cron_trigger_get_cron_triggers(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.schedules.with_raw_response.worker_cron_trigger_get_cron_triggers(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.schedules.with_raw_response.worker_cron_trigger_get_cron_triggers(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_cron_trigger_update_cron_triggers(self, client: Cloudflare) -> None:
        schedule = client.workers.scripts.schedules.worker_cron_trigger_update_cron_triggers(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="[{'cron': '*/30 * * * *'}]",
        )
        assert_matches_type(ScheduleWorkerCronTriggerUpdateCronTriggersResponse, schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_cron_trigger_update_cron_triggers(self, client: Cloudflare) -> None:
        response = client.workers.scripts.schedules.with_raw_response.worker_cron_trigger_update_cron_triggers(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="[{'cron': '*/30 * * * *'}]",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleWorkerCronTriggerUpdateCronTriggersResponse, schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_cron_trigger_update_cron_triggers(self, client: Cloudflare) -> None:
        with client.workers.scripts.schedules.with_streaming_response.worker_cron_trigger_update_cron_triggers(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="[{'cron': '*/30 * * * *'}]",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleWorkerCronTriggerUpdateCronTriggersResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_cron_trigger_update_cron_triggers(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.schedules.with_raw_response.worker_cron_trigger_update_cron_triggers(
                "this-is_my_script-01",
                account_id="",
                body="[{'cron': '*/30 * * * *'}]",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.schedules.with_raw_response.worker_cron_trigger_update_cron_triggers(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body="[{'cron': '*/30 * * * *'}]",
            )


class TestAsyncSchedules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_cron_trigger_get_cron_triggers(self, async_client: AsyncCloudflare) -> None:
        schedule = await async_client.workers.scripts.schedules.worker_cron_trigger_get_cron_triggers(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ScheduleWorkerCronTriggerGetCronTriggersResponse, schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_cron_trigger_get_cron_triggers(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.schedules.with_raw_response.worker_cron_trigger_get_cron_triggers(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleWorkerCronTriggerGetCronTriggersResponse, schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_cron_trigger_get_cron_triggers(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.workers.scripts.schedules.with_streaming_response.worker_cron_trigger_get_cron_triggers(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleWorkerCronTriggerGetCronTriggersResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_cron_trigger_get_cron_triggers(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.schedules.with_raw_response.worker_cron_trigger_get_cron_triggers(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.schedules.with_raw_response.worker_cron_trigger_get_cron_triggers(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_cron_trigger_update_cron_triggers(self, async_client: AsyncCloudflare) -> None:
        schedule = await async_client.workers.scripts.schedules.worker_cron_trigger_update_cron_triggers(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="[{'cron': '*/30 * * * *'}]",
        )
        assert_matches_type(ScheduleWorkerCronTriggerUpdateCronTriggersResponse, schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_cron_trigger_update_cron_triggers(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.workers.scripts.schedules.with_raw_response.worker_cron_trigger_update_cron_triggers(
                "this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body="[{'cron': '*/30 * * * *'}]",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleWorkerCronTriggerUpdateCronTriggersResponse, schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_cron_trigger_update_cron_triggers(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.workers.scripts.schedules.with_streaming_response.worker_cron_trigger_update_cron_triggers(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="[{'cron': '*/30 * * * *'}]",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleWorkerCronTriggerUpdateCronTriggersResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_cron_trigger_update_cron_triggers(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.schedules.with_raw_response.worker_cron_trigger_update_cron_triggers(
                "this-is_my_script-01",
                account_id="",
                body="[{'cron': '*/30 * * * *'}]",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.schedules.with_raw_response.worker_cron_trigger_update_cron_triggers(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body="[{'cron': '*/30 * * * *'}]",
            )
