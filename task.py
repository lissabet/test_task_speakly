from datetime import datetime, timedelta
from typing import List

from constants import LEADERBOARD_DAYS_DELTA, MIN_ACTION_COUNT
from enums import ActionName


class Event:

    def __init__(self, user_id: int, event_date: datetime, action_name: str):
        self.user_id = user_id
        self.event_date = event_date
        self.action_name = action_name

    @property
    def is_word_learnt(self) -> bool:
        return self.action_name == ActionName.WORD_LEARNT.value


def get_30_day_leaderboard_user_ids(engagement_events: List[Event]) -> List[int]:
    event_date_delta = datetime.now() - timedelta(days=LEADERBOARD_DAYS_DELTA)

    events_count_mapping = {}
    result_events_mapping = {}

    for event in engagement_events:
        if event.event_date >= event_date_delta:
            words_learnt_events_count, events_count = events_count_mapping.get(
                event.user_id, (0, 0)
            )

            events_count += 1
            if event.is_word_learnt:
                words_learnt_events_count += 1

            events_count_mapping[event.user_id] = (words_learnt_events_count, events_count, )

            if events_count >= MIN_ACTION_COUNT:
                result_events_mapping[event.user_id] = words_learnt_events_count

    return sorted(result_events_mapping.keys(), key=result_events_mapping.get, reverse=True)


"""
Uncomment this section and run this file to test if your code could be working.
Note that this is only an example and does not substitute any unit tests
"""

if __name__ == '__main__':
    yesterday = datetime.now() - timedelta(days=1)
    events = [
        Event(1, yesterday, ActionName.WORD_LEARNT.value),
        Event(1, yesterday, ActionName.WORD_LEARNT.value),
        Event(1, yesterday, ActionName.WORD_LEARNT.value),
        Event(1, yesterday, ActionName.WORD_LEARNT.value),
        Event(2, yesterday, ActionName.WORD_LEARNT.value),
        Event(2, yesterday, ActionName.WORD_LEARNT.value),
        Event(3, yesterday, ActionName.WORD_LEARNT.value),
        Event(4, yesterday, ActionName.WORD_LEARNT.value)
    ]

    for i in range(16):
        events.append(Event(1, yesterday, ActionName.CORRECT_ANSWER.value))
        events.append(Event(2, yesterday, ActionName.CORRECT_ANSWER.value))
        events.append(Event(3, yesterday, ActionName.CORRECT_ANSWER.value))

    leaderboard = get_30_day_leaderboard_user_ids(events)
    assert (leaderboard == [1, 2, 3, ])
