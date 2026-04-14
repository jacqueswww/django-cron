
class CronStatus:
    NONE = 0
    RUNNING = 1
    SUCCESS = 2
    FAILED = 3


CRON_STATUS_CHOICES = [
    (CronStatus.NONE, 'None'),
    (CronStatus.RUNNING, 'Running'),
    (CronStatus.SUCCESS, 'Success'),
    (CronStatus.FAILED, 'Failed'),
]
