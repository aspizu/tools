from rich import print


def info(title: str, message: str) -> None:
    print(f" --> [bold blue]{title}[/] : [green]{message}[/]")

def warn(title: str, message: str) -> None:
    print(f" [!] [bold yellow]{title}[/] : [green]{message}[/]")


def error(title: str, message: str) -> None:
    print(f" ERR [bold red]{title}[/] : [green]{message}[/]")
