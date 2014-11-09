from fabric.api import local, lcd, run, settings
import os


def update_repository(commit_args, directory="."):

    with lcd(directory):
        # with settings(warn_only=True):
        if local("git status --porcelain", capture=True):
            local("git add . ")
            local("git commit {}".format(commit_args))
            local("git push")


def prepare(commit_args=""):

    # TODO: add testing
    update_repository(commit_args, directory="../swc_blog")

    local('python3 manage.py test')
    update_repository(commit_args)


def stage(project_dir, commit_args=""):
    prepare(commit_args)

    with settings(warn_only=True):
        if run("test -d {}".format(project_dir)).failed:
            run("sudo mkdir {}".format(project_dir))
            run("sudo git clone https://github.com/e9wikner/swc_site.git {}".format(
                project_dir))
            run("sudo chown -R http {}".format(project_dir))
            run("sudo chgrp -R http {}".format(project_dir))

    # Install blog app
    run("sudo pip install --upgrade git+https://github.com/e9wikner/swc_blog")

    with lcd(project_dir):
        run("sudo git pull")
        run("sudo python3 manage.py makemigrations")
        run("sudo python3 manage.py migrate")


def deploy():
    prepare()

    with lcd('/path/to/my/prod/area/'):

        # With git...
        local('git pull /my/path/to/dev/area/')

        # With both
        local('python manage.py migrate myapp')
        local('python manage.py test myapp')
        local('/my/command/to/restart/webserver')