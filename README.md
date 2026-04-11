# ATV1-LDW-ApiFlasgger


# ⚠️ CONFIGURAÇÃO OBRIGATÓRIA

Antes de executar qualquer comando da aplicação, é obrigatório configurar a variável de ambiente abaixo:

## 🔧 Terminal
```powershell
$env:PYTHONPATH = "src"
```

Após configurar o PYTHONPATH, iniciar a aplicação:

```powershell
uv run flask --app app run
