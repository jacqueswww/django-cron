from django.db import models
from django_cron.enums import (
    CronStatus,
    CRON_STATUS_CHOICES,
)


class CronJobLog(models.Model):
    """
    Keeps track of the cron jobs that ran etc. and any error
    messages if they failed.
    """

    code = models.CharField(max_length=64, db_index=True)
    start_time = models.DateTimeField(db_index=True)
    end_time = models.DateTimeField(db_index=True)
    status = models.IntegerField(default=CronStatus.NONE, choices=CRON_STATUS_CHOICES, db_index=True)
    message = models.TextField(default='', blank=True)

    # This field is used to mark jobs executed in exact time.
    # Jobs that run every X minutes, have this field empty.
    ran_at_time = models.TimeField(
        null=True, blank=True, db_index=True, editable=False
    )

    def __unicode__(self):
        return '%s (%s)' % (self.code, 'Success' if self.is_success else 'Fail')

    def __str__(self):
        return "%s (%s)" % (self.code, "Success" if self.is_success else "Fail")

    class Meta:
        indexes = [
            models.Index(fields=['code', 'status', 'ran_at_time']),
            models.Index(fields=['code', 'start_time', 'ran_at_time']),
            models.Index(fields=['code', 'start_time',]),
        ]

    @property
    def is_success(self):
        return self.status == CronStatus.SUCCESS


class CronJobLock(models.Model):
    job_name = models.CharField(max_length=200, unique=True)
    locked = models.BooleanField(default=False)
