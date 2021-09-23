import logging
import cli_app
import cli_app.cli as CLI
from cli_app.settings import APP_SETTINGS as app
from cli_app.utils import log

LOG = logging.getLogger(__name__)


class CliApp:
    @staticmethod
    def run():
        try:
            log.setup_logger(app.log_config)
            LOG.info('Start cli_app')
            CLI.cli(prog_name=cli_app.__title__)

        except Exception as e:
            LOG.exception(str(e))

        finally:
            pass
