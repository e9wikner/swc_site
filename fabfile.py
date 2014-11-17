from fabric.api import local, lcd, run, cd, sudo, settings, env

env.sudo_prefix = "sudo -SE"
HTTP_ROOT = "/srv/http/swconsulting.se"


def update_repository(commit_args, directory="."):

    with lcd(directory):
        # with settings(warn_only=True):
        if local("git status --porcelain", capture=True):
            local("git add . ")
            local("git commit {}".format(commit_args))
            local("git push origin master")


def prepare(commit_args=""):

    # TODO: add testing
    update_repository(commit_args, directory="../swc_blog")

    local('python3 manage.py test')

    update_repository(commit_args)


def collect_static(site_install_dir):

    sudo("chmod g+w " + site_install_dir)
    with cd(site_install_dir):
        run("./manage.py collectstatic")
    sudo("chmod g-w " + site_install_dir)


def migrate(site_install_dir):

    with cd(site_install_dir):
        run("./manage.py makemigrations")
        run("./manage.py migrate")


def stage(commit_args=""):
    prepare(commit_args)

    with settings(warn_only=True):
        if run("test -d {}".format(HTTP_ROOT)).failed:
            sudo("mkdir {}".format(HTTP_ROOT))
            sudo("git clone https://github.com/e9wikner/swc_site.git {}".format(
                HTTP_ROOT))
            sudo("chown -R http {}".format(HTTP_ROOT))
            sudo("chgrp -R http {}".format(HTTP_ROOT))

    # Install blog app
    sudo("pip install --upgrade git+https://github.com/e9wikner/swc_blog")

    collect_static(HTTP_ROOT)
    migrate(HTTP_ROOT)


def deploy():
    prepare()

    with lcd('/path/to/my/prod/area/'):

        # With git...
        local('git pull /my/path/to/dev/area/')

        # With both
        local('python manage.py migrate myapp')
        local('python manage.py test myapp')
        local('/my/command/to/restart/webserver')