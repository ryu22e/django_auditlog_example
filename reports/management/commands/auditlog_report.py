from pathlib import Path
from datetime import timezone

from django.core.management.base import BaseCommand
from dateutil.parser import parse
from auditlog.models import LogEntry


class Command(BaseCommand):
    help = "Output audit log report"

    def _generate_row(self, log_entry):
        return f"{log_entry.timestamp} {log_entry.actor} {log_entry.content_type} {log_entry.action} {log_entry.changes}"

    def add_arguments(self, parser):
        parser.add_argument("--start_datetime", "-s", type=str, help="Start datetime")
        parser.add_argument("--end_datetime", "-e", type=str, help="End datetime")
        parser.add_argument("--output_file", "-o", type=str, help="Output file")

    def handle(self, *args, **options):
        start_datetime = parse(options["start_datetime"]).astimezone(timezone.utc)
        end_datetime = parse(options["end_datetime"]).astimezone(timezone.utc)
        output_file = options["output_file"]

        p = Path(output_file)
        for log_entry in LogEntry.objects.filter(
            timestamp__gte=start_datetime, timestamp__lte=end_datetime
        ):
            row = self._generate_row(log_entry)
            p.write_text(f"{row}\n")

        self.stdout.write(self.style.SUCCESS(f"Report written to {output_file}"))
