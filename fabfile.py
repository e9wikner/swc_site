from fabric.api import local, lcd, run, settings
import os

def prepare(amend_commit):

    commit_args = ""
    if amend_commit:
        commit_args = "--amend"

    with lcd("../swc_blog"):
        # TODO: add testing
        # local("python3 setup.py install")
        local("git add . && git commit {}".format(commit_args))
        local("git push")

    local('python3 manage.py test')
    local("git add . && git commit {}".format(commit_args))
    local("git push")


def stage(project_dir, amend_commit=False):
    prepare(amend_commit)

    with settings(warn_only=True):
        if run("test -d {}".format(os.path.join(project_dir))).failed:
            run("sudo mkdir {}".format(project_dir))
            run("sudo git clone https://github.com/e9wikner/swc_site.git {}".format(
                project_dir))
            run("sudo chown -R http {}".format(project_dir))
            run("sudo chgrp -R http {}".format(project_dir))

    # Install blog app
    run("pip install --upgrade git+https://github.com/e9wikner/swc_blog.git")

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