from invoke import task


@task
def up(ctx):
    """Run Docker compose configuration"""
    ctx.run('docker-compose up -d')


@task
def local_install(ctx):
    ctx.run('pip install -e .')


@task(pre=[local_install])
def tdd(ctx):
    ctx.run('ptw')