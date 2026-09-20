"""Lists the places in the database where a wording still needs to be changed.

The templates are covered by a grep; the prose that makes up most of the site
is not, because it lives in the database. This command finds those places and
prints a work list with a link into the admin for each one. It never writes.
"""

import csv
import re

from django.apps import apps
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import FieldError
from django.core.management.base import BaseCommand
from django.db import DatabaseError
from django.db.models import CharField, Q, TextField
from django.urls import NoReverseMatch, reverse

# Apps whose rows are bookkeeping rather than content somebody would reword.
SKIPPED_APPS = {"admin", "auth", "contenttypes", "sessions", "sites", "socialaccount"}

# Spellings that are already correct, or that are names and compounds rather
# than a reference to people. They are removed from the text before the search,
# so "Pfadfinderinnen und Pfadfinder" does not report its own second half.
DEFAULT_ACCEPTED = [
    r"Pfadfinderinnen und Pfadfindern?",
    r"Pfadfinderinnen, Pfadfinder",
    r"Pfadfinderbund\w*",
    r"Pfadfinderbewegung\w*",
    r"Pfadfindergruppe\w*",
    r"Pfadfinderheim\w*",
    r"Pfadfinderlager\w*",
]

CONTEXT = 60  # characters of text shown on either side of a hit

# A hit that continues into another word is a compound -- Pfadfindertechnik,
# Pfadfinder-Tabu -- where there is nothing to gender. Those are listed last so
# the ones that do need a decision are at the top.
COMPOUND = re.compile(r"[a-zäöüß-]")


class Command(BaseCommand):
    help = "Lists database texts that still contain a given wording."

    def add_arguments(self, parser):
        parser.add_argument(
            "--term",
            default="Pfadfinder",
            help='The wording to look for (default: "Pfadfinder").',
        )
        parser.add_argument(
            "--accept",
            action="append",
            default=None,
            help="A regular expression for a spelling that is already fine. "
            "Repeatable. Replaces the built-in list when given.",
        )
        parser.add_argument(
            "--csv",
            dest="csv_path",
            help="Also write the list to this file, for passing it around.",
        )

    def handle(self, *args, **options):
        term = options["term"]
        accepted = options["accept"] or DEFAULT_ACCEPTED
        accepted_re = re.compile("|".join(accepted)) if accepted else None
        term_re = re.compile(re.escape(term))

        rows = sorted(
            self.find(term, term_re, accepted_re),
            key=lambda row: (row["art"] == "Kompositum", row["model"], row["object"]),
        )

        for row in rows:
            self.stdout.write(
                self.style.MIGRATE_HEADING(
                    f"{row['art']} · {row['model']} · {row['field']}"
                )
                + f"\n  {row['object']}"
                + (f"\n  {row['admin_url']}" if row["admin_url"] else "")
                + f"\n  …{row['context']}…\n"
            )

        if options["csv_path"]:
            with open(options["csv_path"], "w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(rows[0]) if rows else
                                        ["model", "field", "object", "admin_url", "context"])
                writer.writeheader()
                writer.writerows(rows)
            self.stdout.write(f"CSV: {options['csv_path']}")

        eigen = sum(1 for row in rows if row["art"] == "eigenständig")
        self.stdout.write(
            self.style.SUCCESS(
                f"{len(rows)} Fundstellen für {term!r}: "
                f"{eigen} eigenständig, {len(rows) - eigen} in Komposita."
            )
        )

    def find(self, term, term_re, accepted_re):
        for model in apps.get_models():
            if model._meta.app_label in SKIPPED_APPS:
                continue

            fields = [
                f.name
                for f in model._meta.get_fields()
                if isinstance(f, (CharField, TextField))
                and not isinstance(f, GenericForeignKey)
            ]
            if not fields:
                continue

            query = Q()
            for name in fields:
                query |= Q(**{f"{name}__contains": term})

            # A queryset does not run until it is iterated, so the guard has
            # to wrap the loop rather than the call to filter().
            try:
                candidates = list(model.objects.filter(query))
            except (DatabaseError, FieldError) as error:
                self.stderr.write(f"{model._meta.label}: übersprungen ({error})")
                continue

            for obj in candidates:
                for name in fields:
                    value = getattr(obj, name, None)
                    if not isinstance(value, str):
                        continue
                    # Blank out the spellings that are fine, keeping offsets
                    # intact so the context below still lines up with the text.
                    searchable = (
                        accepted_re.sub(lambda m: " " * len(m.group(0)), value)
                        if accepted_re
                        else value
                    )
                    for match in term_re.finditer(searchable):
                        start = max(0, match.start() - CONTEXT)
                        end = min(len(value), match.end() + CONTEXT)
                        rest = value[match.end():]
                        yield {
                            "art": "Kompositum"
                            if COMPOUND.match(rest.lstrip("ns")[:1] or " ")
                            or COMPOUND.match(rest[:1] or " ")
                            else "eigenständig",
                            "model": model._meta.label,
                            "field": name,
                            "object": str(obj)[:80],
                            "admin_url": self.admin_url(obj),
                            "context": " ".join(value[start:end].split()),
                        }

    @staticmethod
    def admin_url(obj):
        meta = obj._meta
        try:
            return reverse(
                f"admin:{meta.app_label}_{meta.model_name}_change", args=[obj.pk]
            )
        except NoReverseMatch:
            return ""
