from checkuser.checker import check_user, kill_user
from checkuser.checker import CheckerUserManager

from checkuser.checker.ovpn import OpenVPNManager
from checkuser.checker.ssh import SSHManager

from checkuser.web import Server, ServerManager

from checkuser.utils import base_cli

__version__ = '2.2.0'
__author__ = 'Kaua Mello'
__email__ = 'vpnlite223@gmail.com

base_cli.description = 'Checker for OpenVPN and SSH'
base_cli.prog = 'checker v' + __version__

base_cli.add_argument(
    '-v',
    '--version',
    action='version',
    version='%(prog)s',
)
