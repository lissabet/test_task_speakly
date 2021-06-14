from datetime import datetime, timedelta
from typing import List
from unittest import TestCase

from constants import MIN_ACTION_COUNT
from enums import ActionName
from task import Event, get_30_day_leaderboard_user_ids


def generate_test_events(
        user_id: int,
        event_date: datetime,
        action_name: ActionName,
        event_count: int,
) -> List[Event]:
    events = []
    for i in range(event_count):
        events.append(Event(user_id, event_date, action_name.value))

    return events


class Get30DayLeaderboardUserIdsTestCase(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_data = datetime.now() - timedelta(days=1)

    def test_ok_with_2_users(self):
        # Generate test data for user_id=1
        events = generate_test_events(
            user_id=1,
            event_date=self.test_data,
            action_name=ActionName.INCORRECT_ANSWER,
            event_count=MIN_ACTION_COUNT + 1,
        )
        events.extend(generate_test_events(
            user_id=1,
            event_date=self.test_data,
            action_name=ActionName.WORD_LEARNT,
            event_count=3,
        ))

        # Generate test data for user_id=2
        events.extend(generate_test_events(
            user_id=2,
            event_date=self.test_data,
            action_name=ActionName.INCORRECT_ANSWER,
            event_count=10,
        ))
        events.extend(generate_test_events(
            user_id=2,
            event_date=self.test_data,
            action_name=ActionName.WORD_LEARNT,
            event_count=10,
        ))

        result = get_30_day_leaderboard_user_ids(engagement_events=events)
        self.assertListEqual(result, [2, 1])

    def test_ok_with_empty_result(self):
        # Generate test data for user_id=1
        events = generate_test_events(
            user_id=1,
            event_date=self.test_data,
            action_name=ActionName.INCORRECT_ANSWER,
            event_count=MIN_ACTION_COUNT - 1,
        )

        # Generate test data for user_id=2
        events.extend(generate_test_events(
            user_id=2,
            event_date=self.test_data,
            action_name=ActionName.INCORRECT_ANSWER,
            event_count=10,
        ))

        result = get_30_day_leaderboard_user_ids(engagement_events=events)
        self.assertListEqual(result, [])
