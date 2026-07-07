#!/bin/bash
LOG_FILE="/var/log/thor-scan.json"

# Extrai os últimos campos do log mais recente
FILE_NAME=$(tail -n 1 $LOG_FILE | jq -r '.file // "Desconhecido"')
SEVERITY=$(tail -n 1 $LOG_FILE | jq -r '.severity // "Info"')
MSG=$(tail -n 1 $LOG_FILE | jq -r '.message // "Sem detalhes"')

# Monta a mensagem de alerta
TEXT="🚨 *Alerta de Segurança THOR*%0A%0AArquivo: \`$FILE_NAME\`%0AClassificação: $SEVERITY%0ADetalhes: $MSG"

# Envia via API do Telegram
curl -s "https://api.telegram.org/bot<SEU_TOKEN>/sendMessage" \
     -d "chat_id=<SEU_CHAT_ID>&text=$TEXT&parse_mode=Markdown"
