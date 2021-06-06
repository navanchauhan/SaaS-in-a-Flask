from app import database_cli


def test_database_commands(app, client):
    runner = app.test_cli_runner()
    assert runner.invoke(database_cli, ["delete"]).exit_code == 0
    assert runner.invoke(database_cli, ["create"]).exit_code == 0
    assert runner.invoke(database_cli, ["admin-create"]).exit_code == 0
