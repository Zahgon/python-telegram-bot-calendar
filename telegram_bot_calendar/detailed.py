from calendar import monthrange

from telegram_bot_calendar.base import *

STEPS = {YEAR: MONTH, MONTH: DAY}

PREV_STEPS = {DAY: MONTH, MONTH: YEAR, YEAR: YEAR}
PREV_ACTIONS = {DAY: GOTO, MONTH: GOTO, YEAR: NOTHING}


class DetailedTelegramCalendar(TelegramCalendar):
    first_step = YEAR

    def __init__(self, calendar_id=0, current_date=None, additional_buttons=None, locale='en',
                 min_date=None,
                 max_date=None, telethon=False, **kwargs):
        super(DetailedTelegramCalendar, self).__init__(calendar_id, current_date=current_date,
                                                       additional_buttons=additional_buttons, locale=locale,
                                                       min_date=min_date, max_date=max_date, is_random=False, telethon=telethon, **kwargs)

    def _build(self, step=None, **kwargs):
        pass

    def _process(self, call_data, *args, **kwargs):
        pass

    def _build_years(self, *args, **kwargs):
        pass

    def _build_months(self, *args, **kwargs):
        pass

    def _build_days(self, *args, **kwargs):
        pass

    def _build_nav_buttons(self, step, diff, mind, maxd, *args, **kwargs):

        pass

    def _get_period(self, step, start, diff, *args, **kwargs):
        pass
