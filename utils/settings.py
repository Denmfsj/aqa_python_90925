from dynaconf import Dynaconf
from definitions import BASE_PATH


# pip isntall dynaconf
d_settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[BASE_PATH / ".settings.toml", BASE_PATH / ".secrets.toml"],
    environments=True,
    load_dotenv=True,
)
