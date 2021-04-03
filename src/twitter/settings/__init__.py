import os
from dotenv import load_dotenv

from .base import *  # noqa:
load_dotenv(override=True)

environment = os.getenv('ENVIRONMENT')


if environment == 'PRODUCTION':
    print('## USING PRODUCTION ENVIRONMENT')
    from .production import *  # noqa:
elif environment == 'DEVELOPMENT':
    print('## USING DEVELOPMENT ENVIRONMENT')
    from .development import *  # noqa:
else:
    print("THERE IS NO ENVIRONMENT VARIABLE $ENVIRONMENT")
