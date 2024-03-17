from django.core.management.base import BaseCommand
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from auditlog.models import LogEntry


class Command(BaseCommand):
    help = "Cleanup auditlog entries"

    def _generate_row(self, log_entry):
        return f"{log_entry.timestamp} {log_entry.get_action_display()} {log_entry.content_type} {log_entry.action} {log_entry.changes}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--retention_days", "-r", type=int, default=1825, help="Retention days"
        )

    def handle(self, *args, **options):
        retention_days = options["retention_days"]

        result = LogEntry.objects.filter(
            timestamp__date__lt=(
                timezone.now() - relativedelta(days=retention_days)
            ).date()
        ).delete()
        c = result[0]

        self.stdout.write(self.style.SUCCESS(f"Deleted {c} rows"))
