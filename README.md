### Vulp Bot — Bot oficial da comunidade Outleep

Bot do Discord para ajudar, administrar e gerenciar a comunidade Outleep com foco em qualidade, organização e extensibilidade.

---

### Destaques
- **Arquitetura limpa (Ports & Adapters)**: separação clara entre camadas (`services/ports` e `services/adapters`).
- **Erros tratados e observabilidade**: middleware de tratamento em `BaseBotPort` com logs estruturados via `loguru` (inclui envio de embeds de erro/log para um canal do servidor).
- **Execução concorrente**: orquestração com `anyio.TaskGroup` iniciando o bot e jobs em paralelo.
- **Comandos via Cogs e Slash Commands**: carregamento dinâmico de cogs e comandos de slash organizados.
- **Persistência simples e robusta**: `SQLModel` + `SQLite` com engine assíncrono (`aiosqlite`).
- **Configuração centralizada**: `src/setup.py` carrega `.env`, cria DB e expõe helpers (sessão assíncrona, variáveis, etc.).

---

### Arquitetura (visão geral)
- `src/main.py`: ponto de entrada; sobe bot e jobs em paralelo.
- `src/bot/`: integrações do bot (cliente, cogs, deps de segurança, UX helpers).
- `src/services/ports`: contratos de alto nível (ex.: `IComunity`).
- `src/services/adapters`: implementações desses contratos para Discord (ex.: `ComunityAdapter`).
- `src/database`: tabelas e repositórios (ex.: `CalendarRepo`).
- `src/jobs`: tarefas de background (ex.: presença).
- `src/integrations/bot_client.py`: instancia o `commands.Bot` com intents corretos.
- `src/setup.py`: carrega `.env`, prepara banco `resources/vulp.db` e provê sessão assíncrona.

---

### Tecnologias
- Python 3.13
- discord.py 2.x
- anyio
- SQLModel + SQLAlchemy Async + aiosqlite
- loguru
- python-dotenv

---

### Pré‑requisitos
- Python 3.13 instalado
- (Opcional) Poetry para gerenciar dependências
- Um bot do Discord configurado (token) e um servidor (guild) para testes

---

### Configuração
1) Crie um arquivo `.env` na raiz do projeto com as variáveis:

```env
BOT_TOKEN=seu_token_do_bot
BOT_OWNER_ID=000000000000000000
BOT_LOG_CHAT_ID=000000000000000000
BOT_GUILD_ID=000000000000000000
```

2) Instale dependências (com Poetry):

```bash
poetry install
```

Se preferir `pip`, ative um venv e instale os pacotes de `pyproject.toml` manualmente.

---

### Execução
- Via módulo principal (sobe bot e jobs):

```bash
python -m src.main
```

O banco `resources/vulp.db` será criado automaticamente se não existir.

---

### Comandos do Bot (exemplos)
- Slash Commands:
  - `/ajuda` — mostra comandos e informações úteis.
  - `/denuncia` — envia embed para denúncias.

- Comandos de manutenção (prefixo `vulp!`, restritos por verificação de owner):
  - `vulp!csync` — carrega cogs e sincroniza slash commands na guild atual.
  - `vulp!cclear` — limpa comandos globais e da guild atual.

Obs.: os cogs em `src/bot/cogs` são carregados dinamicamente.

---

### Banco de Dados
- `SQLite` em `resources/vulp.db`.
- `SQLModel`/`SQLAlchemy` com engine assíncrono (`sqlite+aiosqlite`).
- Criação do schema é automática em `setup.create_db_engine()`.

---

### Logs e Tratamento de Erros
- `loguru` para logging estruturado.
- Middleware em `BaseBotPort.__getattribute__` captura exceções e envia embeds informativos.
- Canal de logs configurável via `BOT_LOG_CHAT_ID`.

---

### Estrutura de Pastas (resumo)
```
src/
  api/
  bot/
    cogs/
    deps/
    ux/
  database/
    repositories/
  integrations/
  jobs/
  services/
    adapters/
    ports/
    utils/
  utils/
  main.py
resources/
  vulp.db
```

---

### Licença
Este projeto está licenciado sob a licença MIT. Veja `LICENSE` para mais detalhes.

---

### Autor
Criado por Emerson Silva.
