from django.core.management.base import BaseCommand
from crud.models import Recruiter, Job, JobDelegation
from faker import Faker
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Seed database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create Recruiters
        recruiters = []
        for _ in range(10):  # Adjust the range as needed
            recruiter = Recruiter(
                name=fake.name(),
                email=fake.unique.email(),
                password=fake.password(),
                mobile=fake.random_int(min=1000000000, max=9999999999),
                userpic=fake.image_url(),
                is_deleted=fake.boolean(),
                user_created=fake.date_this_decade()
            )
            recruiters.append(recruiter)
        Recruiter.objects.bulk_create(recruiters)

        # Create Jobs
        jobs = []
        for _ in range(10):  # Adjust the range as needed
            job = Job(
                jobtitle=fake.job(),
                experience=Decimal(fake.random_number(digits=2)),
                expect_amount=Decimal(fake.random_number(digits=5)),
                location=fake.city(),
                jobdesc=fake.text(),
                jobclient=fake.company()
            )
            jobs.append(job)
        Job.objects.bulk_create(jobs)

        # Create JobDelegations
        for job in Job.objects.all():
            job_delegation = JobDelegation.objects.create(
                jobid=job,
                jobdelegationdate=fake.date_this_decade()
            )
            # Assign random recruiters to the job delegation
            job_delegation.jobassign.set(random.sample(list(Recruiter.objects.all()), k=3))  # Adjust 'k' as needed

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
