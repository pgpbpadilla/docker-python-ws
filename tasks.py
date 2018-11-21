from invoke import task


@task
def up(ctx):
    """Run Docker compose configuration"""
    ctx.run('docker-compose up -d')