import os

site_domain = 'https://www.nautiljon.com'
home_url = site_domain
login_url = site_domain + '/membre/login.php'
notifications_url = site_domain + '/inc/ajax/notifications.php'
messages_url = site_domain + '/watashi/messagerie/'

# expanduser give a cross-platform home directory
HOME = os.path.expanduser('~')
APP_DIR = os.path.dirname(os.path.abspath(__file__))

config = {
    'site_domain': site_domain,
    'home_url': home_url,
    'login_url': login_url,
    'notifications_url': notifications_url,
    'messages_url': messages_url,
    'data_dir_path': os.path.join(HOME, 'nautiljon_notifier')
}

assets = {
    'nautiljon_icon': os.path.join(APP_DIR, 'assets/nautiljon_icon.ico'),
    'nautiljon_icon_desktop': os.path.join(APP_DIR, 'assets/nautiljon_icon_desktop.ico')
}
