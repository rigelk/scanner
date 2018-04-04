from django.core.management.base import BaseCommand, CommandError
import re
import argparse
from functools import reduce
from operator import or_
import tqdm
from smtplib import SMTPServerDisconnected, SMTPRecipientsRefused

from django.db.models import Q
from django.core.mail import get_connection
from registrations.models import Registration, TicketEvent
from registrations.actions.emails import send_email


def integer_range(string):
    m = re.match(r'(\w+)(?:-(\w+))?$', string)
    if not m:
        raise argparse.ArgumentTypeError("'" + string + "' is not a range of code. Expected forms like '02-5f' or '2'.")
    start = m.group(1)

    if m.group(2):
        return Q(numero__gte=start) & Q(numero__lte=m.group(2))

    return Q(numero=start)


class Command(BaseCommand):
    help = "Send tickets to people"

    def add_arguments(self, parser):
        parser.add_argument('event_id', type=int)
        parser.add_argument('ranges', nargs='+', type=integer_range)
        parser.add_argument('-i', '--ignore-sent-status', action='store_false', dest='check_sent_status')

    def handle(self, *args, event_id, ranges, check_sent_status, **options):
        try:
            TicketEvent.objects.get(id=event_id)
        except TicketEvent.DoesNotExist:
            raise CommandError('Event does not exist')

        query = reduce(or_, ranges)

        if check_sent_status:
            query = query & ~Q(ticket_status=Registration.TICKET_SENT)

        connection = get_connection()

        refused = []

        for elem in tqdm.tqdm(Registration.objects.filter(query), desc='Sending tickets'):
            while True:
                try:
                    send_email(elem, connection=connection)
                except SMTPServerDisconnected:
                    connection = get_connection()
                    continue
                except SMTPRecipientsRefused:
                    refused.append(elem)
                    break
                break

        connection.close()

        for elem in refused:
            self.stdout.write('Could not send to {} ({})'.format(elem.contact_email, elem.numero))
