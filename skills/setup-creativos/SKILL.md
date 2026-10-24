---
name: setup-creativos
description: Configura una tienda nueva para usar cod-creativos — crea CONFIG-TIENDA.md con la marca, el país, Shopify, los IDs de Meta, la economía contraentrega, el material permitido y las voces; y revisa que estén instaladas las herramientas (ffmpeg, Codex, Playwright, entorno de voces). Úsala la primera vez que se instala el plugin, cuando el usuario diga "configurar mi tienda", "setup", cambie de tienda o de cuenta de anuncios, o cuando ads-invest o landing-cod no encuentren CONFIG-TIENDA.md.
---

# Setup de cod-creativos

Objetivo: dejar `CONFIG-TIENDA.md` completo en la carpeta de trabajo y las herramientas listas, para que `ads-invest` y `landing-cod` funcionen sin datos inventados.

## 1. Carpeta de trabajo
- Pregunta dónde quiere guardar la investigación (por defecto `~/ads-invest`). Créala si no existe.
- Si ya hay un `CONFIG-TIENDA.md`, léelo y completa solo lo que falte. No lo sobrescribas.
- Si no hay, copia la plantilla `templates/CONFIG-TIENDA.md` del plugin con Write y llénala.

## 2. Datos que se sacan solos (no se le preguntan al usuario)
Usa los conectores si están disponibles; si un conector no está, anótalo como pendiente y sigue.
- **Shopify** (MCP de Shopify): `query{ shop{ name myshopifyDomain primaryDomain{ host } currencyCode billingAddress{ countryCodeV2 } } }` → marca, dominio, moneda y país. `query{ publications(first:10){ nodes{ id name } } }` → el `id` de "Online Store" / "Tienda online". El handle del admin sale de `myshopifyDomain` (lo que va antes de `.myshopify.com`) o de la URL del admin.
- **Meta** (MCP de Meta Ads): `ads_get_ad_accounts` → lista las cuentas y **pregunta cuál usar** si hay varias. Con la cuenta elegida: `ads_get_ad_account_pages` (página), `ads_get_ig_accounts` (instagram_user_id), `ads_get_datasets` (píxel). Si hay varias páginas o píxeles, pregunta.
- **Campañas activas** (opcional): `ads_get_ad_entities` con `level=campaign` para anotar la One CBO vigente y su presupuesto.

## 3. Datos que se le preguntan al usuario (en una sola tanda)
1. Flete por pedido y flete de devolución.
2. Tasas de despacho y de entrega, si las conoce. Si no, 80 % y 90 %.
3. App del formulario contraentrega (por defecto Releasit).
4. Stock licenciado que tiene (Magnific/Freepik, Envato, ninguno) y si el premium le gasta créditos.
5. ¿Usa el plugin **cod-ops** para contabilidad y One CBO? Si sí, anota la ruta de su `tienda.config.json` y su `data.json`.

## 4. Herramientas (revisar e instalar con el visto bueno del usuario)
Corre estas verificaciones y reporta ✅/❌:
```bash
ffmpeg -version | head -1                       # montaje de videos, GIFs, hojas de fotogramas
codex --version                                 # imágenes del producto (packshot, piezas, escenas)
~/.venvs/voz-mlx/bin/python -c "import mlx_audio, soundfile; print('voxcpm ok')"     # voces por avatar (VoxCPM2)
~/.venvs/voz/bin/python -c "import mlx_whisper, librosa, transformers; print('validación ok')"   # whisper, tono y género (+ OmniVoice de respaldo)
uname -m                                        # arm64 = Mac con chip Apple (requerido para mlx)
```
- **ffmpeg:** `brew install ffmpeg`.
- **Codex CLI:** `npm i -g @openai/codex` y `codex login` (requiere cuenta de ChatGPT/OpenAI con generación de imágenes).
- **Voces:** dos entornos separados (no se mezclan: `mlx-audio` rompe el `transformers` de OmniVoice). Motor principal **VoxCPM2** en `~/.venvs/voz-mlx`: `skills/ads-invest/references/voces-voxcpm2.md` § Instalación. Validación (whisper, tono, clasificador de género) y OmniVoice de respaldo en `~/.venvs/voz`: `skills/ads-invest/references/voces-omnivoice.md` § Instalación. Uv + Python 3.11, solo Mac con chip Apple; en otro equipo, adaptar a CUDA/CPU.
- **Navegador (Playwright):** las skills usan un MCP de Playwright (`browser_navigate`, `browser_evaluate`, `browser_run_code_unsafe`). Si no hay ninguno, instala el oficial: `claude mcp add playwright -- npx @playwright/mcp@latest`.
- **Conectores de claude.ai:** Meta Ads (Facebook), Shopify y, si tiene stock, Magnific. Se conectan desde claude.ai → Configuración → Conectores.
- **Permisos de Meta:** crear o activar objetos en Meta puede pedir permiso. Sugiere agregar con `/permissions` las tools que vaya a usar (`ads_creative_upload_media`, `ads_create_ad_set`, `ads_create_creative`, `ads_create_ad`, `ads_activate_entity`, `ads_update_entity`).

No instales nada sin decirle al usuario qué vas a instalar.

## 5. Cierre
- Muestra el `CONFIG-TIENDA.md` final en una tabla corta y lo que quedó pendiente.
- Crea `INICIO.md` y `REGISTRO-INVESTIGACION.md` en la carpeta de trabajo si no existen (plantilla en `skills/ads-invest/templates/REGISTRO-INVESTIGACION.md`).
- Recuérdale que **no** suba `CONFIG-TIENDA.md` ni la carpeta de trabajo a un repositorio público.
- Siguiente paso sugerido: "investiga el producto X" (`ads-invest`) → landing (`landing-cod`) → videos (`ads-invest` Regla 5).
