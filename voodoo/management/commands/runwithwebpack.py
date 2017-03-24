from django.contrib.staticfiles.management.commands.runserver import Command as BaseRunServer
import subprocess


class Command(BaseRunServer):
    """runs django server with a webpack subprocess to compile js"""

    def __init__(self, stdout=None, stderr=None, no_color=False):
        super().__init__(stdout, stderr, no_color)
        self.watcher = None

    def inner_run(self, *args, **options):
        if self.watcher is not None:
            self.watcher.kill()
            self.stdout.write('killed watcher PID {}.'.format(self.watcher.pid))

        self.watcher = subprocess.Popen(['npm', 'run', 'watch'], stdin=subprocess.PIPE, stdout=self.stdout, stderr=self.stderr)
        self.stdout.write('Started watcher on PID {}.'.format(self.watcher.pid))
        super().inner_run(*args, **options)


