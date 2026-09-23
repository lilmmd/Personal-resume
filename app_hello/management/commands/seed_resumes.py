from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from faker import Faker

from app_hello.models import (
    Profile,
    Experience,
    Education,
    Project,
    Skill,
)


class Command(BaseCommand):
    help = "Create 50 fake users and resumes quickly"

    def handle(self, *args, **options):
        fake = Faker()

        TOTAL_USERS = 50

        # --------------------------------
        # Check existing users
        # --------------------------------

        current_users = User.objects.count()

        if current_users >= TOTAL_USERS:
            self.stdout.write(
                self.style.WARNING(
                    f"Database already has {current_users} users."
                )
            )
            return

        users_count = TOTAL_USERS - current_users

        self.stdout.write(
            f"Creating {users_count} users..."
        )

        # --------------------------------
        # Generate usernames/emails
        # --------------------------------

        existing_usernames = set(
            User.objects.values_list("username", flat=True)
        )

        existing_emails = set(
            User.objects.values_list("email", flat=True)
        )

        users = []

        for _ in range(users_count):

            username = fake.user_name()

            while username in existing_usernames:
                username = fake.user_name()

            email = fake.email()

            while email in existing_emails:
                email = fake.email()

            existing_usernames.add(username)
            existing_emails.add(email)

            users.append(
                User(
                    username=username,
                    email=email,
                    password=make_password("password123"),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                )
            )

        # --------------------------------
        # Bulk create users
        # --------------------------------

        users = User.objects.bulk_create(
            users,
            batch_size=100,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {len(users)} users."
            )
        )

        # --------------------------------
        # Prepare all objects
        # --------------------------------

        profiles = []
        experiences = []
        educations = []
        projects = []
        skills = []

        skill_list = [
            "Python",
            "Django",
            "JavaScript",
            "React",
            "HTML",
            "CSS",
            "Git",
            "Docker",
            "PostgreSQL",
            "REST API",
            "FastAPI",
            "Linux",
            "SQL",
            "Redis",
            "Celery",
        ]

        degree_choices = [
            "diploma",
            "associate",
            "bachelor",
            "master",
            "phd",
        ]

        for user in users:

            # --------------------------------
            # Profile
            # --------------------------------

            profiles.append(
                Profile(
                    user=user,
                    phone=fake.phone_number(),
                    job_title=fake.job(),
                    description=fake.paragraph(
                        nb_sentences=3
                    ),
                    interests=", ".join(
                        fake.words(
                            nb=5,
                            unique=True
                        )
                    ),
                )
            )

            # --------------------------------
            # Experiences
            # --------------------------------

            for _ in range(
                fake.random_int(min=1, max=3)
            ):
                experiences.append(
                    Experience(
                        user=user,
                        title=fake.company(),
                        location=fake.city(),
                        duration=f"{fake.year()} - {fake.year()}",
                        position=fake.job(),
                        job_discription=fake.sentence(
                            nb_words=10
                        ),
                    )
                )

            # --------------------------------
            # Education
            # --------------------------------

            for _ in range(
                fake.random_int(min=1, max=2)
            ):
                educations.append(
                    Education(
                        user=user,
                        university=f"{fake.last_name()} University",
                        location=fake.city(),
                        duration=f"{fake.year()} - {fake.year()}",
                        degree=fake.random_element(
                            degree_choices
                        ),
                        study_discription=fake.sentence(
                            nb_words=10
                        ),
                    )
                )

            # --------------------------------
            # Projects
            # --------------------------------

            for _ in range(
                fake.random_int(min=1, max=3)
            ):
                projects.append(
                    Project(
                        user=user,
                        title=fake.catch_phrase(),
                        description=fake.text(
                            max_nb_chars=150
                        ),
                    )
                )

            # --------------------------------
            # Skills
            # --------------------------------

            selected_skills = fake.random_elements(
                elements=skill_list,
                length=fake.random_int(
                    min=4,
                    max=8
                ),
                unique=True,
            )

            for skill in selected_skills:
                skills.append(
                    Skill(
                        user=user,
                        title=skill,
                        level=fake.random_int(
                            min=1,
                            max=5
                        ),
                    )
                )

        # --------------------------------
        # Bulk insert everything
        # --------------------------------

        Profile.objects.bulk_create(
            profiles,
            batch_size=100,
        )

        Experience.objects.bulk_create(
            experiences,
            batch_size=100,
        )

        Education.objects.bulk_create(
            educations,
            batch_size=100,
        )

        Project.objects.bulk_create(
            projects,
            batch_size=100,
        )

        Skill.objects.bulk_create(
            skills,
            batch_size=100,
        )

        # --------------------------------
        # Done
        # --------------------------------

        self.stdout.write(
            self.style.SUCCESS(
                f"""
Done!

Users:       {len(users)}
Profiles:    {len(profiles)}
Experience:  {len(experiences)}
Education:   {len(educations)}
Projects:    {len(projects)}
Skills:      {len(skills)}

Password for all users:
password123
"""
            )
        )
