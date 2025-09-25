import subprocess
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import AccessLog

LOGFILE = 'system_events.log'



# Helper function to append a line to the log file with timestamp
def append_event_line(line: str):
    ts = timezone.localtime().strftime('%Y-%m-%d %H:%M:%S')
    full = f"[{ts}] - {line}"
    safe = full.replace("'", "'\"'\"'")
    cmd = f"/bin/sh -lc 'echo \"{safe}\" >> {LOGFILE}'"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except Exception:
        pass



# Signal handler for post_save -logs creation of AccessLog entries
@receiver(post_save, sender=AccessLog)
def handle_create(sender, instance, created, **kwargs):
    if created:
        status = 'GRANTED' if instance.access_granted else 'DENIED'
        line = f"CREATE: Access log created for card {instance.card_id}. Status: {status}."
        append_event_line(line)


# Signal handler for post_delete: logs deletion of AccessLog entries
@receiver(post_delete, sender=AccessLog)
def handle_delete(sender, instance, **kwargs):
    line = f"DELETE: Access log (ID: {instance.pk}) for card {instance.card_id} was deleted."
    append_event_line(line)

