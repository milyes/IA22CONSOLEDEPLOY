import subprocess, platform, requests, time, json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.live import Live
from rich.text import Text

console = Console()
AUTHORIZED_PASSWORD = "1776"

def check_password():
    console.print("[bold red]🔐 Accès protégé[/bold red]")
    pwd = console.input("Entrez le mot de passe IA22 : ").strip()
    if pwd != AUTHORIZED_PASSWORD:
        console.print("[red]❌ Mot de passe incorrect. Accès refusé.[/red]")
        exit()
    console.print("[green]✅ Mot de passe accepté[/green]\n")

def scan_wifi():
    return ["Scan Wi-Fi indisponible sur Android non-root"]

def system_logs():
    logs = []
    logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] SYSTEM: Terminal IA actif")
    try:
        cpu_info = subprocess.getoutput("top -n 1 | head -n 5")
        logs.append(cpu_info or "⚠️ CPU info indisponible")
    except Exception as e:
        logs.append(f"Erreur CPU : {e}")
    return logs

def generate_mobile_id():
    ip = requests.get("https://ifconfig.me").text.strip()
    data = {
        "device": platform.platform(),
        "ip_public": ip,
        "timestamp": datetime.now().isoformat(),
        "signature": "IA_OCNEP_IZOUBIROU",
        "owner": "Mohamed Ilyes Zoubirou",
        "module": "IA22API_MOBILE_NODE",
        "auth_pass": AUTHORIZED_PASSWORD,
        "valid": True,
        "purpose": "Terminal IA22 mobile léger"
    }
    with open("ia22_mobile_id.json", "w") as f:
        json.dump(data, f, indent=2)
    console.print(f"[bold cyan]📄 Empreinte réseau générée : ia22_mobile_id.json[/bold cyan]")

def show_dashboard():
    with Live(refresh_per_second=4) as live:
        while True:
            table = Table(title="IA22 TERMINAL MOBILE", style="bold magenta")
            table.add_column("🕒", justify="center")
            table.add_column("Log IA", justify="left")
            logs = system_logs()
            for log in logs:
                table.add_row(datetime.now().strftime("%H:%M:%S"), log)

            ip_panel = Panel(requests.get("https://ifconfig.me").text.strip(), title="IP Publique")
            net_panel = Panel("\n".join(scan_wifi()), title="Scan Wi-Fi (indisponible)")
            suggestion = Panel(Text("> connect API IA22", style="bold green"), title="Suggestion")

            layout = Table.grid(expand=True)
            layout.add_row(table)
            layout.add_row(ip_panel)
            layout.add_row(net_panel)
            layout.add_row(suggestion)
            live.update(layout)
            time.sleep(5)

if __name__ == "__main__":
    console.print("[bold blue]🧬 IA22 TERMINAL MOBILE - Initialisation[/bold blue]")
    time.sleep(1)
    check_password()
    generate_mobile_id()
    show_dashboard()
