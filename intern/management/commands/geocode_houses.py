"""Re-run the Nominatim lookup for houses that have no coordinates yet."""

import time

from django.core.management.base import BaseCommand

from intern.models import House


class Command(BaseCommand):
    help = "Look up missing coordinates for houses via Nominatim."

    def add_arguments(self, parser):
        parser.add_argument(
            "--all",
            action="store_true",
            help="Also refresh houses that already have coordinates.",
        )
        parser.add_argument(
            "--delay",
            type=float,
            default=1.1,
            help="Seconds to wait between requests (Nominatim allows one per second).",
        )

    def handle(self, *args, **options):
        houses = House.objects.all().order_by("name")
        if not options["all"]:
            houses = houses.filter(latitude__isnull=True)

        found = missing = 0
        for house in houses:
            location = house.geocode()
            if location is None:
                missing += 1
                self.stdout.write(self.style.WARNING(f"kein Treffer: {house.name}"))
            else:
                house.latitude, house.longitude, house.display_name = location
                house.save(update_fields=["latitude", "longitude", "display_name"])
                found += 1
                self.stdout.write(self.style.SUCCESS(f"{house.name}: {house.display_name}"))
            time.sleep(options["delay"])

        self.stdout.write(f"\n{found} Häuser verortet, {missing} ohne Treffer.")
