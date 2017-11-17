import os

site_domain = "https://www.nautiljon.com"
home_url = site_domain
login_url = site_domain + "/membre/login.php"

# expanduser give a cross-platform home directory
HOME = os.path.expanduser("~")

config = {
    'site_domain': site_domain,
    'home_url': home_url,
    'login_url': login_url,
    'data_dir_path': os.path.join(HOME, 'nautiljon_notifier')
}
