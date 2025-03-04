from factorialhr._cli import account, projects

try:
    import cloup
except ImportError as import_error:
    raise ImportError('Cli not installed. Please install using "pip install factorialhr[cli]".') from import_error


@cloup.group()
def entrypoint():
    pass


entrypoint.add_command(account.account)
entrypoint.add_command(projects.project_entrypoint)
