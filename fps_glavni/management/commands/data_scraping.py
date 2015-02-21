# -*- coding: utf-8 -*-
import os

from django.core.management.base import BaseCommand

from fps_glavni.models import PoliticalParty, Income, Amount


class Command(BaseCommand):

    help = u'Scraps data from pdf files and prepares them for database.' \
           u'Files db with data.'

    def handle(self, *args, **options):
        # predefined values
        party = ['hdz', 'sdp', 'hsu', 'hsp', 'hss']
        vrste_prihoda = ['1.', '2.', '3.', '4.', '5.', '6.', '7.']

        # save political party
        for p in party:
            path = os.path.expanduser('~/Desktop/pdfs/{0}'.format(p))
            with open(path) as f:
                lines = f.readlines()
            f.close()
            enum_lines = list(enumerate(lines))
            starting = [i for i, j in enum_lines if j.strip().startswith('Tablica broj 1')]
            ending = [i for i, j in enum_lines if j.strip().startswith('Ukupno')]
            ending_index = 0
            for i in ending:
                if ending > starting[0]:
                    ending_index = i
                    break
            params = {
                'starting': starting[0],
                'ending': ending_index
            }
            tablica = enum_lines[params.get('starting'):params.get('ending')]
            extracted = []
            for i, j in tablica:
                text = j.strip().split('   ')
                for x in text:
                    if x == '':
                        pass
                    else:
                        extracted.append(unicode(x, 'utf-8'))

            prihodi = []
            prvi_stupac = []
            drugi_stupac = []

            for index, item in enumerate(extracted):
                if item in vrste_prihoda:
                    # ovo su prihodi
                    prihodi_check = (extracted[(index+1)%len(extracted)])
                    if any(x.isdigit() for x in prihodi_check):
                        prihodi.append(' ')
                    else:
                        prihodi.append(prihodi_check.strip())

                    # ovo su vrijednosti za prvi stupac
                    prvi_stupac.append(extracted[(index+2)%len(extracted)].strip())
                    drugi_stupac.append(extracted[(index+3)%len(extracted)].strip())

            # print prihodi
            # print prvi_stupac
            # print drugi_stupac
            # break

            # insert parties
            name = ''
            if p == 'hdz':
                name = 'HRVATSKA DEMOKRATSKA ZAJEDNICA'
            if p == 'sdp':
                name = 'SOCIAL DEMOKRATSKA PARTIJA'
            if p == 'hsu':
                name = 'HRVATSKA STRANKA UMIROVLJENIKA'
            if p == 'hsp':
                name = 'HRVATSKA STRANKA PRAVA'
            if p == 'hss':
                name = 'HRVATSKA SELJAČKA STRANKA'

            pp = PoliticalParty.objects.get_or_create(
                name=name,
                short_name=p,
                slug=p
            )

            # insert prihodi
            for prihod in prihodi:
                income = Income.objects.get_or_create(
                    name = prihod
                )


            # get party object for Income save
            party = PoliticalParty.objects.get(slug=p)
            # insert amount for first column
            year = 2012
            for i, x in enumerate(prihodi):
                income = Income.objects.get(name=prihodi[i])
                iznos = prvi_stupac[i].replace('.', '').replace(',', '.')
                amount = Amount.objects.get_or_create(
                    party=party,
                    income=income,
                    amount=iznos,
                    year=year
                )

            # insert amount for second column
            year = 2013
            for i, x in enumerate(prihodi):
                income = Income.objects.get(name=prihodi[i])
                iznos = prvi_stupac[i].replace('.', '').replace(',', '.')
                amount = Amount.objects.get_or_create(
                    party=party,
                    income=income,
                    amount=iznos,
                    year=year
                )

