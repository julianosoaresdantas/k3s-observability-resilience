# Documentação Técnica: Arquitetura / Technical Documentation: Architecture

## Visão Geral / Overview 
 
K3s cluster running in a local environment with an integrated monitoring stack.

Cluster K3s rodando em ambiente local com stack de monitoramento integrada.

## Estrutura do Cluster / Cluster Structure
- **Orquestrador / Orchestrator:** K3s
- **Observabilidade / Observability:** Prometheus (metrics collection) & Grafana (visualization)
- **Ingress Controller:** Traefik

## Imagens de Arquitetura / Architecture Images 
![Arquitetura Geral / General Architecture](docs/arquitetura_overview.png)
![Fluxo de Dados / Data Flow](docs/arquitetura_fluxo.png)
