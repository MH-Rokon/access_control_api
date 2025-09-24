from django.test import TestCase
from datetime import datetime, timezone
from .models import AccessLog

class AccessLogAPITest(TestCase):
    def setUp(self):
        self.log1 = AccessLog.objects.create(
            card_id="C1001",
            door_name="Main Entrance",
            access_granted=True
        )
        self.log2 = AccessLog.objects.create(
            card_id="C1002",
            door_name="Side Door",
            access_granted=False
        )

    def test_get_logs_list(self):
        logs = AccessLog.objects.all()
        self.assertEqual(logs.count(), 2)

    def test_delete_log(self):
        self.log1.delete()
        logs = AccessLog.objects.all()
        self.assertEqual(logs.count(), 1)

    def test_update_log(self):
        self.log2.access_granted = True
        self.log2.save()
        updated_log = AccessLog.objects.get(id=self.log2.id)
        self.assertTrue(updated_log.access_granted)

    def test_filter_by_card_id(self):
        logs = AccessLog.objects.filter(card_id="C1001")
        self.assertEqual(logs.count(), 1)

    def test_get_log_detail(self):
        log = AccessLog.objects.get(card_id="C1002")
        self.assertEqual(log.door_name, "Side Door")

    def test_timestamp_readonly(self):
        original_time = self.log1.timestamp
        new_time = datetime(2025, 1, 1, tzinfo=timezone.utc)
        self.log1.timestamp = new_time
        self.log1.save()
        updated_log = AccessLog.objects.get(id=self.log1.id)
        self.assertEqual(updated_log.timestamp, new_time)
