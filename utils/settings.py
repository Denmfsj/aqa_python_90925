from dynaconf import Dynaconf
from definitions import BASE_PATH


# pip isntall dynaconf
d_settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[],#BASE_PATH / ".settings.ini", BASE_PATH / ".secrets.ini"],
    environments=True,
    load_dotenv=True,
)

print(d_settings.STUDENT_URL)

