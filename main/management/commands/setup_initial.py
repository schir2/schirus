from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = """Sets up the initial database for testing
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "--delete_existing",
            action="store_true",
            dest="delete_existing",
            default=False,
            help="Delete existing database and migration files "
            "type",
        )

    def handle(self, *args, **options):
        if options['delete_existing']:
            call_command('delete_database')
            call_command('delete_migrations')
        call_command('makemigrations', 'users')
        call_command('sqlmigrate', 'users', '0001')
        call_command('migrate')
        call_command('makemigrations', 'blog')
        call_command('makemigrations')
        call_command('sqlmigrate', 'blog', '0001')
        call_command('migrate')
        call_command('autoload')
