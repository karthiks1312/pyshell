import os

from pyshell.main import execute


def test_exit_stops_shell():
    assert execute("exit") is False


def test_empty_args_continue():
    assert execute("pwd") is True


def test_pwd_prints_cwd(capsys):
    execute("pwd")
    assert capsys.readouterr().out.strip() == os.getcwd()


def test_pwd_too_many_args(capsys):
    execute("pwd extra")
    assert "too many" in capsys.readouterr().out


def test_cd_changes_directory(tmp_path, capsys):
    start = os.getcwd()
    try:
        execute(f"cd {tmp_path}")
        assert os.getcwd() == str(tmp_path.resolve())
    finally:
        os.chdir(start)


def test_cd_missing_directory_does_not_crash(capsys):
    assert execute("cd /definitely/not/here") is True
    assert "cd:" in capsys.readouterr().out


def test_cd_too_many_args(capsys):
    execute("cd a b")
    assert "too many" in capsys.readouterr().out


def test_external_command_receives_arguments(capfd):
    execute("echo hello world")
    assert capfd.readouterr().out.strip() == "hello world"


def test_quoted_arguments_stay_together(capfd):
    execute("echo 'a   b'")
    assert capfd.readouterr().out.strip() == "a   b"


def test_unknown_command(capsys):
    assert execute("nosuchcommand_xyz") is True
    assert "command not found" in capsys.readouterr().out


def test_unbalanced_quote_reports_error(capsys):
    assert execute("echo 'oops") is True
    assert "parse error" in capsys.readouterr().out
