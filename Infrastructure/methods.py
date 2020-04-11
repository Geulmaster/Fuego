import questionary
from Fuego.Apps.organizer import Applications

applications = Applications()

general = ["install", "show_logs", "systems_view", "exit"]
#install - choose systems to install
#show_logs - show recent logs of systems
#systems_view - display any active system server and port
apps_list = ["k8s", "docker", "grafana", "elk", "prometheus", "exit"]

def install():
    app = questionary.select("Choose: ", choices=apps_list).ask()
    method = getattr(applications, app)
    method()