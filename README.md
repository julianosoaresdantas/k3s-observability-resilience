# GuardianSOC: K3s Observability & Resilience

[🇧🇷 Português](#português) | [🇺🇸 English](#english)

---

<a name="português"></a>
## 🇧🇷 Sobre o Projeto (PT-BR)
O GuardianSOC é uma arquitetura de observabilidade e segurança voltada para ambientes containerizados (K3s). O objetivo deste projeto é centralizar a telemetria, detectar ameaças em tempo real e automatizar a resposta a incidentes (SOAR).

### 🛠 Stack Tecnológica
- **Orquestração:** K3s
- **Observabilidade:** Stack LGTM (Loki, Grafana, Tempo, Mimir, Promtail)
- **Segurança/Triagem:** THOR Triage
- **Automação:** Shell Scripts, Python, API do Telegram

### ⚡ Automação de Alertas
O sistema monitora logs de segurança em busca de incidentes (ex: Webshells, Malwares). Ao detectar uma ameaça, o **@GuardianSOC_bot** (SOC_Juliano_Bot) envia um alerta imediato para o Telegram.

### ⚙️ Como usar
1. Clone o repositório: `git clone https://github.com/julianosoaresdantas/k3s-observability-resilience`
2. Configure suas variáveis de ambiente.
3. Inicie os serviços do K3s e a stack de monitoramento.

---

<a name="english"></a>
## 🇺🇸 About the Project (English)
GuardianSOC is an observability and security architecture designed for containerized environments (K3s). The project's goal is to centralize telemetry, detect threats in real-time, and automate incident response (SOAR).

### 🛠 Technology Stack
- **Orchestration:** K3s
- **Observability:** LGTM Stack (Loki, Grafana, Tempo, Mimir, Promtail)
- **Security/Triage:** THOR Triage
- **Automation:** Shell Scripts, Python, Telegram API

### ⚡ Automated Alerts
The system monitors security logs for incidents (e.g., Webshells, Malware). Upon detecting a threat, the **@GuardianSOC_bot** (SOC_Juliano_Bot) triggers an immediate alert via Telegram.

### ⚙️ How to use
1. Clone the repository: `git clone https://github.com/julianosoaresdantas/k3s-observability-resilience`
2. Configure your environment variables.
3. Start the K3s services and the monitoring stack.

---

## 📝 Contact / Contato
**Juliano Soares Dantas**
https://www.linkedin.com/in/juliano-soares-dantas-872b69357/

---
*Este projeto foi desenvolvido como parte de uma iniciativa de SRE para melhorar a resiliência e a postura de segurança em ambientes Cloud Native.*
