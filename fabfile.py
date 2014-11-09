from fabric.api import local, lcd, run, settings


def prepare():

    with lcd("../swc_blog"):
        # TODO: add testing
        # local("python3 setup.py install")
        with settings(warn_only=True):
            if local("git add -p && git commit"):
                local("git push")

    local('python3 manage.py test')
    with settings(warn_only=True):
        local('git add -p && git commit')
        local('git push')


def stage(project_dir):
    prepare()

    with settings(warn_only=True):
        if run("test -d {}".format(project_dir)).failed:
            run("git clone git@github.com:e9wikner/swc_site.git {}".format(
                project_dir))

    with lcd(project_dir):

        run("mkdir temp")
        with lcd("temp"):
            run("git clone git@github.com:e9wikner/swc_blog.git")
            run("python3 swc_blog/setup.py install")
            run("rm -R temp")

        run("git pull")
        run("touch swc_site/wsgi.py")


def deploy():
    prepare()

    with lcd('/path/to/my/prod/area/'):

        # With git...
        local('git pull /my/path/to/dev/area/')

        # With both
        local('python manage.py migrate myapp')
        local('python manage.py test myapp')
        local('/my/command/to/restart/webserver')